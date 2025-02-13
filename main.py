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
                return self.registers[operands[0]]
            case 'ADDI':
                self.registers[operands[0]] = self.registers[operands[1]] + operands[2]
                return self.registers[operands[0]]
            case 'SUB':
                self.registers[operands[0]] = self.registers[operands[2]] - self.registers[operands[1]]
                return self.registers[operands[0]]
            case 'MUL':
                self.registers[operands[0]] = self.registers[operands[1]] * self.registers[operands[2]]
                return self.registers[operands[0]]
            case 'DIV':
                calculated_value = 0
                if self.registers[operands[2]] != 0:
                    calculated_value = self.registers[operands[1]] / self.registers[operands[2]]
                else:
                    print(f'Division by 0 error: {self.registers[operands[1]]} / {self.registers[operands[2]]}')
                return calculated_value
            case 'HALT':
                self.is_halted = True
            case _:
                print('Invalid opcode')

    def main(self, instruction, value_1=None, value_2=None):
        if value_1:
            self.store_value_in_register(value_1)

        if value_2:
            self.store_value_in_register(value_2)

        self.store_instruction_in_memory(instruction)

        instruction_register = self.fetch()

        opcode, operands = self.decode(instruction_register)

        print(f'The result is: {self.execute(opcode,operands)}')


if __name__ == "__main__":
    CPU().main("MUL,R3,R2,R1", 5, 6)

        
        
        
    
   
    
    