import sys

from . import cli, find_files

__project_name__ = "fishhoof"


def main() -> int:
    args = cli.parse_arguments()
    out: str = find_files.build_string_buffer(args)
    sys.stdout.write(out)
    return 0
