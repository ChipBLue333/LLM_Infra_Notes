#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 path/to/problem.cpp"
    exit 1
fi

source_file="$1"
binary_file="/tmp/$(basename "${source_file%.cpp}")"

g++ \
    -std=c++20 \
    -Wall \
    -Wextra \
    -Wpedantic \
    -Wconversion \
    -Wshadow \
    -O0 \
    -g \
    "$source_file" \
    -o "$binary_file"

"$binary_file"

