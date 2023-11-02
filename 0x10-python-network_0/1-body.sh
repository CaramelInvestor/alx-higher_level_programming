#!/bin/bash
#cURL to the end
curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk '{if ($0 == 200) {next} else {getline; print;}}'
