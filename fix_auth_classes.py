import re

for filename in ['login.html', 'signup.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        'class="bg-background p-5 rounded-2xl border border-border shadow-lg"',
        'class="bg-white/95 dark:bg-slate-900/95 backdrop-blur-md p-5 rounded-2xl border border-gray-200 dark:border-white/10 shadow-lg"'
    )
    
    content = content.replace('text-primary-text', 'text-slate-800 dark:text-white')
    content = content.replace('text-secondary-text', 'text-gray-500 dark:text-gray-400')
    content = content.replace('border-border', 'border-gray-200 dark:border-white/10')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Fixed invalid classes in {filename}')
