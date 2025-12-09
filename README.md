# python-webserver-files-download
This is a dedicated internal file-distribution server designed to bypass external access limitations, including sanctions-related restrictions.
It allows you to download required packages or archives to this server first, and then securely fetch them from your isolated or restricted environments.
By hosting files locally, you ensure reliable access to software dependencies even when direct downloads from the internet are unavailable or blocked.

# 1 step
```bash
chmod +x ~/python-webserver-files-download/server.py
```
# 2 step
```bash
sudo nano /etc/systemd/system/http-fileserver.service
```
# 3 step

```bash
[Unit]
Description=Standalone HTTP File Server (port 8002)
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/<username>/python-webserver-files-download
ExecStart=/usr/bin/env python3 /home/<username>/python-webserver-files-download/server.py --host 0.0.0.0 --port 8002 --dir /home/<username>/python-webserver-files-download


Restart=always
RestartSec=3


User=<username>
Group=<username>

[Install]
WantedBy=multi-user.target
```

## Dont forgot open port 8002 in your firewall or iptbales or ufw
