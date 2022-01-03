# Pomodoro Reminder (on Nest Hub or Nest mini)
Automated time management system based on your timetable with Google Smart Device using `pychromecast`

## How it works
![image](https://user-images.githubusercontent.com/25631641/147934109-d0a93cff-0112-4009-92fd-f4bba1a9f6d8.png)

## Quick start

If you have your Google Nest Hub in your room with the same wifi network, let's try this see if it works.
```{python}
import time
import pychromecast


# icalevents package: https://github.com/jazzband/icalevents ----
from icalevents.icalevents import events

# add your webcal url - icalendar 
es  = events("webcal://p50-caldav.icloud.com/published/2/token", fix_apple=True)
# google calendar 
# es  = events(<Google Calendar URL>)
# the first event
print(es[0].summary)

# "省去" is to skip first two words (buggy) + first evenet
url = 'https://api.oick.cn/txt/apiz.php?text=省去我开始要提醒你了，滴滴滴，' + es[0].summary + '&spd=1'

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom display"])

cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()

print(cast.status)

# play media
mc = cast.media_controller
mc.play_media(url,'video/mp4')
mc.block_until_active()
print(mc.status)

# quit app about 20 sec
time.sleep(20)
cast.quit_app()
```

## TODO
- [x] Timetable project - previous python icalendar
- [ ] monitor your mac project - based on github resource 
- [ ] Merge projects - done ✅ 


## notes
```
>>> dir(mc)
['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_check_registered', '_fire_status_changed', '_message_func', '_process_media_status', '_send_command', '_send_start_play_media', '_socket_client', '_start_play_media_sent', '_status_listeners', 'app_id', 'block_until_active', 'channel_connected', 'channel_disconnected', 'disable_subtitle', 'enable_subtitle', 'is_active', 'is_idle', 'is_paused', 'is_playing', 'launch', 'logger', 'media_session_id', 'namespace', 'pause', 'play', 'play_media', 'queue_next', 'queue_prev', 'quick_play', 'receive_message', 'register_status_listener', 'registered', 'rewind', 'seek', 'send_message', 'send_message_nocheck', 'session_active_event', 'skip', 'status', 'stop', 'supporting_app_id', 'target_platform', 'tear_down', 'thumbnail', 'title', 'unregistered', 'update_status']
```
