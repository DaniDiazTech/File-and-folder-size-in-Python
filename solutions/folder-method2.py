from subprocess import run
from pathlib import Path

test_path = Path.home() / 'Documents/tests/'

process = run(['du', '-sh', test_path], capture_output=True, text=True)

size = process.stdout.split()[0]

print(size)