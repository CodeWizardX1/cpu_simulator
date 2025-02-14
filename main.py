import re

class CPU:
    def __init__(self):
        self.program_counter = 0
        self.registers = [0] * 32
        self.numbers_index = 1
        self.memory = []  # list of instruction strings
        self.instruction_register = ''
        self.is_halted = False

    def store_value_in_register(self, value_to_store):
        if self.numbers_index > 31:
            self.numbers_index = 1
        self.registers[self.numbers_index] = value_to_store
        print(f'{value_to_store} was stored in Register #{self.numbers_index}')
        self.numbers_index += 1

    def store_instruction_in_memory(self, instruction_string):
        self.memory.append(instruction_string)


    def fetch(self):
        self.instruction_register = self.memory[self.program_counter]
        self.program_counter += 1
        return self.instruction_register

    @staticmethod
    def decode(instruction_string):
        split_instruction_string = re.split(r'[ ,]+', instruction_string)
        if len(split_instruction_string) > 1:
            opcode = split_instruction_string.pop(0)
            operands = split_instruction_string
            for _ in operands:
                operands.append(int(re.sub(r'\D', '', operands.pop(0))))
            return opcode, operands
        opcode = split_instruction_string[0]
        return opcode, None

    def execute(self, opcode, operands):
        match opcode:
            case 'ADD':
                self.registers[operands[0]] = self.registers[operands[1]] + self.registers[operands[2]]
                return f'The result is: {self.registers[operands[0]]}'
            case 'ADDI':
                self.registers[operands[0]] = self.registers[operands[1]] + operands[2]
                return f'The result is: {self.registers[operands[0]]}'
            case 'SUB':
                self.registers[operands[0]] = self.registers[operands[1]] - self.registers[operands[2]]
                return f'The result is: {self.registers[operands[0]]}'
            case 'MUL':
                self.registers[operands[0]] = self.registers[operands[1]] * self.registers[operands[2]]
                return f'The result is: {self.registers[operands[0]]}'
            case 'DIV':
                if self.registers[operands[2]] != 0:
                    self.registers[operands[0]] = self.registers[operands[1]] / self.registers[operands[2]]
                else:
                    return f'Division by 0 error: {self.registers[operands[1]]} / {self.registers[operands[2]]}'
                return f'The result is: {self.registers[operands[0]]}'
            case _:
                print('Invalid opcode')

    def main(self, instruction, value_1=None, value_2=None):
        if value_1 is not None:
            self.store_value_in_register(value_1)

        if value_2 is not None:
            self.store_value_in_register(value_2)

        self.store_instruction_in_memory(instruction)

        instruction_register = self.fetch()

        opcode, operands = self.decode(instruction_register)

        print(self.execute(opcode,operands))


if __name__ == "__main__":
    new_cpu = CPU()
    
    print('ADDITION')
    new_cpu.main("ADD,R11,R1,R2", 10, 20)
    
    print('SUBTRACTION')
    new_cpu.main("SUB,R8,R3,R4", 5, 10)
    
    print('MULTIPLICATION')
    new_cpu.main("MUL,R13,R5,R6", 3, 4)
    
    print('ADDITION WITH IMMEDIATE VALUE OF 7') 
    new_cpu.main("ADDI,R20,R7,7", 5)
    
    print('DIVISION')
    new_cpu.main('DIV,R16,R8,R9', 30, 2)
    
    print('DIVISION BY 0')
    new_cpu.main("DIV,R21,R10,R11", 3, 0)
