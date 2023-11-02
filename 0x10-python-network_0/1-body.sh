#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk '{if ($0 == 200) {next} else {getline; print;}}'
