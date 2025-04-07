import os
from subprocess import run, PIPE, check_output
from conda.base.context import context
import sys
import re
from pathlib import Path


if __name__ == '__main__':
    env_name = "py313"
    env_path = os.path.join(context.root_prefix, "..", env_name)
    info = check_output(
        ["conda", "info"],
        universal_newlines=True,
    )
    print(info, file=sys.stderr)

    output = run(
        ["conda", "run", "-p", env_path, "which", "python"],
        universal_newlines=True,
        env={
            **os.environ,
            "CONDA_TEST_SAVE_TEMPS": "true",
        },
        check=True,
        stdout=PIPE,
        stderr=PIPE,
    )
    stdout = output.stdout
    stderr = output.stderr
    print(stdout)

    m = re.search(r"CONDA_TEST_SAVE_TEMPS :: .+ (\S+)\n", stderr)
    if m:
        batch = m.group(1)
        print(f"Batch file: {batch}", file=sys.stderr)
        print(Path(batch).read_text(), file=sys.stderr)
