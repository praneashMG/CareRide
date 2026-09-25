import os
filename = 'services.html'
with open(filename, 'r', encoding='utf-8') as f: content = f.read()
new_content = content.replace('class="lg:col-span-2', 'class="md:col-span-2 lg:col-span-2')
if content != new_content:
    with open(filename, 'w', encoding='utf-8') as f: f.write(new_content)
    print('Updated services.html layout')
