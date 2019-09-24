#!/usr/bin/env python3

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter address: ')
if len(address) < 1: exit()

uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
uh = json.loads(data)

total = 0
for item in uh['comments']:
    total = total + int(item['count'])
print(total)

