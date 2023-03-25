# Bu proje, kullanıcının masaüstünde bildirimler gösteren bir program oluşturmayı içerir.
# (This project involves creating a program that displays notifications on the user's desktop.)

import time
import datetime
from plyer import notification

while True:
    now = datetime.datetime.now()

    if now.minute % 5 == 0:
        notification.notify(
            title="Time to Drink Water!",
            message="Remember to drink water every 5 minutes.",
            # Tabi ki test için böyle yazdım.
            # Of course, I wrote it for testing purposes.
            app_name="Water Reminder",
            timeout=10
        )

    time.sleep(300)