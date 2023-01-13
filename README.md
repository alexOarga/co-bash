# _co:bash_ - Cohere powered bash commands

![pypi](https://img.shields.io/pypi/v/co-bash)

This is a CLI tool for converting natural language into
bash commands. It is powered by [Cohere](https://cohere.ai).

# Install

_co:bash_ can be installed via `pip`:

    pip install co-bash

# Setup

To use _co:bash_ you will need your own Cohere API key. You can
get one at [cohere.ai](https://cohere.ai).

You can set your API key in the environment variable `COHERE_API_KEY`.

```bash
export COHERE_API_KEY=XXXXXXXXXX
```

I suggest adding this to your `.bashrc` file.

`[Optional]` You can also set the Cohere model you want to use
with the environment variable `COHERE_MODEL`:

```bash
export COHERE_MODEL=xlarge
```

# Usage

Just use the `co` command to run _co:bash_:

```console
$ co <arguments>
```

# Example

```console
$ co create a git commit with message 'initial commit'
Suggested command:
    git commit -m 'initial commit'
Execute? [y/N]: y
[master (commit-raíz) d55572b] initial commit
 19 files changed, 561 insertions(+)
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 co/__init__.py
 create mode 100644 co/cohere.py
 create mode 100644 co/constants.py
 create mode 100644 co/entrypoint.py
```