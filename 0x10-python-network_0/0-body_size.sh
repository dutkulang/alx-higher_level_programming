#!/bin/bash

# a bash script that gets URL from the Commandline
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
