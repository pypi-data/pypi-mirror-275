#!/usr/bin/env python3
#
#  __main__.py
"""
GunShotMatch Command-Line Interface.
"""
#
#  Copyright © 2020-2023 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import os
import sys
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional

# 3rd party
import click
from consolekit import CONTEXT_SETTINGS, click_group
from consolekit.commands import SuggestionGroup
from consolekit.options import flag_option, version_option
from consolekit.versions import get_version_callback

# this package
import gunshotmatch_cli

if TYPE_CHECKING:
	# 3rd party
	from click.shell_completion import CompletionItem

__all__ = ("decision_tree", "main", "projects", "unknown")


class _TomlPath(click.Path):

	def __init__(self, exists: bool = True):
		super().__init__(exists=exists, dir_okay=False)

	def shell_complete(
			self,
			ctx: click.Context,
			param: click.Parameter,
			incomplete: str,
			) -> List["CompletionItem"]:

		# stdlib
		import glob

		# 3rd party
		from click.shell_completion import CompletionItem

		completions = []
		for file in glob.glob(f"{incomplete}*"):
			if file.endswith(".toml"):
				completions.append(CompletionItem(file, type="plain"))

		return completions


@version_option(
		get_version_callback(
				gunshotmatch_cli.__version__,
				"GunShotMatch CLI",
				{
						"gunshotmatch-pipeline": "GunShotMatch Pipeline",
						"libgunshotmatch": "LibGunShotMatch",
						"scikit-learn": "scikit-learn",
						}
				)
		)
@click_group(context_settings=CONTEXT_SETTINGS, cls=SuggestionGroup)
def main() -> None:
	"""
	GunShotMatch command-line interface.
	"""  # noqa: D403  (false positive)


@click.argument("projects_toml", default="projects.toml", type=_TomlPath())
@main.command()
def projects(projects_toml: str = "projects.toml") -> None:
	"""
	Pipeline for creating projects from raw datafiles.
	"""

	# 3rd party
	import gunshotmatch_pipeline.results
	import sdjson
	from domdf_python_tools.paths import PathPlus
	from gunshotmatch_pipeline.exporters import verify_saved_project, write_combined_csv
	from gunshotmatch_pipeline.projects import Projects, process_projects
	from gunshotmatch_pipeline.utils import project_plural
	from libgunshotmatch.peak import write_project_alignment
	from libgunshotmatch.project import Project

	projects = Projects.from_toml(PathPlus(projects_toml).read_text())
	output_dir = PathPlus(projects.global_settings.output_directory).abspath()

	print(f"Processing {len(projects)} {project_plural(len(projects))}:")
	for project_name in projects.per_project_settings:
		print(f"  {project_name}")
	print(f"Saving to {output_dir.as_posix()!r}")

	for project in process_projects(projects, output_dir, recreate=False):
		project_from_disk = Project.from_file(output_dir / (project.name + ".gsmp"))
		verify_saved_project(project, project_from_disk)

		# for repeat in project.datafile_data.values():
		# 	datafile = repeat.datafile

		# 	verify_saved_file = False
		# 	if verify_saved_file:
		# 		from_file = Datafile.from_file(datafile_export_filename)
		# 		verify_saved_datafile(datafile, from_file)

		write_project_alignment(project, output_dir)
		for repeat in project.datafile_data.values():
			write_combined_csv(repeat, output_dir)

		# Matches Sheet
		# MatchesCSVExporter(
		# 		os.path.join(output_dir, project.name + "_MATCHES.csv"), project, minutes=True, n_hits=5
		# 		)

		write_new_output = True
		matches_json_filename = f"{project.name}.json"
		matches_data = gunshotmatch_pipeline.results.matches(project)

		if (output_dir / matches_json_filename).is_file():
			existing_file_content = (output_dir / matches_json_filename).read_text().strip()
			existing_matches_json = sdjson.loads(existing_file_content)
			matches_data_with_old_mtime: Dict[str, Dict[str, Any]] = {
					"metadata": dict(matches_data["metadata"]),
					"compounds": matches_data["compounds"],
					}
			matches_data_with_old_mtime["metadata"]["created"] = existing_matches_json["metadata"]["created"]
			if sdjson.dumps(matches_data_with_old_mtime, indent=2).strip() == existing_file_content:
				# Unchanged
				write_new_output = False

		if write_new_output:
			(output_dir / matches_json_filename).write_clean(sdjson.dumps(matches_data, indent=2))

		assert project.consolidated_peaks is not None
		print(project.consolidated_peaks)
		print(len(project.consolidated_peaks))


@click.argument("unknown_toml", default="unknown.toml")
@flag_option("-r", "--recreate")
@click.option("-t", "--table", default='')
@click.command()
def _unkn(unknown_toml: str = "unknown.toml", recreate: bool = False, table: str = '') -> str:
	# sys.stderr.write(repr(unknown_toml) + "\n")
	return unknown_toml


def complete_table(ctx: click.Context, param: click.Parameter, incomplete: str) -> List["CompletionItem"]:
	argv = [arg for arg in os.getenv("COMP_WORDS", '').strip().splitlines()]

	unknown_toml_filename = "unknown.toml"
	try:
		with _unkn.make_context(argv[0], argv[2:]) as ctx:
			unknown_toml_filename = _unkn.invoke(ctx)
	except (Exception, SystemExit):
		pass

	try:
		with open(unknown_toml_filename, "rb") as fp:
			# 3rd party
			from click.shell_completion import CompletionItem
			from gunshotmatch_pipeline.utils import tomllib

			unknown_toml_content: Dict[str, Any] = tomllib.load(fp)
			tables = [k for k, v in unknown_toml_content.items() if isinstance(v, dict)]
			table_names = [table for table in tables if table.startswith(incomplete)]
			completions = []
			for table in table_names:
				if ' ' in table:
					completions.append(CompletionItem('"' + table.replace(' ', "\\ ") + '"'))
				else:
					completions.append(CompletionItem(table))
			return completions
	except Exception:
		return []


@click.argument("unknown_toml", default="unknown.toml", type=_TomlPath())
@click.option(
		"-t",
		"--table",
		help="TOML table name for the unknown sample's settings. If not given top-level keys are used",
		default=None,
		shell_complete=complete_table
		)
@flag_option("-r", "--recreate", help="Recreate output files (e.g. if method changed)")
@main.command()
def unknown(unknown_toml: str = "unknown.toml", recreate: bool = False, table: Optional[str] = None) -> None:
	"""
	Pipeline for unknown propellant/OGSR sample.
	"""

	# 3rd party
	from domdf_python_tools.paths import PathPlus
	from gunshotmatch_pipeline.unknowns import UnknownSettings, process_unknown
	from gunshotmatch_pipeline.utils import tomllib

	# from gunshotmatch_pipeline.exporters import write_matches_json

	def iter_unknowns() -> Iterator[UnknownSettings]:

		if table and table == ":all:":
			unknown_settings_toml = tomllib.loads(PathPlus("unknown.toml").read_text())
			table_names = [k for k, v in unknown_settings_toml.items() if isinstance(v, dict)]

			for table_name in table_names:
				yield UnknownSettings(table_name, **unknown_settings_toml[table_name])
				print()

		elif table:
			unknown_settings_toml = tomllib.loads(PathPlus("unknown.toml").read_text())
			yield UnknownSettings(table, **unknown_settings_toml[table])

		else:
			yield UnknownSettings.from_toml(PathPlus(unknown_toml).read_text())

	for unknown in iter_unknowns():
		print(f"Processing unknown {unknown.name!r}")
		project = process_unknown(unknown, unknown.output_directory, recreate=recreate)
		assert project.consolidated_peaks is not None
		print(len(project.consolidated_peaks))


@click.option("-p", "--projects", "projects_toml", default="projects.toml", type=_TomlPath())
@click.option("-u", "--unknown", "unknown_toml", default="unknown.toml", type=_TomlPath(exists=False))
@flag_option(
		"-t",
		"--train-only",
		default=False,
		help="Only train the decision tree, do not predict the class of the unknown",
		)
@flag_option(
		"-v.-V",
		"--visualise/--no-visualise",
		default=True,
		help="Whether to visualise the decision tree (produce dot and PNG files)",
		)
@flag_option(
		"-r/-R",
		"--random-forest/--no-random-forest",
		default=True,
		help="Use a random forest classifier / use a single decision tree.",
		)
@main.command()
def decision_tree(
		projects_toml: str = "projects.toml",
		unknown_toml: str = "unknown.toml",
		train_only: bool = False,
		random_forest: bool = True,
		visualise: bool = True,
		) -> None:
	"""
	Create decision tree and predict class of an unknown sample.
	"""

	# 3rd party
	import numpy
	from domdf_python_tools.paths import PathPlus
	from gunshotmatch_pipeline.decision_tree import data_from_unknown
	from gunshotmatch_pipeline.projects import Projects
	from gunshotmatch_pipeline.unknowns import UnknownSettings

	# this package
	from gunshotmatch_cli.decision_tree import train_decision_tree

	# root_dir = PathPlus(__file__).parent.abspath()
	# trees_dir = root_dir / "trees"
	# decision_tree_data_dir = root_dir / "decision_tree_data"
	# decision_tree_data_dir.maybe_make()

	projects = Projects.from_toml(PathPlus(projects_toml).read_text())

	if not train_only:
		unknown = UnknownSettings.from_toml(PathPlus(unknown_toml).read_text())

	classifier, factorize_map, feature_names = train_decision_tree(
		projects,
		random_forest=random_forest,
		visualise=visualise,
	)

	if train_only:
		sys.exit(0)

	print("\nPredicting class for unknown", unknown.name)

	unknown_sample = data_from_unknown(unknown, feature_names=feature_names)
	# predicted_class = classifier.predict(unknown_sample)
	# print(predicted_class)
	# print(factorize_map[predicted_class[0]])

	proba = classifier.predict_proba(unknown_sample)
	# print("proba:", proba.tolist())
	# argmax = numpy.argmax(proba, axis=1)
	argsort = numpy.argsort(proba, axis=1)
	# print("argmax:", argmax.tolist())
	# print("argsort:", list(reversed(argsort.tolist()[0])))
	# print("classifier.classes_:", list(classifier.classes_))
	# print("Ranked:", [factorize_map[cls] for cls in reversed(argsort.tolist()[0])])
	# print("       ", sorted(classifier.predict_proba(unknown_sample)[0], reverse=True))

	class_names = [factorize_map[cls] for cls in reversed(argsort.tolist()[0])]
	probabilities = sorted(classifier.predict_proba(unknown_sample)[0], reverse=True)
	for idx, (propellant, probability) in enumerate(zip(class_names, probabilities)):
		if probability:
			print(idx + 1, probability, propellant)

	# take = classifier.classes_.take(argmax, axis=0)
	# print("take:", list(take))


@click.argument("projects_toml", default="projects.toml", type=_TomlPath())
@main.command()
def peak_report(projects_toml: str = "projects.toml") -> None:
	"""
	Generate peak reports for the projects.
	"""

	# 3rd party
	from domdf_python_tools.paths import PathPlus
	from gunshotmatch_pipeline.projects import Projects
	from gunshotmatch_pipeline.utils import project_plural
	from gunshotmatch_reports.peaks import build_peak_report
	from libgunshotmatch_mpl.peakviewer import load_project

	projects = Projects.from_toml(PathPlus(projects_toml).read_text())
	output_dir = PathPlus(projects.global_settings.output_directory).abspath()

	print(f"Generating peak reports for {len(projects)} {project_plural(len(projects))}:")
	for project_name in projects.per_project_settings:
		print(f"  {project_name}")
	print(f"Saving to {output_dir.as_posix()!r}")

	for project_name in projects.per_project_settings:
		project = load_project(output_dir / (project_name + ".gsmp"))

		assert project.consolidated_peaks is not None
		print(f"{project.name} – {len(project.consolidated_peaks)} peaks")
		build_peak_report(
				project,
				pdf_filename=output_dir / f"{project.name}_peak_report.pdf",
				title_every_page=True,
				)


@click.argument("projects_toml", default="projects.toml")
@main.command()
def chromatograms(projects_toml: str = "projects.toml") -> None:
	"""
	Generate chromatogram reports for the projects.
	"""

	# 3rd party
	from domdf_python_tools.paths import PathPlus
	from gunshotmatch_pipeline.projects import Projects
	from gunshotmatch_pipeline.utils import project_plural
	from gunshotmatch_reports.chromatogram import build_chromatogram_report
	from libgunshotmatch_mpl.peakviewer import load_project

	projects = Projects.from_toml(PathPlus(projects_toml).read_text())
	output_dir = PathPlus(projects.global_settings.output_directory).abspath()

	print(f"Generating chromatograms for {len(projects)} {project_plural(len(projects))}:")
	for project_name in projects.per_project_settings:
		print(f"  {project_name}")
	print(f"Saving to {output_dir.as_posix()!r}")

	for project_name in projects.per_project_settings:
		project = load_project(output_dir / (project_name + ".gsmp"))

		build_chromatogram_report(
				project,
				pdf_filename=output_dir / f"{project.name}_chromatogram.pdf",
				)


if __name__ == "__main__":
	main()
