import os
import re

filename = 'pricing.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<!-- SECTION 1 - HERO.*?<section.*?</section>', content, re.DOTALL | re.IGNORECASE)
if match:
    hero_block = match.group(0)
    
    badge_match = re.search(r'<div class="inline-flex[^>]*>(.*?)</div>', hero_block, re.DOTALL)
    badge = badge_match.group(1).strip() if badge_match else '<i class="fa-solid fa-tag"></i> Transparent Pricing'
    
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', hero_block, re.DOTALL)
    title = title_match.group(1).strip() if title_match else 'Pricing'
    title = re.sub(r'text-accent|text-primary-text|text-secondary-text', 'text-blue-400', title)
    
    desc_match = re.search(r'<p[^>]*>(.*?)</p>', hero_block, re.DOTALL)
    desc = desc_match.group(1).strip() if desc_match else 'Affordable transport'
    
    img_src = 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=1920&q=80'
    img_alt = 'Pricing Hero'
    
    btn1_style = "bg-blue-600 hover:bg-blue-500 text-white transition-colors duration-300 font-bold px-8 py-3 rounded-lg shadow-lg text-lg w-full sm:w-auto inline-block text-center"
    btn2_style = "bg-transparent border-2 border-white text-white hover:bg-white hover:text-gray-900 transition-colors duration-300 font-bold px-8 py-3 rounded-lg text-lg w-full sm:w-auto inline-block text-center"
    
    buttons = ""
    btn_matches = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', hero_block, re.DOTALL)
    if btn_matches:
        buttons = '<div class="flex flex-col sm:flex-row gap-4 justify-center items-center">\n'
        for i, (href, text) in enumerate(btn_matches):
            text = text.strip()
            style = btn1_style if i == 0 else btn2_style
            buttons += f'                    <a href="{href}" class="{style}">{text}</a>\n'
        buttons += '                </div>'

    new_hero = f'''<section class="relative pt-32 pb-24 lg:pt-48 lg:pb-32 overflow-hidden flex items-center justify-center min-h-[60vh]">
            <img src="{img_src}" alt="{img_alt}" class="absolute inset-0 w-full h-full object-cover object-top z-0">
            <div class="absolute inset-0 bg-gray-900/75 dark:bg-black/80 z-0 pointer-events-none"></div>
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-sm font-bold mb-6 shadow-sm">
                    {badge}
                </div>
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-tight mb-6">
                    {title}
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
                    {desc}
                </p>
                {buttons}
            </div>
        </section>'''
    
    new_section = "<!-- ================================================== -->\n        <!-- SECTION 1 - HERO (Centered Layout) -->\n        <!-- ================================================== -->\n        " + new_hero
    new_content = content.replace(hero_block, new_section)
    with open(filename, 'w', encoding='utf-8') as f: f.write(new_content)
    print('Updated pricing.html')
else:
    print('Still no match')
