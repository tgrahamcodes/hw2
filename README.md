# Programming Assignment #2 — Game of Life

## Overview
This project is a C implementation of **John Conway’s Game of Life**, designed to simulate the evolution of cellular automata based on a set of rules. The program runs on a rectangular grid and progresses through generations based on the state of neighboring cells.

## Features
- Implements **Game of Life** logic.
- Reads an initial configuration from a file.
- Supports configurable board size and generation count.
- Detects termination conditions such as steady states and oscillations.
- Command-line interaction for custom inputs.

## Prerequisites
- A C compiler (e.g., `gcc`)
- Standard C libraries
- Linux or macOS (or Windows with WSL)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repository/HW2.git
   cd HW2
   ```
2. Compile the program:
   ```sh
   gcc -o HW2 src/*.c -Wall -Wextra
   ```

## Usage
Run the program with the following command:
```sh
./HW2 NR NC gens inputfile [print] [pause]
```
where:
- `NR`: Number of rows in the grid.
- `NC`: Number of columns in the grid.
- `gens`: Number of generations to simulate.
- `inputfile`: File containing the initial configuration.
- `[print]` (optional): `'y'` to display each generation, `'n'` to skip printing (default: `'n'`).
- `[pause]` (optional): `'y'` to pause between generations, `'n'` for continuous execution (default: `'n'`).

### Example
```sh
./HW2 20 20 100 patterns/input.txt y n
```
This runs the simulation on a 20x20 board for 100 generations, printing each generation but not pausing between them.

## Input File Format
- Each line contains a sequence of `x` (occupied cell) and `o` (unoccupied cell).
- The grid starts from the upper-left corner and is centered during execution.

Example input file:
```
oxo
xox
xox
oxo
```

## Implementation Details
- Uses dynamically allocated 2D arrays for grid management.
- Alternates between multiple arrays to prevent overwriting data mid-simulation.
- Implements helper functions for neighbor counting and state transitions.
