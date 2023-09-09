#!/usr/bin/env python3

# Automatically increments the SKETCH_VERSION
# 1.0.2+3 -> 1.0.2+4
#
# add this line to platform.txt in respective Arduino board folder, line ≈13:
#   recipe.hooks.prebuild.0.pattern={runtime.platform.path}/tools/autoversioning.py --path "{build.project_name}"
#
# Copyright (C) 2023 - amaider

import argparse
import sys
import re

sys.stdout = sys.stderr

def increment_version(match):
    version = match.group(2)
    build_number = int(match.group(3))
    incremented_build_number = build_number + 1
    print(f'{match.group(1)}{version}+{build_number}{match.group(4)} -> {match.group(1)}{version}+{incremented_build_number}{match.group(4)}')
    return f'{match.group(1)}{version}+{incremented_build_number}{match.group(4)}'

def main():
    parser = argparse.ArgumentParser(
        description="Automatically increment the SKETCH_VERSION"
    )
    parser.add_argument(
        "-p",
        "--path",
        action="store",
        required=True,
        help="Path to the Sketch(.ino) file"
    )

    args = parser.parse_args()

    # Read the file
    file_path = args.path
    with open(file_path, 'r') as file:
        text = file.read()

    # Update the text with the incremented version number
    new_text = re.sub(r'(#define SKETCH_VERSION ")(\d+\.\d+\.\d+)\+(\d+)(")', increment_version, text)

    # Save the updated text back to the file
    with open(file_path, 'w') as file:
        file.write(new_text)


if __name__ == "__main__":
    main()