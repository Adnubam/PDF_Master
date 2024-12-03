#-
#Collection of procedures and Functions to perfom some basic actions over pdf files, please read readme.md for more details!
#Tested on python 3.11.4, PyPDF2 Version 3.0.0
#Script by Ronaldo Mabunda (Mathematician, Software emgineer and Data Analyst)
#March, 2024.

import os
import sys
from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

#rotate a single pdf file
def rotate(path, angle):

    counter = 0
    pdf_writer = PdfWriter()

    #try:
    with open(path, "rb") as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            counter += 1
            pdf_writer.add_page(page.rotate(int(angle)))
            print(f"processing file {basename(path)} {round(counter/len(pdf_reader.pages)*100,2)}%")

        #Checks if the output directory exists, if not, creates!
        check_output_dirr(output_dirr(path))

        save_output(os.path.join(output_dirr(path), basename(path)), pdf_writer)

        print("Rotated.")
    #except Exception as e:
    #   print(e)
        
    #    print("An issue occured reading the file!")
        
#rotate a set of pdf files in a directory
def rotate_files(directory, angle):
    try:
        for file in os.listdir(directory):
            if ".pdf" in file:
                rotate(join_dirr(directory, file), angle)
    except:
        print("Invalid Directory!")
        
#merge a set of pdf files in a directory
def merge_files(directory):

    merger = PdfWriter()

    for file in os.listdir(directory):
        if ".pdf" in file:
            merger.append(join_dirr(directory, file))

    check_output_dirr(directory)

    save_output(join_dirr(output_dirr(directory), "merged-file.pdf"), merger)

#split a pdf file in predefined/specifed pages
def split(path, pages):
    pass
#extract page or a set of pages from a given pdf file
def extract(path, rang_e):
    pass
#scale the pdf file (canvas)
def scale(path, factor):
    pass

#scale the content of a given pdf file

def scale_content(path, factor):

    transform = Transformation().scale(sx = factor, sy = factor)

    try:
        with open(path, "rb") as file:
            pdf_reader = PdfReader(file)
            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                page.add_transformation(transform)
                pdf_writer.add_page(page)

            with open(os.path.join(os.path.dirname(path), "scaled" + os.path.basename(path)),"wb") as output:
                pdf_writer.write(output)
            print("successfully!")
    except:
         print("An issue occured reading the file!")
         
#resize an A_n pdf file to A4
def resize_an_to_a4(path):
    pass
#resize a list of A_n pdf files in a directory to A4
def resize_list_an_to_a4(directory):
    pass
#resize a letter size pdf file to A4
def resize_letter_to_a4(path):
    pass
#resize a list of letter size pdf files to A4
def resize_list_letter_to_a4(directory):
    pass
#group each two following pages of a pdf file into one
def dndt(directory):
    pass
#format dndt system generrated file names
def format_dndt_string(directory):
    pass

#SOME AUXILIAR FUNCTIONS

#Ask the path of a file to eventually perfom an action
def ask_path():
    return input("Introduce the path: ")

#Ask a directory to eventually perfom an action on files into it
def ask_dirr():
    return input("Introduce the directory: ")

#Saves the output pdf_writer file in the output folder
def save_output(path, pdf_writer_object):
    with open(path, "wb") as output:
        pdf_writer_object.write(output)

#checks if the output folder already exists, if not, creates!
def check_output_dirr(path):
    print(output_dirr(path))
    if not os.path.exists(output_dirr(path)):
        os.mkdir(output_dirr(path))

#returns the output directory, accordingly to the path or directory given
def output_dirr(path):
    if os.path.isfile(path):
        output_path = os.path.join(os.path.dirname(path), "Output PDFs")
    elif os.path.isdir(path):
        output_path = os.path.join(path, "Output PDFs")
    else:
        pass
        #raise
    return output_path

#returns the basename of a path, i.e., the last name in the path
def basename(path):
    return os.path.basename(path)

#A shortcut for os.path.join
def join_dirr(dirr1, dirr2):
    return os.path.join(dirr1, dirr2)

#Checks if a given path or dirr exists, and if yes, whether it's a dirr or a path.
def isfile_or_isdirr(path):
    if os.path.isdir(path):
        print("Isdirr.")
    elif os.path.isfile(path):
        print("Isfile.")
    else:
        print("Non of them.")

#EXECUTION STARTS HERE

arg = sys.argv

#print(output_dirr(ask_path()))
#print(os.path.dirname(input("dirr: ")))
#print(isfile_or_isdirr(ask_path()))

if arg[-1] != arg[0]:
    match arg[1]:
        case "rotate":
            path = ask_path()
            angle = float(input("Introduce the Angle: "))
            rotate(path, angle)

        case "rotate_files":
            dirr = ask_dirr()
            angle = float(input("Introduce the Angle: "))
            rotate_files(dirr, angle)

        case "merge_files":
            dirr = ask_dirr()
            merge_files(dirr)
print("Done!")