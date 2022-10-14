# Imports
import time
from plyer import notification

if __name__ == "__main__":
   notification.notify(
      title = "Drink Water Notification",
      message = "Do you know how much water we need to drink per day. Your weight/30=Water we must to drink! SO PLEASE DRINK WATER AS SOON AS POSSIBLE!",
      app_icon = "",
      timeout = 10
   )

   time.sleep(20)