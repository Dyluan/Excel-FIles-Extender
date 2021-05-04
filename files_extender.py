import pandas as pd

class Extend:

    def __init__(self, filename, path_to_file, number_of_files_to_extend, output_name):

        if path_to_file[-1:] != '\\':
            self.path_to_file = path_to_file + '\\'
        
        else:
            self.path_to_file = path_to_file

        self.file = self.path_to_file + filename
        self.file_name = filename.split('.')[0]
        self.nb_files = number_of_files_to_extend
        self.output_name = output_name
        self.file_format = filename.split('.')[-1]

        self.go()

    def go(self):

        first_file = self.path_to_file + self.file_name + '_1.' + self.file_format

        if 'csv' in self.file_format:
            csv_reader = 1
            new_dataframe = pd.read_csv(first_file, sep=';', encoding='utf-8')
        
        else:
            csv_reader = 0
            new_dataframe = pd.read_excel(first_file)
        

        for i in range(2, self.nb_files+1):
            
            files = self.path_to_file + self.file_name + '_' + str(i) + '.' + self.file_format

            if csv_reader:
                new_dataframe = new_dataframe.append(pd.read_csv(files, sep=';', encoding='utf-8'))
            
            else:
                new_dataframe = new_dataframe.append(pd.read_excel(files))
        
        output = self.path_to_file + self.output_name

        if csv_reader:
            new_dataframe.to_csv(output, sep=';', index=False)
        
        else:
            new_dataframe.to_excel(output, index=False)
    
        return

e = Extend('links.csv', 'C:\\Users\\Dylan\\Documents\\python\\django\\apprendre\\mysite\\appartements\\aliloca\\festirent', 10, 'output.csv')