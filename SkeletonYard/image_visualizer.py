from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


import time
import numpy as np
from vispy import app
import vispy

from PyQt5.QtWidgets import *
import vispy.app
import sys

from vispy.app import use_app
use_app('PyQt5')
from vispy import scene
from vispy import color
from vispy.color.colormap import Colormap

import h5py

import numpy as np
from scipy.special import logsumexp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import io
import time
import scipy.signal
import scipy


import numpy as np
from scipy.special import logsumexp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import io
import time
import scipy.signal
import scipy
import torch

from scipy import signal



import imageio
from vispy import visuals

from skimage.transform import rescale, resize, downscale_local_mean

class Canvas(scene.SceneCanvas):

    def __init__(self):
        scene.SceneCanvas.__init__(self,keys='interactive', size=(1024, 1024))

        self.unfreeze()
        self.load_image()
        self.scaler=0.000001

        self.view=self.central_widget.add_view()
        self.image=scene.visuals.Image(self.image,parent=self.view.scene, cmap='bwr',clim=[0,255])
        print('success')

    def load_image(self):
        self.image=np.load('microscop_image.npy')
        self.image=np.load('microscop_org.npy')
        print(self.image)



class MainWindow(QMainWindow):
    def __init__(self, canvas=None,parent=None):
        super(MainWindow, self).__init__(parent)
        self.canvas=canvas
        widget = QWidget()
        self.setCentralWidget(widget)
        self.l0 = QGridLayout()
        self.l0.addWidget(canvas.native)
        widget.setLayout(self.l0)

        self.writer = imageio.get_writer('cg.gif')



canvas = Canvas()
vispy.use('PyQt5')
w = MainWindow(canvas)
w.show()
vispy.app.run()
