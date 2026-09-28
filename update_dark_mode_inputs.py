import os, glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Inject color-scheme
    if 'color-scheme: dark;' not in content:
        content = content.replace("html[data-theme='dark'] {", "html[data-theme='dark'] {\n            color-scheme: dark;")
        
    # 2. Inject calendar picker invert rule
    picker_rule = '''
        /* Fix native date/time picker icons in dark mode */
        html[data-theme='dark'] input[type="date"]::-webkit-calendar-picker-indicator,
        html[data-theme='dark'] input[type="time"]::-webkit-calendar-picker-indicator,
        html[data-theme='dark'] input[type="datetime-local"]::-webkit-calendar-picker-indicator {
            filter: invert(1) brightness(1.5);
        }
    </style>'''
    
    if '::-webkit-calendar-picker-indicator' not in content:
        content = content.replace('</style>', picker_rule)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filename}')
