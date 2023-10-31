from .action import ActionEntity
from .palette import PrimaryEntity, SuccessEntity, InfoEntity, SecondaryEntity, WarningEntity, ErrorEntity


class CommonEntity():
    common: dict = {}
    primary: PrimaryEntity
    secondary: SecondaryEntity
    info: InfoEntity
    success: SuccessEntity
    warning = WarningEntity
    error = ErrorEntity
    grey: dict = {}
    divider: str = ''
    action: ActionEntity

    def __init__(self, options: dict):
        self.common = options['common']
        self.primary = options['primary']
        self.secondary = options['secondary']
        self.info = options['info']
        self.success = options['success']
        self.warning = options['warning']
        self.error = options['error']
        self.grey = options['grey']
        self.divider = options['divider']
        self.action = options['action']
    
    def convert_to_json(self):
        pass

