#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
# This file is part of debian-rt.                                       #
#                                                                       #
# debian-rt is free software: you can redistribute it and/or modify     #
# it under the terms of the GNU General Public License as published     #
# by the Free Software Foundation, either version 3 of the License,     #
# or (at your option) any later version.                                #
#                                                                       #
# debian-rt is distributed in the hope that it will be useful,          #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.       #
#########################################################################

import csv
import gettext
import os
import sys

TRANSLATION_DOMAIN = "debian-rt"
LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")

gettext.install(TRANSLATION_DOMAIN, LOCALE_DIR)

try:
    import apt
except ImportError:
    print _("Couldn't import apt module. "
            "Check if python-apt is correctly installed.")
    sys.exit(1)

cache = apt.Cache()
reader = csv.DictReader(open('apps_list.csv'))

for entry in reader:
    desc = entry['description']
    name = entry['name']
    if not cache.has_key(name):
        print _("Warning: the package %(name)s (%(desc)s) was not found "
                "in apt cache. Ignoring.") % {'name': name,
                                              'desc': desc}
        continue
    package = cache[name]
    if package.isInstalled and not package.isUpgradable:
        print _("Latest version of package %(name)s is already installed. "
                "Ignoring.") % {'name': name}
    elif package.isInstalled and package.isUpgradable:
        print _("Version %(ver)s of package %(name)s (%(desc)s) is installed."
                " Version %(cand)s is available.") % \
        {'name': name, 'desc': desc, 'ver': package.installed.version,
         'cand': package.candidate.version}
        option = raw_input(_("Upgrade? (y/n): "))
        if option.lower() == _('y'):
            package.markUpgrade()
    else:
        option = raw_input(_("Install %s ? (y/n): ") % desc)
        if option.lower() == _('y'):
            package.markInstall()

print "\n------------------------------------\n\n"

option = raw_input(_("Install selected packages? (y/n): "))
if option.lower() == _('y'):
    cache.commit(apt.progress.TextFetchProgress(),
                 apt.progress.InstallProgress())
