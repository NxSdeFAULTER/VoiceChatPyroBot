# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2220765
API_HASH = "e7e5db5d294362c87a7f216396b64f05"

# Get this from @Botfather
TOKEN = "1550034711:AAH7e5_08S0BilifkhFbT7SStap_RAarfdE"

# Your mongodb uri
MONGO_DB_URI = ""

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1409172724,
    1142197555,
    1426137815,
    690571049
]

# The ID of the group where your bot streams
GROUP = -1001445249123

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
