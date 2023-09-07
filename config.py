from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN" ,"6632416439:AAGYi9gaVlML4OLXBnoUS84jg_tXz6xmxW8")
API_ID = int(getenv("API_ID", "17881110"))
API_HASH = getenv("API_HASH" ,"41d02175c2858cae93b745ffa4aaed24")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://logi:logi@logimee.ufrkju8.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1955509952").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1955509952").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001770039008"))
OWNER_USERNAME = str(getenv("OWNER_USERNAME" ,"cl_me_logesh"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME" ,"logi")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/dev-logesh/music-video-bot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = "team_vampir"
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = "Team_vampir"
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))

STRING_SESSION1="BQC7cH4KLo3veqtnJCElfBhiHU-CYiG7HZ8HjtiEabL_pxLXHCobGjccBwGo7RRUrB-fdjmTGjmsSVIScs7LSAfXenl2-69KQaG5iEMybv7FsEdXdeV7PPrzTGpwEaCkGPLarZ2nzI0Wi7TvnX5Iv__w-BRJJO2yKKQydho1V7zpXeZryA3bn_C4CVMr2zz5uBsAyGQZph9Pz3LdhzIcj-Nsio3pHBwp0BrlbwVfY025isCWK3Y_Yv5MgvGda9KOeOYT7yJVl7SJoCNWqjVmcbqK53rhnjGVrnL8TRMErQxfzWWXqiJe8CtjEYa0F68nVVrQUJ_1XavEms2o0KfFoHdgAAAAAUk_nSsA"

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
