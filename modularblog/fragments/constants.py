"""
Values that are used throughout the app
"""

CODE_LANGUAGE_GENERIC = 'generic'
CODE_LANGUAGE_PYTHON = 'python'
CODE_LANGUAGE_BASH = 'bash'
CODE_LANGUAGE_JAVASCRIPT = 'javascript'
CODE_LANGUAGE_HTML = 'html'
CODE_LANGUAGE_CSS = 'css'

CODE_LANGUAGE_CHOICES = (
    (CODE_LANGUAGE_GENERIC, 'Generic'),
    (CODE_LANGUAGE_PYTHON, 'Python'),
    (CODE_LANGUAGE_BASH, 'Bash'),
    (CODE_LANGUAGE_JAVASCRIPT, 'JavaScript'),
    (CODE_LANGUAGE_HTML, 'HTML'),
    (CODE_LANGUAGE_CSS, 'CSS'),
)

EMBED_TYPE_RAW = 'raw'
EMBED_TYPE_VIMEO = 'vimeo'
EMBED_TYPE_YOUTUBE = 'youtube'
EMBED_TYPE_TWEET = 'tweet'
EMBED_TYPE_INSTAGRAM = 'instagram'

EMBED_TYPE_CHOICES = (
    (EMBED_TYPE_RAW, 'Raw'),
    (EMBED_TYPE_VIMEO, 'Vimeo'),
    (EMBED_TYPE_YOUTUBE, 'Youtube'),
    (EMBED_TYPE_TWEET, 'Tweet'),
    (EMBED_TYPE_INSTAGRAM, 'Instagram'),
)
