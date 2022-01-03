# Pomodoro Reminder (on Nest Hub or Nest mini)
Automated time management system based on your timetable with Google Smart Device using `pychromecast`

## How it works
![image](https://user-images.githubusercontent.com/25631641/147935578-f27934a1-b945-46f8-b93a-9944f2bc2dfa.png)

Key points:
- icalevents (load calendar: share the link)
- MP3 API: https://api.oick.cn/txt/apiz.php?text=xxxx&spd=1
- pychromecast: `mc.play_media(url,'video/mp4')`


## Quick start

If you have your Google Nest Hub in your room with the same wifi network, let's try this see if it works.
```{python}
import time
import pychromecast

# import calevents 
from icalevents.icalevents import events
es  = events("webcal://p50-caldav.icloud.com/published/2/token", fix_apple=True)
url = 'https://api.oick.cn/txt/apiz.php?text=省去我开始要提醒你了，滴滴滴，' + es[0].summary + '&spd=1'

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom display"])
cast = chromecasts[0]

# play media with message embedding
mc = cast.media_controller
mc.play_media(url,'video/mp4')
mc.block_until_active()

# quit app about 20 sec
time.sleep(20)
cast.quit_app()
```

## TODO
- [x] Timetable project - previous python icalendar
- [ ] customise your timetable use previous project
- [ ] monitor your mac project - based on github resource 
- [ ] Merge projects - done ✅ 



