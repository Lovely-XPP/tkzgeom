from PyQt5 import QtCore, QtWidgets

import Constant as c


def fill_code_fields(scene):
    if c.TYPES[scene.current_tab_idx] != 'code':
        return

    scene.ui.packages_listWidget.clear()
    for i, package in enumerate(scene.project_data.packages):
        item = QtWidgets.QListWidgetItem(package)
        if i > 5:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        scene.ui.packages_listWidget.addItem(item)