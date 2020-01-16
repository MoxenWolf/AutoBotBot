import os
import platform
import sys

from pybuilder.core import use_plugin, init, task, Author
import itertools

# plugins
use_plugin("python.distutils")
use_plugin("python.core")
use_plugin("python.install_dependencies")
# use_plugin("python.flake8")
# use_plugin("pypi:pybuilder_pytest")
# use_plugin("pypi:pybuilder_pytest_coverage")
# use_plugin("python.sphinx")

default_task = [
    "install_dependencies", "build_exe"
]

# project meta
name = "autobotbot"
version = "0.1.0"
summary = "Auto Bot Bot"
description = __doc__
authors = (Author("Ben Sutton", "ben.sutton@alleninstitute.org"),)
url = "https://github.com/MoxenWolf/AutoBotBot"


@init
def initialize(project):
    project.set_property("verbose", True)

    # modules / dist
    project.set_property("dir_source_main_python", "src")
    project.set_property("dir_source_main_scripts", "scripts")
    project.set_property("dir_dist", "dist/{0}-{1}".format(name, version))

    # dependencies
    project.depends_on_requirements("requirements.txt")

    # entry points (typically the .py files in bfi
    project.set_property(
        "distutils_entry_points",
        {
            "gui_scripts": [
                "autobotbot=abb_cli:main"
            ]
        },
    )

    resource_patterns = ["yaml", "yml", "ui", "json"]
    for directory, subdirectory, files in os.walk("src/autobotbot"):
        directory = directory.replace("src/autobotbot\\", "").replace("\\", "/")
        for file, pattern in itertools.product(files, resource_patterns):
            if pattern in file.lower():
                project.include_file("autobotbot", directory + "/" + file)

@task
def build_exe(project, logger):
    from PyInstaller import __main__ as pyi
    from PyInstaller.utils.hooks import collect_data_files, collect_submodules
    version_text = 'src\\autobotbot\\resources\\exe_versioning\\file_version_info.txt'
    # build your command line argument
    pyi_args = ['src\\abb_cli.py',
                '--noconsole',
                '--clean',
                '--name',
                'autobotbot',
                f'--version-file={version_text}',
                ]
    # martins method for file locations:
    for package in ['mpeconfig']:

        for file in collect_data_files(package):
            pyi_args.extend(['--add-data', f'{file[0]};{file[1]}'])

    pyi_args.append(f"--add-data")
    # pyi_args.append("src/bautobotbotfi/resources/ui_files;autobotbot/resources/ui_files")

    # build the exe
    print(f'{" ".join(pyi_args)}')
    pyi.run(pyi_args)
