import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

sys.path.append(os.path.abspath('_exts'))

extensions = []
master_doc = 'index'
highlight_language = 'php'

project = u'TitleNova API'
copyright = u'2020 Punctual Abstract'

version = '0'
release = '0.0.1'

html_extra_path = 'html'

lexers['php'] = PhpLexer(startinline=True)

