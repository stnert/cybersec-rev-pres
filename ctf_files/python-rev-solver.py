#!/usr/bin/env python3

"""
Author: Lolo    
Date: 12/10/2023

Unpacks a script hidden behind hundreds of exec(base64decode(str))

Usage:
    /usr/bin/docker run -it --rm -v $(pwd):/data -w /data python:3.11 bash python-rev-solver.sh -i
"""

import hashlib
import argparse
import ast
import base64
import sys

try:
    import astor
except ModuleNotFoundError:
    print("pip install astor")
    sys.exit(1)

sys.setrecursionlimit(100000)

ERROR_DECODING_COUNTER = 0
NOTBASE64_COUNTER      = 0

def import_challenge(challenge_file, original_hash):
    with open(challenge_file, 'rb') as f:
        data          = f.read()
        sha256hash    = hashlib.sha256(data).hexdigest()

        assert sha256hash == original_hash
        return data

def truncate_string(value, max_length=80):
    return (value[:max_length] + '...') if len(value) > max_length else value

def truncate_filename(value, max_length=80):
    return (value[:max_length] + '_etc') if len(value) > max_length else value

def handle_str_argument(value):
    print("Handling string argument:", truncate_string(repr(value)))

    try:
        decoded = base64.b64decode(value)
        tree    = ast.parse(decoded)

        show_ast(tree)

    except Exception as e:
        """
        global ERROR_DECODING_COUNTER

        ""
        Generally, the errors are the following:

        Insert your flag: Error decoding: SyntaxError('invalid non-printable character U+001A', ('<unknown>', 1, 1, '\x1a´┐¢\x1d~V´┐¢', 1, 1))
        Good flag!Error decoding: Error('Invalid base64-encoded string: number of data characters (9) cannot be 1 more than a multiple of 4')
        Wrong flag!Error decoding: SyntaxError('invalid non-printable character U+001A', ('<unknown>', 1, 1, '\x1a´┐¢\x1d~V´┐¢', 1, 1))
        ""

        with open(f'python-rev-error_decoding_{ERROR_DECODING_COUNTER}.py', 'w') as f:
            f.write("Error decoding: " + repr(e))
            f.write("\n")
            f.write(value)

        ERROR_DECODING_COUNTER += 1
        """
        pass

def handle_notbase64_code(node):
    """ Rewrite the code as real python code """
    return astor.to_source(node)

def show_ast(node, annotate_fields=True, level=0):
    if isinstance(node, ast.Module):
        if len(node.body) == 1 and isinstance(node.body[0], ast.Expr):
            expr_node = node.body[0]
            if isinstance(expr_node.value, ast.Call) and \
               isinstance(expr_node.value.func, ast.Name) and \
               expr_node.value.func.id == 'exec' and \
               isinstance(expr_node.value.args, list) and \
               len(expr_node.value.args) == 1 and \
               isinstance(expr_node.value.args[0], ast.Call) and \
               isinstance(expr_node.value.args[0].func, ast.Name) and \
               expr_node.value.args[0].func.id == 'b64decode':
                handle_str_argument(expr_node.value.args[0].args[0].s)
        else:
            global NOTBASE64_COUNTER
            with open(f'python-rev-ast_{NOTBASE64_COUNTER}.py', 'w') as f:
                f.write(handle_notbase64_code(node))

            NOTBASE64_COUNTER += 1

    if isinstance(node, ast.AST):
        print('  ' * level + node.__class__.__name__)
        if annotate_fields:
            for name, value in ast.iter_fields(node):
                if isinstance(value, ast.AST):
                    show_ast(value, annotate_fields, level + 2)
                else:
                    if name == 'args' and isinstance(value, list):
                        # Check if it's a list of a single string argument
                        if len(value) == 1 and isinstance(value[0], ast.Str):
                            handle_str_argument(value[0].s)

                    truncated_value = truncate_string(repr(value))
                    print('  ' * (level + 1) + f'{name}: {truncated_value}')
                    show_ast(value, annotate_fields, level + 2)
        else:
            for child in ast.iter_child_nodes(node):
                show_ast(child, annotate_fields, level + 1)

    elif isinstance(node, list):
        for child in node:
            show_ast(child, annotate_fields, level)
    else:
        truncated_value = truncate_string(repr(node))
        print('  ' * level + truncated_value)

def first_step():
    chall_code = import_challenge(
            'python-rev-for-freaks/python_freak.py',
            'b9a8a345bd6020d3e8b02fb061e7cd7deb3d2ed1d39674267afbb64660eccafe')

    tree = ast.parse(chall_code)
    show_ast(tree)

if __name__ == '__main__':
    first_step()

# /usr/bin/docker run -it --rm -v $(pwd):/data -w /data python:3.11 bash python-rev-solver.sh -i
