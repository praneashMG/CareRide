import re

for filename in ['login.html', 'signup.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the left side brand section
    pattern = r'<!-- Left Side - Brand Section -->\s*<div class="hidden md:flex md:w-5/12 relative p-8 flex-col justify-between [^"]*">'
    
    replacement = '''<!-- Left Side - Brand Section -->
            <div class="hidden md:flex md:w-5/12 relative p-8 flex-col justify-between bg-cover bg-center border-r border-border" 
                 style="background-image: url('https://images.unsplash.com/photo-1573497620053-ea5300f94f21?auto=format&fit=crop&w=1200&q=80');">
                <!-- Soft overlay to maintain text contrast -->
                <div class="absolute inset-0 bg-white/85 dark:bg-slate-900/90 backdrop-blur-[2px]"></div>'''

    new_content = re.sub(pattern, replacement, content)
    
    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filename}')
    else:
        print(f'Pattern not found in {filename}')
