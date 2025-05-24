import random
import copy

# Designation:
# U = Up (White), D = Down (Yellow), F = Front (Red),
# B = Back (Orange), L = Left (Green), R = Right (Blue)
default_colors = {
    'U': ['W'] * 4,
    'D': ['Y'] * 4,
    'F': ['R'] * 4,
    'B': ['O'] * 4,
    'L': ['G'] * 4,
    'R': ['B'] * 4
}

MOVES = ['R', "R'", 'U', "U'", 'F', "F'"]

class Cube:
    def __init__(self, faces=None):
        if faces is None:
            self.faces = copy.deepcopy(default_colors)
        else:
            self.faces = copy.deepcopy(faces)

    def is_solved(self):
        # Each face are of the same color
        for face in self.faces.values():
            if len(set(face)) != 1:
                return False
        return True

    def move(self, action):
        c = copy.deepcopy(self)
        f = c.faces

        if action == 'R':
            # Clockwise rotation of the right edge
            f['R'] = [f['R'][2], f['R'][0], f['R'][3], f['R'][1]]
            f['U'][1], f['U'][3], f['B'][2], f['B'][0], f['D'][1], f['D'][3], f['F'][1], f['F'][3] = \
                f['F'][1], f['F'][3], f['U'][1], f['U'][3], f['B'][2], f['B'][0], f['D'][1], f['D'][3]

        elif action == "R'":
            # Turning the right edge counterclockwise
            f['R'] = [f['R'][1], f['R'][3], f['R'][0], f['R'][2]]
            f['F'][1], f['F'][3], f['D'][1], f['D'][3], f['B'][2], f['B'][0], f['U'][1], f['U'][3] = \
                f['U'][1], f['U'][3], f['F'][1], f['F'][3], f['D'][1], f['D'][3], f['B'][2], f['B'][0]

        elif action == 'U':
            # Clockwise rotation of the top edge
            f['U'] = [f['U'][2], f['U'][0], f['U'][3], f['U'][1]]
            f['F'][0], f['F'][1], f['R'][0], f['R'][1], f['B'][0], f['B'][1], f['L'][0], f['L'][1] = \
                f['R'][0], f['R'][1], f['B'][0], f['B'][1], f['L'][0], f['L'][1], f['F'][0], f['F'][1]

        elif action == "U'":
            # Turning the top edge counterclockwise
            f['U'] = [f['U'][1], f['U'][3], f['U'][0], f['U'][2]]
            f['F'][0], f['F'][1], f['L'][0], f['L'][1], f['B'][0], f['B'][1], f['R'][0], f['R'][1] = \
                f['L'][0], f['L'][1], f['B'][0], f['B'][1], f['R'][0], f['R'][1], f['F'][0], f['F'][1]

        elif action == 'F':
            # Clockwise rotation of the front edge
            f['F'] = [f['F'][2], f['F'][0], f['F'][3], f['F'][1]]
            f['U'][2], f['U'][3], f['R'][0], f['R'][2], f['D'][0], f['D'][1], f['L'][1], f['L'][3] = \
                f['L'][3], f['L'][1], f['U'][2], f['U'][3], f['R'][0], f['R'][2], f['D'][1], f['D'][0]

        elif action == "F'":
            # Turning the front edge counterclockwise
            f['F'] = [f['F'][1], f['F'][3], f['F'][0], f['F'][2]]
            f['L'][3], f['L'][1], f['U'][2], f['U'][3], f['R'][0], f['R'][2], f['D'][1], f['D'][0] = \
                f['U'][2], f['U'][3], f['R'][0], f['R'][2], f['D'][0], f['D'][1], f['L'][3], f['L'][1]

        return c

    def get_neighbors(self):
        return [self.move(m) for m in MOVES]

    def scramble(self, steps=5):
        scrambled = self
        for _ in range(steps):
            move = random.choice(MOVES)
            scrambled = scrambled.move(move)
        return scrambled

    def __eq__(self, other):
        return self.faces == other.faces

    def __hash__(self):
        return hash(str(self.faces))

    def __str__(self):
        return self.as_string()

    def as_string(self):
        return ''.join(f"{face}:{self.faces[face][0]} " for face in ['U','D','F','B','L','R'])

    def print_cube(self):
        f = self.faces

        color_map = {
            'W': '\033[47m  \033[0m',  # White
            'Y': '\033[43m  \033[0m',  # Yellow
            'R': '\033[41m  \033[0m',  # Red
            'O': '\033[45m  \033[0m',  # Orange (shown as purple)
            'G': '\033[42m  \033[0m',  # Green
            'B': '\033[44m  \033[0m',  # Blue
        }

        def face_str(face):
            return f"{color_map[face[0]]}{color_map[face[1]]}\n{color_map[face[2]]}{color_map[face[3]]}"

        # U (Up)
        print("     " + face_str(f['U']).replace("\n", "\n     "))

        # L + F + R + B
        print(
            face_str(f['L']).split('\n')[0] +
            face_str(f['F']).split('\n')[0] +
            face_str(f['R']).split('\n')[0] +
            face_str(f['B']).split('\n')[0]
        )
        print(
            face_str(f['L']).split('\n')[1] +
            face_str(f['F']).split('\n')[1] +
            face_str(f['R']).split('\n')[1] +
            face_str(f['B']).split('\n')[1]
        )

        # D (Down)
        print("     " + face_str(f['D']).replace("\n", "\n     "))
