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
from common import *

# Printing messages
stdout  = True 
log     = False

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

# Check y the package 'util-linux' that provides the program chrt 
cache = apt.Cache()
pkg = cache['util-linux']

if not pkg.isInstalled:
    printrt ("The package 'util-linux' is not installed", stdout, log)
    printrt ("Installing 'util-linux' ...", stdout, log)
    # Mark util-linux for install
    pkg.markInstall()
    # Install the package   
    cache.commit()
else:
    printrt ("The package 'util-linux' is already installed", stdout, log)
    sys.exit(0)

# Copy the script to /etc/init.d/
if os.path.isfile(file):
    try:
        shutil.copy(file, file_final)
    except:
        print "Could not copy " + file + " into " + file_final
        sys.exit(1) 
else:
    print "The file " + file + " does not exist"
    sys.exit(1) 


# Finish 
sys.exit(0)


