import os
import shutil
from blueness import NAME, VERSION, DESCRIPTION
from setuptools.command.install import install
from blueness.pypi import setup


class CustomInstallCommand(install):
    def run(self):
        target_dir = os.path.join(os.path.dirname(__file__), NAME, ".abcli")
        os.makedirs(target_dir, exist_ok=True)

        source_dir = os.path.join(os.path.dirname(__file__), "..", ".abcli")

        # for filename in os.listdir(source_dir):
        #    if filename.endswith(".sh"):
        #        shutil.copy(os.path.join(source_dir, filename), target_dir)

        # Run standard install process
        install.run(self)


setup(
    filename=__file__,
    repo_name="blueness",
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.argparse",
    ],
    include_package_data=True,
    package_data={
        NAME: [".abcli/*.sh"],
    },
    cmdclass={
        "install": CustomInstallCommand,
    },
)
