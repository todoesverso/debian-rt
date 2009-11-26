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
import shutil
import datetime
import os
import re

#if len(sys.argv) < 2:
#    sys.exit(1)

# Check if we are root
#if os.geteuid() != 0:
#    print "You must be root to run this script."
#    sys.exit(1)

now = datetime.datetime.now()
#path        = '/etc/secusity/'
path        = '/tmp/'
file        = path + 'limits.conf'
file_bkp    = file + '.' + now.strftime("%Y%m%d%H%M%S") + '.back'


# Create backup of the file.
if os.path.isfile(file):
    try:
        shutil.copy(file, file_bkp)
    except:
        print "Could not copy " + file + " into " + file_bkp
        sys.exit(1) 
else:
    print "The file " + file + " does not exist"
    sys.exit(1) 

# Strings to be added
audio_h         = "#@audio: Automatically added by debian-rt script.\n"
audio_msg       = "#@audio: The file " + file_bkp + " was created\n"

audio_rtprio    = "@audio           -   rtprio      99\n"
audio_nice      = "@audio           -   nice        -10\n"
audio_memlock   = "@audio           -   memlock     unlimited\n"
audio_list      = [audio_h, audio_msg, audio_rtprio, audio_nice, audio_memlock]

# Remove any line with "@audio" 
lineas = [l for l in open(file) if not "@audio" in l]
out = open(file, "w")
out.writelines(lineas)

# Now add the lines we want
out.writelines(audio_list)

# Finish 
out.close()
sys.exit(0)


