# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eink_calendar', 'eink_calendar.api', 'eink_calendar.ui']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.100.0,<3.0.0',
 'google-auth-httplib2>=0.1.1,<0.2.0',
 'google-auth-oauthlib>=1.1.0,<2.0.0',
 'inky[example-depends,rpi]>=1.5.0,<2.0.0',
 'pillow>=10.0.1,<11.0.0',
 'pyxdg>=0.28,<0.29']

entry_points = \
{'console_scripts': ['eink-calendar = eink_calendar.__main__:main']}

setup_kwargs = {
    'name': 'eink-calendar',
    'version': '0.2.0',
    'description': 'Shows Google Calendar events on an Inky Impression display',
    'long_description': "# eInk Calendar\n\nDisplays Google Calendar events on an Inky Impression display connected to a\nRaspberry Pi.\n\n![Example showing how the UI looks](https://i.imgur.com/cKqnSmU.png)\n\n## Installation\n\nThis project is available on PyPI and can be installed with `pipx`.\n\n```bash\npipx install eink-calendar\n```\n\nThen, you will need to create a desktop OAuth2 client ID using the Google Cloud\nconsole. For details on how to do this, see\n[Google's Documentation][oauth2_client_docs].\n\nOnce you have created the client ID, download the client secret JSON file to\n`~/.local/share/eink-calendar/credentials.json`.\n\nThen, start the application:\n\n```bash\neink-calendar\n```\n\nA browser window will automatically open prompting you to give eInk Calendar\nread access to your calendars. Once this process completes, the application\nwill start. You only need to complete this process once.\n\n## Development\n\nIf you want to develop without the eInk display connected, start the\napplication with the following flag:\n\n```bash\neink-calendar --no-display\n```\n\nThe generated images will be opened using your image viewer instead.\n\n[oauth2_client_docs]: https://developers.google.com/identity/protocols/oauth2/native-app\n",
    'author': 'Tyler Compton',
    'author_email': 'xaviosx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
