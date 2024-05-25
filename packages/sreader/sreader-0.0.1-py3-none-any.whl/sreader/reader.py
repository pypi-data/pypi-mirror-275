"""
Space Reader: Convert any file path into LLM-friendly inputs.
"""

import os
import json
import fnmatch
from .utils import PathType, OutputFormat
from .utils import detect_path_type, dict_to_tree_string, dict_to_markdown


def read(path: str, output_format: str = OutputFormat.DICT, **kwargs):
    """
    Read the file.
    :param path: the path.
    :param output_format: the output format.
    :param kwargs: other optional parameters:
        - allowed_invisible: whether to allow invisible files.
        - filters: the filter, with the wildcard pattern.
    :return: the file content.
    """
    # Default values for kwargs
    allowed_invisible = kwargs.get('allowed_invisible', False)
    filters = kwargs.get('filters', None)

    path_type = detect_path_type(path)
    if path_type == PathType.DIRECTORY_PATH:
        return read_dir(path, output_format, allowed_invisible, filters)
    elif path_type == PathType.FILE_PATH:
        return read_file(path, output_format)
    elif path_type == PathType.GIT_URL:
        return read_git(path, output_format)


def read_dir(dir_path: str, output_format=OutputFormat.DICT, allowed_invisible=True, filters=None):
    """
    Recursively reads the file structure from the given directory path and prints it.

    :param dir_path: str, the path to the directory
    :param output_format: str, the output format, default is "dict"
    :param allowed_invisible: whether to allow invisible files.
    :param filters: the filter, with the wildcard pattern.

    :example:
    >>> read_dir("path/to/directory")
    {
        "path/to/directory": {
            "files": ["file1.txt", "file2.txt"],
            "dirs": {
                "subdir1": {
                    "files": ["file3.txt"]
                }
            }
        }
    }
    """

    def _read_structure(current_path, invisible=True):
        structure = {"files": [], "dirs": {}}
        with os.scandir(current_path) as it:
            for entry in it:
                if entry.name.startswith('.') and not invisible:
                    continue
                if entry.is_dir():
                    structure["dirs"][entry.name] = _read_structure(os.path.join(current_path, entry.name))
                else:
                    structure["files"].append(entry.name)
        return structure

    def _filter_structure(structure, filter_list):
        def match_patterns(filename):
            return any(fnmatch.fnmatch(filename, pattern) for pattern in filter_list)

        filtered_structure = {"files": [], "dirs": {}}
        for file in structure["files"]:
            if match_patterns(file):
                filtered_structure["files"].append(file)

        for dir_name, dir_structure in structure["dirs"].items():
            filtered_substructure = _filter_structure(dir_structure, filter_list)
            if filtered_substructure["files"] or filtered_substructure["dirs"]:
                filtered_structure["dirs"][dir_name] = filtered_substructure

        return filtered_structure

    result_dict = {dir_path: _read_structure(dir_path, allowed_invisible)}

    if filters:
        result_dict = {dir_path: _filter_structure(result_dict[dir_path], filters)}

    # format the output.
    if output_format == OutputFormat.TREE:
        return dict_to_tree_string(result_dict)
    elif output_format == OutputFormat.JSON:
        return json.dumps(result_dict, indent=4)
    elif output_format == OutputFormat.markdown:
        return dict_to_markdown(result_dict)
    else:
        return result_dict


def read_file(file_path: str, output_format: str):
    """
    Read the file.
    :param file_path: the path.
    :param output_format: the output format.

    :return: the file content.
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_git(git_url: str, output_format: str):
    """
    Read the file from the Git URL.
    :param git_url: the Git URL.
    :param output_format: the output format.

    :return: the file content.
    """
    pass


def read_aws(url: str, output_format: str):
    """
    Read the file from the URL.
    :param output_format: the output format.
    :param url: the input URL.

    :return: the file content.
    """
    pass
