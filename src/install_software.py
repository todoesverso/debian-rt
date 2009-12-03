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

import apt
import os
import csv

cache = apt.Cache()
reader = csv.DictReader(open('apps_list.csv'))

for entry in reader:
    desc = entry['description']
    name = entry['name']
    if not cache.has_key(name):
        print "Advertencia: el paquete %s (%s) no se encuentra en la cache \
de apt. Ignorando." % (name, desc)
        continue
    package = cache[name]
    if package.isInstalled and not package.isUpgradable:
        print "El paquete %s ya se encuentra instalado y actualizado. \
Ignorando" % name
        continue
    elif package.isInstalled and package.isUpgradable:
        print "El paquete %s (%s) se encuentra instalado en su versión %s.\n" \
              "La versión %s se encuentra disponible." % \
        (name, desc, package.installed.version, package.candidate.version)
        option = raw_input("Actualizar? (s/n): ")
        if option.lower() == 's':
            package.markUpgrade()
    else:
        option = raw_input("Instalar %s ? (s/n): " % desc)
        if option.lower() == 's':
            package.markInstall()

print "\n------------------------------------\n\n"

option = raw_input("Confirma instalar lo seleccionado? (s/n): ")
if option.lower() == 's':
    cache.commit(apt.progress.TextFetchProgress(),
                 apt.progress.InstallProgress())

