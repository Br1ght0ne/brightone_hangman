from setuptools import setup

setup(name='brightone_hangman',
      version='0.2',
      description='Simple hangman game',
      author='filalex77',
      url='https://github.com/filalex77/brightone_hangman',
      author_email='filalex77@gmail.com',
      license='MIT',
      packages=['brightone_hangman'],
      package_data={
          'brightone_hangman': ['easy', 'medium', 'hard']
      },
      zip_safe=False)
