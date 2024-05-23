#!/usr/bin/env python3
import os
import time
import subprocess
from sys import argv, exit
import eurmlsdk

if len(argv) < 2:
        print("Required arguments missing")
        print("Please provide model file and feed type")
        exit(1)
if len(argv) < 4 and argv[2] == "live_feed":
        # Define the command to start rpicam-vid in the background
        rpicam_command = "rpicam-vid -n -t 0 --inline --listen -o tcp://127.0.0.1:8889 &"
        predict_command = "eurmlsdk predict {} tcp://127.0.0.1:8889".format(argv[1])
        # Use subprocess to run the command in the background
        subprocess.Popen(rpicam_command, shell=True)
        subprocess.Popen(predict_command, shell=True)
        rpicam_process_id = os.system("lsof -i :8889 | grep rpicam | awk '{print $2}'")
        predict_process_id = os.system("lsof -i :8889 | grep eurmlsdk | awk '{print $2}'")
        time.sleep(100)
        os.system("kill -9 {}".format(rpicam_process_id))
        time.sleep(10)
        os.system("kill -9 {}".format(predict_process_id))
        # Now, execute the eurmlsdk predict command
elif len(argv) < 4:
        print("Using default image 'img.jpg' for prediction")
        os.system("eurmlsdk predict {} img.jpg".format(argv[1]))
        os.system("eurmlsdk validate pose {}".format(argv[1]))
else:
        os.system("eurmlsdk predict {} {}".format(argv[1],argv[3]))
        os.system("eurmlsdk validate pose {}".format(argv[1]))  