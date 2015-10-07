from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
import os
from dotastatus import DotaStatus

def status_exit(w, data):
   Gtk.main_quit()

def status_show(w, data):
   status = DotaStatus()
   status.showStatus()

ind_app = appindicator.Indicator.new("server-status", os.path.abspath('icon.png'),appindicator.IndicatorCategory.APPLICATION_STATUS)
ind_app.set_status (appindicator.IndicatorStatus.ACTIVE)

# create a menu
menu = Gtk.Menu()
status_item = Gtk.MenuItem("Check server status")
about_item = Gtk.MenuItem("About Dota Status")
exit_item = Gtk.MenuItem("Exit")
menu.append(status_item)
menu.append(about_item)
menu.append(exit_item)
status_item.connect("activate", status_show,'')
exit_item.connect("activate", status_exit, '')
status_item.show()
about_item.show()
exit_item.show()
ind_app.set_menu(menu)
Gtk.main()