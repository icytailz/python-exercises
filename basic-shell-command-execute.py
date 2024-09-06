import subprocess

command = "df -h"

result = subprocess.run(
    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    print("Command output: \n", result.stdout)
else:
    print("Error:\n", result.stderr)
