from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='SpotToBee',
    version='1.0.3',
    author='Brendan Stupik',
    author_email='brndst@protonmail.com',
    description='Convert a CSV or Spotify playlist URL to a MusicBee smart playlist',
	long_description=long_description,
    long_description_content_type="text/markdown",
	license='MIT',
    url='https://github.com/Brendan00x0/SpotToBee',
    install_requires=[
		'spotipy>=2.0.0',
		'pandas>=1.0.0',
		'configparser>=5.0.0'
	],
    entry_points={
        'console_scripts': [
            'SpotToBee = SpotToBee:main'
        ]
    }
)
