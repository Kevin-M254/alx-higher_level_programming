#!/bin/bash
# send a request to an URL with curl and display the size of the body
curl -s "$1" | wc -c
