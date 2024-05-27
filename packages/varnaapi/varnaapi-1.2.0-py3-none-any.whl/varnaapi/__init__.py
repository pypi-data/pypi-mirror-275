from .models import BasicDraw, Structure, Comparison, Motif, VARNA, FileDraw
from .param import load_config
from .settings import set_VARNA, enable_hack, check_settings_exists, load_settings

__version__ = '1.2.0'

check_settings_exists()
load_settings()
