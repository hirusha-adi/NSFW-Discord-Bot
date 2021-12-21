import json


class PleaseWait:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    TITLE = embed["PleaseWaitEmbed"]["TITLE"]
    DESCRIPTION = embed["PleaseWaitEmbed"]["DESCRIPTION"]
    THUMBNAIL = embed["PleaseWaitEmbed"]["THUMBNAIL"]
    FOOTER = embed["PleaseWaitEmbed"]["FOOTER"]

    if embed["PleaseWaitEmbed"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embed["PleaseWaitEmbed"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embed["PleaseWaitEmbed"]["COLOR"] == "blue":
        COLOR = 0x0000ff

    AUTHOR_NAME = embed["PleaseWaitEmbed"]["AUTHOR_NAME"]
    AUTHOR_URL = embed["PleaseWaitEmbed"]["AUTHOR_URL"]


class ErrorEmbeds:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    TITLE = embed["ERROR"]["TITLE"]
    DESCRIPTION = embed["ERROR"]["DESCRIPTION"]
    THUMBNAIL = embed["ERROR"]["THUMBNAIL"]
    FIELD_NAME = embed["ERROR"]["FIELD_NAME"]

    if embed["ERROR"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embed["ERROR"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embed["ERROR"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class Common:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    if embed["COMMON"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embed["COMMON"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embed["COMMON"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class Help:
    with open("nsfwbot/database/embeds.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    if embed["HELP"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embed["HELP"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embed["HELP"]["COLOR"] == "blue":
        COLOR = 0x0000ff

    THUMBNAIL = embed["HELP"]["COLOR"]
