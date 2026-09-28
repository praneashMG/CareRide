import re

filename = 'home2.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<a href="scheduling.html" class="btn-primary text-lg px-8 py-3">',
    '<a href="scheduling.html" class="btn-primary text-lg px-8 py-3 whitespace-nowrap inline-flex justify-center items-center">'
)

content = content.replace(
    '<a href="services.html" class="btn-outline text-lg px-8 py-3">',
    '<a href="services.html" class="btn-outline text-lg px-8 py-3 whitespace-nowrap inline-flex justify-center items-center">'
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated buttons in home2.html')
