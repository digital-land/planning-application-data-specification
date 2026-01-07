import glob
import re

import yaml
from integrity_checks.utils import print_error, print_warning
from utils import check_kebab_case


def check_codelist_names(codelists):
    """
    Check rule 1 & 3: codelist attr must be string, kebab-case and unique across all codelists
    """
    seen = set()
    has_errors = False
    for path, meta in codelists.items():
        codelist = meta.get("codelist")
        if not isinstance(codelist, str) or not check_kebab_case(codelist):
            print_error(
                "codelist", path, f"codelist '{codelist}' must be kebab-case string"
            )
            has_errors = True
        if codelist in seen:
            print_error("codelist", path, f"duplicate codelist '{codelist}'")
            has_errors = True
        seen.add(codelist)
    return not has_errors


def check_codelist_source(codelists):
    """
    Check rule 2: source is empty = error, should be either path or url
    """
    has_errors = False
    for path, meta in codelists.items():
        source = meta.get("source", "")
        valid_source = (
            source
            and isinstance(source, str)
            and (source.startswith("http") or source.startswith("data/"))
        )
        if not valid_source:
            print_error(
                "codelist", path, f"source is missing or not a valid url/path: {source}"
            )
            has_errors = True
    return not has_errors


def check_codelist_github_discussion(codelists):
    """
    Check rule 3: warning if github discussion number is empty
    """
    for path, meta in codelists.items():
        if not meta.get("github-discussion"):
            print_warning("codelist", path, "github-discussion is empty")


def check_codelist_entry_date(codelists):
    """
    Check rule 4: entry-date should not be blank
    """
    has_errors = False
    for path, meta in codelists.items():
        if not meta.get("entry-date"):
            print_error("codelist", path, "entry-date is missing or blank")
            has_errors = True
    return not has_errors


def check_codelist_name_plural(codelists):
    """
    Check rule 9: warn if name or plural is missing or not capitalised correctly
    """
    for path, meta in codelists.items():
        for key in ["name", "plural"]:
            val = meta.get(key)
            if not val:
                print(f"Warning in {path}: {key} is missing")
            elif not val[0].isupper():
                print(f"Warning in {path}: {key} should start with a capital letter")


def check_codelist_end_date(codelists):
    """
    Check rule 10: warn if end-date is missing (should be present, even if blank)
    """
    for path, meta in codelists.items():
        if "end-date" not in meta:
            print(f"Warning in {path}: end-date is missing")


def check_all(codelists):
    ok = True
    ok &= check_codelist_names(codelists)
    ok &= check_codelist_source(codelists)
    check_codelist_github_discussion(codelists)
    ok &= check_codelist_entry_date(codelists)
    check_codelist_name_plural(codelists)
    check_codelist_end_date(codelists)
    return ok


if __name__ == "__main__":
    check_all()
