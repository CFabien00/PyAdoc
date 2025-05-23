# PyAdoc

**PyAdoc** is a command-line tool that extracts docstrings from all Python files in a given directory,
and compiles them into a single file in [AsciiDoc](https://asciidoc.org/) format.

## Installation

```bash
pip install git+https://github.com/CFabien00/PyAdoc.git
```

### Localy (dev)

Clone and install using `pip` :

```shell
git clone https://github.com/tonutilisateur/pyadoc.git
cd pyadoc
python -m build
pip install dist/pyadoc-0.1.0-py3-none-any.whl
```

## Usage

```shell
pyadoc <source_repository> <destination_repository_of_adoc_file>
```

Example :

```shell
pyadoc ~/workspace/my_project_python ~/workspace/docs
```

This will create a documentation.adoc file in the destination directory,
containing all the docstrings extracted from the .py files in the source directory.

### Result example

```adoc
:toc:
:sectnums:
:toclevels: 2
:toc-title: Code overview

== /path/to/this_file.py

=== Classe : MyCustomClass(_InheritObj_)

This object is used for something.

==== _create_something

Creates something somehow

*@params* :

* foo : str
* bar : float
```

## Structure

```
pyadoc/
├── pyadoc/
│   ├── __init__.py
│   ├── main.py
│   └── core.py
├── pyproject.toml
└── README.md
```

## Development

The CLI entry point is defined in `pyproject.toml` using `[project.scripts]` :

```toml
[project.scripts]
pyadoc = "pyadoc.main:main"
```

This allows **_pyadoc_** to be used as a system command after installation with `pip`.

### TODO

* [ ] Support other format than AsciiDoc (Markdown, HTML, …)

* [ ] Advance CLI options (files to exclude, custom format)

* [ ] Unit Tests

## Author

CFabien00 - https://github.com/CFabien00