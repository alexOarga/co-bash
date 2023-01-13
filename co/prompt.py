

def generate_prompt(distro_info, pwd, input_prompt):
    prompt = f"""
Here are some one line bash commands to perform certain tasks.
Here is some information that might be useful:
Distribution info: {distro_info}
Current directory: {pwd}

A one-line bash command to: not print stderr:
Command: $ 2>/dev/null

A one-line bash command to: add write, read and execution permissions to file test:
Command: $ chmod +rwx test

A one-line bash command to: list all files in the current folder that contain the letter a:
Command: $ ls . | grep a

A one-line bash command to: {input_prompt}
Command: $"""
    return prompt