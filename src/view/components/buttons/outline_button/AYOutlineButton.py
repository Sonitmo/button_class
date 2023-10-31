from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


styles = """
        QPushButton {{
            outline: {};
            margin: {};
            font-weight: {};
            line-height: {};
            font-size: {};
            font-family: {};
            min-width: {};
            padding: {} {};
            border-radius: {};
            border: 1px solid {};
            color: {};
        }}
        QPushButton::hover {{
            background-color: {};
            border: {};
        }}

"""


class AYOutlineButton(QPushButton):
    def __init__(self, text='AYOutlineButton', 
                 outline='0px',
                 margin='0px',
                 font_weight='700',
                 line_height='1.71429',
                 font_size='0.875rem',
                 font_family='"Public Sans", sans-serif',
                 min_width='64px',
                 padding_x='5px',
                 padding_y='12px',
                 border_radius='8px',
                 border='rgba(145, 158, 171, 0.32)',
                 color='rgb(0, 0, 0)',
                 hover_bg_color='rgba(33, 43, 54, 0.08)',
                 hover_bd_color='2px solid rgb(0, 0, 0)',
                 disabled=False):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(styles.format(
            outline,
            margin,
            font_weight,
            line_height,
            font_size,
            font_family,
            min_width,
            padding_x,
            padding_y,
            border_radius,
            border,
            color,
            hover_bg_color,
            hover_bd_color
        ))
        if disabled is False:
            self.setCursor(Qt.PointingHandCursor)
        

