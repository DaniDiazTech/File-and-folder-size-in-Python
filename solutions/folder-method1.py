from pathlib import Path
from humanize import naturalsize

def get_size(path = '.'):
    size = 0

    for file_ in Path(path).rglob('*'):

        size += file_.stat().st_size
    
    return naturalsize(size)

test_path = Path.home() / 'Documents/tests/'

print(get_size(test_path))