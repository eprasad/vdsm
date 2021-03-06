#
# Copyright 2012 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#


"""
vdsm compatiblity for old netinfo module required by
the rhevm-3.0 vdsm-bootstrap package.
"""


import subprocess


from vdsm.netinfo import *


#
# old bootstrap does not start libvirtd
#
subprocess.Popen(
    ['/sbin/service', 'libvirtd', 'start'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    close_fds=True,
)
