from subprocess import run

process = run(['du', '-h', 'lorem.txt'], capture_output=True, text=True)

size = process.stdout.split()[0]

print(size)
