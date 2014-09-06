#!/usr/bin/python

import os
import time

matrix1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,1,1,1]]
matrix2 = [[1,1,1,0],[0,0,0,1],[1,1,1,0],[1,1,1,1]]
matrix3 = [[1,1,1,1],[0,0,1,1],[1,0,0,1],[0,1,1,0]]
matrix4 = [[1,0,0,1],[1,0,0,1],[1,1,1,1],[0,0,0,1]]
matrix5 = [[1,1,1,1],[1,0,0,0],[0,1,1,1],[1,1,1,1]]
matrix6 = [[1,0,0,0],[1,0,0,0],[1,1,1,1],[1,1,1,1]]
matrix7 = [[1,1,1,1],[0,0,0,1],[0,0,1,0],[0,0,1,0]]
matrix8 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
matrix9 = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[0,0,0,1]]
matrix0 = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
colon = [[0,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]


matrix = [matrix0,matrix1,matrix2,matrix3,matrix4,matrix5,matrix6,matrix7,matrix8,matrix9]

buffer_width = 8

ln = ''

try:
    while 1:
        for row in range(0, 2):
            print ' '
        for row in range(0, 4):

            time_array = [time.strftime("%I", time.localtime())[0],time.strftime("%I", time.localtime())[1],time.strftime("%M", time.localtime())[0],time.strftime("%M", time.localtime())[1]]

            line = ''
            for col in range(0,buffer_width):
                line = line + ' '

            for digit in range(0,4):
                for col in range(0,4):
                    if matrix[int(time_array[digit])][row][col] == 1:
                        line = line + '*'
                    else:
                        line = line + ' '
                line = line + '  '
                if digit == 1:
                    for colon_col in range (0,4):
                        if colon[row][colon_col] == 1:
                            line = line + '*'
                        else:
                            line = line + ' '
                    line = line + '  '
            print line
        
        #\x1b[7m
        time.sleep(60)
        os.system('clear')
except (KeyboardInterrupt):
    pass