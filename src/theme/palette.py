from ..entities import ThemeEntity, ActionEntity, CommonEntity, TextEntity, BackgroundEntity
from ..utils import alpha
from ..entities.palette import PrimaryEntity, SuccessEntity, InfoEntity, SecondaryEntity, WarningEntity, ErrorEntity




GREY = {
  0: '#FFFFFF',
  100: '#F9FAFB',
  200: '#F4F6F8',
  300: '#DFE3E8',
  400: '#C4CDD5',
  500: '#919EAB',
  600: '#637381',
  700: '#454F5B',
  800: '#212B36',
  900: '#161C24',
}

PRIMARY = PrimaryEntity({
  'lighter': '#C8FAD6',
  'light': '#5BE49B',
  'main': '#00A76F',
  'dark': '#007867',
  'darker': '#004B50',
  'contrastText': '#FFFFFF',

})

SECONDARY = SecondaryEntity({
  'lighter': '#EFD6FF',
  'light': '#C684FF',
  'main': '#8E33FF',
  'dark': '#5119B7',
  'darker': '#27097A',
  'contrastText': '#FFFFFF',
})

INFO = InfoEntity({
  'lighter': '#CAFDF5',
  'light': '#61F3F3',
  'main': '#00B8D9',
  'dark': '#006C9C',
  'darker': '#003768',
  'contrastText': '#FFFFFF'
})

SUCCESS = SuccessEntity({
  'lighter': '#D3FCD2',
  'light': '#77ED8B',
  'main': '#22C55E',
  'dark': '#118D57',
  'darker': '#065E49',
  'contrastText': '#FFFFFF',
})

WARNING = WarningEntity({
  'lighter': '#FFF5CC',
  'light': '#FFD666',
  'main': '#FFAB00',
  'dark': '#B76E00',
  'darker': '#7A4100',
  'contrastText': GREY[800],
})

ERROR = ErrorEntity({
  'lighter': '#FFE9D5',
  'light': '#FFAC82',
  'main': '#FF5630',
  'dark': '#B71D18',
  'darker': '#7A0916',
  'contrastText': '#FFFFFF',
})


COMMON = {
  'common': { 'black': '#000000', 'white': '#FFFFFF' },
  'primary': PRIMARY,
  'secondary': SECONDARY,
  'info': INFO,
  'success': SUCCESS,
  'warning': WARNING,
  'error': ERROR,
  'grey': GREY,
  'divider': alpha(GREY[500], 0.24),
  'action': ActionEntity({
    'hover': alpha(GREY[500], 0.08),
    'selected': alpha(GREY[500], 0.16),
    'disabled': alpha(GREY[500], 0.8),  #alpha(GREY[500], 0.8),
    'disabled_background': alpha(GREY[500], 0.24),
    'focus': alpha(GREY[500], 0.24),
    'hover_opacity': 0.08,
    'disabled_opacity': 0.48,
  },
) 
}

COMMON_OBJ = CommonEntity(COMMON)


def palette(theme_mode):
  
  if theme_mode == 'light':
    theme = {
      'mode': 'light',
      'text': TextEntity({
        'primary': GREY[800],
        'secondary': GREY[600],
        'disabled': GREY[500],
      }),
      'background': BackgroundEntity({ 'paper': '#FFFFFF', 'default': '#FFFFFF', 'neutral': GREY[200] }),
      'action': COMMON_OBJ.action.update(GREY[500]),
            }

    # light_theme_obj = ThemeEntity(theme, COMMON)
  
  else:
    theme = {
    'mode': 'dark',
    'text': TextEntity({
      'primary': '#FFFFFF',
      'secondary': GREY[500],
      'disabled': GREY[600],
    }),
    'background': BackgroundEntity({
      'paper': GREY[800],
      'default': GREY[900],
      'neutral': alpha(GREY[500], 0.16),
    }),
    'action': COMMON_OBJ.action.update(GREY[600]),
    # 'common': COMMON,
        }

  theme_obj = ThemeEntity(theme, COMMON)

  return theme_obj


# print(palette('dark'))
'''
{
   "mode":"dark",
   "text":{
      "primary":"#FFFFFF",
      "secondary":"#919EAB",
      "disabled":"#637381"
   },
   "background":{
      "paper":"#212B36",
      "default":"#161C24",
      "neutral":"grba(2, 4, 5, 0.7)"
   },
   "action":{
      "hover":"grba(2, 4, 5, 0.7)",
      "selected":"grba(2, 4, 5, 0.7)",
      "disabled":"grba(2, 4, 5, 0.7)",
      "disabledBackground":"grba(2, 4, 5, 0.7)",
      "focus":"grba(2, 4, 5, 0.7)",
      "hoverOpacity":0.08,
      "disabledOpacity":0.48
   },
   "common":{
      "black":"#000000",
      "white":"#FFFFFF"
   },
   "primary":{
      "lighter":"#C8FACD",
      "light":"#5BE584",
      "main":"#00AB55",
      "dark":"#007B55",
      "darker":"#005249",
      "contrastText":"#FFFFFF"
   },
   "secondary":{
      "lighter":"#D6E4FF",
      "light":"#84A9FF",
      "main":"#3366FF",
      "dark":"#1939B7",
      "darker":"#091A7A",
      "contrastText":"#FFFFFF"
   },
   "info":{
      "lighter":"#CAFDF5",
      "light":"#61F3F3",
      "main":"#00B8D9",
      "dark":"#006C9C",
      "darker":"#003768",
      "contrastText":"#FFFFFF"
   },
   "success":{
      "lighter":"#D8FBDE",
      "light":"#86E8AB",
      "main":"#36B37E",
      "dark":"#1B806A",
      "darker":"#0A5554",
      "contrastText":"#FFFFFF"
   },
   "warning":{
      "lighter":"#FFF5CC",
      "light":"#FFD666",
      "main":"#FFAB00",
      "dark":"#B76E00",
      "darker":"#7A4100",
      "contrastText":"#212B36"
   },
   "error":{
      "lighter":"#FFE9D5",
      "light":"#FFAC82",
      "main":"#FF5630",
      "dark":"#B71D18",
      "darker":"#7A0916",
      "contrastText":"#FFFFFF"
   },
   "grey":{
      "0":"#FFFFFF",
      "100":"#F9FAFB",
      "200":"#F4F6F8",
      "300":"#DFE3E8",
      "400":"#C4CDD5",
      "500":"#919EAB",
      "600":"#637381",
      "700":"#454F5B",
      "800":"#212B36",
      "900":"#161C24"
   },
   "divider":"grba(2, 4, 5, 0.7)"
}
'''