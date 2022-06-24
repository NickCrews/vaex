
# -*- coding: utf-8 -*-
#
# vaex documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 26 10:05:05 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'IPython.sphinxext.ipython_console_highlighting',
    'nbsphinx',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.load_style',
	'sphinx_sitemap',
	'myst_parser',
]
# for sphinx_sitemap
html_baseurl = 'https://vaex.io/docs/'
# todo: might want to change this for multiple versions
sitemap_url_scheme = "{link}"
sitemap_filename = "sitemap-docs.xml"



import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# if not on_rtd:
# 	extensions.append('sphinxcontrib.googleanalytics')

# 	googleanalytics_id = 'UA-60052576-1'
# 	analytics_id = 'UA-60052576-1'
# Add any paths that contain templates here, relative to this directory.
#templates_path = ['ntemplates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'vaex'
copyright = u'2014, Maarten A. Breddels'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
if 1:
	import vaex.meta._version
	# The short X.Y version.
	version = vaex.meta._version.__version__
	# The full version, including alpha/beta/rc tags.
	release = vaex.meta._version.__version__
else:
	print("failed finding vaex module, try finding version")
	import sys
	import os
	import imp

	def system(cmd):
		print("Executing: ", cmd)
		ret = os.system(cmd)
		if ret != 0:
			print("error, return code is", ret)
			sys.exit(ret)

	path_version_file = os.path.join(os.path.dirname(__file__), "../../python/vaex/vaex/version.py")
	if not os.path.exists(path_version_file):
		system("version=`git describe --tags --long`; python/vaex/vaex/setversion.py ${version}")

	version = imp.load_source('version', path_version_file)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'
html_theme = "sphinx_book_theme"

# html_theme = "vaex_theme"
# html_theme_path = ['_theme']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = dict(
	# analytics_id='UA-60052576-1'  this is configured in rtfd.io
	# canonical_url="https://vaex.io/docs/",
	repository_url="https://github.com/vaexio/vaex",
	use_edit_page_button=True,
	use_repository_button=True,
	use_issues_button=True,
	path_to_docs="docs/source/",
	home_page_in_toc=True,
	extra_navbar="",
	navbar_footer_text="",
	extra_footer='Theme by the <a href="https://ebp.jupyterbook.org">Executable Book Project</a>',
	twitter_url="https://twitter.com/vaex_io",
)
# html_style = "helpme"

extra_navbar = "<h1>dsadsa</h2>"

html_sidebars = {
	"**": ["sbt-sidebar-footer.html", "sbt-sidebar-nav.html", "sidebar-search-bs.html"]
}
html_logo = "_static/logo-grey.svg"
html_favicon = "_static/vaex_alt.png"
html_baseurl = "https://vaex.io/docs/"

# templates_path = ['_templates']

# not sure if this helps, otherwise it does not work on rtd
html_context = dict(
	# canonical_url="https://vaex.io/docs/"
)

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['nstatic']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = [
		]

def update_conf_md():
	current = os.path.dirname(__file__)
	source = os.path.join(current, '../../packages/vaex-core/vaex/settings.py')
	root = os.path.join(current, '../../')
	dest = os.path.join(current, 'conf.md')
	time_source = os.path.getmtime(os.path.abspath(os.path.join(source)))
	time_dest = os.path.getmtime(os.path.abspath(os.path.join(dest)))
	should_update = time_source > time_dest
	if should_update:
		cmd = f"(cd {root}; vaex settings docgen)"
		print(cmd)
		err = os.system(cmd)
		if err != 0:
			raise RuntimeError('Error executing command')

update_conf_md()

# def convert(names, ext="html", include_source=True, include_dest=True):
# 	for name in names:
# 		source = "../../examples/{name}.ipynb".format(name=name)
# 		dest = "{name}.{ext}".format(name=name, ext=ext)
# 		should_make = True
# 		if os.path.exists(dest):
# 			time_source = os.path.getmtime(os.path.abspath(os.path.join(source)))
# 			time_dest = os.path.getmtime(os.path.abspath(os.path.join(dest)))
# 			should_make = time_source > time_dest
# 		cwd = os.getcwd()
# 		#cmd = "cd docs; cd source; jupyter-nbconvert {source} --to {ext} --output-dir={cwd} --output={dest}".format(source=source, cwd=cwd, ext=ext, dest=dest)
# 		cmd = "cd docs; cd source; jupyter-nbconvert {source} --to {ext} --output-dir={cwd} ".format(source=source, cwd=cwd, ext=ext, dest=dest)
# 		if should_make:
# 			print("executing %s" % cmd)
# 			os.system(cmd)
# 			if on_rtd:
# 				pass
# 				# nb convert on rtd puts the output in the same directory..
# 				#import shutil
# 				#shutil.move("../../examples/" + dest, dest)
# 		else:
# 			print("%s is already up to date" % name)
# 		if include_source:
# 			html_extra_path.append(source)
# 		if include_dest:
# 			html_extra_path.append(dest)
# convert("example_movies example_start example_volume_rendering example_virtual_columns example_tables".split(), "html", True, True)
# convert("tutorial_ipython_notebook advanced_plotting fileformat healpix_plotting".split(), "rst", True, False)


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'vaexdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'vaex.tex', u'vaex Documentation',
   u'Maarten A. Breddels', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'vaex', u'vaex Documentation',
     [u'Maarten A. Breddels'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'vaex', u'vaex Documentation',
   u'Maarten A. Breddels', 'vaex', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

autoclass_content = 'both'

autodoc_default_options = {
	'show-inheritance': True
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    's3fs': ('https://s3fs.readthedocs.io/en/latest', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'dask': ('https://docs.dask.org/en/latest/', None),
    'gcsfs': ('https://gcsfs.readthedocs.io/en/latest/', None),
    's3fs': ('https://s3fs.readthedocs.io/en/latest/', None),
    'pyarrow': ('https://arrow.readthedocs.io/en/stable/', None)
}

nbsphinx_thumbnails = {
    'example_jupyter_ipyvolume': 'screenshot/example_jupyter_ipyvolume.png',
    'example_jupyter_plotly': 'screenshot/example_jupyter_plotly.png',
}
exclude_patterns = ['**.ipynb_checkpoints']
