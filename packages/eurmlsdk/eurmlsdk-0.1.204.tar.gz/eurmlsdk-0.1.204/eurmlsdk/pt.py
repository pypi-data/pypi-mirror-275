#!/usr/bin/env python3
from sys import argv, exit
import os
if len(argv) <2:
    print("Required arguments missing")
    print("Please provide model file and feed type")
    exit(1)
elif len(argv) <3: 
    model = argv[1]
    command = ("eurmlsdk pt-predict {}".format(model))
    os.system(command)
    exit(1)
