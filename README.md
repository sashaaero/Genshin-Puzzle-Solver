# Genshin-Puzzle-Solver
Script solves cube puzzles from Inazuma. Notice that it only solves now common puzzles.

Scripts needs initial puzzle data from you, such as current state, what happen if you interact with the cube and desired result.
There is a `puzzle` dictionary that has presets you can change.

## Puzzle state
`state` key in `puzzle` dict.

For puzzle current state I suggest to use such values
0 - cube looks on you
1 - cube looks left
2 - cube looks forward
3 - cube looks right

For example state value could be `'state': [0, 2, 3, 3]`.

(Dont forget everything is 0 based, not 1)

## Interactions
`moves` key in `puzzle` dict.

Here you need to provide list of lists.
For each cube we need to know what cubes moves after you interact with it.
For example if you hit leftmost cube and it moves with his right neighbor - value is `[0, 1]`

Example
```
'moves': [
  [0, 3],  # interactions with leftmost cube, moves itself and the third one
  [1, 2],  # etc
  [0, 2],
  [0, 1, 2, 3]
],
```

## Result
Field describes desired result of a puzzle.
There are two types of result:
- we don't care about the side cubes looking, it should just be the same -- `'result': 'same'`
- we wan't specific directions -- `'result': [0, 0, 0, 0]` (all cubes face us)

## Usage
After you insert all data just run it as `python cube.py`
