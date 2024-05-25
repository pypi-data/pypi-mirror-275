import re
import os


class PathType:
    GIT_URL = "Git URL"
    DIRECTORY_PATH = "Directory Path"
    FILE_PATH = "File Path"
    UNKNOWN = "Unknown"


class OutputFormat:
    DICT = "dict"
    TREE = "tree"
    JSON = "json"
    markdown = "markdown"


def detect_path_type(path):
    """
    Detect the type of the path.
    :param path: the path.
    :return:
    """
    git_url_pattern = re.compile(
        r'^(?:https?|git|ssh|git@[-\w.]+):(//)?(([\w./~-]+/)+)([\w./~-]+)(\.git)?(/)?$'
    )

    if git_url_pattern.match(path):
        return PathType.GIT_URL
    elif os.path.isdir(path):
        return PathType.DIRECTORY_PATH
    elif os.path.isfile(path):
        return PathType.FILE_PATH
    else:
        return PathType.UNKNOWN


def dict_to_markdown(file_structure):
    """
    Converts a nested dictionary representing a file structure to a markdown format string.

    :param file_structure: dict, the nested dictionary representing the file structure
    :return: str, the file structure in Markdown format
    """

    def _add_items(name, content, indent):
        nonlocal markdown_str
        markdown_str += f"{' ' * indent}- **{name}**\n"

        files = content.get('files', [])
        dirs = content.get('dirs', {})

        for file in files:
            markdown_str += f"{' ' * (indent + 2)}- {file}\n"

        for dir_name, dir_content in dirs.items():
            _add_items(dir_name, dir_content, indent + 2)

    markdown_str = ''
    for root_dir, c in file_structure.items():
        markdown_str += f"## {root_dir}\n"
        _add_items('', c, 0)

    return markdown_str


def dict_to_tree_string(file_structure, prefix=''):
    """
    Converts a nested dictionary representing a file structure to a string format similar to the `tree` command.

    :param file_structure: dict, the nested dictionary representing the file structure
    :param prefix: str, the prefix string used for indentation
    :return: str, the file structure in tree format
    """

    def _add_items(name, content, item_prefix, is_last):
        nonlocal tree_str
        tree_str += item_prefix + ('└── ' if is_last else '├── ') + name + '\n'
        sub_prefix = item_prefix + ('    ' if is_last else '│   ')

        files = content.get('files', [])
        dirs = list(content.get('dirs', {}).keys())

        for index, file in enumerate(files):
            is_last_file = index == len(files) - 1 and not dirs
            tree_str += sub_prefix + ('└── ' if is_last_file else '├── ') + file + '\n'

        for i, dir_name in enumerate(dirs):
            _add_items(dir_name, content['dirs'][dir_name], sub_prefix, i == len(dirs) - 1)

    tree_str = ''
    for root_dir, c in file_structure.items():
        tree_str += root_dir + '\n'
        _add_items('', c, prefix, True)

    return tree_str
