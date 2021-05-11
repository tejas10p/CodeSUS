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
    
    def define_line_remover(self):
        splitted_s = self.s.split('\n')
        edited_s = ''

        for line in splitted_s:
            line = line.strip()
            if(line.startswith('#define')):
                pass
            else:
                edited_s += line + '\n'
        
        self.s = edited_s

    
    def package_printing_remover(self):
        prog_string = self.s
        prog_line = prog_string.split("\n")
        edit_string = ""
        remove_print = "cout"
        edited_string = []
        for x in prog_line:
            x = x.strip()
            edit_string = ""
            if (x.startswith("#") and not x.startswith("#define")):
                pass
            else:
                try:
                    prog_string = x.index(remove_print)
                except ValueError:
                    edit_string = edit_string + x + ""
                else:
                    current_index = 0
                    while(current_index < prog_string):
                        edit_string += x[current_index]
                        current_index += 1
            if(edit_string != ""):
                edited_string.append(edit_string)
        self.s = ""
        for i in edited_string:
            self.s += i + '\n'
