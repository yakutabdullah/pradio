
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QLabel, QTextEdit, QWidget, QPixmap, QBoxLayout, \
    QHBoxLayout, QLCDNumber, QProgressBar, QDial, QIcon, SIGNAL, QObject
from PyQt4.QtGui import QDialog, QPushButton, QGridLayout, QApplication, QTextBlock, QTextFormat
from _functools import partial
import gst
import os


player = gst.element_factory_make("playbin", "player")

music_station = {'Kiss FM':'http://kissfm.live24.gr/kiss2111',
                 'Real FM':'http://kissfm.live24.gr/kiss2111',
                 'Venus FM':'http://kissfm.live24.gr/kiss2111',
                 'Kiss FM':'http://kissfm.live24.gr/kiss2111',
                 'Nova FM':'http://kissfm.live24.gr/kiss2111',
                 'Son FM':'http://kissfm.live24.gr/kiss2111'}

class Pradio(QDialog):   

    
    def __init__(self, parent=None):      
        
        super(Pradio, self).__init__(parent)
      
# logo...................................
        self.label = QLabel()
        self.pixmap = QPixmap('/usr/share/pradyo/plogo.png')
        self.label.setPixmap(self.pixmap)     
        
        #/usr/share/pradyo/pradyo.py  
        

# progress barr.....................................

        self.bar =QProgressBar()
        self.bar.setMinimum(0)
        self.bar.setMaximum(100)
        self.bar.setValue(40)        

#label...........................................
        self.lcd = QLCDNumber(3)
        self.lcd.display('5')
        self.lcd.resize(50,50)
               
# button..............................................
        self.Btn1=QPushButton('Kiss FM')       
        self.Btn2=QPushButton('Real FM')
        self.Btn3=QPushButton('Venus FM')
        self.Btn4=QPushButton('Kiss FM')
        self.Btn5=QPushButton('Nova FM')
        self.Btn6=QPushButton('Son FM')
        self.connect(self.Btn1, SIGNAL('clicked()'),partial(self.play,self.Btn1.text()))
        self.connect(self.Btn2, SIGNAL('clicked()'),partial(self.play,self.Btn2.text()))
        self.connect(self.Btn3, SIGNAL('clicked()'),partial(self.play,self.Btn3.text()))
        self.connect(self.Btn4, SIGNAL('clicked()'),partial(self.play,self.Btn4.text()))
        self.connect(self.Btn5, SIGNAL('clicked()'),partial(self.play,self.Btn5.text()))
        self.connect(self.Btn6, SIGNAL('clicked()'),partial(self.play,self.Btn6.text()))
       

# ses buttonu........................................
       
        self.dial = QDial()
        self.dial.setValue(30)
        self.connect(self.dial, SIGNAL("valueChanged(int)"),self.VolumeChange)
        self.dial.setNotchesVisible(True)
         
         
# oynatma tuslarii......................................
     
        self.PlayBtn = QtGui.QPushButton('', self)
        self.PlayBtn.setIcon(QtGui.QIcon('/usr/share/pradyo/a.png'))
        self.PlayBtn.setIconSize(QtCore.QSize(48,48))

      #  self.PlayBtn.clicked.connect(self.play)
        self.PlayBtn.setFlat(True)
         
        self.StopBtn = QtGui.QPushButton('', self)
        self.StopBtn.setIcon(QtGui.QIcon('/usr/share/pradyo/s.png'))
        self.StopBtn.setIconSize(QtCore.QSize(48,48))
        self.StopBtn.setFlat(True)
        self.StopBtn.clicked.connect(self.stop_radio)

# layout............................      
        grid = QGridLayout()        
        grid.addWidget(self.PlayBtn,0,1)
        grid.addWidget(self.StopBtn,0,2)
        grid.addWidget(self.Btn1,1, 0, 3, 1)
        grid.addWidget(self.Btn2,1, 0, 7, 1)
        grid.addWidget(self.Btn3,1, 0, 11, 1)
        grid.addWidget(self.Btn4,1, 1, 3, 1)
        grid.addWidget(self.Btn5,1, 1, 7, 1)
        grid.addWidget(self.Btn6,1, 1, 11, 1)       
        grid.addWidget(self.dial, 0, 4, 2, 1)       
        grid.addWidget(self.label,0,0,1,1)       
        self.setLayout(grid)        
        self.setWindowTitle('Pradyo')
        self.setFixedSize(650, 300)
        
    def VolumeChange(self):

        VolumeChange=self.dial.value()
        print(VolumeChange)
        player.set_property('volume', VolumeChange/100.0)
        
        
        
        
    def play(self,value):
        deg =str(value)
        player.set_state(gst.STATE_NULL)
      #  print(value)   
      #  music_stream_uri=music_station[value]
       # print(music_stream_uri)
        music =music_station[deg]
        print(str(music))
        player.set_property('uri',music)
        
        player.set_state(gst.STATE_PLAYING)
       
        self.PlayBtn.setIcon(QtGui.QIcon('/usr/share/pradyo/a.png'))
        self.PlayBtn.setIconSize(QtCore.QSize(48,48))
        
        
        
    def stop_radio(self):

        print ("Radio stops")
        player.set_state(gst.STATE_NULL)
        
        self.PlayBtn.setIcon(QtGui.QIcon('/usr/share/pradyo/d.png'))
        self.PlayBtn.setIconSize(QtCore.QSize(48,48)) 
        
        def Close(self):
            self.close()      
   
        
uygulama = QApplication([])


pencer = Pradio()

pencer.show()  


uygulama.exec_()
