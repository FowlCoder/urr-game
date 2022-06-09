import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PyQt6.QtGui import QPixmap

sprite_black = "player_black.png"
sprite_white = "player_white.png"
sprite_diag = "board_diag.png"
sprite_end = "board_end.png"
sprite_eyes = "board_eyes.png"
sprite_five = "board_five.png"
sprite_fives = "board_fives.png"
sprite_flower = "board_flower.png"
sprite_start = "board_start.png"
sprite_twelve = "board_twelve.png"


def roll_dice():
    result = 1
    for die in range(2):
        binary_roll = random.choice([0, 1])
        result += binary_roll
    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URR")
        main_layout = QVBoxLayout()

        self.roll_result = roll_dice()
        self.player_text = QLabel("You rolled a " + str(self.roll_result) + "!")
        main_layout.addWidget(self.player_text)
        self.cpu_text = QLabel()
        main_layout.addWidget(self.cpu_text)
        self.cpu_scoreboard = QLabel("CPU Remaining Pieces: 5")
        main_layout.addWidget(self.cpu_scoreboard)
        self.player_scoreboard = QLabel("Player Remaining Pieces: 5")
        main_layout.addWidget(self.player_scoreboard)
        self.button_new = QPushButton("New Piece")
        self.button_new.clicked.connect(self.piece_new)
        main_layout.addWidget(self.button_new)

        self.button_move1 = QPushButton("Move")
        self.button_move1.clicked.connect(lambda: self.piece_move(1))
        self.button_move2 = QPushButton("Move")
        self.button_move2.clicked.connect(lambda: self.piece_move(2))
        self.button_move3 = QPushButton("Move")
        self.button_move3.clicked.connect(lambda: self.piece_move(3))
        self.button_move4 = QPushButton("Move")
        self.button_move4.clicked.connect(lambda: self.piece_move(4))
        self.button_move5 = QPushButton("Move")
        self.button_move5.clicked.connect(lambda: self.piece_move(5))

        self.tile_black1 = QLabel()
        self.tile_black2 = QLabel()
        self.tile_black3 = QLabel()
        self.tile_black4 = QLabel()
        self.tile_black5 = QLabel()
        self.tile_white1 = QLabel()
        self.tile_white2 = QLabel()
        self.tile_white3 = QLabel()
        self.tile_white4 = QLabel()
        self.tile_white5 = QLabel()
        self.tile_diag = QLabel()
        self.tile_end = QLabel()
        self.tile_eyes = QLabel()
        self.tile_five = QLabel()
        self.tile_fives = QLabel()
        self.tile_flower = QLabel()
        self.tile_start = QLabel()
        self.tile_twelve = QLabel()
        pixmap_black = QPixmap(sprite_black)
        pixmap_white = QPixmap(sprite_white)
        pixmap_diag = QPixmap(sprite_diag)
        pixmap_end = QPixmap(sprite_end)
        pixmap_eyes = QPixmap(sprite_eyes)
        pixmap_five = QPixmap(sprite_five)
        pixmap_fives = QPixmap(sprite_fives)
        pixmap_flower = QPixmap(sprite_flower)
        pixmap_start = QPixmap(sprite_start)
        pixmap_twelve = QPixmap(sprite_twelve)
        self.tile_black1.setPixmap(pixmap_black)
        self.tile_black2.setPixmap(pixmap_black)
        self.tile_black3.setPixmap(pixmap_black)
        self.tile_black4.setPixmap(pixmap_black)
        self.tile_black5.setPixmap(pixmap_black)
        self.tile_white1.setPixmap(pixmap_white)
        self.tile_white2.setPixmap(pixmap_white)
        self.tile_white3.setPixmap(pixmap_white)
        self.tile_white4.setPixmap(pixmap_white)
        self.tile_white5.setPixmap(pixmap_white)
        self.tile_diag.setPixmap(pixmap_diag)
        self.tile_end.setPixmap(pixmap_end)
        self.tile_eyes.setPixmap(pixmap_eyes)
        self.tile_five.setPixmap(pixmap_five)
        self.tile_fives.setPixmap(pixmap_fives)
        self.tile_flower.setPixmap(pixmap_flower)
        self.tile_start.setPixmap(pixmap_start)
        self.tile_twelve.setPixmap(pixmap_twelve)

        self.board_layout = QGridLayout()
        self.board_layout.addWidget(self.tile_start, 0, 0)
        self.board_layout.addWidget(self.tile_eyes, 0, 1)
        self.board_layout.addWidget(self.tile_five, 0, 2)
        self.board_layout.addWidget(self.tile_flower, 0, 3)
        self.board_layout.addWidget(self.tile_diag, 0, 4)
        self.board_layout.addWidget(self.tile_fives, 0, 5)
        self.board_layout.addWidget(self.tile_twelve, 0, 6)
        self.board_layout.addWidget(self.tile_end, 0, 7)

        self.trash_layout = QHBoxLayout()

        main_layout.addLayout(self.board_layout)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.set_player = {1, 2, 3, 4, 5}
        self.set_cpu = {-1, -2, -3, -4, -5}
        self.line = [0, 0, 0, 0, 0, 0, 0, 0]
        self.score_player = 5
        self.score_cpu = 5
        self.end = False

    def piece_new(self):
        if self.end:
            self.set_player = {1, 2, 3, 4, 5}
            self.set_cpu = {-1, -2, -3, -4, -5}
            self.line = [0, 0, 0, 0, 0, 0, 0, 0]
            self.score_player = 5
            self.score_cpu = 5
            self.cpu_scoreboard.setText("CPU Remaining Pieces: 5")
            self.player_scoreboard.setText("Player Remaining Pieces: 5")
            self.button_new.setText("New Piece")
            self.tile_white1.hide()
            self.tile_white2.hide()
            self.tile_white3.hide()
            self.tile_white4.hide()
            self.tile_white5.hide()
            self.tile_black1.hide()
            self.tile_black2.hide()
            self.tile_black3.hide()
            self.tile_black4.hide()
            self.tile_black5.hide()
            self.button_move1.hide()
            self.button_move2.hide()
            self.button_move3.hide()
            self.button_move4.hide()
            self.button_move5.hide()
            self.end = False
        else:
            pos = self.roll_result
            if len(self.set_player) > 0 and self.line[pos - 1] <= 0:
                captured = self.line[pos - 1]
                if captured != 0:
                    self.set_cpu.add(captured)
                    self.which_cpu_piece(captured).hide()
                piece = self.set_player.pop()
                if self.which_player_piece(piece).isHidden():
                    self.which_player_piece(piece).show()
                    self.which_player_button(piece).show()
                self.line[pos - 1] = piece
                self.board_layout.addWidget(self.which_player_piece(piece), 0, pos - 1)
                self.board_layout.addWidget(self.which_player_button(piece), 1, pos - 1)
                self.cpu_turn()

    def cpu_turn(self):
        roll = roll_dice()
        self.cpu_text.setText("CPU rolled a " + str(roll) + "!")
        pos = len(self.line) - roll
        if len(self.set_cpu) > 0 and self.line[pos] >= 0:
            captured = self.line[pos]
            if captured != 0:
                self.set_player.add(captured)
                self.which_player_piece(captured).hide()
                self.which_player_button(captured).hide()
            piece = self.set_cpu.pop()
            if self.which_cpu_piece(piece).isHidden():
                self.which_cpu_piece(piece).show()
            self.line[pos] = piece
            self.board_layout.addWidget(self.which_cpu_piece(piece), 0, pos)
        else:
            choices = set()
            for piece in self.line:
                if piece < 0:
                    choices.add(piece)
            while len(choices) > 0:
                choice = choices.pop()
                og_pos = self.line.index(choice)
                pos = og_pos - roll
                if pos < 0:
                    self.line[og_pos] = 0
                    self.score_cpu -= 1
                    self.cpu_scoreboard.setText("CPU Remaining Pieces: " +
                                                str(self.score_cpu))
                    self.which_cpu_piece(choice).hide()
                    if self.score_cpu == 0:
                        self.cpu_scoreboard.setText("CPU WIN!!")
                        self.button_new.setText("REMATCH?")
                        self.end = True
                    break
                elif self.line[pos] >= 0:
                    captured = self.line[pos]
                    if captured != 0:
                        self.set_player.add(captured)
                        self.which_player_piece(captured).hide()
                        self.which_player_button(captured).hide()
                    self.line[og_pos] = 0
                    self.line[pos] = choice
                    self.board_layout.addWidget(self.which_cpu_piece(choice), 0, pos)
                    break

        self.roll_result = roll_dice()
        self.player_text.setText("You rolled a " + str(self.roll_result) + "!")

    def piece_move(self, which):
        og_pos = self.line.index(which)
        pos = og_pos + self.roll_result
        if pos >= len(self.line):
            self.line[og_pos] = 0
            self.score_player -= 1
            self.player_scoreboard.setText("Player Remaining Pieces: " +
                                           str(self.score_player))
            self.which_player_piece(which).hide()
            self.which_player_button(which).hide()
            if self.score_player == 0:
                self.player_scoreboard.setText("YOU WIN!!")
                self.button_new.setText("REMATCH?")
                self.end = True
            else:
                self.cpu_turn()
        elif self.line[pos] <= 0:
            captured = self.line[pos]
            if captured != 0:
                self.set_cpu.add(captured)
                self.which_cpu_piece(captured).hide()
            self.line[og_pos] = 0
            self.line[pos] = which
            self.board_layout.addWidget(self.which_player_piece(which), 0, pos)
            self.board_layout.addWidget(self.which_player_button(which), 1, pos)
            self.cpu_turn()

    def print_debug_info(self):
        print(self.line)
        print(self.set_player)
        print(self.set_cpu)
        print()

    def which_player_piece(self, which):
        if which == 1:
            return self.tile_black1
        elif which == 2:
            return self.tile_black2
        elif which == 3:
            return self.tile_black3
        elif which == 4:
            return self.tile_black4
        elif which == 5:
            return self.tile_black5

    def which_player_button(self, which):
        if which == 1:
            return self.button_move1
        elif which == 2:
            return self.button_move2
        elif which == 3:
            return self.button_move3
        elif which == 4:
            return self.button_move4
        elif which == 5:
            return self.button_move5

    def which_cpu_piece(self, which):
        if which == -1:
            return self.tile_white1
        elif which == -2:
            return self.tile_white2
        elif which == -3:
            return self.tile_white3
        elif which == -4:
            return self.tile_white4
        elif which == -5:
            return self.tile_white5


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
