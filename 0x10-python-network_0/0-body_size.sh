#!/bin/bash

curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
