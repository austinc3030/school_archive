#!/bin/python

import requests

def get_changelog():
    discord_changelog_md_url = "https://raw.githubusercontent.com/discord/discord-api-docs/main/docs/Change_Log.md"
    request = requests.get(discord_changelog_md_url)
    changelog = request.content.decode("utf-8").split("\n")

    return changelog

def main():
    changelog = get_changelog()

    for line in changelog:
        
        print(line)

if __name__:
    main()