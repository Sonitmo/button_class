# from .hover import HoverEntity


class Color:
    lighter: str = ''
    light: str = ''
    main: str = ''
    dark: str = ''
    darker: str = ''
    contrastText: str = ''
    # hover: HoverEntity

    def __init__(self, options: dict):
        self.lighter = options['lighter']
        self.light = options['light']
        self.main = options['main']
        self.dark = options['dark']
        self.darker = options['darker']
        self.contrastText = options['contrastText']
        # self.hover = options['hover']

class PrimaryEntity(Color):
    pass


class SecondaryEntity(Color):
    pass


class InfoEntity(Color):
    pass
    

class SuccessEntity(Color):
    pass


class WarningEntity(Color):
    pass


class ErrorEntity(Color):
    pass













PRIMARY = {
  'lighter': '#C8FACD',
  'light': '#5BE584',
  'main': '#00AB55',
  'dark': '#007B55',
  'darker': '#005249',
  'contrastText': '#FFFFFF',
}