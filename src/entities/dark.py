from .text import TextEntity
from .background import BackgroundEntity
from .common import CommonEntity
from .action import ActionEntity


class DarkEntity():
    mode: str = 'dark'
    text: TextEntity
    background: BackgroundEntity
    action: ActionEntity
    common: CommonEntity


    def __init__(self, options: dict):
        self.mode = options['mode']
        self.text = options['text']
        self.background = options['background']
        self.action = options['action']
        self.common = options['common']


