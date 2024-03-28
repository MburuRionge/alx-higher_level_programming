#!/bin/bash
# Get size of GET request content
curl -Is $1 | grep 'Content-Length' | cut -d' ' -f2
