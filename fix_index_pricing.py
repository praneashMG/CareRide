import os

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the Popular Ride Packages layout
# Header margin
content = content.replace(
    'text-center max-w-3xl mx-auto mb-12 flex flex-col items-center gap-4',
    'text-center max-w-3xl mx-auto mb-20 flex flex-col items-center gap-4'
)

# 2. Fix md:grid-cols-3 to lg:grid-cols-3 for the pricing cards (lines ~385)
content = content.replace(
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-8">\n                    <!-- Package 1 -->',
    '<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">\n                    <!-- Package 1 -->'
)

# 3. Change md:-translate-y-4 to lg:-translate-y-4 on the middle card
content = content.replace(
    'transform md:-translate-y-4',
    'transform lg:-translate-y-4'
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
