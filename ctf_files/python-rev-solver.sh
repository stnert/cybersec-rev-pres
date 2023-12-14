#!/usr/bin/env bash

# Author: Lolo
# Created: 10/12/2023

set -e

info() {
    echo -e "\033[0;32m$@\033[0m"
}

die() {
    echo -e "\033[0;31m$@\033[0m"
    exit 1
}

warn() {
    echo -e "\033[0;33m$@\033[0m"
}

usage() {
    info "Usage: $0 [-h]"
    info "       $0 [-i]"
    info "       $0 [-s]"
    info "Options:"
    info "  -h: Show this help message"
    info "  -i: Initial unpacking"
    info "  -s: Solve"

    exit 0
}

install_stuff() {
    info "Installing python-rev-solver dependencies"
    pip install -r requirements.txt
}

initial_unpacking() {
    install_stuff

    info "Removing old python-rev-solver errors"
    rm python-rev-error_decoding_* || true

    info "Running python-rev-solver"
    python3 python-rev-solver.py
}

solve() {
    install_stuff

    info "Solving python-rev-solver"
    info "python-rev-ast has been modified to use atheris and dumb homemade fuzzer. didnt work."

    #python3 python-rev-fuzz_0.py
    python3 python-rev-ast_2.py
}

while getopts ":his" opt; do
    case $opt in
        h) usage ;;
        i) initial_unpacking ;;
        s) solve ;;
    esac
done
