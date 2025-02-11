import re

class CPU:
    def __init__(self, cache_enabled=True):
        self.registers = [0]*8
        self.program_counter = 0
        self.cache_enabled = cache_enabled
        self.instructions = [] #list of instruction strings, ex: "ADD R1, R2, R3"
        self.data_memory = [] #list of integers
        self.cache = [
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
        ]
        
    def fetch(self):
        return self.instructions[self.program_counter]
    
    def decode(self, instruction_string):
        split_instructions = re.split(r'[ ,]+', instruction_string)
        opcode = split_instructions[0]
        source_register_1 = int(split_instructions[1][1:])
        source_register_2 = int(split_instructions[2][1:])
        destination_register = int(split_instructions[3][1:])
        return (opcode, [source_register_1, source_register_2, destination_register])
        
        
        
    
    def execute(self, opcode, operand_list):
        pass
    
    def updatePC(self, opcode, operand_list):
        pass
    
    def readMemory(self, address):
        pass
    
    def writeMemory(self, address, value):
        pass
    
    

#MAIN PROGRAM

if __name__ == "__main__":
    new_cpu = CPU()
    
    