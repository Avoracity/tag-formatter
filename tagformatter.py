# -*- coding: utf-8 -*-
"""
/****************************************************************************************************************************
File         : tagformatter.py
Author       : Michael Alvarez
Version      : [Spyder: Python 3.8]
Date         : 2021-08-02
****************************************************************************************************************************/
"""


def tag_formatter():
    file_name = input("Type the name of the file to have formatted tags : ")
    begin_line = input("Type the specified tag without it's brackets (i.e. body ) : ")
    end_line = "</{}>".format(begin_line)
    new_format = '<'+begin_line+'>'+"{}"+end_line # to avoid having the brackets at the end of the line for formatting, a variable is made
    # with open _ as _ ensures the file is closed after use, avoiding memory leaks..
    with open(file_name+".txt", "r") as tag_file:
        lines = tag_file.readlines()

        for line in lines:      
            print(new_format.format(line.strip())) #.strip() removes leading and trailing whitespaces
tag_formatter()


