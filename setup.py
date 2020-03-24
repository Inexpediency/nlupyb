try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='bigboisbot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'answer_generator',
        'config',
        'dataset',
        'main',
        ],
    # libraries=[
    #     'scipy',
    #     'numpy',
    #     'setuppy-generator',
    #     'python-telegram-bot',
    #     'scikit-learn',
    #     'python-telegram-bot'
    #     'nltk',
    #     ],
    scripts='main.py'
)
