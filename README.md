# CPU Simulator

A simple CPU simulator that can store values in registers, place instructions into memory, then fetch, decode, and execute those instructions.

## Features

- Simulates a CPU with 32 registers, an instruction register, and a memory list.
- Supports basic arithmetic operations: `ADD`, `SUB`, `MUL`, `DIV`, and `ADDI`.
- Fetches, decodes, and executes instructions stored in memory.
- Handles division by zero errors gracefully.


### Example Operations

- **Addition**
  ```python
  new_cpu.main("ADD,R11,R1,R2", 10, 20)
  ```
  Stores `10` in Register 1 and `20` in Register 2, then performs `R11 = R1 + R2`.

- **Subtraction**
  ```python
  new_cpu.main("SUB,R8,R3,R4", 5, 10)
  ```
  Stores `5` in Register 3 and `10` in Register 4, then performs `R8 = R3 - R4`.

- **Multiplication**
  ```python
  new_cpu.main("MUL,R13,R5,R6", 3, 4)
  ```
  Stores `3` in Register 5 and `4` in Register 6, then performs `R13 = R5 * R6`.

- **Addition with an Immediate Value**
  ```python
  new_cpu.main("ADDI,R20,R7,7", 5)
  ```
  Stores `5` in Register 7, then performs `R20 = R7 + 7`.

- **Division**
  ```python
  new_cpu.main("DIV,R16,R8,R9", 30, 2)
  ```
  Stores `30` in Register 8 and `2` in Register 9, then performs `R16 = R8 / R9`.

- **Division by Zero Handling**
  ```python
  new_cpu.main("DIV,R21,R10,R11", 3, 0)
  ```
  Attempts to divide `3` by `0` and returns an error message.

## Code Overview

### `CPU` Class

- `store_value_in_register(value)`: Stores a given integer value into a register.
- `store_instruction_in_memory(instruction)`: Stores an instruction string into memory.
- `fetch()`: Retrieves the next instruction from memory.
- `decode(instruction)`: Decodes an instruction into an opcode and operand list.
- `execute(opcode, operands)`: Executes the decoded instruction.
- `main(instruction, value_1=None, value_2=None)`: Convenience method to store values, store instructions, and execute them.
