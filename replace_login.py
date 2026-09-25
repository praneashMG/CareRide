import os, re
filename = 'login.html'
with open(filename, 'r', encoding='utf-8') as f: content = f.read()

pattern = r'<!-- Left Side - Brand Section -->.*?<!-- Right Side - Login Form -->'
replacement = """<!-- Left Side - Brand Section -->
            <div class="hidden md:flex md:w-5/12 relative p-8 flex-col justify-between bg-slate-50 dark:bg-slate-800/50 border-r border-border">
                <div class="absolute inset-0 opacity-[0.03] dark:opacity-[0.05] pointer-events-none">
                    <i class="fas fa-hand-holding-heart text-9xl absolute bottom-4 right-4 text-accent"></i>
                    <i class="fas fa-car-side text-7xl absolute top-10 left-4 text-accent"></i>
                </div>

                <div class="relative z-10">
                    <!-- Logo -->
                    <a href="index.html" class="text-3xl font-serif font-extrabold tracking-wide flex items-center gap-2 shrink-0">
                        <i class="fa-solid fa-hand-holding-heart text-accent"></i>
                        <span class="text-accent">CareRide</span>
                    </a>

                    <div class="mt-12">
                        <h2 class="text-3xl font-bold text-primary-text leading-tight mb-4">
                            Start Your<br>Care Journey<br>Today
                        </h2>
                        <p class="text-secondary-text text-sm">
                            Join 500+ families who trust CareRide for safe, compassionate senior transportation.
                        </p>
                    </div>
                </div>

                <div class="relative z-10 mt-12">
                    <div class="bg-white dark:bg-slate-900/50 p-5 rounded-2xl border border-border">
                        <i class="fas fa-quote-left text-accent opacity-50 text-sm mb-2"></i>
                        <p class="italic text-sm text-primary-text">"CareRide gives me total peace of mind knowing my mother is safely escorted to every appointment."</p>
                        <p class="text-xs text-secondary-text mt-3">- Sarah M., Family Member</p>
                    </div>
                </div>
            </div>

            <!-- Right Side - Login Form -->"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
if content != new_content:
    with open(filename, 'w', encoding='utf-8') as f: f.write(new_content)
    print('Updated login.html')
else:
    print('Pattern not found')
