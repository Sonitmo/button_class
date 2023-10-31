from PIL import ImageColor

def alpha(hex_color, opacity):
  rbg_tuple = ImageColor.getcolor(hex_color, "RGB")
  y = list(rbg_tuple)
  y.append(opacity)
  rgba_tuple = tuple(y)
  return f'rgba{str(rgba_tuple)}'


# print(alpha('#919EAB', 0.08))