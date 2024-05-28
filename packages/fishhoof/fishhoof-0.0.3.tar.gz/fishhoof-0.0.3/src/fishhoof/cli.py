import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find files in the specified directory."
    )
    parser.add_argument(
        "directories", type=str, nargs="+", help="The directories to search in."
    )
    parser.add_argument(
        "--exclude",
        type=str,
        action="append",
        default=[],
        help="Substrings to exclude from paths.",
    )
    parser.add_argument(
        "--ext",
        type=str,
        action="append",
        default=[],
        help="File extensions to include.",
    )
    parser.add_argument(
        "--newer",
        type=str,
        default="",
        help="Ignore files older than specified number of seconds.",
    )
    return parser.parse_args()
