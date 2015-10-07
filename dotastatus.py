#!/usr/bin/python
from gi.repository import Notify, GdkPixbuf
import json
import os

class DotaStatus:
    def __init__(self):
        Notify.init("Dota Status")
        self.server_cases = {'Normal': ['Dota server is alive','images/status-normal.png'],
        'Low Load': ['Dota server is in Low load mode','images/status-low-load.png'],
        'Offline':['Dota server is Offline','images/status-offline.png'],
        'Critical':['Dota server is in critical mode','images/status-critical.png'],
        'High Load':['Dota server is in high load mode','images/status-high-load.png'],
        'Steambd':['Cannot connect to Steamdb','images/status-normal.png']}

    def showStatus(self):
        '''Using curl because steamdb has bot protection and maybe they will be
        give me a ban soon'''
        try:
            json_db = os.popen('curl https://crowbar.steamdb.info/Barney').read()
            objects = json.loads(json_db)
            title = objects['services']['dota2']['title']
            #status = objects['services']['dota2']['status']
            notification = Notify.Notification.new(self.server_cases[title][0])
            image = GdkPixbuf.Pixbuf.new_from_file(self.server_cases[title][1])
        except:
            notification = Notify.Notification.new(self.server_cases['Steambd'][0])
            image = GdkPixbuf.Pixbuf.new_from_file(self.server_cases['Steambd'][1])

        notification.set_icon_from_pixbuf(image)
        notification.set_image_from_pixbuf(image)
        notification.show()

#dota_status = DotaStatus()
#dota_status.showStatus()
