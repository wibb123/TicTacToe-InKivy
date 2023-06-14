# Tic Tac Toe Game

This is a simple implementation of the Tic Tac Toe game using the Kivy framework. The game allows for a 1-player mode against a computer opponent or a 2-player mode where two players can play against each other.

## Prerequisites

- Python 3.x
- Kivy framework (version x.x.x) - installation instructions can be found at [Kivy Installation Guide](https://kivy.org/doc/stable/gettingstarted/installation.html)

## Getting Started

1. Clone the repository or download the source code.
2. Install the necessary dependencies mentioned in the Prerequisites section.
3. Open a terminal or command prompt and navigate to the directory where the code is located.
4. Run the following command to start the Tic Tac Toe game:

    ```
    python main.py
    ```

## How to Play

- The game is played on a 3x3 grid.
- Players take turns placing their symbols (X or O) on an empty square.
- The first player to get three of their symbols in a row, column, or diagonal wins the game.
- If all squares are filled and no player has won, the game is a draw.

## Features

- Two game modes: 1-player (against the computer) and 2-player (two players can play against each other).
- Responsive grid layout using Kivy's UI framework.
- Pop-up windows to display game results (winner or draw).
- Ability to start a new game after a game ends.

## File Structure

- `main.py`: Contains the command to launch the game.
- `tic_tac_toe_grid.py`: Contains the main Kivy app and the UI logic for the Tic Tac Toe grid.
- `game_logic.py`: Implements the game logic, including moves, turns, win conditions, and game state.
- `tictactoe.kv`: Contains the Kivy language file defining the UI layout.
- `tic_tac_toe_test`: Contains basic unit tests for game functionality.

## Testing

- Unit tests for various components of the game can be found in the `tic_tac_toe_test` directory.
- Run the tests using your preferred testing framework or by executing the test files directly.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
