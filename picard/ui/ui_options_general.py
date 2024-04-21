# Form implementation generated from reading ui file 'ui/options_general.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from picard.i18n import gettext as _


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GeneralOptionsPage(object):
    def setupUi(self, GeneralOptionsPage):
        GeneralOptionsPage.setObjectName("GeneralOptionsPage")
        GeneralOptionsPage.resize(403, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeneralOptionsPage.sizePolicy().hasHeightForWidth())
        GeneralOptionsPage.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(GeneralOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(parent=GeneralOptionsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")
        self.server_port = QtWidgets.QSpinBox(parent=self.groupBox)
        self.server_port.setMinimum(1)
        self.server_port.setMaximum(65535)
        self.server_port.setProperty("value", 80)
        self.server_port.setObjectName("server_port")
        self.gridlayout.addWidget(self.server_port, 1, 1, 1, 1)
        self.server_host_primary_warning = QtWidgets.QFrame(parent=self.groupBox)
        self.server_host_primary_warning.setStyleSheet("QFrame { background-color: #ffc107; color: black }\n"
"QCheckBox { color: black }")
        self.server_host_primary_warning.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.server_host_primary_warning.setObjectName("server_host_primary_warning")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.server_host_primary_warning)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.server_host_primary_warning)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.use_server_for_submission = QtWidgets.QCheckBox(parent=self.server_host_primary_warning)
        self.use_server_for_submission.setObjectName("use_server_for_submission")
        self.verticalLayout_4.addWidget(self.use_server_for_submission)
        self.gridlayout.addWidget(self.server_host_primary_warning, 3, 0, 1, 2)
        self.server_host = QtWidgets.QComboBox(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_host.sizePolicy().hasHeightForWidth())
        self.server_host.setSizePolicy(sizePolicy)
        self.server_host.setEditable(True)
        self.server_host.setObjectName("server_host")
        self.gridlayout.addWidget(self.server_host, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(1, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.rename_files_2 = QtWidgets.QGroupBox(parent=GeneralOptionsPage)
        self.rename_files_2.setObjectName("rename_files_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rename_files_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.login_error = QtWidgets.QLabel(parent=self.rename_files_2)
        self.login_error.setText("")
        self.login_error.setObjectName("login_error")
        self.verticalLayout_3.addWidget(self.login_error)
        self.logged_in = QtWidgets.QLabel(parent=self.rename_files_2)
        self.logged_in.setText("")
        self.logged_in.setObjectName("logged_in")
        self.verticalLayout_3.addWidget(self.logged_in)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QPushButton(parent=self.rename_files_2)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.logout = QtWidgets.QPushButton(parent=self.rename_files_2)
        self.logout.setObjectName("logout")
        self.horizontalLayout.addWidget(self.logout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.vboxlayout.addWidget(self.rename_files_2)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=GeneralOptionsPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.analyze_new_files = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.analyze_new_files.setObjectName("analyze_new_files")
        self.verticalLayout.addWidget(self.analyze_new_files)
        self.cluster_new_files = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.cluster_new_files.setObjectName("cluster_new_files")
        self.verticalLayout.addWidget(self.cluster_new_files)
        self.ignore_file_mbids = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.ignore_file_mbids.setObjectName("ignore_file_mbids")
        self.verticalLayout.addWidget(self.ignore_file_mbids)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.update_check_groupbox = QtWidgets.QGroupBox(parent=GeneralOptionsPage)
        self.update_check_groupbox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_check_groupbox.sizePolicy().hasHeightForWidth())
        self.update_check_groupbox.setSizePolicy(sizePolicy)
        self.update_check_groupbox.setObjectName("update_check_groupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.update_check_groupbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_for_plugin_updates = QtWidgets.QCheckBox(parent=self.update_check_groupbox)
        self.check_for_plugin_updates.setObjectName("check_for_plugin_updates")
        self.verticalLayout_2.addWidget(self.check_for_plugin_updates)
        self.program_update_check_group = QtWidgets.QWidget(parent=self.update_check_groupbox)
        self.program_update_check_group.setMinimumSize(QtCore.QSize(0, 0))
        self.program_update_check_group.setObjectName("program_update_check_group")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.program_update_check_group)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.check_for_updates = QtWidgets.QCheckBox(parent=self.program_update_check_group)
        self.check_for_updates.setObjectName("check_for_updates")
        self.verticalLayout_6.addWidget(self.check_for_updates)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.program_update_check_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.update_check_days = QtWidgets.QSpinBox(parent=self.program_update_check_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_check_days.sizePolicy().hasHeightForWidth())
        self.update_check_days.setSizePolicy(sizePolicy)
        self.update_check_days.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.update_check_days.setMinimum(1)
        self.update_check_days.setObjectName("update_check_days")
        self.gridLayout.addWidget(self.update_check_days, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.program_update_check_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.update_level = QtWidgets.QComboBox(parent=self.program_update_check_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_level.sizePolicy().hasHeightForWidth())
        self.update_level.setSizePolicy(sizePolicy)
        self.update_level.setEditable(False)
        self.update_level.setObjectName("update_level")
        self.gridLayout_2.addWidget(self.update_level, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.program_update_check_group)
        self.program_update_check_frame = QtWidgets.QFrame(parent=self.update_check_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.program_update_check_frame.sizePolicy().hasHeightForWidth())
        self.program_update_check_frame.setSizePolicy(sizePolicy)
        self.program_update_check_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.program_update_check_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.program_update_check_frame.setObjectName("program_update_check_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.program_update_check_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2.addWidget(self.program_update_check_frame)
        self.vboxlayout.addWidget(self.update_check_groupbox)
        spacerItem2 = QtWidgets.QSpacerItem(181, 21, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(GeneralOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(GeneralOptionsPage)
        GeneralOptionsPage.setTabOrder(self.server_host, self.server_port)
        GeneralOptionsPage.setTabOrder(self.server_port, self.use_server_for_submission)
        GeneralOptionsPage.setTabOrder(self.use_server_for_submission, self.login)
        GeneralOptionsPage.setTabOrder(self.login, self.logout)
        GeneralOptionsPage.setTabOrder(self.logout, self.analyze_new_files)
        GeneralOptionsPage.setTabOrder(self.analyze_new_files, self.cluster_new_files)
        GeneralOptionsPage.setTabOrder(self.cluster_new_files, self.ignore_file_mbids)
        GeneralOptionsPage.setTabOrder(self.ignore_file_mbids, self.check_for_plugin_updates)
        GeneralOptionsPage.setTabOrder(self.check_for_plugin_updates, self.check_for_updates)
        GeneralOptionsPage.setTabOrder(self.check_for_updates, self.update_check_days)
        GeneralOptionsPage.setTabOrder(self.update_check_days, self.update_level)

    def retranslateUi(self, GeneralOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_("MusicBrainz Server"))
        self.label_4.setText(_("You have configured an unofficial MusicBrainz server. By default submissions of releases, recordings and disc IDs will go to the primary database on musicbrainz.org."))
        self.use_server_for_submission.setText(_("Submit data to the configured server"))
        self.label_7.setText(_("Port:"))
        self.label.setText(_("Server address:"))
        self.rename_files_2.setTitle(_("MusicBrainz Account"))
        self.login.setText(_("Log in"))
        self.logout.setText(_("Log out"))
        self.groupBox_2.setTitle(_("General"))
        self.analyze_new_files.setText(_("Automatically scan all new files"))
        self.cluster_new_files.setText(_("Automatically cluster all new files"))
        self.ignore_file_mbids.setText(_("Ignore MBIDs when loading new files"))
        self.update_check_groupbox.setTitle(_("Update Checking"))
        self.check_for_plugin_updates.setText(_("Check for plugin updates during startup"))
        self.check_for_updates.setText(_("Check for program updates during startup"))
        self.label_2.setText(_("Days between checks:"))
        self.label_3.setText(_("Updates to check:"))
