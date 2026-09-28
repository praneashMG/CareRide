import re

filename = 'drivers.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Standard 1
content = content.replace(
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-fingerprint"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Extensive Backgrounds</h3>
                        <p class="text-secondary-text text-sm">National and county-level criminal background checks, plus continuous monitoring against sex offender registries.</p>
                    </div>''',
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors h-full flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-fingerprint"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Extensive Backgrounds</h3>
                        <p class="text-secondary-text text-sm flex-grow">National and county-level criminal background checks, plus continuous active monitoring against all sex offender registries.</p>
                    </div>'''
)

# Update Standard 2
content = content.replace(
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-car-burst"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Flawless Driving History</h3>
                        <p class="text-secondary-text text-sm">We require a minimum of 5 years clean driving history, verified through the Department of Motor Vehicles.</p>
                    </div>''',
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors h-full flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-car-burst"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Clean Driving Records</h3>
                        <p class="text-secondary-text text-sm flex-grow">We strictly require a minimum of five years clean driving history verified through the DMV.</p>
                    </div>'''
)

# Update Standard 3
content = content.replace(
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-vial"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Routine Drug Screening</h3>
                        <p class="text-secondary-text text-sm">Pre-employment 10-panel drug testing is mandatory, followed by randomized screening throughout employment.</p>
                    </div>''',
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors h-full flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-vial"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Routine Drug Testing</h3>
                        <p class="text-secondary-text text-sm flex-grow">Pre-employment ten-panel drug testing is mandatory, followed by rigorous randomized screening throughout their entire employment.</p>
                    </div>'''
)

# Update Standard 4
content = content.replace(
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-chalkboard-user"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Behavioral Interviews</h3>
                        <p class="text-secondary-text text-sm">Multiple rounds of interviews designed to test empathy, patience, and problem-solving in high-stress situations.</p>
                    </div>''',
    '''<div class="bg-card p-8 rounded-2xl shadow-sm border border-border hover:border-accent transition-colors h-full flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/30 text-accent rounded-full flex items-center justify-center text-2xl mb-6 shadow-sm">
                            <i class="fa-solid fa-chalkboard-user"></i>
                        </div>
                        <h3 class="text-xl font-bold text-primary-text mb-3">Behavioral Interviews</h3>
                        <p class="text-secondary-text text-sm flex-grow">Multiple interview rounds are designed to test empathy, patience, and problem-solving in high-stress medical situations.</p>
                    </div>'''
)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated drivers.html cards')
