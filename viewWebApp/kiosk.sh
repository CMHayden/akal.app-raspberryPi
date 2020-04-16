#!/bin/bash

# Turns off screensaver and disables the "display power management system"
xset s noblank
xset s off
xset -dpms

# Hides mouse
unclutter -root &

# Remove flags that could cause warning bar to appear
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

# Launches kiosk mode 
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk https://www.akal.app &

# Forces browser to refresh every 30 minutes
while true; do
    xdotool keydown ctrl+r; xdotool keyup ctrl+r;
    sleep 1800
done