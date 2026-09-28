import re

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-accent text-white px-4 py-1 rounded-full text-sm font-bold uppercase tracking-wider"',
    'class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-accent text-white px-4 py-1 rounded-full text-sm font-bold uppercase tracking-wider whitespace-nowrap"'
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed MOST POPULAR badge wrapping in index.html')
