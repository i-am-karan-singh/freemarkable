#!/bin/bash
rclone copy -P bs:/digitalpaper /home/root/digitalpaper
python3 /home/root/freemarkable/rem_live.py
