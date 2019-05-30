# vlc-control

#Usuage example
```
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
player.play(path, filter)
player.shuffle()
player.next()
```
Supported methods:
```
launch()
close()

play(path, filter)
pause()
toggle()
stop()
prev()
next()

clear()
add(path, filter)
shuffle()
noshuffle()

get_volume()
set_volume()
fade_volume(target, time)

track_info()
```

Say thanks to https://github.com/amol9/vlc-ctrl
