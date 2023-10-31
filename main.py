

# import các thư viện hệ thống
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QWidget, QVBoxLayout, QSplitter, QHBoxLayout
from PySide6.QtGui import QIcon
from src.view import AYContainedButton, AYOutlineButton, AYTextButton, AYSoftButton, AYAddButton, AYIconButton, AYFloatingActionButton


import math
from src.theme import palette
import numpy as np
from src.utils import alpha



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(1500, 700))
        self.setWindowTitle('POSTMAN')

        # init theme
        self.theme = palette('light')
        print('themeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print(self.theme.action.active)
        print('themeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print(self.theme.__dict__)
    

        main_layout = QVBoxLayout()

        # section_header
        section_header = QFrame()
        section_header.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header.setMinimumHeight(50)
        hlo_section_header = QHBoxLayout(section_header)

        btn_ay_default = AYContainedButton('Default')
        btn_ay_primary = AYContainedButton(text='Primary', background_color=self.theme.primary.main, hover_bg_color=self.theme.primary.dark)
        btn_ay_secondary= AYContainedButton(text='Secondary', background_color=self.theme.secondary.main, hover_bg_color=self.theme.secondary.dark)
        btn_ay_disable= AYContainedButton(text='Disabled', background_color=self.theme.action.disabled_background, hover_bg_color=self.theme.action.disabled_background, disabled=True)
        btn_ay_link = AYContainedButton('Link')
        btn_ay_info= AYContainedButton(text='Info', background_color=self.theme.info.main, hover_bg_color=self.theme.info.dark, disabled=True)
        btn_ay_success= AYContainedButton(text='Success', background_color=self.theme.success.main, hover_bg_color=self.theme.success.dark, disabled=True)
        btn_ay_warning= AYContainedButton(text='Warning', background_color=self.theme.warning.main, hover_bg_color=self.theme.warning.dark, disabled=True)
        btn_ay_error= AYContainedButton(text='Error', background_color=self.theme.error.main, hover_bg_color=self.theme.error.dark, disabled=True)


        hlo_section_header.addWidget(btn_ay_default) 
        hlo_section_header.addWidget(btn_ay_primary)
        hlo_section_header.addWidget(btn_ay_secondary)
        hlo_section_header.addWidget(btn_ay_disable)
        hlo_section_header.addWidget(btn_ay_link)
        hlo_section_header.addWidget(btn_ay_info)
        hlo_section_header.addWidget(btn_ay_success)
        hlo_section_header.addWidget(btn_ay_warning)
        hlo_section_header.addWidget(btn_ay_error)


        # section_header_1
        section_header_1 = QFrame()
        section_header_1.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_1.setMinimumHeight(50)
        hlo_section_header_1 = QHBoxLayout(section_header_1)

        btn_ay_outline_default = AYOutlineButton('Default')
        btn_ay_outline_primary = AYOutlineButton(text='Primary', color=self.theme.primary.main, border=alpha(self.theme.primary.main, 0.5), hover_bg_color=alpha(self.theme.primary.main, 0.08), hover_bd_color=f'2px solid {self.theme.primary.main}')
        btn_ay_outline_secondary= AYOutlineButton(text='Secondary', color=self.theme.secondary.main, border=alpha(self.theme.secondary.main, 0.5), hover_bg_color=alpha(self.theme.secondary.main, 0.08), hover_bd_color=f'2px solid {self.theme.secondary.main}')
        btn_ay_outline_disable= AYOutlineButton(text='Disabled', color=self.theme.action.disabled, border=self.theme.action.disabled, hover_bg_color='', hover_bd_color=f'1px solid {self.theme.action.disabled}', disabled=True)
        btn_ay_outline_link = AYOutlineButton('Link')
        btn_ay_outline_info = AYOutlineButton(text='Info', color=self.theme.info.main, border=alpha(self.theme.info.main, 0.5), hover_bg_color=alpha(self.theme.info.main, 0.08), hover_bd_color=f'2px solid {self.theme.info.main}')
        btn_ay_outline_success = AYOutlineButton(text='Success', color=self.theme.success.main, border=alpha(self.theme.success.main, 0.5), hover_bg_color=alpha(self.theme.success.main, 0.08), hover_bd_color=f'2px solid {self.theme.success.main}')
        btn_ay_outline_warning = AYOutlineButton(text='Warning', color=self.theme.warning.main, border=alpha(self.theme.warning.main, 0.5), hover_bg_color=alpha(self.theme.warning.main, 0.08), hover_bd_color=f'2px solid {self.theme.warning.main}')
        btn_ay_outline_error = AYOutlineButton(text='Error', color=self.theme.error.main, border=alpha(self.theme.error.main, 0.5), hover_bg_color=alpha(self.theme.error.main, 0.08), hover_bd_color=f'2px solid {self.theme.error.main}')


        hlo_section_header_1.addWidget(btn_ay_outline_default)
        hlo_section_header_1.addWidget(btn_ay_outline_primary)
        hlo_section_header_1.addWidget(btn_ay_outline_secondary)
        hlo_section_header_1.addWidget(btn_ay_outline_disable)
        hlo_section_header_1.addWidget(btn_ay_outline_link)
        hlo_section_header_1.addWidget(btn_ay_outline_info)
        hlo_section_header_1.addWidget(btn_ay_outline_success)
        hlo_section_header_1.addWidget(btn_ay_outline_warning)
        hlo_section_header_1.addWidget(btn_ay_outline_error)

        # section_header_2
        section_header_2 = QFrame()
        section_header_2.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_2.setMinimumHeight(50)
        hlo_section_header_2 = QHBoxLayout(section_header_2)

        btn_ay_text_default = AYTextButton('Default')
        btn_ay_text_primary = AYTextButton(text='Primary', color=self.theme.primary.main, hover_bg_color=alpha(self.theme.primary.main, 0.08), hover_bd_color=self.theme.primary.main)
        btn_ay_text_secondary= AYTextButton(text='Secondary', color=self.theme.secondary.main, hover_bg_color=alpha(self.theme.secondary.main, 0.08), hover_bd_color=self.theme.secondary.main)
        btn_ay_text_disable= AYTextButton(text='Disabled', color=self.theme.action.disabled, hover_bg_color='', hover_bd_color=self.theme.action.disabled, disabled=True)
        btn_ay_text_link = AYTextButton('Link')
        btn_ay_text_info = AYTextButton(text='Info', color=self.theme.info.main, hover_bg_color=alpha(self.theme.info.main, 0.08), hover_bd_color=self.theme.info.main)
        btn_ay_text_success = AYTextButton(text='Success', color=self.theme.success.main, hover_bg_color=alpha(self.theme.success.main, 0.08), hover_bd_color=self.theme.success.main)
        btn_ay_text_warning = AYTextButton(text='Warning', color=self.theme.warning.main, hover_bg_color=alpha(self.theme.warning.main, 0.08), hover_bd_color=self.theme.warning.main)
        btn_ay_text_error = AYTextButton(text='Error', color=self.theme.error.main, hover_bg_color=alpha(self.theme.error.main, 0.08), hover_bd_color=self.theme.error.main)


        hlo_section_header_2.addWidget(btn_ay_text_default)
        hlo_section_header_2.addWidget(btn_ay_text_primary)
        hlo_section_header_2.addWidget(btn_ay_text_secondary)
        hlo_section_header_2.addWidget(btn_ay_text_disable)
        hlo_section_header_2.addWidget(btn_ay_text_link)
        hlo_section_header_2.addWidget(btn_ay_text_info)
        hlo_section_header_2.addWidget(btn_ay_text_success)
        hlo_section_header_2.addWidget(btn_ay_text_warning)
        hlo_section_header_2.addWidget(btn_ay_text_error)


        # section_header_3
        section_header_3 = QFrame()
        section_header_3.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_3.setMinimumHeight(50)
        hlo_section_header_3 = QHBoxLayout(section_header_3)

        btn_ay_soft_default = AYSoftButton('Default')
        btn_ay_soft_primary = AYSoftButton(text='Primary', color=self.theme.primary.dark, background_color=alpha(self.theme.primary.main, 0.16), hover_bg_color=alpha(self.theme.primary.main, 0.32))
        btn_ay_soft_secondary = AYSoftButton(text='Secondary', color=self.theme.secondary.dark, background_color=alpha(self.theme.secondary.main, 0.16), hover_bg_color=alpha(self.theme.secondary.main, 0.32))
        btn_ay_soft_disable = AYSoftButton(text='Disabled', color=self.theme.action.disabled, background_color=self.theme.action.disabled_background, hover_bg_color='', disabled=True)
        btn_ay_soft_link = AYSoftButton('Link')
        btn_ay_soft_info = AYSoftButton(text='Info', color=self.theme.info.dark, background_color=alpha(self.theme.info.main, 0.16), hover_bg_color=alpha(self.theme.info.main, 0.32), disabled=True)
        btn_ay_soft_success = AYSoftButton(text='Success', color=self.theme.success.dark, background_color=alpha(self.theme.success.main, 0.16), hover_bg_color=alpha(self.theme.success.main, 0.32), disabled=True)
        btn_ay_soft_warning = AYSoftButton(text='Warning', color=self.theme.warning.dark, background_color=alpha(self.theme.warning.main, 0.16), hover_bg_color=alpha(self.theme.warning.main, 0.32), disabled=True)
        btn_ay_soft_error = AYSoftButton(text='Error', color=self.theme.error.dark, background_color=alpha(self.theme.error.main, 0.16), hover_bg_color=alpha(self.theme.error.main, 0.32), disabled=True)


        hlo_section_header_3.addWidget(btn_ay_soft_default)
        hlo_section_header_3.addWidget(btn_ay_soft_primary)
        hlo_section_header_3.addWidget(btn_ay_soft_secondary)
        hlo_section_header_3.addWidget(btn_ay_soft_disable)
        hlo_section_header_3.addWidget(btn_ay_soft_link)
        hlo_section_header_3.addWidget(btn_ay_soft_info)
        hlo_section_header_3.addWidget(btn_ay_soft_success)
        hlo_section_header_3.addWidget(btn_ay_soft_warning)
        hlo_section_header_3.addWidget(btn_ay_soft_error)

        # section_header_4
        section_header_4 = QFrame()
        section_header_4.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_4.setMinimumHeight(50)
        hlo_section_header_4 = QHBoxLayout(section_header_4)

        btn_ay__icon_default = AYIconButton()
        btn_ay__icon_primary = AYIconButton(color=self.theme.primary.main, hover_bg_color=alpha(self.theme.primary.main, 0.08))
        btn_ay__icon_secondary= AYIconButton(color=self.theme.secondary.main, hover_bg_color=alpha(self.theme.secondary.main, 0.08))
        btn_ay__icon_disable= AYIconButton(color=self.theme.action.disabled, hover_bg_color='transparent', disabled=True)
        btn_ay__icon_info= AYIconButton(color=self.theme.info.main, hover_bg_color=alpha(self.theme.info.main, 0.08))
        btn_ay__icon_success= AYIconButton(color=self.theme.success.main, hover_bg_color=alpha(self.theme.success.main, 0.08))
        btn_ay__icon_warning= AYIconButton(color=self.theme.warning.main, hover_bg_color=alpha(self.theme.warning.main, 0.08))
        btn_ay__icon_error= AYIconButton(color=self.theme.error.main, hover_bg_color=alpha(self.theme.error.main, 0.08))



        hlo_section_header_4.addWidget(btn_ay__icon_default) 
        hlo_section_header_4.addWidget(btn_ay__icon_primary)
        hlo_section_header_4.addWidget(btn_ay__icon_secondary)
        hlo_section_header_4.addWidget(btn_ay__icon_disable)
        hlo_section_header_4.addWidget(btn_ay__icon_info)
        hlo_section_header_4.addWidget(btn_ay__icon_success)
        hlo_section_header_4.addWidget(btn_ay__icon_warning)
        hlo_section_header_4.addWidget(btn_ay__icon_error)



        # section_header_5
        section_header_5 = QFrame()
        section_header_5.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_5.setMinimumHeight(20)
        hlo_section_header_5 = QHBoxLayout(section_header_5)

        # Tạo một QIcon từ một tập tin hình ảnh (ví dụ: "icon.png")
        icon = QIcon("e:/Python/pyside6/Lop_hoc_vscode/postman/icons/plus.png")

        btn_ay_icon_primary_1 = AYAddButton(text='', link_icon=icon, background_color=self.theme.error.main, hover_bg_color=self.theme.error.dark)
        btn_ay_icon_primary_2 = AYAddButton(text='New', link_icon=icon, background_color=self.theme.primary.main, hover_bg_color=self.theme.primary.dark)

        hlo_section_header_5.addWidget(btn_ay_icon_primary_1)
        hlo_section_header_5.addWidget(btn_ay_icon_primary_2)


        # section_header_6
        section_header_6 = QFrame()
        section_header_6.setStyleSheet('background-color: rgba(145, 158, 171, 0.04)')
        section_header_6.setMinimumHeight(50)
        hlo_section_header_6 = QHBoxLayout(section_header_6)

        # btn_ay_floating_action_default = AYFloatingActionButton()
        btn_ay_default_primary = AYFloatingActionButton(background_color=self.theme.primary.main, hover_bg_color=self.theme.primary.dark)
        btn_ay_default_secondary = AYFloatingActionButton(background_color=self.theme.secondary.main, hover_bg_color=self.theme.secondary.dark)

        btn_ay_default_primary_text = AYFloatingActionButton(text='primary', background_color=self.theme.primary.main, hover_bg_color=self.theme.primary.dark)
        btn_ay_default_secondary_text = AYFloatingActionButton(text='secondary', background_color=self.theme.secondary.main, hover_bg_color=self.theme.secondary.dark)
        
        btn_ay_soft_primary_text = AYFloatingActionButton(text='primary', color=self.theme.primary.main, background_color=alpha(self.theme.primary.main, 0.16), hover_bg_color=alpha(self.theme.primary.main, 0.32))
        btn_ay_soft_secondary_text = AYFloatingActionButton(text='secondary', color=self.theme.secondary.main, background_color=alpha(self.theme.secondary.main, 0.16), hover_bg_color=alpha(self.theme.secondary.main, 0.32))


        # hlo_section_header_6.addWidget(btn_ay_floating_action_default) 
        hlo_section_header_6.addWidget(btn_ay_default_primary)
        hlo_section_header_6.addWidget(btn_ay_default_secondary)
        hlo_section_header_6.addWidget(btn_ay_default_primary_text)
        hlo_section_header_6.addWidget(btn_ay_default_secondary_text)
        # hlo_section_header_6.addWidget(btn_ay__icon_disable)
        # hlo_section_header_6.addWidget(btn_ay_floating_action_info)
        hlo_section_header_6.addWidget(btn_ay_soft_primary_text)
        hlo_section_header_6.addWidget(btn_ay_soft_secondary_text)
        # hlo_section_header_6.addWidget(btn_ay_outline_primary_text)
        # hlo_section_header_6.addWidget(btn_ay__icon_success)
        # hlo_section_header_6.addWidget(btn_ay__icon_warning)
        # hlo_section_header_6.addWidget(btn_ay__icon_error)



        # section_main
        section_main = QFrame()
        section_main.setStyleSheet('background-color: green')

        # section_bottom
        section_bottom = QFrame()
        section_bottom.setStyleSheet('background-color: green')

        # section_body
        section_body = QFrame()
        vlo_section_body = QVBoxLayout(section_body)
        section_body.setStyleSheet('background-color: gray')

        # splitter chia section_body thành 2 phần là section_main và section_bottom
        splitter_body = QSplitter(Qt.Vertical, section_body)
        splitter_body.addWidget(section_main)
        splitter_body.addWidget(section_bottom)

        # thêm splitter vào section_body
        vlo_section_body.addWidget(splitter_body)

        # section_bottom được chia thành 2 phần là section_bottom_menu và section_footer
        vlo_section_bottom = QVBoxLayout(section_bottom)
        # section_bottom.setLayout(section_bottom_layout)

        section_bottom_menu = QFrame()
        section_bottom_menu.setStyleSheet('background-color: yellow')
        section_bottom_menu.setFixedSize(self.width(), 40)

        section_bottom_footer = QFrame()
        section_bottom_footer.setStyleSheet('background-color: yellow')

        vlo_section_bottom.addWidget(section_bottom_menu)
        vlo_section_bottom.addWidget(section_bottom_footer)

        # main_layout gồm 2 phần chính là section_header và splitter_body
        main_layout.addWidget(section_header)
        main_layout.addWidget(section_header_1)
        main_layout.addWidget(section_header_2)
        main_layout.addWidget(section_header_3)
        main_layout.addWidget(section_header_4)
        main_layout.addWidget(section_header_5)
        main_layout.addWidget(section_header_6)
        main_layout.addWidget(section_body)
        

        # Khai báo widget
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
