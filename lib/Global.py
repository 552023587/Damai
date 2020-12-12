import os
import re

LIB_PATH = os.path.split(os.path.realpath(__file__))[0]
APP_PATH = re.sub(r"lib","",LIB_PATH)