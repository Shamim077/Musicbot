from Musicbot.core.bot import Anony
from Musicbot.core.dir import dirr
from Musicbot.core.git import git
from Musicbot.core.userbot import Userbot
from Musicbot.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
