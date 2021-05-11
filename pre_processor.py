import re

class pre_processing_module:
    
    def __init__(self,code):
        self.s = code
    
    def replacer(self,match):
            self.s = match.group(0)
            if self.s.startswith('/'):
                return " " 
            else:
                return self.s

    def comment_remover(self):
        regex_expression = r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"'
        pattern = re.compile(regex_expression, re.DOTALL | re.MULTILINE)
        self.s = re.sub(pattern, self.replacer, self.s)
    
    def define_remover(self):
        to_be_replaced = {}
        splitted_s = self.s.split('\n')

        for line in splitted_s:
            rec = line
            rec = rec.strip()
            if rec.startswith('#define'):
                line = ' '.join(line.split())
                space1 = line.index(' ')
                space2 = line.index(' ', space1 + 1)
                var = line[space1:space2]
                var = var.strip()
                org = line[space2:]
                org = org.strip()
                to_be_replaced[var] = org
            
        return to_be_replaced
