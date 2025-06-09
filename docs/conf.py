# -- Basic project info --
project = 'UHC Card'
author = 'My5.tv/activate'
release = '1.0.0'

# -- Extensions (none needed) --
extensions = []

# -- Paths --
templates_path = []  # No need if you're not using Sphinx templates
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output --
html_theme = 'alabaster'  # Minimal theme, required but won't affect your HTML files

# Static files like CSS
html_static_path = ['_static']

# Hide "View page source"
html_show_sourcelink = False

# Disable Sphinx branding
html_theme_options = {
    'show_powered_by': False,
}

# Favicon (optional)
html_favicon = 'favicon.ico'  # Only if placed in docs/
