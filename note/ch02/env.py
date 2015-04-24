__author__ = 'Christen'

# Getting the version numbers of Qt, SIP and PyQt

# When you report a bug in PyQt you need to supply information about the configuration you are using,
# including the versions of the Qt library, SIP and PyQt modules.
# The following code should help.

from PyQt4.QtCore import QT_VERSION_STR

from PyQt4.pyqtconfig import Configuration

print("Qt version:", QT_VERSION_STR)

cfg = Configuration()

print("SIP version:", cfg.sip_version_str)

print("PyQt version:", cfg.pyqt_version_str)




