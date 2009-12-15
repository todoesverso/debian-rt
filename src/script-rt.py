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
import apt
import shutil
import gettext

TRANSLATION_DOMAIN = "debian-rt"
LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")

gettext.install(TRANSLATION_DOMAIN, LOCALE_DIR)

#if len(sys.argv) < 2:
#    sys.exit(1)

# Check if we are root
#if os.geteuid() != 0:
#    print "You must be root to run this script."
#    sys.exit(1)

#path        = '/etc/init.d/'
path        = '/tmp/'
file        = 'script-rt.sh'
file_final  = path + file
sym_link    = '/etc/rcS.d/S99rtimer'

# Check the package 'util-linux' that provides the program chrt 
cache = apt.Cache()
pkg = cache['util-linux']

if not pkg.isInstalled:
    print _("The package 'util-linux' is not installed")
    print _("Installing 'util-linux' ...")
    # Mark util-linux for install
    pkg.markInstall()
    # Install the package   
    try:
        cache.commit()
    except:
        print _("Could not install 'util-linux'")
        print _("Aborting ...")
        sys.exit(1)

# Copy the script to /etc/init.d/
if os.path.isfile(file):
    try:
        shutil.copy(file, file_final)
    except:
        print _("Could not copy %(file)s into %(file_final)s \n") 
                % {'file': file, 'file_final': file_final}
        sys.exit(1) 
else:
    print _("The file %(file)s does not exist") % {'file': file}
    sys.exit(1) 

# Make sure that the script has executable bit
os.chmod(file_final, 0755)

# Create the symbolic link
if not os.symlink(file_final, sym_link):
    print _("Could not create symlink %(sym_link)s ... \n") 
            % {'sym_link': sym_link}
    sys.exit(1)

# Finish 
sys.exit(0)
