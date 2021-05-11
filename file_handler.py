import glob
import os
import pathlib
import algorithm as wf
import pre_processor as pp

class file_bridge:
    def __init__(self,location,report_name):
        file_search = location + '\\*.cpp'
        file_list = glob.glob(file_search)
        pre_processed_codes = []
        threshold = 0.3
        r_location = str(pathlib.Path(__file__).parent.absolute())
        report_location = r_location + '\\' + "Reports" + '\\' + report_name + ".txt"
        report_file = open(report_location,'w+')
        file_names = []

        for i in file_list:
            current_file = open(i,'r')
            file_names.append((os.path.basename(i))[:7])
            code = current_file.read()
            pre_processor = pp.pre_processing_module(code)
            pre_processor.helper()
            pre_processed_codes.append(pre_processor.s)
            current_file.close()

        for i in range(len(pre_processed_codes) - 1):
            for j in range(len(pre_processed_codes) - i - 1):
                checker = wf.wagner_fischer(pre_processed_codes[i], pre_processed_codes[i + j + 1])
                checker.restricted_tabulation(threshold)
                plagiarism_percentage = (float)(checker.score_generator())
                plagiarism_percentage_formatted = "{:.2f}".format(plagiarism_percentage)
                if(plagiarism_percentage > 70.0):
                    str_result = file_names[i] + '\t' + file_names[i + j + 1] + '\t' + (plagiarism_percentage_formatted) + '\n'
                    report_file.write(str_result)
        
        report_file.close()