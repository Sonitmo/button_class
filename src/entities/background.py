class BackgroundEntity():
    paper: str = '#FFFFFF'
    default: str = ''
    neutral: str = ''
    def __init__(self, options: dict) -> None:
        self.paper = options['paper']
        self.default = options['default']
        self.neutral = options['neutral']