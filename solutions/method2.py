from pathlib import Path
from humanize import naturalsize

size = Path('lorem.txt').stat().st_size

print(naturalsize(size))