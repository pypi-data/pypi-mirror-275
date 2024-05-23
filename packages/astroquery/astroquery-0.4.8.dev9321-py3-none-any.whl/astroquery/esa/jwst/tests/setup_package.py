# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os


# setup paths to the test data
# can specify a single file or a list of files
def get_package_data():
    paths = [os.path.join('data', '*.vot'),
             os.path.join('data', '*.xml'),
             os.path.join('data', '*.zip'),
             os.path.join('data', '*.gz'),
             os.path.join('data', '*.tar'),
             os.path.join('data', '*.fits'),
             os.path.join('data', '*.txt'),
             ]  # etc, add other extensions
    # you can also enlist files individually by names
    # finally construct and return a dict for the sub module
    return {'astroquery.esa.jwst.tests': paths}
