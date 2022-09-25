class Grid:

    # Normal connect 4 's dimensions
    m_long = 7
    m_high = 6

    m_grid = []

    def __init__(self):
        for j in range(0, self.m_high):
            line = []
            for i in range(0, self.m_long):
                cell = "-"
                line.append(cell)
            self.m_grid.append(line)
