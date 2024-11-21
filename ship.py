class ship:
    def __init__(self, id, size, name):
        self.id = id
        self.size = size
        self.name = name
        self.coords = [[-1, -1]] * size
        self.hit = [False] * size


    def place_ship(self, x, y, orientation):
        for i in range(self.size):
            if orientation == 1:
                self.coords[i] = [x, y + i]
            else:
                self.coords[i] = [x + i, y]