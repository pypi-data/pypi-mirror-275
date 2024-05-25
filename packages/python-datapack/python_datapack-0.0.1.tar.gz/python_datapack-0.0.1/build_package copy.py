
import os
commands = [
	"py -m pip install --upgrade pip setuptools build twine",
	"py -m build",
	"py -m twine upload --repository python_datapack dist/*"
]

for command in commands:
	if os.system(command) != 0:
		print(f"Error while executing '{command}'")
		exit(1)

