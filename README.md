# Pomodoro (on Nest Hub or Nest mini)
Automated time management system based on your timetable with Google Smart Device using `pychromecast`

## Quick start

If you have your Google Nest Hub in your room with the same wifi network, let's try this see if it works.
```
import time
import pychromecast

# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()
# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom display"])

cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()

print(cast.status)

mc = cast.media_controller
mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)

cast.quit_app()
```

## TODO
- [x] Timetable project - previous python icalendar
- [ ] Notification project - based on github resource 
- [ ] Merge projects - done ✅ 


## notes
```
>>> dir(mc)
['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_check_registered', '_fire_status_changed', '_message_func', '_process_media_status', '_send_command', '_send_start_play_media', '_socket_client', '_start_play_media_sent', '_status_listeners', 'app_id', 'block_until_active', 'channel_connected', 'channel_disconnected', 'disable_subtitle', 'enable_subtitle', 'is_active', 'is_idle', 'is_paused', 'is_playing', 'launch', 'logger', 'media_session_id', 'namespace', 'pause', 'play', 'play_media', 'queue_next', 'queue_prev', 'quick_play', 'receive_message', 'register_status_listener', 'registered', 'rewind', 'seek', 'send_message', 'send_message_nocheck', 'session_active_event', 'skip', 'status', 'stop', 'supporting_app_id', 'target_platform', 'tear_down', 'thumbnail', 'title', 'unregistered', 'update_status']
```
