from random import randint

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import BooleanProperty, Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class TicTacToeGrid(GridLayout):
    GridLayout.cols = 3
    is_x_turn = BooleanProperty(True)
    count = 0
    finished_ind = BooleanProperty(False)
    single_player_ind = BooleanProperty(False)
    button_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(3):
            for j in range(3):
                size = dp(100)
                b = Button(text="", font_size="80dp", size=(size, size), on_press=self.on_button_click,
                           disabled_color=[0, 1, 0, 1])
                self.add_widget(b)
                self.button_list[i][j] = b
        self.add_widget(Label(size_hint=(1, None)))
        new_1_player_game_button = Button(text="Start New 1-Player Game", on_press=self.new_1_player_game,
                                          size_hint=(1, None))
        self.add_widget(new_1_player_game_button)
        new_2_player_game_button = Button(text="Start New 2-Player Game", on_press=self.new_2_player_game,
                                          size_hint=(1, None))
        self.add_widget(new_2_player_game_button)
        self.disable_all_buttons()

    def on_button_click(self, widget):
        self.human_move(widget)
        if self.single_player_ind and not self.finished_ind:
            Clock.schedule_once(self.computer_make_move, 0.4)

    def human_move(self, widget):
        if self.is_x_turn:
            widget.disabled_color = [1, 0, 0, 1]
            widget.text = 'X'
            self.is_x_turn = False
        else:
            widget.disabled_color = [0, 1, 0, 1]
            widget.text = 'O'
            self.is_x_turn = True
        widget.disabled = True
        self.count += 1
        self.win_check()

    def computer_make_move(self, dt):
        test_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in range(len(self.button_list)):
            for b in range(len(self.button_list[row])):
                test_list[row][b] = self.button_list[row][b].text
        square = self.choice_algorithm(test_list)
        self.button_list[square[0]][square[1]].text = 'O'
        self.is_x_turn = True

        self.button_list[square[0]][square[1]].disabled = True
        self.count += 1
        self.win_check()

    def choice_algorithm(self, test_list):
        choice_list = []
        for row in range(len(test_list)):
            for b in range(len(test_list[row])):
                if test_list[row][b] == '':
                    choice_list.append([row, b])
        return choice_list[randint(0, len(choice_list) - 1)]

    def new_1_player_game(self, widget):
        self.single_player_ind = True
        self.new_game()

    def new_2_player_game(self, widget):
        self.single_player_ind = False
        self.new_game()

    def new_game(self):
        self.count = 0
        self.finished_ind = False
        self.is_x_turn = True
        for row in self.button_list:
            for b in row:
                b.disabled = False
                b.text = ""

    def disable_all_buttons(self):
        for row in self.button_list:
            for b in row:
                b.disabled = True

    # Check to see if someone won
    def win_check(self):
        test_list = []
        for row in self.button_list:
            for b in row:
                test_list.append(b.text)
        if (test_list[0] == test_list[1] == test_list[2] == 'X'  # row1
                or test_list[3] == test_list[4] == test_list[5] == 'X'  # row2
                or test_list[6] == test_list[7] == test_list[8] == 'X'  # row3
                or test_list[0] == test_list[3] == test_list[6] == 'X'  # col1
                or test_list[1] == test_list[4] == test_list[7] == 'X'  # col2
                or test_list[2] == test_list[5] == test_list[8] == 'X'  # col3
                or test_list[0] == test_list[4] == test_list[8] == 'X'  # diagonal1
                or test_list[2] == test_list[4] == test_list[6] == 'X'):  # diagonal2
            self.finished_ind = True
            self.disable_all_buttons()
            popup = Popup(title="Tic Tac Toe", content=Label(text="Congratulations X, you have won!"),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
        elif (test_list[0] == test_list[1] == test_list[2] == 'O'  # row1
              or test_list[3] == test_list[4] == test_list[5] == 'O'  # row2
              or test_list[6] == test_list[7] == test_list[8] == 'O'  # row3
              or test_list[0] == test_list[3] == test_list[6] == 'O'  # col1
              or test_list[1] == test_list[4] == test_list[7] == 'O'  # col2
              or test_list[2] == test_list[5] == test_list[8] == 'O'  # col3
              or test_list[0] == test_list[4] == test_list[8] == 'O'  # diagonal1
              or test_list[2] == test_list[4] == test_list[6] == 'O'):  # diagonal2
            self.finished_ind = True
            self.disable_all_buttons()
            popup = Popup(title="Tic Tac Toe", content=Label(text="Congratulations O, you have won!"),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
        elif self.count == 9:
            self.disable_all_buttons()
            self.finished_ind = True
            popup = Popup(title="Tic Tac Toe", content=Label(text="No winner this time, try again!"),
                          size_hint=(None, None), size=(400, 400))
            popup.open()


class TicTacToeApp(App):
    pass


TicTacToeApp().run()
