# system76-driver: Universal driver for System76 computers
# Copyright (C) 2005-2013 System76, Inc.
#
# This file is part of `system76-driver`.
#
# `system76-driver` is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# `system76-driver` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with `system76-driver`; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Gtk UI.
"""

import platform

from gi.repository import GLib, Gtk

from . import __version__, get_datafile


GLib.threads_init()


class UI:
    def __init__(self, model, product, dry=False):
        assert isinstance(model, str)
        assert isinstance(product, dict)
        assert isinstance(dry, bool)
        self.model = model
        self.product = product
        self.dry = dry
        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_datafile('gtk3.glade'))
        self.window = self.builder.get_object('mainWindow')
        self.window.connect('destroy', Gtk.main_quit)

        self.builder.get_object('sysName').set_text(product['name'])
        self.builder.get_object('sysModel').set_text(model)
        self.builder.get_object('ubuntuVersion').set_text(platform.dist()[1])
        self.builder.get_object('driverVersion').set_text(__version__)

    def run(self):
        self.window.show()
        Gtk.main()

