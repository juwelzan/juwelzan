from PyQt6 import QtWidgets, uic
import sys

class Simpl_Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("simpel_calculetor_jr.ui", self) 
        
        self.zog.clicked.connect(self.zog_1)
        self.bog.clicked.connect(self.bog_1)
        self.gun.clicked.connect(self.gun_1)
        self.vag.clicked.connect(self.vag_1)
        
        self.Button_1.clicked.connect(self.add_1)
        self.Button_2.clicked.connect(self.add_2)
        self.Button_3.clicked.connect(self.add_3)
        self.Button_4.clicked.connect(self.add_4)
        self.Button_5.clicked.connect(self.add_5)
        self.Button_6.clicked.connect(self.add_6)
        self.Button_7.clicked.connect(self.add_7)
        self.Button_8.clicked.connect(self.add_8)
        self.Button_9.clicked.connect(self.add_9)
        self.Button_0.clicked.connect(self.add_0)
        
        self.Clear.clicked.connect(self.Clear_1)
        self.Del.clicked.connect(self.Del_1)
        self.dot.clicked.connect(self.dot_1)
        self.soman.clicked.connect(self.soman_1)
        
        
        self.show()
        
        
    def zog_1(self):
        text=self.label.text()
        self.label.setText(text+"+")
    
    
    def bog_1(self):
        text=self.label.text()
        self.label.setText(text+"-")
    
    
    def gun_1(self):
        text=self.label.text()
        self.label.setText(text+"*")
    
    
    
    def vag_1(self):
        text=self.label.text()
        self.label.setText(text+"/")
        
        
    def add_1(self):
        text=self.label.text()
        self.label.setText(text+"1")
        
    def add_2(self):
        text=self.label.text()
        self.label.setText(text+"2")    
        
    def add_3(self):
        text=self.label.text()
        self.label.setText(text+"3")    
        
    def add_4(self):
        text=self.label.text()
        self.label.setText(text+"4")    
        
    def add_5(self):
        text=self.label.text()
        self.label.setText(text+"5")    
        
    def add_6(self):
        text=self.label.text()
        self.label.setText(text+"6")    
        
        
    def add_7(self):
        text=self.label.text()
        self.label.setText(text+"7")        
        
        
    def add_8(self):
        text=self.label.text()
        self.label.setText(text+"8")    
        
        
    def add_9(self):
        text=self.label.text()
        self.label.setText(text+"9")    
        
        
    def add_0(self):
        text=self.label.text()
        self.label.setText(text+"0")    
        
    def Clear_1(self):
        
        self.label.setText("")    
        
    def Del_1(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])    
        
        
        
    def dot_1(self):
        text=self.label.text()
        self.label.setText(text+".") 
           
        
    def soman_1(self):
        text=self.label.text()
        try:
            ans=eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("not mess")
        
        
        
        
        
app = QtWidgets.QApplication(sys.argv)
window = Simpl_Calculator()
app.exec()
