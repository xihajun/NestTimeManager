from time import time, sleep
import pychromecast
from icalevents.icalevents import events
import datetime
from datetime import timezone

while True:
    es  = events("webcal://p50-caldav.icloud.com/published/2/token", fix_apple=True)

    now = datetime.datetime.now(timezone.utc)
    for i in es:
        duration = i.start - now

        gap = duration.total_seconds()
        if gap <= 200 and gap >0:
            startnotif = True
            message = i.summary
            url = 'https://api.oick.cn/txt/apiz.php?text=省去我开始要提醒你了，滴滴滴，去' + message + '&spd=1'
            break
        else:
            startnotif = False
        endtime = i.end - now

        gap = endtime.total_seconds()
        if gap <= 200 and gap >0:
            endnotif = True
            message = i.summary
            url = 'https://api.oick.cn/txt/apiz.php?text=省去快去休息了，休息身体最重要滴滴滴滴滴&spd=1'
            break
        else:
            endnotif = False
    print(startnotif,endnotif)
    if startnotif or endnotif:
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom display"])
        cast = chromecasts[0]
        cast.wait()
        mc = cast.media_controller
        mc.play_media(url,'video/mp4')
        mc.block_until_active()
        sleep(20)
        cast.quit_app()
    sleep(60)
