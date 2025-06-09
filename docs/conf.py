# -- Basic project info --
project = 'UHC Card'
author = 'UHC Card'
release = '1.0.0'

# -- Extensions --
extensions = []  # No Sphinx extensions needed for raw HTML

# -- Paths --
templates_path = []  # Not needed unless you use Jinja templates
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output --
html_theme = 'alabaster'  # Required by Sphinx, but doesn't affect raw HTML
html_static_path = ['_static']  # For loading CSS, JS, etc.
html_extra_path = ['.']  # ✅ This ensures index.html is included in the build output

# Hide Sphinx-specific features
html_show_sourcelink = False
html_theme_options = {
    'show_powered_by': False,
}

# Optional: if you have a favicon
html_favicon = 'favicon.ico'
