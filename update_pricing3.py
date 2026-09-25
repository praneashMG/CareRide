import os
import re

filename = 'pricing.html'
with open(filename, 'r', encoding='utf-8') as f: content = f.read()

match = re.search(r'<!-- SECTION 1 - HERO.*?<!--\s*=*\s*-->\s*<!-- SECTION 2', content, re.DOTALL | re.IGNORECASE)
if not match:
    match = re.search(r'<!-- SECTION 1 - HERO.*?<!-- SECTION 2', content, re.DOTALL | re.IGNORECASE)

if match:
    badge = '<i class="fa-solid fa-tag"></i> Transparent & Upfront Pricing'
    title = 'Simple, Predictable <br class="hidden sm:block"/><span class="text-blue-400">Pricing</span>'
    desc = 'No hidden fees. No surge pricing. Just clear rates for professional care.'
    img_src = 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=1920&q=80'
    img_alt = 'Pricing Hero'
    buttons = '<div class="flex flex-col sm:flex-row gap-4 justify-center items-center">\n                    <a href="#packages" class="bg-blue-600 hover:bg-blue-500 text-white transition-colors duration-300 font-bold px-8 py-3 rounded-lg shadow-lg text-lg w-full sm:w-auto inline-block text-center">View Packages</a>\n                </div>'

    new_hero = f'''<!-- ================================================== -->
        <!-- SECTION 1 - HERO (Centered Layout) -->
        <!-- ================================================== -->
        <section class="relative pt-32 pb-24 lg:pt-48 lg:pb-32 overflow-hidden flex items-center justify-center min-h-[60vh]">
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
        </section>\n\n        <!-- ================================================== -->\n        <!-- SECTION 2'''
    
    new_content = content.replace(match.group(0), new_hero)
    with open(filename, 'w', encoding='utf-8') as f: f.write(new_content)
    print('Updated pricing.html')
else:
    print('Still no match for SECTION 2 block')
