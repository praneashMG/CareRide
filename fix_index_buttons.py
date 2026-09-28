import re

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<a href="signup.html" class="btn-primary text-lg px-8 py-3">',
    '<a href="signup.html" class="btn-primary text-lg px-8 py-3 whitespace-nowrap inline-flex justify-center items-center">'
)

content = content.replace(
    '<a href="how-it-works.html" class="btn-outline text-lg px-8 py-3">',
    '<a href="how-it-works.html" class="btn-outline text-lg px-8 py-3 whitespace-nowrap inline-flex justify-center items-center">'
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated buttons in index.html')
