from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

# Tạo một QIcon từ một tập tin hình ảnh (ví dụ: "icon.png")
# icon = QIcon("e:/Python/pyside6/Lop_hoc_vscode/postman/icons/plus.png")

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


class AYAddButton(QPushButton):
    def __init__(self, text, link_icon,
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
                 color='rgb(255, 255, 255)', 
                 background_color='rgb(33, 43, 54)',
                 hover_bg_color='rgb(69, 79, 91)',
                 disabled=False):
        super().__init__()
        print('hahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        self.setText(text)
        self.setIcon(link_icon)
        # Căn chỉnh biểu tượng và văn bản của nút
        self.setIconSize(link_icon.actualSize(self.size()))

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
        

