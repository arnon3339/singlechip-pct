import numpy as np
import PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget,
  QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog,
  QDesktopWidget)
from PyQt5.QtCore import QRect
from PIL.ImageQt import ImageQt
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pydicom

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.desk = QDesktopWidget()
        self.screen_geo = self.desk.screenGeometry(0)
        self.init_UI()
    
    def init_UI(self):
        vbox = QVBoxLayout()
        
        self.file_label = QLabel("Filename: ")
        self.file_btn = QPushButton("Choose file")
        self.track_btn = QPushButton("Reconstruct tracks")
        self.paht_btn = QPushButton("Estimate paths")
        self.img_btn = QPushButton("Reconstruct image")
        
        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.subplots()
        ds = pydicom.dcmread("/home/g0/Projects/pct/image/imgs/cp600.dcm")
        image = self.ax.imshow(ds.pixel_array, cmap=plt.cm.bone) 
        # self.ax.set_axis_off()
        
        vbox.addWidget(self.file_label)
        vbox.addWidget(self.file_btn)
        vbox.addWidget(self.track_btn)
        vbox.addWidget(self.paht_btn)
        vbox.addWidget(self.img_btn)
        vbox.addWidget(self.canvas)
        
        self.file_btn.clicked.connect(self.set_filename)
        
        self.setLayout(vbox)
        
    def set_filename(self):
        fdialog = QFileDialog()
        print(self.screen_geo.width())
        fdialog.setGeometry(QRect(self.screen_geo.width()/4,
                                  self.screen_geo.height() /4,
                                  self.screen_geo.width()/2,
                                  self.screen_geo.height()/2))
        fname = fdialog.getOpenFileName(self, 'Open file', 
         './',"ROOT files (*.root)")
        if fname[0]:
            self.file_label.setText(fname[0])
        