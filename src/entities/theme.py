from .text import TextEntity
from .background import BackgroundEntity
from .action import ActionEntity
from .common import CommonEntity

class ThemeEntity(CommonEntity):
    mode: str = ""
    text: TextEntity
    background: BackgroundEntity
    action: ActionEntity


    def __init__(self, options: dict, common: dict):
        super().__init__(common)
        self.mode = options["mode"]
        self.text = options["text"]
        self.background = options["background"]
        # self.action = options['action']
        # self.action = light["action"]

