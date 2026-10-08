"""Prepare a local development release or check its tag and package version."""

import argparse
from datetime import date
import os
from pathlib import Path
import re
import subprocess
import sys

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

ROOT = Path(__file__).resolve().parents[1]


def run(*args, root=ROOT):
    return subprocess.check_output(args, cwd=root, text=True).strip()


def validate_version(version):
    match = re.fullmatch(r"(\d{4})\.([1-9]\d?)\.([1-9]\d?)\.dev([1-9]\d*)", version)
    if not match:
        raise ValueError("Use VERSION=YYYY.M.D.devN, without leading zeros or a v prefix")
    date(*(int(match[i]) for i in (1, 2, 3)))
    return version


def package_version(text):
    return tomllib.loads(text)["project"]["version"]


def replace_version(text, version):
    section = re.search(r"(?ms)^\[project\]\s*\n(.*?)(?=^\[|\Z)", text)
    if not section:
        raise ValueError("pyproject.toml has no [project] section")
    body, count = re.subn(r'(?m)^(version\s*=\s*)[\'\"][^\'\"]+[\'\"]',
                          lambda match: f'{match[1]}"{version}"', section[1])
    if count != 1:
        raise ValueError("Expected one version in the [project] section")
    updated = text[:section.start(1)] + body + text[section.end(1):]
    if package_version(updated) != version:
        raise ValueError("Could not update the package version")
    return updated


def check_release(version, root=ROOT):
    validate_version(version)
    tagged = run("git", "show", f"refs/tags/{version}:pyproject.toml", root=root)
    if package_version(tagged) != version:
        raise ValueError(f"Tag {version} does not match the package version in its commit")
    return run("git", "rev-parse", f"refs/tags/{version}^{{commit}}", root=root)


def release_checks(root):
    subprocess.run(["make", "checks"], cwd=root, check=True)
    subprocess.run([sys.executable, "-m", "pytest", "tests/test_package_distribution.py",
                    "tests/test_installed_wheel.py", "tests/test_installable_package.py"], cwd=root, check=True)
    subprocess.run(["make", "package"], cwd=root, check=True)


def prepare_release(version, root=ROOT, checks=release_checks):
    validate_version(version)
    if run("git", "branch", "--show-current", root=root) != "main":
        raise ValueError("Prepare releases on main")
    if run("git", "status", "--porcelain", "--untracked-files=normal", root=root):
        raise ValueError("Commit or move aside uncommitted and untracked files before preparing a release")
    if run("git", "tag", "--list", version, root=root):
        raise ValueError(f"Tag {version} already exists; choose a new version")
    path = root / "pyproject.toml"
    original = path.read_text()
    updated = replace_version(original, version)
    path.write_text(updated)
    try:
        checks(root)
        changed = run("git", "diff", "--name-only", root=root).splitlines()
        if any(name != "pyproject.toml" for name in changed) or run("git", "diff", "--cached", "--name-only", root=root) or run("git", "ls-files", "--others", "--exclude-standard", root=root):
            raise ValueError("Checks changed other files; review them before preparing the release")
    except Exception:
        if path.read_text() == updated:
            path.write_text(original)
        raise
    if updated != original:
        subprocess.run(["git", "add", "pyproject.toml"], cwd=root, check=True)
        subprocess.run(["git", "commit", "-m", f"tool: prepare development prerelease {version}"], cwd=root, check=True)
    subprocess.run(["git", "tag", "-a", version, "-m", f"Development prerelease {version}"], cwd=root, check=True)
    return check_release(version, root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "check"))
    args = parser.parse_args()
    version = os.environ.get("VERSION", "")
    try:
        commit = prepare_release(version) if args.action == "prepare" else check_release(version)
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Release stopped: {error}\n")
    print(f"Verified {version} at {commit}. Nothing has been pushed or published.")


if __name__ == "__main__":
    main()
