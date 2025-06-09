project = 'UHC Card'
author = 'UHC Card'
release = '1.0.0'

extensions = []
templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'  # ✅ Optional but recommended

html_theme = 'alabaster'
html_static_path = ['_static']
html_extra_path = ['.']

html_show_sourcelink = False
html_theme_options = {
    'show_powered_by': False,
}
