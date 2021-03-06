from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
import os
from dotastatus import DotaStatus

def status_exit(w, data):
   Gtk.main_quit()

def status_show(w, data):
   status = DotaStatus()
   status.showStatus()

def status_about(w, data):
   about = Gtk.Window()
   about.set_title("About Dota Status")
   about.set_default_size(400,300)
   about_label = Gtk.Label()
   about_label.set_markup("Dota 2 server status notifier \n"
                 "<a title=\"Steam Database Project\" href='https://steamstat.us/'>Steam Status</a>\n "
                 "<a href=\'https://github.com/drkpkg/dotastatus' "
                 "title=\"Volvo pls\">Github project</a> for more info \n"
                 "Powered by <a title=\"Steam Database Project\" href=\'https://steamdb.info/'>Steamdb</a>")
   about.add(about_label)
   about_label.show()
   about.show()

ind_app = appindicator.Indicator.new("server-status", 
os.path.abspath('/usr/share/dotastatus/icon.png'),
appindicator.IndicatorCategory.APPLICATION_STATUS)
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
about_item.connect("activate", status_about,'')
exit_item.connect("activate", status_exit, '')
status_item.show()
about_item.show()
exit_item.show()
ind_app.set_menu(menu)
Gtk.main()
