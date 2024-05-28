import argparse
import io
import pathlib
import time
import typing

import humanize
import pytimeparse


class FileWithTimestamp:
    def __init__(self, file: pathlib.Path, timestamp: float):
        self.file = file
        self.timestamp = timestamp

    def __lt__(self, other: "FileWithTimestamp") -> bool:
        return self.timestamp < other.timestamp


def find_files(directories: typing.List[str]) -> typing.List[pathlib.Path]:
    files = []
    for directory in directories:
        for entry in pathlib.Path(directory).rglob("*"):
            if entry.is_file():
                files.append(entry)
    return files


def filter_files(
    files: typing.List[pathlib.Path], exclude_substrings: typing.List[str]
) -> typing.List[pathlib.Path]:
    return [
        file
        for file in files
        if not any(substring in str(file) for substring in exclude_substrings)
    ]


def filter_by_extensions(
    files: typing.List[pathlib.Path], extensions: typing.List[str]
) -> typing.List[pathlib.Path]:
    extensions = [f".{ext}" for ext in extensions if not ext.startswith(".")]
    extensions = [ext.lower() for ext in extensions]
    if extensions:
        return [file for file in files if any(file.suffix == ext for ext in extensions)]
    return files


def filter_by_age(
    files: typing.List[FileWithTimestamp], max_age_seconds: float
) -> typing.List[FileWithTimestamp]:
    current_time = time.time()
    return [file for file in files if current_time - file.timestamp <= max_age_seconds]


def build_path_list(args) -> typing.List[FileWithTimestamp]:
    files: typing.List[pathlib.Path] = find_files(args.directories)
    files = filter_files(files, args.exclude)
    files = filter_by_extensions(files, args.ext)
    if args.newer:
        max_age_seconds = pytimeparse.parse(args.newer)
    else:
        max_age_seconds = float("inf")
    file_timestamps: typing.List[FileWithTimestamp] = [
        FileWithTimestamp(file, file.stat().st_mtime) for file in files
    ]
    file_timestamps.sort(key=lambda x: x.timestamp, reverse=True)
    file_timestamps = filter_by_age(file_timestamps, max_age_seconds)
    return file_timestamps


def build_string_buffer(args: argparse.Namespace) -> str:
    file_timestamps = build_path_list(args)
    out_buffer: io.StringIO = io.StringIO()
    file_timestamps.sort(key=lambda x: x.timestamp, reverse=False)
    for file_with_timestamp in file_timestamps:
        d = humanize.naturaldelta(time.time() - file_with_timestamp.timestamp)
        out_buffer.write(f"age: {d}, path: {file_with_timestamp.file}\n")
    return out_buffer.getvalue()


if __name__ == "__main__":
    print(build_string_buffer())
