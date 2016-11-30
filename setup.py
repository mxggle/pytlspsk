import os
import subprocess
from distutils.core import setup, Extension

# build C extension
subprocess.call(['make', '-C', 'pytlspsk'])

setup(
  name = 'pytlspsk',
  packages = ['pytlspsk'], # this must be the same as the name above
  version = '0.1',
  description = 'OpenSSL TLS-PSK wrapper for Socket',
  author = 'Jignesh Vasoya',
  author_email = 'jigneshvasoya@gmail.com',
  url = 'https://github.com/jigneshvasoya/pytlspsk', # use the URL to the github repo
  download_url = 'https://github.com/jigneshvasoya/pytlspsk/tarball/0.1', # I'll explain this in a second
  keywords = ['OpenSSL', 'TLS-PSK', 'tlspsk', 'security', 'ssl socket'], # arbitrary keywords
  classifiers = [
      'Development Status :: 1 - Begining',
      'Intended Audience :: Developers',
      'License :: MIT License',
      'Operating System :: Linux - Ubuntu',
      'Programming Language :: Python',
      'Programming Language :: C',
      ],
  package_data={'pytlspsk': ['_ssl_psk.so']},
)
