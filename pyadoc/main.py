import sys

from pyadoc.core import DocstringsDocumentCreator


def main():
    if len(sys.argv) != 3:
        print("Usage: pyadoc <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    docs = DocstringsDocumentCreator(input_dir, output_dir).create_docstring_doc()
    print(f"Documentation générée dans {docs}")
