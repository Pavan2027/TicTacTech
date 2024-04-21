import sys
from random import randint
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Import GUI file
from ui_main import Ui_MainWindow

# Import AI file
from ai_movement import ai_move

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Window Icon
        self.setWindowIcon(QIcon('icons/app_icon_2.png'))

        # Status bar message  
        self.statusBar().showMessage("A game made in PyQT by Pavan D Umesh")

        # Counter to keep track of who's turn it is
        self.counter = 0
        self.game_end = False

        self.chooser = randint(0, 1)
        self.ui.pva_label.setText('You have challenged the AI')

        # Keep track of chosen tiles
        self.o_tile = []
        self.x_tile = []

        # Track of victors
        self.x_win = False
        self.o_win = False

        # Changing pages
        self.ui.pva_change_btn.clicked.connect(lambda: self.pva_pressed())
        self.ui.pvp_change_btn.clicked.connect(lambda: self.changePage(self.ui.pvp_pg))
        self.ui.pva_to_home_btn.clicked.connect(lambda: self.changePage(self.ui.main_pg))
        self.ui.pvp_to_home_btn.clicked.connect(lambda: self.changePage(self.ui.main_pg))

        #Clicking buttons for PVP
        self.ui.pvpbtn1.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn1))
        self.ui.pvpbtn2.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn2))
        self.ui.pvpbtn3.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn3))
        self.ui.pvpbtn4.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn4))
        self.ui.pvpbtn5.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn5))
        self.ui.pvpbtn6.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn6))
        self.ui.pvpbtn7.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn7))
        self.ui.pvpbtn8.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn8))
        self.ui.pvpbtn9.clicked.connect(lambda: self.clickerPVP(self.ui.pvpbtn9))
        self.ui.pvp_restart_btn.clicked.connect(lambda: self.reset())

        #Clicking buttons for PVA
        self.ui.pvabtn1.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn1))
        self.ui.pvabtn2.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn2))
        self.ui.pvabtn3.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn3))
        self.ui.pvabtn4.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn4))
        self.ui.pvabtn5.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn5))
        self.ui.pvabtn6.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn6))
        self.ui.pvabtn7.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn7))
        self.ui.pvabtn8.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn8))
        self.ui.pvabtn9.clicked.connect(lambda: self.clickerPVA(self.ui.pvabtn9))
        self.ui.pva_restart_btn.clicked.connect(lambda: self.resetPVA())

        self.show()

    # Function to clear and change pages
    def changePage(self, cur_page):
        self.ui.stackedWidget.setCurrentWidget(cur_page)
        self.reset()

    # Reset the page
    def reset(self):
        btn_list = [
            self.ui.pvpbtn1,
            self.ui.pvpbtn2,
            self.ui.pvpbtn3,
            self.ui.pvpbtn4,
            self.ui.pvpbtn5,
            self.ui.pvpbtn6,
            self.ui.pvpbtn7,
            self.ui.pvpbtn8,
            self.ui.pvpbtn9,
            self.ui.pvabtn1,
            self.ui.pvabtn2,
            self.ui.pvabtn3,
            self.ui.pvabtn4,
            self.ui.pvabtn5,
            self.ui.pvabtn6,
            self.ui.pvabtn7,
            self.ui.pvabtn8,
            self.ui.pvabtn9,
        ]

        for btn in btn_list:
            btn.setText("")
            btn.setEnabled(True)
        self.ui.pvp_label.setText("X goes first!")
        self.counter = 0
        self.x_tile = []
        self.o_tile = []
        self.x_win = False
        self.o_win = False
        self.game_end = False

    # On clicking button
    def clickerPVP(self, btn:QPushButton):
        if self.counter % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            self.ui.pvp_label.setText("O's turn")
            self.counter += 1
            if btn == self.ui.pvpbtn1:
                self.x_tile.append(1)
            elif btn == self.ui.pvpbtn2:
                self.x_tile.append(2)
            elif btn == self.ui.pvpbtn3:
                self.x_tile.append(3)
            elif btn == self.ui.pvpbtn4:
                self.x_tile.append(4)
            elif btn == self.ui.pvpbtn5:
                self.x_tile.append(5)
            elif btn == self.ui.pvpbtn6:
                self.x_tile.append(6)
            elif btn == self.ui.pvpbtn7:
                self.x_tile.append(7)
            elif btn == self.ui.pvpbtn8:
                self.x_tile.append(8)
            elif btn == self.ui.pvpbtn9:
                self.x_tile.append(9)
        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.ui.pvp_label.setText("X's turn")
            self.counter += 1
            if btn == self.ui.pvpbtn1:
                self.o_tile.append(1)
            elif btn == self.ui.pvpbtn2:
                self.o_tile.append(2)
            elif btn == self.ui.pvpbtn3:
                self.o_tile.append(3)
            elif btn == self.ui.pvpbtn4:
                self.o_tile.append(4)
            elif btn == self.ui.pvpbtn5:
                self.o_tile.append(5)
            elif btn == self.ui.pvpbtn6:
                self.o_tile.append(6)
            elif btn == self.ui.pvpbtn7:
                self.o_tile.append(7)
            elif btn == self.ui.pvpbtn8:
                self.o_tile.append(8)
            elif btn == self.ui.pvpbtn9:
                self.o_tile.append(9)
        self.gameOverCheck()
    
    def resetPVA(self):
        btn_list = [
            self.ui.pvabtn1,
            self.ui.pvabtn2,
            self.ui.pvabtn3,
            self.ui.pvabtn4,
            self.ui.pvabtn5,
            self.ui.pvabtn6,
            self.ui.pvabtn7,
            self.ui.pvabtn8,
            self.ui.pvabtn9,
        ]

        for btn in btn_list:
            btn.setText("")
            btn.setEnabled(True)
        self.counter = 0
        self.x_tile = []
        self.o_tile = []
        self.x_win = False
        self.o_win = False
        self.game_end = False
        self.ui.pva_label.setText("So you have challenged the AI again")
        self.chooser = randint(0, 1)
        self.pva_pressed()

    def pva_pressed(self):
        self.changePage(self.ui.pva_pg)
        if self.chooser == 0:
            temp = (1, 3, 7, 9)[randint(0, 3)]
            if temp == 1:
                self.ui.pvabtn1.setText("X")
                self.ui.pvabtn1.setEnabled(False)
            elif temp == 3:
                self.ui.pvabtn3.setText("X")
                self.ui.pvabtn3.setEnabled(False)
            elif temp == 7:
                self.ui.pvabtn7.setText("X")
                self.ui.pvabtn7.setEnabled(False)
            elif temp == 9:
                self.ui.pvabtn9.setText("X")
                self.ui.pvabtn9.setEnabled(False)
            self.x_tile.append(temp)
            self.counter += self.chooser + 1

    def clickerPVA(self, btn:QPushButton):
        if self.counter % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            if btn == self.ui.pvabtn1:
                self.x_tile.append(1)
            elif btn == self.ui.pvabtn2:
                self.x_tile.append(2)
            elif btn == self.ui.pvabtn3:
                self.x_tile.append(3)
            elif btn == self.ui.pvabtn4:
                self.x_tile.append(4)
            elif btn == self.ui.pvabtn5:
                self.x_tile.append(5)
            elif btn == self.ui.pvabtn6:
                self.x_tile.append(6)
            elif btn == self.ui.pvabtn7:
                self.x_tile.append(7)
            elif btn == self.ui.pvabtn8:
                self.x_tile.append(8)
            elif btn == self.ui.pvabtn9:
                self.x_tile.append(9)

            self.gameOverCheck()
            if not self.game_end:
                self.o_tile.append(ai_move(self.o_tile, self.x_tile))
                if self.o_tile[-1] == 1:
                    self.ui.pvabtn1.setText("O")
                    self.ui.pvabtn1.setEnabled(False)
                elif self.o_tile[-1] == 2:
                    self.ui.pvabtn2.setText("O")
                    self.ui.pvabtn2.setEnabled(False)
                elif self.o_tile[-1] == 3:
                    self.ui.pvabtn3.setText("O")
                    self.ui.pvabtn3.setEnabled(False)
                elif self.o_tile[-1] == 4:
                    self.ui.pvabtn4.setText("O")
                    self.ui.pvabtn4.setEnabled(False)
                elif self.o_tile[-1] == 5:
                    self.ui.pvabtn5.setText("O")
                    self.ui.pvabtn5.setEnabled(False)
                elif self.o_tile[-1] == 6:
                    self.ui.pvabtn6.setText("O")
                    self.ui.pvabtn6.setEnabled(False)
                elif self.o_tile[-1] == 7:
                    self.ui.pvabtn7.setText("O")
                    self.ui.pvabtn7.setEnabled(False)
                elif self.o_tile[-1] == 8:
                    self.ui.pvabtn8.setText("O")
                    self.ui.pvabtn8.setEnabled(False)
                elif self.o_tile[-1] == 9:
                    self.ui.pvabtn9.setText("O")
                    self.ui.pvabtn9.setEnabled(False)
        else:
            btn.setText("O")
            btn.setEnabled(False)
            if btn == self.ui.pvabtn1:
                self.o_tile.append(1)
            elif btn == self.ui.pvabtn2:
                self.o_tile.append(2)
            elif btn == self.ui.pvabtn3:
                self.o_tile.append(3)
            elif btn == self.ui.pvabtn4:
                self.o_tile.append(4)
            elif btn == self.ui.pvabtn5:
                self.o_tile.append(5)
            elif btn == self.ui.pvabtn6:
                self.o_tile.append(6)
            elif btn == self.ui.pvabtn7:
                self.o_tile.append(7)
            elif btn == self.ui.pvabtn8:
                self.o_tile.append(8)
            elif btn == self.ui.pvabtn9:
                self.o_tile.append(9)
        
            self.gameOverCheck()
            if not self.game_end:
                self.x_tile.append(ai_move(self.x_tile, self.o_tile))
                if self.x_tile[-1] == 1:
                    self.ui.pvabtn1.setText("X")
                    self.ui.pvabtn1.setEnabled(False)
                elif self.x_tile[-1] == 2:
                    self.ui.pvabtn2.setText("X")
                    self.ui.pvabtn2.setEnabled(False)
                elif self.x_tile[-1] == 3:
                    self.ui.pvabtn3.setText("X")
                    self.ui.pvabtn3.setEnabled(False)
                elif self.x_tile[-1] == 4:
                    self.ui.pvabtn4.setText("X")
                    self.ui.pvabtn4.setEnabled(False)
                elif self.x_tile[-1] == 5:
                    self.ui.pvabtn5.setText("X")
                    self.ui.pvabtn5.setEnabled(False)
                elif self.x_tile[-1] == 6:
                    self.ui.pvabtn6.setText("X")
                    self.ui.pvabtn6.setEnabled(False)
                elif self.x_tile[-1] == 7:
                    self.ui.pvabtn7.setText("X")
                    self.ui.pvabtn7.setEnabled(False)
                elif self.x_tile[-1] == 8:
                    self.ui.pvabtn8.setText("X")
                    self.ui.pvabtn8.setEnabled(False)
                elif self.x_tile[-1] == 9:
                    self.ui.pvabtn9.setText("X")
                    self.ui.pvabtn9.setEnabled(False)
        self.gameOverCheck()
        

    def gameOverCheck(self):
        # Check if horizontal lines match
        if 1 in self.x_tile:
            if 2 in self.x_tile and 3 in self.x_tile:
                self.x_win = True
        if 4 in self.x_tile:
            if 5 in self.x_tile and 6 in self.x_tile:
                self.x_win = True
        if 7 in self.x_tile:
            if 8 in self.x_tile and 9 in self.x_tile:
                self.x_win = True
        if 1 in self.o_tile:
            if 2 in self.o_tile and 3 in self.o_tile:
                self.o_win = True
        if 4 in self.o_tile:
            if 5 in self.o_tile and 6 in self.o_tile:
                self.o_win = True
        if 7 in self.o_tile:
            if 8 in self.o_tile and 9 in self.o_tile:
                self.o_win = True
        
        # Check vertical lines
        for i in range(3 if len(self.x_tile) >= 3 else len(self.x_tile)):
            if self.x_tile[i] in (1, 2, 3):
                if self.x_tile[i] + 3 in self.x_tile and self.x_tile[i] + 6 in self.x_tile:
                    self.x_win = True
        for i in range(3 if len(self.o_tile) >= 3 else len(self.o_tile)):
            if self.o_tile[i] in (1, 2, 3):
                if self.o_tile[i] + 3 in self.o_tile and self.o_tile[i] + 6 in self.o_tile:
                    self.o_win = True

        # Check diagonals
        if 1 in self.x_tile:
            if 5 in self.x_tile and 9 in self.x_tile:
                self.x_win = True
        elif 3 in self.x_tile:
            if 5 in self.x_tile and 7 in self.x_tile:
                self.x_win = True
        if 1 in self.o_tile:
            if 5 in self.o_tile and 9 in self.o_tile:
                self.o_win = True
        elif 3 in self.o_tile:
            if 5 in self.o_tile and 7 in self.o_tile:
                self.o_win = True

        if self.x_win:
            self.ui.pvp_label.setText("Game Over! X Wins!")
            self.ui.pva_label.setText("Game Over! X Wins!")
            self.game_end = True
            self.gameOver()
        elif self.o_win:
            self.ui.pvp_label.setText("Game Over! O Wins!")
            self.ui.pva_label.setText("Game Over! O Wins!")
            self.game_end = True
            self.gameOver()
        elif (len(self.x_tile) + len(self.o_tile) == 9) and not self.x_win and not self.o_win:
            self.ui.pvp_label.setText("Game Over! Game Drawn!")
            self.ui.pva_label.setText("Game Over! Game Drawn!")
            self.game_end = True
            self.gameOver()

    def gameOver(self):
        btn_list = [
            self.ui.pvpbtn1,
            self.ui.pvpbtn2,
            self.ui.pvpbtn3,
            self.ui.pvpbtn4,
            self.ui.pvpbtn5,
            self.ui.pvpbtn6,
            self.ui.pvpbtn7,
            self.ui.pvpbtn8,
            self.ui.pvpbtn9,
            self.ui.pvabtn1,
            self.ui.pvabtn2,
            self.ui.pvabtn3,
            self.ui.pvabtn4,
            self.ui.pvabtn5,
            self.ui.pvabtn6,
            self.ui.pvabtn7,
            self.ui.pvabtn8,
            self.ui.pvabtn9,
        ]

        for btn in btn_list:
            btn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())