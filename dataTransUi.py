# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataTransUi.ui'
#
# Created: Mon Sep 08 12:21:10 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dataTransWidget(object):
    def setupUi(self, dataTransWidget):
        dataTransWidget.setObjectName(_fromUtf8("dataTransWidget"))
        dataTransWidget.resize(606, 550)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dataTransWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(dataTransWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_11 = QtGui.QLabel(dataTransWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.cbBalanceSty = QtGui.QComboBox(dataTransWidget)
        self.cbBalanceSty.setMinimumSize(QtCore.QSize(150, 0))
        self.cbBalanceSty.setStatusTip(_fromUtf8(""))
        self.cbBalanceSty.setObjectName(_fromUtf8("cbBalanceSty"))
        self.horizontalLayout_2.addWidget(self.cbBalanceSty)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(dataTransWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtModelArea = QtGui.QLineEdit(self.groupBox)
        self.txtModelArea.setAutoFillBackground(False)
        self.txtModelArea.setObjectName(_fromUtf8("txtModelArea"))
        self.gridLayout.addWidget(self.txtModelArea, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.txtDeltaY = QtGui.QLineEdit(self.groupBox)
        self.txtDeltaY.setObjectName(_fromUtf8("txtDeltaY"))
        self.gridLayout.addWidget(self.txtDeltaY, 2, 4, 1, 1)
        self.txtDeltaX = QtGui.QLineEdit(self.groupBox)
        self.txtDeltaX.setObjectName(_fromUtf8("txtDeltaX"))
        self.gridLayout.addWidget(self.txtDeltaX, 1, 4, 1, 1)
        self.txtDeltaZ = QtGui.QLineEdit(self.groupBox)
        self.txtDeltaZ.setObjectName(_fromUtf8("txtDeltaZ"))
        self.gridLayout.addWidget(self.txtDeltaZ, 3, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.txtModelSpan = QtGui.QLineEdit(self.groupBox)
        self.txtModelSpan.setObjectName(_fromUtf8("txtModelSpan"))
        self.gridLayout.addWidget(self.txtModelSpan, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txtWindSpeed = QtGui.QLineEdit(self.groupBox)
        self.txtWindSpeed.setObjectName(_fromUtf8("txtWindSpeed"))
        self.gridLayout.addWidget(self.txtWindSpeed, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txtModelRefChord = QtGui.QLineEdit(self.groupBox)
        self.txtModelRefChord.setObjectName(_fromUtf8("txtModelRefChord"))
        self.gridLayout.addWidget(self.txtModelRefChord, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.txtModelRootChord = QtGui.QLineEdit(self.groupBox)
        self.txtModelRootChord.setObjectName(_fromUtf8("txtModelRootChord"))
        self.gridLayout.addWidget(self.txtModelRootChord, 2, 1, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 2, 5, 1)
        self.pbtnModelDataExport = QtGui.QPushButton(self.groupBox)
        self.pbtnModelDataExport.setObjectName(_fromUtf8("pbtnModelDataExport"))
        self.gridLayout.addWidget(self.pbtnModelDataExport, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.pbtnModelDataInput = QtGui.QPushButton(self.groupBox)
        self.pbtnModelDataInput.setObjectName(_fromUtf8("pbtnModelDataInput"))
        self.gridLayout.addWidget(self.pbtnModelDataInput, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(dataTransWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.txtAeroFile = QtGui.QLineEdit(self.groupBox_2)
        self.txtAeroFile.setObjectName(_fromUtf8("txtAeroFile"))
        self.gridLayout_2.addWidget(self.txtAeroFile, 6, 2, 1, 1)
        self.pbtnDynamicFile = QtGui.QPushButton(self.groupBox_2)
        self.pbtnDynamicFile.setObjectName(_fromUtf8("pbtnDynamicFile"))
        self.gridLayout_2.addWidget(self.pbtnDynamicFile, 2, 3, 1, 1)
        self.txtStaticFile = QtGui.QLineEdit(self.groupBox_2)
        self.txtStaticFile.setObjectName(_fromUtf8("txtStaticFile"))
        self.gridLayout_2.addWidget(self.txtStaticFile, 1, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 7, 1, 1, 3)
        self.pbtnAeroFile = QtGui.QPushButton(self.groupBox_2)
        self.pbtnAeroFile.setObjectName(_fromUtf8("pbtnAeroFile"))
        self.gridLayout_2.addWidget(self.pbtnAeroFile, 6, 3, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 0, 1, 1, 3)
        self.txtDynamicFile = QtGui.QLineEdit(self.groupBox_2)
        self.txtDynamicFile.setObjectName(_fromUtf8("txtDynamicFile"))
        self.gridLayout_2.addWidget(self.txtDynamicFile, 2, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 5, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 6, 1, 1, 1)
        self.pbtnStaticFile = QtGui.QPushButton(self.groupBox_2)
        self.pbtnStaticFile.setObjectName(_fromUtf8("pbtnStaticFile"))
        self.gridLayout_2.addWidget(self.pbtnStaticFile, 1, 3, 1, 1)
        self.pbtnBodyFile = QtGui.QPushButton(self.groupBox_2)
        self.pbtnBodyFile.setObjectName(_fromUtf8("pbtnBodyFile"))
        self.gridLayout_2.addWidget(self.pbtnBodyFile, 5, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 1, 1, 1, 1)
        self.txtBodyFile = QtGui.QLineEdit(self.groupBox_2)
        self.txtBodyFile.setObjectName(_fromUtf8("txtBodyFile"))
        self.gridLayout_2.addWidget(self.txtBodyFile, 5, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 4, 1, 1, 3)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 3, 1, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.line_5 = QtGui.QFrame(self.groupBox_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_3.addWidget(self.line_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.spbFileHeaderNums = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbFileHeaderNums.sizePolicy().hasHeightForWidth())
        self.spbFileHeaderNums.setSizePolicy(sizePolicy)
        self.spbFileHeaderNums.setMaximum(10)
        self.spbFileHeaderNums.setProperty("value", 1)
        self.spbFileHeaderNums.setObjectName(_fromUtf8("spbFileHeaderNums"))
        self.horizontalLayout_10.addWidget(self.spbFileHeaderNums)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spbFileFooterNums = QtGui.QSpinBox(self.groupBox_4)
        self.spbFileFooterNums.setMaximum(10)
        self.spbFileFooterNums.setObjectName(_fromUtf8("spbFileFooterNums"))
        self.horizontalLayout_6.addWidget(self.spbFileFooterNums)
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.spbAngleStartCol = QtGui.QSpinBox(self.groupBox_7)
        self.spbAngleStartCol.setMinimum(1)
        self.spbAngleStartCol.setMaximum(10)
        self.spbAngleStartCol.setObjectName(_fromUtf8("spbAngleStartCol"))
        self.horizontalLayout_9.addWidget(self.spbAngleStartCol)
        self.horizontalLayout_5.addWidget(self.groupBox_7)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.spbAngleEndCol = QtGui.QSpinBox(self.groupBox_6)
        self.spbAngleEndCol.setMinimum(1)
        self.spbAngleEndCol.setMaximum(10)
        self.spbAngleEndCol.setObjectName(_fromUtf8("spbAngleEndCol"))
        self.horizontalLayout_8.addWidget(self.spbAngleEndCol)
        self.horizontalLayout_5.addWidget(self.groupBox_6)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.spbForceStartCol = QtGui.QSpinBox(self.groupBox_8)
        self.spbForceStartCol.setMinimum(1)
        self.spbForceStartCol.setMaximum(50)
        self.spbForceStartCol.setObjectName(_fromUtf8("spbForceStartCol"))
        self.horizontalLayout_7.addWidget(self.spbForceStartCol)
        self.horizontalLayout_5.addWidget(self.groupBox_8)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spbForceEndCol = QtGui.QSpinBox(self.groupBox_5)
        self.spbForceEndCol.setSuffix(_fromUtf8(""))
        self.spbForceEndCol.setPrefix(_fromUtf8(""))
        self.spbForceEndCol.setMinimum(1)
        self.spbForceEndCol.setMaximum(50)
        self.spbForceEndCol.setObjectName(_fromUtf8("spbForceEndCol"))
        self.horizontalLayout_3.addWidget(self.spbForceEndCol)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_11.addWidget(self.label_18)
        self.txtColumnOffset = QtGui.QLineEdit(self.groupBox_2)
        self.txtColumnOffset.setObjectName(_fromUtf8("txtColumnOffset"))
        self.horizontalLayout_11.addWidget(self.txtColumnOffset)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.line_4 = QtGui.QFrame(self.groupBox_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pbtnGenerateFile = QtGui.QPushButton(self.groupBox_2)
        self.pbtnGenerateFile.setObjectName(_fromUtf8("pbtnGenerateFile"))
        self.horizontalLayout_4.addWidget(self.pbtnGenerateFile)
        self.pbtnHelp = QtGui.QPushButton(self.groupBox_2)
        self.pbtnHelp.setObjectName(_fromUtf8("pbtnHelp"))
        self.horizontalLayout_4.addWidget(self.pbtnHelp)
        self.pbtnExit = QtGui.QPushButton(self.groupBox_2)
        self.pbtnExit.setObjectName(_fromUtf8("pbtnExit"))
        self.horizontalLayout_4.addWidget(self.pbtnExit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dataTransWidget)
        QtCore.QObject.connect(self.pbtnExit, QtCore.SIGNAL(_fromUtf8("clicked()")), dataTransWidget.close)
        QtCore.QMetaObject.connectSlotsByName(dataTransWidget)
        dataTransWidget.setTabOrder(self.cbBalanceSty, self.txtModelArea)
        dataTransWidget.setTabOrder(self.txtModelArea, self.txtModelSpan)
        dataTransWidget.setTabOrder(self.txtModelSpan, self.txtModelRootChord)
        dataTransWidget.setTabOrder(self.txtModelRootChord, self.txtModelRefChord)
        dataTransWidget.setTabOrder(self.txtModelRefChord, self.txtWindSpeed)
        dataTransWidget.setTabOrder(self.txtWindSpeed, self.txtDeltaX)
        dataTransWidget.setTabOrder(self.txtDeltaX, self.txtDeltaY)
        dataTransWidget.setTabOrder(self.txtDeltaY, self.txtDeltaZ)
        dataTransWidget.setTabOrder(self.txtDeltaZ, self.pbtnModelDataInput)
        dataTransWidget.setTabOrder(self.pbtnModelDataInput, self.pbtnModelDataExport)
        dataTransWidget.setTabOrder(self.pbtnModelDataExport, self.txtStaticFile)
        dataTransWidget.setTabOrder(self.txtStaticFile, self.pbtnStaticFile)
        dataTransWidget.setTabOrder(self.pbtnStaticFile, self.txtDynamicFile)
        dataTransWidget.setTabOrder(self.txtDynamicFile, self.pbtnDynamicFile)
        dataTransWidget.setTabOrder(self.pbtnDynamicFile, self.txtBodyFile)
        dataTransWidget.setTabOrder(self.txtBodyFile, self.pbtnBodyFile)
        dataTransWidget.setTabOrder(self.pbtnBodyFile, self.txtAeroFile)
        dataTransWidget.setTabOrder(self.txtAeroFile, self.pbtnAeroFile)
        dataTransWidget.setTabOrder(self.pbtnAeroFile, self.spbFileHeaderNums)
        dataTransWidget.setTabOrder(self.spbFileHeaderNums, self.spbFileFooterNums)
        dataTransWidget.setTabOrder(self.spbFileFooterNums, self.spbAngleStartCol)
        dataTransWidget.setTabOrder(self.spbAngleStartCol, self.spbAngleEndCol)
        dataTransWidget.setTabOrder(self.spbAngleEndCol, self.spbForceStartCol)
        dataTransWidget.setTabOrder(self.spbForceStartCol, self.spbForceEndCol)
        dataTransWidget.setTabOrder(self.spbForceEndCol, self.txtColumnOffset)
        dataTransWidget.setTabOrder(self.txtColumnOffset, self.pbtnGenerateFile)
        dataTransWidget.setTabOrder(self.pbtnGenerateFile, self.pbtnHelp)
        dataTransWidget.setTabOrder(self.pbtnHelp, self.pbtnExit)

    def retranslateUi(self, dataTransWidget):
        dataTransWidget.setWindowTitle(_translate("dataTransWidget", "天平数据转换", None))
        self.label_5.setText(_translate("dataTransWidget", "实验数据转换", None))
        self.label_11.setText(_translate("dataTransWidget", "天平类型", None))
        self.cbBalanceSty.setToolTip(_translate("dataTransWidget", "选择天平类型", None))
        self.groupBox.setTitle(_translate("dataTransWidget", "模型参数", None))
        self.label_2.setText(_translate("dataTransWidget", "展长（m）", None))
        self.label.setText(_translate("dataTransWidget", "参考面积（㎡）", None))
        self.txtModelArea.setText(_translate("dataTransWidget", "0.", None))
        self.label_6.setText(_translate("dataTransWidget", "模型重心距天平位置：", None))
        self.txtDeltaY.setText(_translate("dataTransWidget", "0.", None))
        self.txtDeltaX.setText(_translate("dataTransWidget", "0.", None))
        self.txtDeltaZ.setText(_translate("dataTransWidget", "0.", None))
        self.label_7.setText(_translate("dataTransWidget", "ΔX（m）", None))
        self.label_8.setText(_translate("dataTransWidget", "ΔY（m）", None))
        self.label_9.setText(_translate("dataTransWidget", "ΔZ（m）", None))
        self.txtModelSpan.setText(_translate("dataTransWidget", "0.", None))
        self.label_4.setText(_translate("dataTransWidget", "实验风速（m/s）", None))
        self.txtWindSpeed.setText(_translate("dataTransWidget", "0.", None))
        self.label_3.setText(_translate("dataTransWidget", "平均气动弦长（m）", None))
        self.txtModelRefChord.setText(_translate("dataTransWidget", "0.", None))
        self.label_10.setText(_translate("dataTransWidget", "根弦长（m）", None))
        self.txtModelRootChord.setText(_translate("dataTransWidget", "0.", None))
        self.pbtnModelDataExport.setText(_translate("dataTransWidget", "模型参数导出...", None))
        self.pbtnModelDataInput.setText(_translate("dataTransWidget", "载入模型参数", None))
        self.groupBox_2.setTitle(_translate("dataTransWidget", "数据文件", None))
        self.pbtnDynamicFile.setText(_translate("dataTransWidget", "...", None))
        self.pbtnAeroFile.setText(_translate("dataTransWidget", "...", None))
        self.label_16.setText(_translate("dataTransWidget", "请选择原始数据文件目录：", None))
        self.label_13.setText(_translate("dataTransWidget", "体轴文件", None))
        self.label_15.setText(_translate("dataTransWidget", "风轴文件", None))
        self.pbtnStaticFile.setText(_translate("dataTransWidget", "...", None))
        self.pbtnBodyFile.setText(_translate("dataTransWidget", "...", None))
        self.label_14.setText(_translate("dataTransWidget", "动态文件", None))
        self.label_12.setText(_translate("dataTransWidget", "静态文件", None))
        self.label_17.setText(_translate("dataTransWidget", "选择生成数据文件目录：", None))
        self.groupBox_3.setTitle(_translate("dataTransWidget", "Headers行数", None))
        self.groupBox_4.setTitle(_translate("dataTransWidget", "Footer行数", None))
        self.groupBox_7.setTitle(_translate("dataTransWidget", "角度起始列", None))
        self.groupBox_6.setTitle(_translate("dataTransWidget", "角度终止列", None))
        self.groupBox_8.setTitle(_translate("dataTransWidget", "力/力矩起始列", None))
        self.groupBox_5.setTitle(_translate("dataTransWidget", "力/力矩起始列", None))
        self.label_18.setText(_translate("dataTransWidget", "角度列偏移量", None))
        self.pbtnGenerateFile.setText(_translate("dataTransWidget", "生成数据文件...", None))
        self.pbtnHelp.setText(_translate("dataTransWidget", "帮助", None))
        self.pbtnExit.setText(_translate("dataTransWidget", "退出", None))

