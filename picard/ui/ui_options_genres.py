# Form implementation generated from reading ui file 'ui/options_genres.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from PyQt6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from picard.i18n import gettext as _


class Ui_GenresOptionsPage(object):
    def setupUi(self, GenresOptionsPage):
        GenresOptionsPage.setObjectName("GenresOptionsPage")
        GenresOptionsPage.resize(590, 471)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(GenresOptionsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.use_genres = QtWidgets.QGroupBox(parent=GenresOptionsPage)
        self.use_genres.setFlat(False)
        self.use_genres.setCheckable(True)
        self.use_genres.setChecked(False)
        self.use_genres.setObjectName("use_genres")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.use_genres)
        self.verticalLayout.setObjectName("verticalLayout")
        self.only_my_genres = QtWidgets.QCheckBox(parent=self.use_genres)
        self.only_my_genres.setObjectName("only_my_genres")
        self.verticalLayout.addWidget(self.only_my_genres)
        self.artists_genres = QtWidgets.QCheckBox(parent=self.use_genres)
        self.artists_genres.setObjectName("artists_genres")
        self.verticalLayout.addWidget(self.artists_genres)
        self.folksonomy_tags = QtWidgets.QCheckBox(parent=self.use_genres)
        self.folksonomy_tags.setObjectName("folksonomy_tags")
        self.verticalLayout.addWidget(self.folksonomy_tags)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_5 = QtWidgets.QLabel(parent=self.use_genres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.hboxlayout.addWidget(self.label_5)
        self.min_genre_usage = QtWidgets.QSpinBox(parent=self.use_genres)
        self.min_genre_usage.setMaximum(100)
        self.min_genre_usage.setObjectName("min_genre_usage")
        self.hboxlayout.addWidget(self.min_genre_usage)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label_6 = QtWidgets.QLabel(parent=self.use_genres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.hboxlayout1.addWidget(self.label_6)
        self.max_genres = QtWidgets.QSpinBox(parent=self.use_genres)
        self.max_genres.setMaximum(100)
        self.max_genres.setObjectName("max_genres")
        self.hboxlayout1.addWidget(self.max_genres)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.ignore_genres_4 = QtWidgets.QLabel(parent=self.use_genres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_genres_4.sizePolicy().hasHeightForWidth())
        self.ignore_genres_4.setSizePolicy(sizePolicy)
        self.ignore_genres_4.setObjectName("ignore_genres_4")
        self.hboxlayout2.addWidget(self.ignore_genres_4)
        self.join_genres = QtWidgets.QComboBox(parent=self.use_genres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.join_genres.sizePolicy().hasHeightForWidth())
        self.join_genres.setSizePolicy(sizePolicy)
        self.join_genres.setEditable(True)
        self.join_genres.setObjectName("join_genres")
        self.join_genres.addItem("")
        self.join_genres.setItemText(0, "")
        self.join_genres.addItem("")
        self.join_genres.addItem("")
        self.hboxlayout2.addWidget(self.join_genres)
        self.verticalLayout.addLayout(self.hboxlayout2)
        self.label_genres_filter = QtWidgets.QLabel(parent=self.use_genres)
        self.label_genres_filter.setObjectName("label_genres_filter")
        self.verticalLayout.addWidget(self.label_genres_filter)
        self.genres_filter = QtWidgets.QPlainTextEdit(parent=self.use_genres)
        self.genres_filter.setObjectName("genres_filter")
        self.verticalLayout.addWidget(self.genres_filter)
        self.label_test_genres_filter = QtWidgets.QLabel(parent=self.use_genres)
        self.label_test_genres_filter.setObjectName("label_test_genres_filter")
        self.verticalLayout.addWidget(self.label_test_genres_filter)
        self.test_genres_filter = QtWidgets.QPlainTextEdit(parent=self.use_genres)
        self.test_genres_filter.setObjectName("test_genres_filter")
        self.verticalLayout.addWidget(self.test_genres_filter)
        self.label_test_genres_filter_error = QtWidgets.QLabel(parent=self.use_genres)
        self.label_test_genres_filter_error.setText("")
        self.label_test_genres_filter_error.setObjectName("label_test_genres_filter_error")
        self.verticalLayout.addWidget(self.label_test_genres_filter_error)
        self.verticalLayout_2.addWidget(self.use_genres)
        spacerItem = QtWidgets.QSpacerItem(181, 31, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5.setBuddy(self.min_genre_usage)
        self.label_6.setBuddy(self.min_genre_usage)

        self.retranslateUi(GenresOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(GenresOptionsPage)

    def retranslateUi(self, GenresOptionsPage):
        self.use_genres.setTitle(_("Use genres from MusicBrainz"))
        self.only_my_genres.setText(_("Use only my genres"))
        self.artists_genres.setText(_("Fall back on album\'s artists genres if no genres are found for the release or release group"))
        self.folksonomy_tags.setText(_("Use folksonomy tags as genre"))
        self.label_5.setText(_("Minimal genre usage:"))
        self.min_genre_usage.setSuffix(_(" %"))
        self.label_6.setText(_("Maximum number of genres:"))
        self.ignore_genres_4.setText(_("Join multiple genres with:"))
        self.join_genres.setItemText(1, _(" / "))
        self.join_genres.setItemText(2, _(", "))
        self.label_genres_filter.setText(_("Genres or folksonomy tags to include or exclude, one per line:"))
        self.label_test_genres_filter.setText(_("Playground for genres or folksonomy tags filters (cleared on exit):"))
