import os, re
filename = 'contact.html'
with open(filename, 'r', encoding='utf-8') as f: content = f.read()

pattern = r'<div class="relative w-full h-\[400px\] lg:h-\[500px\] rounded-3xl overflow-hidden shadow-lg border border-border">.*?</ul>\s*</div>\s*</div>'
replacement = '''<div class="relative w-full h-[400px] lg:h-[500px] rounded-3xl overflow-hidden shadow-lg border border-border">
                    <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1680108873729!5m2!1sen!2sus" 
                        class="absolute inset-0 w-full h-full" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>'''

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if content != new_content:
    with open(filename, 'w', encoding='utf-8') as f: f.write(new_content)
    print('Updated contact.html with iframe map')
else:
    print('Failed to find map block in contact.html')
