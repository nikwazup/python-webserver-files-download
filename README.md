# python-webserver-files-download
this is special server to donwload files, if you have problem with sancions you can download packages at your server and download from server files to your sancions server

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
