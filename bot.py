#!/usr/bin/env python
from mastodon import Mastodon
from random import choice
import os

masto = Mastodon(
    api_base_url='https://botsin.space',
    client_id="client_id.txt",
    access_token="access_token.txt"
)

def readFile(fn):
    with open(fn) as fi:
        lines = fi.readlines()
    lines = (line.strip()
             for line in lines
             if not line.startswith("#"))
    return list(lines)

if __name__ == '__main__':
    deeds = []
    for fn in os.listdir("deeds"):
        deeds.extend(readFile(os.path.join("deeds", fn)))
    deed = choice(deeds)
    text = "Today's good deed: " + deed
    print("Tooting:", text)
    # masto.status_post(text)

