from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


styles = """
        QPushButton {{
            outline: {};
            border: {};
            margin: {};
            font-weight: {};
            line-height: {};
            font-size: {};
            font-family: {};
            min-width: {};
            padding: {} {};
            border-radius: {};
            color:  {};
            background-color: {};
        }}
        QPushButton::hover {{
            background-color: {};
        }}

"""


class AYSoftButton(QPushButton):
    def __init__(self, text, 
                 outline='0px',
                 border='0px currentcolor',
                 margin='0px',
                 font_weight='700',
                 line_height='1.71429',
                 font_size='0.875rem',
                 font_family='"Public Sans", sans-serif',
                 min_width='64px',
                 padding_x='6px',
                 padding_y='12px',
                 border_radius='8px',
                 color='rgb(0, 0, 0)', 
                 background_color='rgba(145, 158, 171, 0.08)',
                 hover_bg_color='rgba(145, 158, 171, 0.24)',
                 disabled=False):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(styles.format(
            outline,
            border,
            margin,
            font_weight,
            line_height,
            font_size,
            font_family,
            min_width,
            padding_x,
            padding_y,
            border_radius,
            color, 
            background_color,
            hover_bg_color
        ))
        if disabled is False:
            self.setCursor(Qt.PointingHandCursor)
        

