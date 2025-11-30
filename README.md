# Ai-Home-Work-2
# Generalized Tic-Tac-Toe (m×m, k-in-a-row)
A full adversarial search agent that plays **generalized Tic-Tac-Toe** using:

- ✔ Minimax  
- ✔ Alpha–Beta Pruning  
- ✔ Depth-Limited Search (for m>3)  
- ✔ Domain-Specific Heuristic  
- ✔ Deterministic Move Ordering  
- ✔ Clean modular architecture  
- ✔ Full test suite provided  

This project fully satisfies requirements of the "Adversarial Search – Homework 2" assignment.

---

## Features

### Game Engine
Implements the full rule system for arbitrary board sizes:
- Board size: **m × m**  
- Win condition: **k-in-a-row**  
- Supports rows, columns, and both diagonals  
- Core engine functions:
  - `player(board)`
  - `actions(board)`
  - `result(board, move)`
  - `winner(board)`
  - `terminal(board)`
  - `utility(board)`

---

###  Search Algorithms
#### ✔ Minimax  
Used primarily for verifying correctness on 3×3 boards.

#### ✔ Alpha–Beta Pruning  
Returns the *same* moves as Minimax on all 3×3 positions — but significantly faster.

#### ✔ Depth-Limited Alpha–Beta + Heuristic  
Used for larger boards like:

- 4×4 with k=3  
- 5×5 with k=4  

Heuristic prevents blunders, detects threats, wins, and blocks.

---

###  Heuristic Function
A simple, symmetric, threat-based evaluation:

- +100 for `(k-1)` in a row (winning threat)
- -100 for opponent `(k-1)` in a row (block required)
- ±10 for `(k-2)` formations  

Works on arbitrary board sizes.

---

### Move Ordering
All search functions use:
```python
sorted(game.actions(state))
