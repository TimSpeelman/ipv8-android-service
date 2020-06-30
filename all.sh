#!/bin/bash
trap 'exit 0' SIGTERM
set -e

#create dist and build
script -c "./reset.sh"
script -a -c "./build.sh"
script -a -c "./apk.sh"
