from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "a6ff05d5e26feb62d29eea1c411a15b9")
      API_ID = int(getenv("API_ID", "28771159"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7703810356:AAF5WoMi_OAYdzxUbqF59PIuVP8p8py9AKg")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002785696328").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
