import codecs

import setuptools

with codecs.open("README.rst", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(name='searchlogit',
                 version='0.3.62',
                 description='Extensions for a Python package for \
                              GPU-accelerated estimation of mixed logit models.',
                 long_description=long_description,
                 long_description_content_type="text/x-rst",
                 url='https://github.com/RyanJafefKelly/searchlogit',
                 author='Ryan Kelly, Prithvi Beeramoole, Zeke Ahern and Alexander Paz',
                 author_email='ryan@kiiii.com',
                 license='MIT',
                 packages=['searchlogit'],
                 zip_safe=False,
                 python_requires='>=3.5',
                 install_requires=[
                     'numpy>=1.13.1',
                     'scipy>=1.0.0'
                 ])
