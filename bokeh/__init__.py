""" Bokeh is a Python interactive visualization library that targets modern
web browsers for presentation.

Its goal is to provide elegant, concise construction of novel graphics in the
style of d3.js, but also deliver this capability with high-performance
interactivity over very large or streaming datasets. Bokeh can help anyone
who would like to quickly and easily create interactive plots, dashboards,
and data applications.

For full documentation, please visit: https://bokeh.pydata.org

"""
from __future__ import absolute_import, print_function

# configure Bokeh version
from .util.version import __version__; __version__

# configure Bokeh logger
from .util import logconfig
del logconfig

# Configure warnings to always show, despite Python's active efforts
# to hide them from users.
import warnings
from .util.warnings import BokehDeprecationWarning, BokehUserWarning
warnings.simplefilter('always', BokehDeprecationWarning)
warnings.simplefilter('always', BokehUserWarning)

# imports below are names we want to make available in the bokeh
# module as transitive imports

from . import sampledata; sampledata

def license():
    ''' Print the Bokeh license to the console.

    Returns:
        None

    '''
    from os.path import join
    with open(join(__path__[0], 'LICENSE.txt')) as lic:
        print(lic.read())
