#!/usr/bin/env python
from mastodon import Mastodon
from random import choice

masto = Mastodon(
    api_base_url='https://botsin.space',
    client_id="client_id.txt",
    access_token="access_token.txt"
)

if __name__ == '__main__':
    # print("Publishing to Mastodon version", masto.retrieve_mastodon_version())
    with open("deeds.txt") as fi:
        deed = choice(fi.readlines()).rstrip()
    text = "Today's good deed: " + deed
    print("Tooting:", text)
    masto.status_post(text)

