from time import time, sleep
import pychromecast
from icalevents.icalevents import events
import datetime
from datetime import timezone

# counter to avoid keep loading icalendar (might block your account)
counter = 6
icalurl = "webcal://p51-caldav.icloud.com/published/2/token"
es  = events(icalurl, fix_apple=True)
startnotif = False
endnotif = False

# timetable checker
while True:
    # limit the usage
    if counter // 6:
        es  = events(icalurl, fix_apple=True)
    counter += 1
    
    # notification settings
    now = datetime.datetime.now(timezone.utc)
    for i in es:
        duration = i.start - now
        
        print("Start Time Left:",abs(duration.total_seconds()))
        gap = duration.total_seconds()
        if gap <= 600 and gap > 0:
            startnotif = True
            message = i.summary
            url = 'https://api.oick.cn/txt/apiz.php?text=省去我开始要提醒你了，滴滴滴，去' + message + '&spd=1'
            break
        else:
            startnotif = False
        
        endtime = i.end - now
        gap = endtime.total_seconds()
        print("End Time Left:", abs(endtime.total_seconds()))
        if gap <= 600 and gap > 0:
            endnotif = True
            message = i.summary
            url = 'https://api.oick.cn/txt/apiz.php?text=省去快去休息了，休息身体最重要滴滴滴滴滴&spd=1'
            break
        else:
            endnotif = False

    print("start:",startnotif, end=" ")
    print("end:",endnotif)
    
    if startnotif or endnotif:
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom display"])
        cast = chromecasts[0]
        cast.wait()
        mc = cast.media_controller
        mc.play_media(url,'video/mp4')
        mc.block_until_active()
        sleep(20)
        cast.quit_app()
        if startnotif:
            sleep(1800)
    sleep(180)