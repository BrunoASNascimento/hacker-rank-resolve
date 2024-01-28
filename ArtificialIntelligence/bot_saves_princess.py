def displayPathtoPrincess(n, grid):
    p_position = None
    m_position = None

    # Find positions of 'm' and 'p' and break early when found
    for i in range(n):
        if 'm' in grid[i]:
            m_position = (i, grid[i].index('m'))
        if 'p' in grid[i]:
            p_position = (i, grid[i].index('p'))
        if m_position and p_position:
            break

    # Calculate horizontal and vertical distances
    horizon = m_position[1] - p_position[1]
    vertical = m_position[0] - p_position[0]

    # Generate moves list directly based on distances
    moves = []
    moves.extend(['LEFT'] * abs(horizon) if horizon >
                 0 else ['RIGHT'] * abs(horizon))
    moves.extend(['UP'] * abs(vertical) if vertical >
                 0 else ['DOWN'] * abs(vertical))

    return '\n'.join(moves)


# Input and function call remain the same
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

print(displayPathtoPrincess(m, grid))
