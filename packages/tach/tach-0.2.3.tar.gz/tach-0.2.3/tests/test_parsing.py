from __future__ import annotations

import os

import pytest
from pydantic import ValidationError

from tach import filesystem as fs
from tach.check import check
from tach.core.config import PackageConfig, ProjectConfig, TagDependencyRules
from tach.filesystem import file_to_module_path
from tach.parsing.config import parse_package_config, parse_project_config


def test_file_to_mod_path():
    assert file_to_module_path("__init__.py") == ""
    assert file_to_module_path("domain_one/__init__.py") == "domain_one"
    assert file_to_module_path("domain_one/interface.py") == "domain_one.interface"


def test_parse_valid_project_config():
    result = parse_project_config("example/valid/")
    assert result == ProjectConfig(
        constraints=[
            TagDependencyRules(tag="one", depends_on=["two"]),
            TagDependencyRules(tag="two", depends_on=["one"]),
            TagDependencyRules(tag="three", depends_on=[]),
        ],
        exclude=["domain_thr.*"],
        exclude_hidden_paths=True,
    )


def test_run_valid_project_config():
    current_dir = os.getcwd()
    try:
        project = "./example/valid/"
        fs.chdir(project)
        project_config = parse_project_config()
        results = check(
            ".",
            project_config,
            exclude_paths=project_config.exclude,
            exclude_hidden_paths=project_config.exclude_hidden_paths,
        )
        assert results == []
    finally:
        # Make sure not to dirty the test directory state
        fs.chdir(current_dir)


def test_parse_valid_strict_package_config():
    result = parse_package_config("example/valid/domain_one")
    assert result == PackageConfig(strict=True, tags=["one"])


def test_parse_valid_multi_tag_package_config():
    result = parse_package_config("example/valid/domain_two")
    assert result == PackageConfig(strict=False, tags=["two", "shared"])


def test_package_with_no_config():
    result = parse_package_config("example/")
    assert result is None


def test_invalid_project_config():
    with pytest.raises(ValidationError):
        parse_project_config("example/invalid/")


def test_empty_project_config():
    with pytest.raises(ValueError):
        parse_project_config("example/invalid/empty")


def test_invalid_package_config():
    with pytest.raises(ValidationError):
        parse_package_config("example/invalid")


def test_empty_package_config():
    with pytest.raises(ValueError):
        parse_package_config("example/invalid")


def test_exclude_hidden_paths_fails():
    current_dir = os.getcwd()
    hidden_project = "./example/invalid/hidden/"
    fs.chdir(hidden_project)
    try:
        project_config = parse_project_config()
        assert project_config.exclude_hidden_paths is False
        results = check(
            ".",
            project_config,
            exclude_hidden_paths=project_config.exclude_hidden_paths,
        )
        assert len(results) == 1
        assert "strict mode" in results[0].error_info.exception_message

        project_config.exclude_hidden_paths = True
        assert check(".", project_config, exclude_hidden_paths=True) == []
    finally:
        # Make sure not to dirty the test directory state
        fs.chdir(current_dir)
