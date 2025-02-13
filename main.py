import re



class CPU:
    def __init__(self):
        self.program_counter = 0
        self.registers = [0]*32
        self.memory = [] #list of instruction strings
        self.instruction_register = ''
        self.cache = [
            {'tag': None, 'data': None},
            {'tag': None, 'data': None},
            {'tag': None, 'data': None},
            {'tag': None, 'data': None}
        ]
        self.is_halted = False
        self.current_opcode = ''
        self.current_operands = []
        self.temp_result = []
        self.memory_data = []
        
    
    def fetch(self):
        self.instruction_register = self.memory[self.program_counter]
        self.program_counter += 1
        
    
    def decode(self, instruction_string):
        pass
        
        
        
        
    
   
    
    