import gi
from math import pi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

Ans = 0

class MyWindow(Gtk.Window):
    calc_box = [
        ["7", "8", "9", "DEL", "AC"],
        ["4", "5", "6", "\u00d7", "\u00f7"],
        ["1", "2", "3", "+", "-"],
        ["0", ".", "\u03c0" ,"Ans", "="]
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
            x = 0
            x = Ans # The eval() method don´t recognice Ans as a variable.
            for item in text_entered:
                if item == "\u00d7":
                    text_entered = text_entered.replace("\u00d7", "*")
                elif item == "\u00f7":
                   text_entered = text_entered.replace("\u00f7", "/")
                elif item == "\u03c0":
                    text_entered = text_entered.replace("\u03c0", "pi")
            try:
               self.entry.set_text(str(eval(text_entered))) #The eval() method returns the result evaluated from the expression.
               Ans = eval(text_entered)
            except (SyntaxError, NameError):
                self.entry.set_text("The entered values are not valid")
        else:
            text_entered += label
            self.entry.set_text(text_entered)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
