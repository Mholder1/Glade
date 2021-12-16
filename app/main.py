import gi
from gi.repository import Gtk as gtk
from country import Country

gi.require_version('Gtk', '3.0')


class Main:
    def __init__(self):
        # connect to glade file and initalize the signals
        gladeFile = "app.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        # global variables of treeview and list store
        self.treeview = self.builder.get_object('treeview')
        self.listStore = gtk.ListStore(str)
        self.appendColumn()

        window = self.builder.get_object('Main_Window')
        window.connect('delete-event', gtk.main_quit)
        window.show()

    def printCity(self, widget):
        entry = self.builder.get_object('toAddCountry')
        text = entry.get_text().strip()

        country = Country()

        city = country.getCapCity(text)
        self.listStore.append([city])

    def appendColumn(self):
        # render the text to be visible in treeview
        renderer = gtk.CellRendererText()
        Column_text = gtk.TreeViewColumn(
            title="Capital city", cell_renderer=renderer, text=0)
        self.treeview.append_column(Column_text)
        self.treeview.set_model(self.listStore)


if __name__ == '__main__':
    main = Main()
    gtk.main()
