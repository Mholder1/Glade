import gi
from gi.repository import Gtk as gtk
import os
import json
gi.require_version('Gtk', '3.0')


class Main:
    def __init__(self):
        gladeFile = "app.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.treeview = self.builder.get_object('treeview')
        self.listStore = gtk.ListStore(str)
        self.appendColumn()

        window = self.builder.get_object('Main_Window')
        window.connect('delete-event', gtk.main_quit)
        window.show()

    def printCity(self, widget):
        capitalCities = '/home/marcus/Glade/cities.json'

        entry = self.builder.get_object('toAddCountry')
        text = entry.get_text().strip()

        readfile = open(capitalCities)
        data = json.load(readfile)
        for line in data["cities"]:
            if text.capitalize() == line["country"]:
                self.listStore.append([line["city"]])

        readfile.close

    def appendColumn(self):
        renderer = gtk.CellRendererText()
        Column = gtk.TreeViewColumn(
            title="City", cell_renderer=renderer, text=0)
        self.treeview.append_column(Column)
        self.treeview.set_model(self.listStore)


if __name__ == '__main__':
    main = Main()
    gtk.main()
