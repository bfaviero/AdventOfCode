data="""..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""

N = "N"
S = "S"
W = "W"
E = "E"
NE = "NE"
NW = "NW"
SE = "SE"
SW = "SW"
directions = [N, S, W, E, NE, NW, SE, SW]


transforms = {
    N: lambda row, col: (row - 1, col),
    S: lambda row, col: (row + 1, col),
    W: lambda row, col: (row, col - 1),
    E: lambda row, col: (row, col + 1),
    NE: lambda row, col: (row - 1, col + 1),
    NW: lambda row, col: (row - 1, col - 1),
    SE: lambda row, col: (row + 1, col + 1),
    SW: lambda row, col: (row + 1, col - 1),
}

headings = [N, S, W, E, NE, NW, SE, SW]
def transform(row, col, direction):
    return transforms[direction](row, col)


from pydash import count_by
mapp = [list(line) for line in data1.split("\n")]


class Elf():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.current_proposal = None
    
    def __repr__(self):
        return str((self.row, self.col, self.current_proposal))
    
    def get_proposed_position(self):
        if self.current_proposal is None:
            return (self.row, self.col)
        return transform(self.row, self.col, self.current_proposal)
    
    def move(self):
        row, col = self.get_proposed_position()
        self.row = row
        self.col = col
    
# Create Elves
elves = []
max_length = max(len(row) for row in mapp)
for i in range(len(mapp)):
    for j in range(max_length):
        value = mapp[i][j]
        if value == "#":
            elves.append(Elf(i, j))


def is_alone(elf, points):
    row, col = elf.row, elf.col
    for heading in directions:
        row2, col2 = transform(row, col, heading)
        if (row2, col2) in points:
            return False
    return True

def is_valid_point(row, col, points):
    return (row, col) not in points

def is_valid(heading, elf, points):
    next_row, next_col = transform(elf.row, elf.col, heading)
    return is_valid_point(next_row, next_col, points)
   

# for row in mapp:
#     print(''.join(row))
# print("")


proposals = [
    ([N, NE, NW], N),
    ((S, SE, SW), S),
    ((W, NW, SW), W),
    ((E, NE, SE), E),
]

for roundd in range(0, 1000):  # pick a random high bound
    points = set([(elf.row, elf.col) for elf in elves])
    for elf in elves:
        elf.current_proposal = None

    for elf in elves:
        if is_alone(elf, points):
            continue
        for proposal in proposals:
            (headings, next_direction) = proposal
            if all([is_valid(heading, elf, points) for heading in headings]):
                elf.current_proposal = next_direction
                break

    proposed_directions = [elf.get_proposed_position() for elf in elves]
    count = count_by(proposed_directions)

    moved = False
    for elf in elves:
        if count[elf.get_proposed_position()] > 1:
            continue
        if elf.current_proposal is None:
            continue
        elf.move()
        moved = True

    if not moved:
        break # stop when we don't move

    proposals = proposals[1:] + [proposals[0]]

minr, minc, maxr, maxc = 999, 999, 0, 0
for elf in elves:
    minr = min(minr, elf.row)
    maxr = max(maxr, elf.row)
    minc = min(minc, elf.col)
    maxc = max(maxc, elf.col)

print(((maxc-minc + 1) * (maxr-minr+ 1)) - len(elves))
print(roundd)