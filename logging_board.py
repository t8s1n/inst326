from board import Board


class LoggingBoard(Board):  # subclass of board

    # Overrides
    def __init__(self):
        super().__init__()
        self.log = []

    def claim_square(self, player, index):
        super().claim_square(player, index)
        self.log.append(f'{player} selects the square {index}')

    def get_winner(self):
        winner = super().get_winner()
        if winner:
            self.log.append(f"player {winner} wins!")
        return winner

    def game_over(self):
        game_over = super().game_over()
        if game_over:
            for message in self.log:
                print(message)
        return game_over
