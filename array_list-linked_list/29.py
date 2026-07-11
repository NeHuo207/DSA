class DynamicMatrix:
    def __init__(self):
        self.rows = []

    def add_row(self, num_cols=0, fill=0):
        self.rows.append([fill] * num_cols)

    def add_col(self, fill=0):
        for row in self.rows:
            row.append(fill)

    def set(self, i, j, val):
        self.rows[i][j] = val

    def get(self, i, j):
        return self.rows[i][j]

    def shape(self):
        return (len(self.rows), len(self.rows[0]) if self.rows else 0)


m = DynamicMatrix()
m.add_row(3)
m.add_row(3)
m.set(0, 1, 99)
m.add_col(fill=-1)
print(f"  shape = {m.shape()}, get(0,1) = {m.get(0, 1)}, rows = {m.rows}")
