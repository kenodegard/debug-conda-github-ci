import os
from subprocess import check_output
from conda.base.context import context


if __name__ == "__main__":
    env_name = "py313"
    env_path = os.path.join(context.root_prefix, "..", env_name)
    output = check_output(
        ["conda", "run", "-p", env_path, "which", "python"], 
        universal_newlines=True,
    )
    print(output)
