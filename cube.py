puzzle = {
    'state': [0, 2, 3, 3], 
    'moves': [
        [0, 3],
        [1, 2],
        [0, 2],
        [0, 1, 2, 3]
    ],
    'mod': 4,
    'result': 'same'
}


def main():
    queue = [([], puzzle['state'])]
    cache = {tuple(puzzle['state'])}
    for way, curr in queue:
        if puzzle['result'] == 'same':
            if len(set(curr)) == 1:
                return way
        elif curr == puzzle['result']:
            return way

        for i, move in enumerate(puzzle['moves']):
            new_state = curr[:]
            for j in move:
                new_state[j] = (new_state[j] + 1) % puzzle['mod']
            if tuple(new_state) in cache:
                break
            queue.append((way + [i], new_state))
            cache.add(tuple(new_state))

    return 'No way'


if __name__ == '__main__':
    print(main())
