# app.py
#
# Copyright 2021 Emmanuel Martín González
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
from math import pi, tau, e

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

TIMES_CHAR = "\u00d7"
DIVIDED_BY_CHAR = "\u00f7"
TAU_CHAR = "\u03c4"
PI_CHAR = "\u03c0"

OPERATORS = (TIMES_CHAR, DIVIDED_BY_CHAR, '+', '-', '^')

Ans = 0
class MainWindow(Gtk.Window):
    calc_box = [
        [TAU_CHAR, "e", "(", ")", "AC"],
        ["7", "8", "9", "^", "DEL"],
        ["4", "5", "6", TIMES_CHAR, DIVIDED_BY_CHAR],
        ["1", "2", "3", "+", "-"],
        ["0", ".", PI_CHAR, "Ans", "="]
    ]

    def __init__(self):
        super().__init__(title="Cafriess")
        self.set_size_request(200, 300)

        vertical_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(vertical_box)

        grid = Gtk.Grid()
        self.entry = Gtk.Entry()


        vertical_box.pack_end(grid, False, True, False)
        vertical_box.pack_end(self.entry, False, True, False)

        y = 0
        for row in self.calc_box:
            x = 0
            for column in row:
                button = Gtk.Button(label=column)
                button.set_hexpand(True)
                button.connect("clicked", self.on_button_clicked)
                grid.attach(button, x, y, 1, 1)
                x += 1
            y += 1

    def on_button_clicked(self, widget):
        label = widget.get_label()
        text_entered = self.entry.get_text()
        if label == "DEL":
            text_entered = text_entered[:-1]
            self.entry.set_text(text_entered)
        elif label == "AC":
            self.entry.set_text("")
        elif label == "=":
            global Ans
            text_entered = text_entered.replace(TIMES_CHAR, "*")
            text_entered = text_entered.replace(DIVIDED_BY_CHAR, "/")
            text_entered = text_entered.replace(PI_CHAR, "pi")
            text_entered = text_entered.replace(TAU_CHAR, "tau")
            text_entered = text_entered.replace("^", "**")
            try:
               self.entry.set_text(str(eval(text_entered))) #The eval() method returns the result evaluated from the expression.
               Ans = eval(text_entered)
            except (SyntaxError, NameError):
                self.entry.set_text("The entered values are not valid")
        else:
            if label in OPERATORS and text_entered[-1] in OPERATORS:
                text_entered = text_entered[:-1]
            elif len(text_entered) > 0 and\
                    label in (PI_CHAR, TAU_CHAR, "e", "Ans") and\
                    text_entered[-1] not in OPERATORS:
                text_entered += TIMES_CHAR
            text_entered += label
            self.entry.set_text(text_entered)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
