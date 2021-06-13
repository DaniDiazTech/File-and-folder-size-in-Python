import os
from humanize import naturalsize

size = os.stat('lorem.txt').st_size

print(size)
print(naturalsize(size))