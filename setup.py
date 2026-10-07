"""Copy canonical specification resources into release artefacts at build time."""

from pathlib import Path
import shutil

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.sdist import sdist


PACKAGE = "planning_application_specification"
RESOURCE = Path(PACKAGE) / "resources"
ROOT = Path(__file__).parent
SOURCE_ROOT = ROOT if (ROOT / "specification").is_dir() else ROOT / RESOURCE
DEFINITION_DIRS = ("application", "codelist", "component", "dataset", "field", "module", "usage")
GUIDANCE_DIRS = ("dataset", "module", "component")


def resource_paths():
    """List only canonical, local resources needed by the package."""
    specification = SOURCE_ROOT / "specification"
    paths = list(specification.glob("*.schema.md"))
    paths.append(specification / "combined-application-types.csv")
    for directory in DEFINITION_DIRS:
        paths.extend((specification / directory).glob("*.md" if directory in ("component", "field") else "*.schema.md"))
    for directory in GUIDANCE_DIRS:
        paths.extend((specification / "guidance" / directory).rglob("*.md"))
    paths.extend((specification / "example").rglob("*.json"))
    for directory in ("need", "justification"):
        paths.extend((SOURCE_ROOT / "user-needs" / directory).glob("*.md"))

    for directory in ("codelist", "usage"):
        paths.extend((SOURCE_ROOT / "data" / directory).glob("*.csv"))
    for filename in ("planning-application-type.csv", "planning-requirement.csv"):
        paths.append(SOURCE_ROOT / "data" / filename)

    missing = [path for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing package resource: {missing[0]}")
    return tuple(sorted({path.relative_to(SOURCE_ROOT) for path in paths}))


def copy_resources(destination):
    resource_root = Path(destination) / RESOURCE
    if resource_root.exists():
        shutil.rmtree(resource_root)
    copied = []
    for relative in resource_paths():
        target = Path(destination) / RESOURCE / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE_ROOT / relative, target)
        copied.append(target)
    return copied


class BuildWithResources(build_py):
    def run(self):
        super().run()
        self.resource_outputs = copy_resources(self.build_lib)

    def get_outputs(self, include_bytecode=1):
        return super().get_outputs(include_bytecode) + [str(path) for path in getattr(self, "resource_outputs", ())]


class SourceWithResources(sdist):
    def make_release_tree(self, base_dir, files):
        super().make_release_tree(base_dir, files)
        copy_resources(base_dir)


setup(cmdclass={"build_py": BuildWithResources, "sdist": SourceWithResources})
