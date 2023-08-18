from setuptools import setup

setup(
    packages=['yt'],
    package_dir={'yt': 'yt'},
    name='yt-prompt',
    version='0.0.5',
        entry_points = {
        "console_scripts": ['youtube = yt.yt:main']
        },
    description="Downloads Videos as mp4 files in best quality.",
        author = "Caraveo",
    author_email = "jon@ziawe.com",
    url = "https://github.com/Caraveo/yt-prompt",
)