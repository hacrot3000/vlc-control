#! /usr/bin/python
from player import Player
from filter import Filter

player = Player()
player.setup_crondbus();

try:
    player.get_dbus_interface()
except :
    player.launch()

player.get_dbus_interface(True);

path = "/mnt/Software/Music/Thich_nghe"

filter = Filter(random=False)

player.clear()
player.play(path, filter);
player.shuffle();
player.next()