def parse_directory():
    root = {}
    curr = root
    for line in stdin:
        args = line.strip().split(' ')
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '/':
                    curr = root
                else:
                    curr = curr[args[2]]
        elif args[0] == 'dir':
            curr[args[1]] = {'..': curr}
        else:
            curr[args[1]] = int(args[0])
    return root

def get_dir_sizes(root, sizes):
    index = len(sizes)
    sizes.append(0)
    for key in root:
        if key != '..':
            size = root[key] if isinstance(root[key], int) else get_dir_sizes(root[key], sizes)
            sizes[index] += size
    return sizes[index]

sizes = []
size = get_dir_sizes(parse_directory(), sizes)
min_deletion = max(0, 30000000 - (70000000 - size))
print(min(s for s in sizes if s >= min_deletion))



                
