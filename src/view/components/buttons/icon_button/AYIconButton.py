from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor
import xml.etree.ElementTree as ET


icon = QIcon("e:/Python/pyside6/Lop_hoc_vscode/postman/icons/alarm.svg")

import xml.etree.ElementTree as ET





styles = """
        QPushButton {{
            outline: {};
            border: {};
            margin: {};

            width: {};
            height: {};

            font-size: {};

            padding: {} {} {} {};
            border-radius: {};
            color:  {};
            background-color: {};
        }}
        QPushButton::hover {{
            background-color: {};
        }}

"""


class AYIconButton(QPushButton):
    def __init__(self, 
                 outline='0px',
                 border='100px currentcolor',
                 margin='0px',
                 width='20px',
                 height='20px',
                #  font_weight='700',
                #  line_height='1.71429',
                 font_size='1.5rem',
                #  font_family='"Public Sans", sans-serif',
                #  min_width='64px',
                 padding_top='8px',
                 padding_right='8px',
                 padding_bottom='8px',
                 padding_left='8px',
                #  padding_y='12px',
                 border_radius='50%',
                 color='rgb(0, 0, 0)', 
                 background_color='transparent',
                 hover_bg_color='rgba(99, 115, 129, 0.08)',
                 disabled=False):
        super().__init__()
        # self.change_color_icon(color)
        icon = self.set_new_icon(color=color)
        self.setIcon(icon)
        # Căn chỉnh biểu tượng và văn bản của nút
        # self.setIconSize(icon.actualSize(self.size()))
        self.setStyleSheet(styles.format(
            outline,
            border,
            margin,
            width,
            height,
            # font_weight,
            # line_height,
            font_size,
            # font_family,
            # min_width,
            # padding_x,
            padding_top,
            padding_right,
            padding_bottom,
            padding_left,
            border_radius,
            color, 
            background_color,
            hover_bg_color
        ))
        if disabled is False:
            self.setCursor(Qt.PointingHandCursor)
    

    def set_new_icon(self, color):
            # Đọc tệp SVG
        with open("e:/Python/pyside6/Lop_hoc_vscode/postman/icons/alarm.svg", "r") as file:
            svg_content = file.read()

        # Phân tích tệp SVG thành cấu trúc dữ liệu XML
        root = ET.fromstring(svg_content)

        # Thay đổi thuộc tính fill thành màu khác
        # new_fill_color = "blue"
        for element in root.iter():
            if 'fill' in element.attrib:
                element.set('fill', color)

        #Lưu tệp SVG đã được chỉnh sửa
        new_svg_content = ET.tostring(root, encoding='unicode')
        with open(f"e:/Python/pyside6/Lop_hoc_vscode/postman/icons/alarm.{color}.svg", "w") as file:
            file.write(new_svg_content)

        return QIcon(f"e:/Python/pyside6/Lop_hoc_vscode/postman/icons/alarm.{color}.svg")
        

