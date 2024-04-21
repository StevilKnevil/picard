# Form implementation generated from reading ui file 'ui/options_interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from picard.i18n import gettext as _


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InterfaceOptionsPage(object):
    def setupUi(self, InterfaceOptionsPage):
        InterfaceOptionsPage.setObjectName("InterfaceOptionsPage")
        InterfaceOptionsPage.resize(466, 543)
        self.vboxlayout = QtWidgets.QVBoxLayout(InterfaceOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(parent=InterfaceOptionsPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolbar_show_labels = QtWidgets.QCheckBox(parent=self.groupBox)
        self.toolbar_show_labels.setObjectName("toolbar_show_labels")
        self.verticalLayout_3.addWidget(self.toolbar_show_labels)
        self.show_menu_icons = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show_menu_icons.setObjectName("show_menu_icons")
        self.verticalLayout_3.addWidget(self.show_menu_icons)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ui_language = QtWidgets.QComboBox(parent=self.groupBox)
        self.ui_language.setObjectName("ui_language")
        self.horizontalLayout.addWidget(self.ui_language)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_theme = QtWidgets.QLabel(parent=self.groupBox)
        self.label_theme.setObjectName("label_theme")
        self.verticalLayout_3.addWidget(self.label_theme)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ui_theme = QtWidgets.QComboBox(parent=self.groupBox)
        self.ui_theme.setObjectName("ui_theme")
        self.horizontalLayout_2.addWidget(self.ui_theme)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.vboxlayout.addWidget(self.groupBox)
        self.miscellaneous_box = QtWidgets.QGroupBox(parent=InterfaceOptionsPage)
        self.miscellaneous_box.setObjectName("miscellaneous_box")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.miscellaneous_box)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.allow_multi_dirs_selection = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.allow_multi_dirs_selection.setObjectName("allow_multi_dirs_selection")
        self.vboxlayout1.addWidget(self.allow_multi_dirs_selection)
        self.builtin_search = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.builtin_search.setObjectName("builtin_search")
        self.vboxlayout1.addWidget(self.builtin_search)
        self.use_adv_search_syntax = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.use_adv_search_syntax.setObjectName("use_adv_search_syntax")
        self.vboxlayout1.addWidget(self.use_adv_search_syntax)
        self.new_user_dialog = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.new_user_dialog.setObjectName("new_user_dialog")
        self.vboxlayout1.addWidget(self.new_user_dialog)
        self.quit_confirmation = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.quit_confirmation.setObjectName("quit_confirmation")
        self.vboxlayout1.addWidget(self.quit_confirmation)
        self.file_save_warning = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.file_save_warning.setObjectName("file_save_warning")
        self.vboxlayout1.addWidget(self.file_save_warning)
        self.filebrowser_horizontal_autoscroll = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.filebrowser_horizontal_autoscroll.setObjectName("filebrowser_horizontal_autoscroll")
        self.vboxlayout1.addWidget(self.filebrowser_horizontal_autoscroll)
        self.starting_directory = QtWidgets.QCheckBox(parent=self.miscellaneous_box)
        self.starting_directory.setObjectName("starting_directory")
        self.vboxlayout1.addWidget(self.starting_directory)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.starting_directory_path = QtWidgets.QLineEdit(parent=self.miscellaneous_box)
        self.starting_directory_path.setEnabled(False)
        self.starting_directory_path.setObjectName("starting_directory_path")
        self.horizontalLayout_4.addWidget(self.starting_directory_path)
        self.starting_directory_browse = QtWidgets.QPushButton(parent=self.miscellaneous_box)
        self.starting_directory_browse.setEnabled(False)
        self.starting_directory_browse.setObjectName("starting_directory_browse")
        self.horizontalLayout_4.addWidget(self.starting_directory_browse)
        self.vboxlayout1.addLayout(self.horizontalLayout_4)
        self.ui_theme_container = QtWidgets.QWidget(parent=self.miscellaneous_box)
        self.ui_theme_container.setEnabled(True)
        self.ui_theme_container.setObjectName("ui_theme_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ui_theme_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vboxlayout1.addWidget(self.ui_theme_container)
        self.vboxlayout.addWidget(self.miscellaneous_box)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(InterfaceOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(InterfaceOptionsPage)
        InterfaceOptionsPage.setTabOrder(self.toolbar_show_labels, self.show_menu_icons)
        InterfaceOptionsPage.setTabOrder(self.show_menu_icons, self.ui_language)
        InterfaceOptionsPage.setTabOrder(self.ui_language, self.ui_theme)
        InterfaceOptionsPage.setTabOrder(self.ui_theme, self.allow_multi_dirs_selection)
        InterfaceOptionsPage.setTabOrder(self.allow_multi_dirs_selection, self.builtin_search)
        InterfaceOptionsPage.setTabOrder(self.builtin_search, self.use_adv_search_syntax)
        InterfaceOptionsPage.setTabOrder(self.use_adv_search_syntax, self.new_user_dialog)
        InterfaceOptionsPage.setTabOrder(self.new_user_dialog, self.quit_confirmation)
        InterfaceOptionsPage.setTabOrder(self.quit_confirmation, self.file_save_warning)
        InterfaceOptionsPage.setTabOrder(self.file_save_warning, self.filebrowser_horizontal_autoscroll)
        InterfaceOptionsPage.setTabOrder(self.filebrowser_horizontal_autoscroll, self.starting_directory)
        InterfaceOptionsPage.setTabOrder(self.starting_directory, self.starting_directory_path)
        InterfaceOptionsPage.setTabOrder(self.starting_directory_path, self.starting_directory_browse)

    def retranslateUi(self, InterfaceOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_("Appearance"))
        self.toolbar_show_labels.setText(_("Show text labels under icons"))
        self.show_menu_icons.setText(_("Show icons in menus"))
        self.label.setText(_("User interface language:"))
        self.label_theme.setText(_("User interface color theme:"))
        self.miscellaneous_box.setTitle(_("Miscellaneous"))
        self.allow_multi_dirs_selection.setText(_("Allow selection of multiple directories"))
        self.builtin_search.setText(_("Use builtin search rather than looking in browser"))
        self.use_adv_search_syntax.setText(_("Use advanced query syntax"))
        self.new_user_dialog.setText(_("Show the new user dialog when starting Picard"))
        self.quit_confirmation.setText(_("Show a quit confirmation dialog for unsaved changes"))
        self.file_save_warning.setText(_("Show a confirmation dialog when saving files"))
        self.filebrowser_horizontal_autoscroll.setText(_("Adjust horizontal position in file browser automatically"))
        self.starting_directory.setText(_("Begin browsing in the following directory:"))
        self.starting_directory_browse.setText(_("Browse…"))
