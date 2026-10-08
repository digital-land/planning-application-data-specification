"""Release preparation changes only a temporary Git repository."""
import importlib.util
from pathlib import Path
import subprocess

import pytest

spec = importlib.util.spec_from_file_location("prepare_release", Path(__file__).resolve().parents[1] / "scripts/prepare_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


@pytest.fixture
def repo(tmp_path):
    def git(*args):
        return release.run("git", *args, root=tmp_path)
    git("init", "-b", "main")
    git("config", "user.name", "Release test")
    git("config", "user.email", "release@example.test")
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "example"\nversion = "2026.10.7.dev1"\n\n[other]\nversion = "unchanged"\n')
    git("add", "pyproject.toml")
    git("commit", "-m", "Initial")
    return tmp_path


def test_prepare_commits_version_and_matching_annotated_tag(repo):
    seen = []
    commit = release.prepare_release("2026.10.8.dev1", repo, checks=lambda root: seen.append(release.package_version((root / "pyproject.toml").read_text())))
    assert seen == ["2026.10.8.dev1"]
    assert release.check_release("2026.10.8.dev1", repo) == commit
    assert release.run("git", "cat-file", "-t", "refs/tags/2026.10.8.dev1", root=repo) == "tag"
    assert release.run("git", "status", "--porcelain", root=repo) == ""
    assert 'version = "unchanged"' in (repo / "pyproject.toml").read_text()
    with pytest.raises(ValueError, match="already exists"):
        release.prepare_release("2026.10.8.dev1", repo, checks=lambda root: None)


def test_existing_version_needs_no_extra_commit(repo):
    before = release.run("git", "rev-parse", "HEAD", root=repo)
    assert release.prepare_release("2026.10.7.dev1", repo, checks=lambda root: None) == before


def test_failed_checks_restore_version_without_commit_or_tag(repo):
    original = (repo / "pyproject.toml").read_text()
    def fail(root):
        raise subprocess.CalledProcessError(1, "checks")
    with pytest.raises(subprocess.CalledProcessError):
        release.prepare_release("2026.10.8.dev1", repo, checks=fail)
    assert (repo / "pyproject.toml").read_text() == original
    assert release.run("git", "tag", root=repo) == ""


@pytest.mark.parametrize("version", ["", "v2026.10.8.dev1", "2026.02.8.dev1", "2026.2.30.dev1", "2026.10.8", "2026.10.8.dev0"])
def test_invalid_versions_rejected(version):
    with pytest.raises(ValueError):
        release.validate_version(version)


def test_uncommitted_files_stop_release(repo):
    (repo / "notes.txt").write_text("unfinished")
    with pytest.raises(ValueError, match="uncommitted"):
        release.prepare_release("2026.10.8.dev1", repo, checks=lambda root: None)


def test_mismatched_manual_tag_fails(repo):
    release.run("git", "tag", "2026.10.8.dev1", root=repo)
    with pytest.raises(ValueError, match="does not match"):
        release.check_release("2026.10.8.dev1", repo)
