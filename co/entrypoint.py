import click
import subprocess
import os
from co.utils import get_key, get_model, get_distro_info
from co.cohere import generate
from co.prompt import generate_prompt


@click.command()
@click.argument('cmd', metavar='<The bash command you are searching for>', nargs=-1)
def co(cmd):
    # Generate prompt
    cmd = ' '.join(list(cmd))
    if len(cmd) == 0:
        print("Usage: co <description of the command>")
        return
    pwd = os.getcwd()
    distro_info = get_distro_info()
    prompt = generate_prompt(distro_info, pwd, cmd)
    # Get key and model
    key = get_key()
    model = get_model()
    # Generate command
    generation = generate(prompt, key, model)
    suggestion = generation.generations[0].text
    if len(suggestion) > 0:
        suggestion = suggestion[1:] # remove first space
    if click.confirm(f"Suggested command:\n    {suggestion}\nExecute?"):
        cmd = [c for c in suggestion.split(' ') if len(c) > 0]
        subprocess.run(cmd, cwd=pwd, shell=True)
    else:
        print("Canceled")


if __name__ == '__main__':
    co()
