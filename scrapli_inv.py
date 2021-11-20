import os

eve_user = os.environ["EVE_USER"]
eve_pass = os.environ["EVE_PASS"]

inv = {
    "router-1": {
        "type": "ios",
        "host": "192.168.7.150",
        "user": eve_user,
        "pass": eve_pass,
        "enable_pass": eve_pass,
    },
    "switch-1": {
        "type": "ios",
        "host": "192.168.7.151",
        "user": eve_user,
        "pass": eve_pass,
        "enable_pass": eve_pass,
    },
}
