"""Setup script for the Configa project.
"""
import setuptools


PACKAGES = [
    'logga>=1.0.0',
    'pylint>=1.6.4',
    'pytest>=2.9.2',
    'pytest-cov>=2.3.0',
    'sphinx_rtd_theme>=0.1.10a0',
    'twine',
    'Sphinx>=1.4.5',
]

SETUP_KWARGS = {
    'name': 'configa',
    'version': '1.0.0',
    'description': 'Python config wrapper, with added goodness',
    'author': 'Lou Markovski',
    'author_email': 'lou.markovski@gmail.com',
    'url': 'https://github.com/loum/configa',
    'install_requires': PACKAGES,
    'packages': setuptools.find_packages(),
    'package_data': {
        'configa': [
        ],
    },
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
}

setuptools.setup(**SETUP_KWARGS)
