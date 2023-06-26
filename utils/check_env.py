import os
import platform
import yaml

"""default config.yml
API_Key: ""
OS: "Fedora"
Desktop_ENV: "GNOME"
HOTWORD: "commander"
Threat_Barrier: 5
Next_CMD_Delay: 10
"""


def get_desktop_env():
    """Get the desktop environment

    Returns:
        string: deskdop_name
    """
    if platform.system() == 'Windows':
        return 'Windows'
    elif platform.system() == 'Darwin':
        return 'Aqua'
    else:
        # Assume it's a Linux or Linux-like system
        return os.environ.get('XDG_CURRENT_DESKTOP') or os.environ.get('DESKTOP_SESSION')


def get_os():
    """get os name

    Returns:
        str: os_name
    """
    return platform.system()


def default_config():
    """configure the default desktop environment and os version
    """
    with open('config.yml', 'r') as f:
        data = yaml.safe_load(f)

    data['OS'] = get_os()
    data['Desktop_ENV'] = get_desktop_env()
    # print(f"{data['OS']} and {data['Desktop_ENV']}")
    with open('config.yml', 'w') as f:
        yaml.safe_dump(data, f)
