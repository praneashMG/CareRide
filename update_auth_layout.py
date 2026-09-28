import re

for filename in ['login.html', 'signup.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact regex to replace the left panel
    pattern = r'<!-- Left Side - Brand Section -->.*?<!-- Right Side - .*? Form -->'
    
    replacement_form = 'Login' if filename == 'login.html' else 'Sign Up'

    replacement = f'''<!-- Left Side - Brand Section -->
            <div class="hidden md:flex md:w-5/12 flex-col bg-slate-50 dark:bg-slate-900 border-r border-border relative overflow-hidden">
                
                <!-- Text Content Top (Solid Background) -->
                <div class="p-8 pb-10 relative z-10 flex-shrink-0 bg-slate-50 dark:bg-slate-900">
                    <!-- Logo -->
                    <a href="index.html" class="text-3xl font-serif font-extrabold tracking-wide flex items-center gap-2 shrink-0">
                        <i class="fa-solid fa-hand-holding-heart text-accent"></i>
                        <span class="text-accent">CareRide</span>
                    </a>

                    <div class="mt-8">
                        <h2 class="text-3xl font-bold text-primary-text leading-tight mb-4">
                            Start Your<br>Care Journey<br>Today
                        </h2>
                        <p class="text-secondary-text text-sm">
                            Join 500+ families who trust CareRide for safe, compassionate senior transportation.
                        </p>
                    </div>
                </div>

                <!-- Image Bottom (No overlay) -->
                <div class="flex-grow relative">
                    <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1573497620053-ea5300f94f21?auto=format&fit=crop&w=1200&q=80');"></div>
                    <!-- Small gradient fading to white at the top to blend the image seamlessly -->
                    <div class="absolute inset-x-0 top-0 h-16 bg-gradient-to-b from-slate-50 dark:from-slate-900 to-transparent"></div>
                    
                    <!-- Quote Box Overlaid on Image -->
                    <div class="absolute bottom-8 left-8 right-8">
                        <div class="bg-background/95 backdrop-blur-md p-5 rounded-2xl border border-border shadow-lg">
                            <i class="fas fa-quote-left text-accent opacity-50 text-sm mb-2"></i>
                            <p class="italic text-sm text-primary-text">"CareRide gives me total peace of mind knowing my mother is safely escorted to every appointment."</p>
                            <p class="text-xs text-secondary-text mt-3">- Sarah M., Family Member</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Side - {replacement_form} Form -->'''

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filename}')
    else:
        print(f'Pattern not found in {filename}')
