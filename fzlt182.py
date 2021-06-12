def maze_runner(maze, directions):
    x, y = [(j, i) for i in range(len(maze))
            for j in range(len(maze)) if maze[i][j] == 2][0]
    for d in directions:
        if d == "N":
            y -= 1
        elif d == "E":
            x += 1
        elif d == "S":
            y += 1
        elif d == "W":
            x -= 1
        if y < 0 or y > len(maze) - 1 or x < 0 or x > len(maze) - 1 or maze[y][x] == 1:
            return "Dead"
        if maze[y][x] == 3:
            return "Finish"
    return "Lost"
