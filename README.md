# Conda Run in Python Subprocess No Longer Works with Conda 25.3.1 on Windows
I create two test cases, the first is calling the conda run command directly on the command line: 
```shell
conda run -n py313 which python
```

The second is calling the same command from a Python script:
```python
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
```

Independent of the conda version this works fine on Linux and MacOs. 

But for windows this test fails for conda Version 25.3.1 while it works fine for 25.1.1. 
