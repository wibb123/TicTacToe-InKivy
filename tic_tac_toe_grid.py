from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from game_logic import TicTacToeGame


class TicTacToeGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = TicTacToeGame()
        self.cols = 3
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        label = Label(text='', size_hint=(0.5, 0.25))
        label.bind()
        self.add_widget(label)
        label = Label(text='', size_hint=(0.5, 0.25))
        label.bind()
        self.add_widget(label)
        label = Label(text='', size_hint=(0.5, 0.25))
        label.bind()
        self.add_widget(label)
        for row in range(3):
            for col in range(3):
                button = Button(text='', font_size='80dp')
                button.bind(on_press=lambda instance, row=row, col=col: self.on_button_click(row, col))
                self.buttons[row][col] = button
                self.add_widget(button)
        new_1_player_game_button = Button(text="Start New 1-Player Game",
                                          size_hint=(1, None))
        new_1_player_game_button.bind(on_press=lambda instance, x=1: self.new_game(x))
        self.add_widget(new_1_player_game_button)
        new_2_player_game_button = Button(text="Start New 2-Player Game",
                                          size_hint=(1, None))
        new_2_player_game_button.bind(on_press=lambda instance, x=2: self.new_game(x))
        self.add_widget(new_2_player_game_button)
        reset_game_button = Button(text="Reset Game",
                                   size_hint=(1, None))
        if self.game.single_player_ind:
            x = 1
        else:
            x = 2
        reset_game_button.bind(on_press=lambda instance, x=x: self.new_game(x))
        self.add_widget(reset_game_button)

    def on_button_click(self, row, col):
        self.game.make_move(row, col)
        self.fill_square(row, col)
        winner, line = self.game.win_check()
        if winner is None:
            self.game.next_turn()
            if self.game.single_player_ind:
                (row, col) = self.game.get_best_move()
                self.game.make_move(row, col)
                self.fill_square(row, col)
                winner, line = self.game.win_check()
                if winner is None:
                    self.game.next_turn()
                else:
                    self.game_end_popup(winner, line)
        else:
            self.game_end_popup(winner, line)

    def fill_square(self, row, col):
        button = self.buttons[row][col]
        if self.game.is_x_turn:
            button.text = 'X'
        else:
            button.text = 'O'
        button.disabled = True

    def game_end_popup(self, winner, line):
        if winner == 'X':
            self.show_winner_popup('X')
            for square in line:
                self.change_colour(square[0], square[1])
        elif winner == 'O':
            self.show_winner_popup('O')
            for square in line:
                self.change_colour(square[0], square[1])
        elif winner == 'draw':
            self.show_draw_popup()

    def change_colour(self, row, col):
        button = self.buttons[row][col]
        button.background_color = [0, 1, 0, 1]

    def show_winner_popup(self, winner):
        self.disable_all_buttons()
        popup = Popup(title='Tic Tac Toe', content=Label(text=f'Congratulations {winner}, you have won!'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def show_draw_popup(self):
        self.disable_all_buttons()
        popup = Popup(title='Tic Tac Toe', content=Label(text='No winner this time, try again!'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def disable_all_buttons(self):
        for row in self.buttons:
            for b in row:
                b.disabled = True

    def reset_all_buttons(self):
        for row in self.buttons:
            for b in row:
                b.disabled = False
                b.text = ''
                b.background_color = [1, 1, 1, 1]

    def new_game(self, players):
        self.game.new_game(players)
        self.reset_all_buttons()


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


if __name__ == '__main__':
    TicTacToeApp().run()
