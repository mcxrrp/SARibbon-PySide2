# -*- coding: utf-8 -*-
"""
@Module     SARibbonApplicationButton
@Author     ROOT
"""
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton


class SARibbonApplicationButton(QPushButton):
    def __init__(self, *_args):
        """
        __init__(parent=None)
        __init__(str, parent=None)
        __init__(QIcon, str, parent=None)
        """
        super().__init__(*_args)
        self.setFocusPolicy(Qt.NoFocus)
        self.setFlat(True)
