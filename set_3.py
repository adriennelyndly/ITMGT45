def relationship_status(from_member, to_member, social_graph):
    from_follows = social_graph[from_member]["following"]
    to_follows = social_graph[to_member]["following"]

    if to_member in from_follows and from_member in to_follows:
        return "friends"
    elif to_member in from_follows:
        return "follower"
    elif from_member in to_follows:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    n = len(board)

    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]

    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if len(set(column)) == 1 and column[0] != "":
            return column[0]

    diagonal1 = [board[i][i] for i in range(n)]
    if len(set(diagonal1)) == 1 and diagonal1[0] != "":
        return diagonal1[0]

    diagonal2 = [board[i][n - 1 - i] for i in range(n)]
    if len(set(diagonal2)) == 1 and diagonal2[0] != "":
        return diagonal2[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        found_leg = False

        for leg in route_map:
            start = leg[0]
            end = leg[1]
            if start == current_stop:
                total_time += route_map[leg]["travel_time_mins"]
                current_stop = end
                found_leg = True
                break

        if not found_leg:
            raise ValueError(f"No outgoing leg starting from: {current_stop}")

    return total_time