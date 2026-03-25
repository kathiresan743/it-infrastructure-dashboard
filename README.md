# IT Infrastructure Dashboard

A real-time IT infrastructure monitoring dashboard built with Python Flask and Paramiko SSH.

## What it does
- Monitors multiple Linux servers simultaneously over the network
- Shows live CPU, RAM and Disk usage for each server
- Color coded status — Green (Online) Red (Offline)
- Auto refreshes every 30 seconds
- Detects and alerts on high resource usage
- Built and tested on 6 real lab PCs at SASTRA University AI and Robotics Lab

## Technologies Used
- Python 3.12
- Flask (web framework)
- Paramiko (SSH connections)
- HTML CSS JavaScript (dashboard frontend)

## How to Run
pip install flask paramiko
python app.py
Open browser → http://localhost:5000

## Project Background
Built as part of my hands-on infrastructure work at SASTRA University AI and Robotics Lab
where I manage 10+ Linux workstations supporting AI and robotics research.

## Author
Kathiresan Gunasekaran
Cloud Support Engineer | Linux Administrator
gkathir743@gmail.com
