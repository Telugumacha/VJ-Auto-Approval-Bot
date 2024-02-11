# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25255983"))
    API_HASH = getenv("API_HASH", "5d3616ef09b67e8cf45a96a11fa57b22")
    BOT_TOKEN = getenv("BOT_TOKEN", "6772654586:AAGG1HqLwow5OxiHEAl3RraQLX2Fx5V6Xqg")
    FSUB = getenv("FSUB", "Telugumacha_updates")
    CHID = int(getenv("CHID", "-1002080428958"))
    SUDO = list(map(int, getenv("SUDO", "5136811766").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mecesa9366:Olt6lwGCkBiCDVKz@cluster0.dkbhwox.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
