from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, LOG_SESSION, STRING1, STRING2,
                    STRING3, STRING4, STRING5)

app = Client(
    "YukkiMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)


if False:
    ASS_CLI_1 = None
else:
    ASS_CLI_1 = Client(
        api_id=17881110,
        api_hash="41d02175c2858cae93b745ffa4aaed24",
        session_name="BQC7cH4KLo3veqtnJCElfBhiHU-CYiG7HZ8HjtiEabL_pxLXHCobGjccBwGo7RRUrB-fdjmTGjmsSVIScs7LSAfXenl2-69KQaG5iEMybv7FsEdXdeV7PPrzTGpwEaCkGPLarZ2nzI0Wi7TvnX5Iv__w-BRJJO2yKKQydho1V7zpXeZryA3bn_C4CVMr2zz5uBsAyGQZph9Pz3LdhzIcj-Nsio3pHBwp0BrlbwVfY025isCWK3Y_Yv5MgvGda9KOeOYT7yJVl7SJoCNWqjVmcbqK53rhnjGVrnL8TRMErQxfzWWXqiJe8CtjEYa0F68nVVrQUJ_1XavEms2o0KfFoHdgAAAAAUk_nSsA"
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING2:
    ASS_CLI_2 = None
else:
    ASS_CLI_2 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING2,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING3:
    ASS_CLI_3 = None
else:
    ASS_CLI_3 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING3,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING4:
    ASS_CLI_4 = None
else:
    ASS_CLI_4 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING4,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING5:
    ASS_CLI_5 = None
else:
    ASS_CLI_5 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING5,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not LOG_SESSION:
    LOG_CLIENT = None
else:
    LOG_CLIENT = Client(LOG_SESSION, API_ID, API_HASH)
