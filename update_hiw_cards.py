import re

filename = 'how-it-works.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Step 1
content = content.replace(
    '''<h3 class="text-xl font-bold text-primary-text mb-3">1. Background & Motor Vehicle Check</h3>
                        <p class="text-secondary-text text-sm flex-grow">We conduct national and local criminal background checks, sex offender registry screenings, and require a flawless 5-year driving history.</p>''',
    '''<h3 class="text-xl font-bold text-primary-text mb-3">1. Background & Driving Check</h3>
                        <p class="text-secondary-text text-sm flex-grow">We conduct national and local criminal background checks, sex offender registry screenings, and require a flawless 5-year driving history.</p>'''
)

# Update Step 2 (Title is same, text is same, just making sure)
content = content.replace(
    '''<h3 class="text-xl font-bold text-primary-text mb-3">2. Clinical Safety Training</h3>
                        <p class="text-secondary-text text-sm flex-grow">Every driver must hold active CPR, Basic Life Support, and First Aid certifications, plus training in secure wheelchair tie-down procedures.</p>''',
    '''<h3 class="text-xl font-bold text-primary-text mb-3">2. Clinical Safety Training</h3>
                        <p class="text-secondary-text text-sm flex-grow">Every driver must hold active CPR, Basic Life Support, and First Aid certifications, plus training in secure wheelchair tie-down procedures.</p>'''
)

# Update Step 3
content = content.replace(
    '''<h3 class="text-xl font-bold text-primary-text mb-3">3. Empathy & Dementia Training</h3>
                        <p class="text-secondary-text text-sm flex-grow">Drivers complete specialized courses on interacting with seniors, managing cognitive decline behaviors, and providing compassionate emotional support.</p>''',
    '''<h3 class="text-xl font-bold text-primary-text mb-3">3. Empathy & Dementia Training</h3>
                        <p class="text-secondary-text text-sm flex-grow">All drivers complete specialized courses on interacting safely with seniors, managing cognitive decline behaviors, and providing compassionate, dedicated emotional support.</p>'''
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated how-it-works.html cards')
