import re

filename = 'how-it-works.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div class="bg-card p-6 rounded-2xl border border-border hover:border-accent transition-colors">',
    '<div class="bg-card p-6 rounded-2xl border border-border hover:border-accent transition-colors h-full flex flex-col">'
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated FAQ cards in how-it-works.html')
