
class Grid:
    def __init__(self, pixels, type):
        self.pixels = pixels
        self.type = type

    def enhance(self, enhancer):
        default = '.' if self.type == '#' else '#'
        new_default = enhancer[(convert_binary('111111111') if default == '#' else 0)]
        new_type = '.' if new_default == '#' else '#'
        new_pixels = set()

        neighbour_coords = ((-1, -1), (0, -1), (1, -1),
                            (-1, 0), (0, 0), (1, 0),
                            (-1, 1), (0, 1), (1, 1),)
        
        for pixel in get_relevant_pixels(self.pixels):
            binary = ''
            for x, y in neighbour_coords:
                neighbour = (pixel[0] + x, pixel[1] + y)
                if self.type == '#':
                    binary += '1' if neighbour in self.pixels else '0'
                else:
                    binary += '0' if neighbour in self.pixels else '1'

            result_pixel_type = enhancer[convert_binary(binary)]
            if result_pixel_type == new_type:
                new_pixels.add((pixel))

        self.pixels = new_pixels
        self.type = new_type

    def display(self):
        min_x = min(pixel[0] for pixel in self.pixels)
        max_x = max(pixel[0] for pixel in self.pixels)
        min_y = min(pixel[1] for pixel in self.pixels)
        max_y = max(pixel[1] for pixel in self.pixels)
        default = '.' if self.type == '#' else '#'
        print('top left' , min_x, min_y)
        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                line += (self.type if (x, y) in self.pixels else default)
            print(line)
        print('')
        

def convert_binary(binary):
    result = 0
    while binary:
        result *= 2
        result += (1 if binary[0] == '1' else 0)
        binary = binary[1:]
    return result

def get_relevant_pixels(pixels):
    result = set()
    for pixel in pixels:
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                result.add((pixel[0] + x, pixel[1] + y))
    return result

pixels = set()
file = open("aoc input.txt", "r")
for i, line in enumerate(file):
    if i == 0:
       enhancer = line
    elif i > 1:
        for j in range(len(line)):
            if line[j] == '#':
                pixels.add((j, i))

grid = Grid(pixels, '#')
grid.display()
for i in range(50):
    print(i)
    pixels = grid.enhance(enhancer)

grid.display()
print(len(grid.pixels))
