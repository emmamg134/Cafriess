import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    calc_box = [
        ["7", "8", "9", "%", "Del"],
        ["4", "5", "6", "x", "(", ")"],
        ["3", "2", "1", "-", "x^2", "sqrt"],
        ["0", ",", "%", "+", "="]
    ]

    def __init__(self):
        super().__init__(title="Cafriess")
        
        vertical_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.add(vertical_box)

        entry = Gtk.Entry()
        entry.set_text("Hagamos matemáticas")
        grid = Gtk.Grid()

        vertical_box.pack_start(entry, True, True, False)
        vertical_box.pack_end(grid, True, True, False)

        y = 0
        for row in self.calc_box:
            x = 0
            for column in row:
                button = Gtk.Button(label=column)
                button.connect("clicked", self.on_button_clicked)
                grid.attach(button, x, y, 1, 1)
                x += 1
            y += 1

    def on_button_clicked(self, widget):
        print("Me canse")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
