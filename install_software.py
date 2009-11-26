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

import os

apps = []

for entry in open('programas_disponibles.txt'):
    desc, name = entry.strip().split(';')
    option = raw_input("Instalar %s ? (s/n): " % desc)
    if option.lower() == 's':
        apps.append(name)

print "\n------------------------------------\n\n"

option = raw_input("Confirma instalar lo seleccionado? (s/n): ")
if option.lower() == 's':
   os.system("aptitude install " + " ".join(apps))
