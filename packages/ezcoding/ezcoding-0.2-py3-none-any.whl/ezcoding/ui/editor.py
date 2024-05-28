# -*- coding: utf-8 -*-

from typing import Optional, Dict, AnyStr, Union

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QDialog, QWidget, QTableWidget, QPushButton, QSpacerItem, QHBoxLayout, QVBoxLayout,
                               QSizePolicy, QTableWidgetItem, QHeaderView)

from ezcoding.generator import Generator
from ezcoding.utils import is_built_in_variable


def set_table_item_not_editable(item: QTableWidgetItem):
    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)


class EditorUI(object):

    def __init__(self, editor: QDialog):
        editor.setMinimumSize(960, 360)
        editor.setWindowTitle('Variable Value Editor')

        self.table = QTableWidget(editor)
        self.apply = QPushButton('Apply', editor)
        self.discard = QPushButton('Discard', editor)
        self.bottom_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.bottom_layout = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Variable', 'Value', 'Preview', 'Reset'])
        self.table.setColumnWidth(0, 128)
        self.table.setColumnWidth(1, 192)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table.setColumnWidth(3, 64)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        self.apply.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.discard.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.bottom_layout.addSpacerItem(self.bottom_spacer)
        self.bottom_layout.addWidget(self.apply)
        self.bottom_layout.addWidget(self.discard)

        self.layout.addWidget(self.table)
        self.layout.addLayout(self.bottom_layout)

        editor.setLayout(self.layout)


class Editor(QDialog):

    def __init__(self, values: Dict[AnyStr, Union[AnyStr, Generator]], parent: Optional[QWidget] = None,
                 flags: Qt.WindowType = Qt.WindowType.Dialog):
        super().__init__(parent, flags)
        self.__ui = EditorUI(self)
        self.__load_table(values)
        self.__values: Dict[AnyStr, Union[AnyStr, Generator]] = values
        self.__bind_signals()

    def __load_table(self, values: Dict[AnyStr, Union[AnyStr, Generator]]):
        self.__ui.table.setRowCount(len(values))
        font = QFont('Consolas', 10)
        row_index = 0
        for variable in values:
            value = values[variable]
            not_editable = isinstance(value, Generator) or is_built_in_variable(variable)
            value_text = ''
            preview_text = ''
            if isinstance(value, str):
                value_text = value
                preview_text = value
            elif isinstance(value, Generator):
                value_text = type(value).__name__
                preview_text = value.generate(**values)

            variable_item = QTableWidgetItem(variable)
            variable_item.setFont(font)
            set_table_item_not_editable(variable_item)
            self.__ui.table.setItem(row_index, 0, variable_item)

            value_item = QTableWidgetItem(value_text)
            value_item.setFont(font)
            if not_editable:
                set_table_item_not_editable(value_item)
            self.__ui.table.setItem(row_index, 1, value_item)

            preview_item = QTableWidgetItem(preview_text)
            preview_item.setFont(font)
            set_table_item_not_editable(preview_item)
            self.__ui.table.setItem(row_index, 2, preview_item)

            if not_editable:
                reset_item = QTableWidgetItem()
                set_table_item_not_editable(reset_item)
                self.__ui.table.setItem(row_index, 3, reset_item)
            else:
                reset_button = QPushButton('Reset')
                reset_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                self.__ui.table.setCellWidget(row_index, 3, reset_button)

            row_index += 1

    def __bind_signals(self):
        self.__ui.apply.clicked.connect(self.__on_apply_clicked)
        self.__ui.discard.clicked.connect(self.__on_discard_clicked)

    def __update_values(self):
        rows = self.__ui.table.rowCount()
        for i in range(rows):
            variable = self.__ui.table.item(i, 0).text()
            value = self.__values[variable]
            if not isinstance(value, str):
                continue
            value = self.__ui.table.item(i, 1).text()
            self.__values[variable] = value

    @Slot(bool)
    def __on_apply_clicked(self, checked: bool):
        self.__update_values()
        self.close()

    @Slot(bool)
    def __on_discard_clicked(self, checked: bool):
        self.close()
