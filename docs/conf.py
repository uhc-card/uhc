project = 'UHC Card'
author = 'UHC Card'
release = '1.0.0'

extensions = []
templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'  # Required, but doesn't affect your index.html
html_static_path = ['_static']
html_extra_path = ['.']  # ← copies index.html to output

html_show_sourcelink = False
html_theme_options = {
    'show_powered_by': False,
}
