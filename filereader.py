import os
from point2d import Point2D

class Filereader:
    def __init__(self):
        pass
        
    def getpoint(self):
        path = ".\\"
        dirs =  os.listdir(path)
        file_read_list =[]
        file_input_list =[]
        for filename in dirs:
            if filename.endswith(".txt"):   
                f = open(filename,'r')
                while True:
                    file = f.readlines()
                    for line in file:
                        if  "points" in line:
                            start_index = line.index("points")
                            file_read_list = file[start_index+1:]
                            if 'end\n' in file_read_list:
                                file_read_list.pop(-1)
                    break
                file_input=[point.strip() for point in file_read_list]
                for i in range(len(file_input)):
                    if '\t' in file_input[i]:
                        file_input[i] = file_input[i].split('\t')
                        xcoord = float(file_input[i][0])
                        ycoord = float(file_input[i][1])
                        file_input_list.extend((xcoord,ycoord))
                n = 2
                result = [file_input_list[i * n:(i + 1) * n] for i in range((len(file_input_list) + n - 1) // n )]
        return result

