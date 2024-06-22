from SafoneAPI import SafoneAPI

from ZenakuX-Music.core.bot import VIP
from ZenakuX-Music.core.dir import dirr
from ZenakuX-Music.core.git import git
from ZenakuX-Music.core.userbot import Userbot
from ZenakuX-Music.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SASUKE()
api = SafoneAPI()
userbot = Userbot()
HELPABLE = {}

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "sasukexmusic_bot"  # connect music api key "Dont change it"
