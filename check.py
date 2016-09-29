import platform
print "Python:", platform.python_version()
assert platform.python_version()[0] == '2'

import numpy as np
print 'numpy:', np.__version__

import pandas as pd
print 'pandas:', pd.__version__
assert pd.__version__[:4] == '0.18'

import matplotlib as plt
print 'matplotlib:', plt.__version__

import flask
print 'flask:', flask.__version__

import jupyter
print 'jupyter:', jupyter.__version__

print '\nCONGRATULATIONS! If you can see this, things should be fine..'
print '\nGood luck on the workshop :)'
