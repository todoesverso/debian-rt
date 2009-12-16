#!/usr/bin/env python

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

import sys
import os
import re
import gettext

TRANSLATION_DOMAIN = "debian-rt"
LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")

gettext.install(TRANSLATION_DOMAIN, LOCALE_DIR)

# Check if we are root
#if os.geteuid() != 0:
#    print "You must be root to run this script."
#    sys.exit(1)

file = '/etc/passwd'
passwd = open(file, "r")
users_list = []

for line in passwd:
    user = re.match('^\w+', line)
    if user:
        real = re.match('.*/home/'+user.group()+'.*', line)
        really_real = re.match('.*100\d.*', line)
        if real and really_real:
            users_list.append(user.group())

print users_list            

