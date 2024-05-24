import os
import sys
import yaml

RG_DIR = os.path.join(os.path.expanduser("~"), ".roadguard")
RG_CONFIG_FILE = os.path.join(RG_DIR, "config.yaml")
RG_SOURCE = os.path.dirname(os.path.abspath(__file__))

try:
    with open(RG_CONFIG_FILE, "r") as f:
        RG_CONFIG = yaml.load(f, Loader=yaml.SafeLoader)
except FileNotFoundError:
    print(f"Config file not found at {RG_CONFIG_FILE}")
    sys.exit(1)

os.environ.setdefault(
    "OPENAI_API_KEY",
    RG_CONFIG.get("OPENAI_API_KEY", "")
)

RG_SAMPLE_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'roadguard-sample-data')
