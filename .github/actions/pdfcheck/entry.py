import os
import subprocess
import sys

dir = os.path.dirname(__file__)
os.chdir(dir)

current_dir = os.getcwd()
print(f"Directory changed to {current_dir}")

runargs = sys.argv[1:]
print("Running command:\n" + " ".join(runargs))
subprocess.run(runargs)
