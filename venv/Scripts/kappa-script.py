#!E:\Lumiere\report_generator\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kappa','console_scripts','kappa'
__requires__ = 'kappa'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kappa', 'console_scripts', 'kappa')()
    )
