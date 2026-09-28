import re

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-user-nurse"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Vetted Companions</h3>
                        <p class="text-secondary-text text-sm">All drivers undergo rigorous background checks, driving history reviews, and are CPR/First Aid certified.</p>
                    </div>''',
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow h-full flex flex-col">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-user-nurse"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Vetted Companions</h3>
                        <p class="text-secondary-text text-sm flex-grow">All of our drivers undergo rigorous background checks, comprehensive driving history reviews, and are fully CPR/First Aid certified.</p>
                    </div>'''
)

content = content.replace(
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-door-open"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Door-Through-Door</h3>
                        <p class="text-secondary-text text-sm">We don't just wait at the curb. We help passengers out of their homes, into the car, and safely into their destination.</p>
                    </div>''',
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow h-full flex flex-col">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-door-open"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Door-Through-Door</h3>
                        <p class="text-secondary-text text-sm flex-grow">We never just wait at the curb. We safely help passengers from their homes into their final destination.</p>
                    </div>'''
)

content = content.replace(
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-location-crosshairs"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Live Family Tracking</h3>
                        <p class="text-secondary-text text-sm">Monitor rides in real-time through the Family Dashboard. Receive SMS alerts when the ride begins and ends.</p>
                    </div>''',
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow h-full flex flex-col">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-location-crosshairs"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Live Family Tracking</h3>
                        <p class="text-secondary-text text-sm flex-grow">Easily monitor rides in real-time through the Family Dashboard. Receive SMS alerts when the ride begins and ends.</p>
                    </div>'''
)

content = content.replace(
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-wheelchair"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Accessible Vehicles</h3>
                        <p class="text-secondary-text text-sm">Our modern fleet includes vehicles equipped with wheelchair ramps and hydraulic lifts for full accessibility.</p>
                    </div>''',
    '''<div class="bg-background p-6 rounded-xl border border-border text-center hover:shadow-lg transition-shadow h-full flex flex-col">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                            <i class="fa-solid fa-wheelchair"></i>
                        </div>
                        <h3 class="text-lg font-bold text-primary-text mb-3">Accessible Vehicles</h3>
                        <p class="text-secondary-text text-sm flex-grow">Our modern and specialized fleet includes vehicles equipped with secure wheelchair ramps and hydraulic lifts for full accessibility.</p>
                    </div>'''
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html cards')
