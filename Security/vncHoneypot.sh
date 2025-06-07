#!/bin/bash  
LOGFILE="/home/fred/.vnc/ubuntu-s-1vcpu-1gb-lon1-01:1.log"  
CONNECT_PATTERN="Connections: accepted:"  
DISCONNECT_PATTERN="VNCSConnST:  closing"  
PIDFILE="/tmp/vnc_ffmpeg_pid.txt"  
cat /dev/null > /home/fred/.vnc/ubuntu-s-1vcpu-1gb-lon1-01\:1.log  
vncserver --I-KNOW-THIS-IS-INSECURE -localhost no -geometry 1024x768 -depth 32 -SecurityTypes None  
tail -F "$LOGFILE" | while read -r line; do  
       if echo "$line" | grep -q "$CONNECT_PATTERN"; then  
               echo "$(date): VNC client connected, starting ffmpeg"  
               # Extract IP address  
               IP=$(echo "$line" | awk '{print $3}' | cut -d':' -f1)  
  
               # Sanitize IP in case it has characters we don't want in filenames (just in case)  
               SAFE_IP=$(echo "$IP" | tr -cd '[:alnum:]._-')  
  
               # Filename includes date and IP  
               FILENAME="/home/john/files/$(date +'%d-%m-%Y-%H-%M-%S')-${SAFE_IP}.mp4"  
  
               # Start ffmpeg and save PID  
               ffmpeg -f x11grab -video_size 1024x768 -framerate 30 -i :1.0 -c:v libx264 -preset ultrafast -crf 23 "$FILENAME" &  
  
               # Send IP in ntfy notification  
               curl -d "Connection to VNC server from IP $SAFE_IP" ntfy.sh/[your ntfy string]  
  
               echo $! > "$PIDFILE"  # Save ffmpeg PID  
       elif echo "$line" | grep -q "$DISCONNECT_PATTERN"; then  
               echo "$(date): VNC client disconnected, stopping ffmpeg"  
  
       if [ -f "$PIDFILE" ]; then  
               PID=$(cat "$PIDFILE")  
               if ps -p $PID > /dev/null; then  
                       kill $PID  
                       echo "ffmpeg process $PID killed"  
                       fi  
                       rm -f "$PIDFILE"  
       fi  
   fi  
done
