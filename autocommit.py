import os
import subprocess

subprocess.call("git add .", shell=True)
subprocess.call("git commit -m \"`date`\"", shell=True)
subprocess.call("git push -u origin main", shell=True)




















#