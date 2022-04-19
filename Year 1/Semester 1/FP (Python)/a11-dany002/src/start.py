from AI.BotMoves import BotMoves
from UI.console import Console
from Services.BoardService import BoardService
from Repository.BoardRepository import BoardRepository

if __name__ == "__main__":


    board_repository_for_player = BoardRepository()
    board_repository_for_bot = BoardRepository()
    board_service_for_player = BoardService(board_repository_for_player)
    board_service_for_bot = BoardService(board_repository_for_bot)
    bot_moves = BotMoves(board_service_for_player)
    file = open("settings.properties", "r")
    player1 = None
    player2 = None
    for line in file:
        command = line.strip().split("=", maxsplit=1)
        if command[0] == "player1 ":
            player_or_ai = command[1].strip()
            player_or_ai = player_or_ai[1:-1]
            if player_or_ai == "player":
                player1 = "player"
            else:
                player1 = "AI"
        elif command[0] == "player2 ":
            player_or_ai = command[1].strip()
            player_or_ai = player_or_ai[1:-1]
            if player_or_ai == "player":
                player2 = "player"
            else:
                player2 = "AI"
    if player1 == "player" and player2 == "AI" or player1 == "AI" and player2 == "player":
        ui = Console(board_service_for_player, board_service_for_bot, bot_moves)
        ui.run_command_player_vs_bot()
    elif player1 == "AI" and player2 == "AI":
        bot_moves_for_ai = BotMoves(board_service_for_bot)
        ui = Console(board_service_for_player, board_service_for_bot, bot_moves, bot_moves_for_ai)
        ui.run_command_ai_vs_ai()

    """
    settings.properties options:
    player1 = "AI"
    player2 = "AI"
    
    player1 = "AI"
    player2 = "player"
    
    player1 = "player"
    player2 = "AI"
    """