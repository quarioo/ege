def check_uno_game(n, a, q, initial_card, players_hands, moves):
    current_player = 0
    direction = 1
    stack = []
    top_card = initial_card
    hands = [set(hand) for hand in players_hands]
    active_players = set(range(n))

    for turn, move in enumerate(moves, start=1):
        parts = move.split()
        player = int(parts[-1]) - 1

        if move.startswith('->'):
            card = ' '.join(parts[1:3])
            is_uno = 'AND uno' in move

            # Check if it's the player's turn
            if player != current_player and card != top_card:
                return turn

            # Check if the player has the card
            if card not in hands[player]:
                return turn

            # Check if the move is valid
            if stack and (card.split()[1] not in ['X', '@']):
                return turn

            if not stack and card.split()[1] not in ['X', '@'] and card != top_card and \
                    card.split()[0] != top_card.split()[0] and card.split()[1] != top_card.split()[
                1] and top_card.split()[0] != 'black':
                return turn

            # Check Uno call
            if len(hands[player]) == 2 and not is_uno:
                return turn
            if len(hands[player]) != 2 and is_uno:
                return turn

            # Update game state
            hands[player].remove(card)
            top_card = card
            if len(hands[player]) == 0:
                active_players.remove(player)

            if card.split()[1] == '#':
                current_player = (current_player + direction) % n
            elif card.split()[1] in ['X', '@']:
                stack.append(card)

            if player != current_player:  # It was a catch
                stack = [card]

            current_player = (player + direction) % n

        elif move.startswith('<<-'):
            k = int(parts[1])
            taken_cards = parts[2:2 + k]

            # Check if it's the player's turn
            if player != current_player:
                return turn

            # Check if the number of cards taken is correct
            expected_cards = 0
            if stack:
                expected_cards = 2 * len(stack) if stack[0].split()[1] == 'X' else 4 * len(stack)

            if k != expected_cards and (expected_cards > 0 or k != 1):
                return turn

            # Update game state
            hands[player].update(taken_cards)
            stack.clear()
            current_player = (current_player + direction) % n

        while current_player not in active_players and active_players:
            current_player = (current_player + direction) % n

    return 0


# Read input
t = int(input())
for _ in range(t):
    n, a, q, *initial_card = input().split()
    n, a, q = map(int, [n, a, q])
    initial_card = ' '.join(initial_card)

    players_hands = [input().split() for _ in range(n)]
    moves = [input()]