AUTHOR = 'DCM Modeling Project Participants'
SITENAME = 'DCM Modeling Project'
SITEURL = "https://dcm-modeling.kg.ac.rs/output"

PATH = "content"

TIMEZONE = 'Europe/Belgrade'
DEFAULT_LANG = 'en'

# --- Theme ---
import attila
THEME = attila.get_path()

# --- Plugins ---
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'

# --- Markdown ---
MARKDOWN = {
    'extensions': ['attr_list']
}

# --- Static files ---
STATIC_PATHS = ['images']

# --- Covers ---
HOME_COVER = '/images/spine_cover1.png'

COPYRIGHT_YEAR = 2026

# --- URLs required by Attila ---
TAGS_URL = 'tags'
CATEGORIES_URL = 'category'

# --- Feeds (disabled for development) ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Pagination ---
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

# Menu items
MENUITEMS = [
    ('DCM Modeling', '/index.html'),
    ('News/Events', '/category/news.html'),
    ('Work Packages', '/pages/work-packages.html'),
    ('Deliverables', '/pages/deliverables.html'),
    ('Participants', '/pages/participants.html'),
    ('Contact', '/pages/contact.html'),
]
INDEX_URL = 'index.html'


SHOW_PAGES_ON_MENU = False

SOCIAL = (('twitter', 'https://twitter.com'),
          ('github', 'https://github.com/imilos'),
          ('envelope','mailto:milos.ivanovic@pmf.kg.ac.rs'))
