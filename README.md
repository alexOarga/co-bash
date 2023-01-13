# _co:bash_ - Cohere powered bash commands

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

```console
$ co <arguments>
```

# Example

```console
$ co list all available nvidia gpus and their usage
Suggested command:
    nvidia-smi
Execute? [y/N]: y
Fri Jan 13 13:45:49 2023       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.161.03   Driver Version: 470.161.03   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
