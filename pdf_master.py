#-
#Collection of procedures and Functions to perfom some basic actions over pdf files, please read readme.md for more details!
#Tested on python 3.11.4, PyPDF2 Version 3.0.0
#Script by Ronaldo Mabunda (Mathematician, Software Developer and Data Analyst)
#March, 2024.

import os
import sys
from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

#rotate a single pdf file
def rotate(path, angle):

    counter = 0
    pdf_writer = PdfWriter()

    try:
        with open(path, "rb") as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                counter += 1
                pdf_writer.add_page(page.rotate(int(angle)))
                print(f"processing file {basename(path)} {round(counter/len(pdf_reader.pages)*100,2)}%")

            #Saves the Output file! (join_dir, dirname and basename defined further in the code)
            save_output(join_dir(dirname(path), "rotated - " + basename(path)), pdf_writer)

            print("File Rotated.")
    except:
        print("An issue occured finishing the task!")
        
#merge a set of pdf files in a directory
def merge_files(directory):

    merger = PdfWriter()

    for file in os.listdir(directory):
        if ".pdf" in file:
            merger.append(join_dir(directory, file))

    #saving the output file
    save_output(join_dir(directory, "Merged-File.pdf"), merger)

    print("Files Merged!")

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

            save_output(join_dir(dirname(path), "Scaled - " + basename(path)), pdf_writer)

            
            print("Content File Scaled!")
    except:
         print("An issue occured finishing the task!")
         
#resize an A_3 pdf file to A4
def resize_an_to_a4(path):
    pass

#resize a letter size pdf file to A4
def resize_letter_to_a4(path):
    pass

#SOME AUXILIAR FUNCTIONS

#Ask the path of a file to eventually perfom an action
def ask_path():
    return input("Introduce the path: ")

#Ask the directory of a file to eventually perfom an action
def ask_dir():
    return input("Introduce the directory: ")

#Saves the output pdf_writer file in the output folder
def save_output(path, pdf_writer_object):
    with open(path, "wb") as output:
        pdf_writer_object.write(output)

#returns the basename of a path, i.e., the last name in the path
def basename(path):
    return os.path.basename(path)

#returns the basename of a path, i.e., the last name in the path
def dirname(path):
    return os.path.dirname(path)

#A shortcut for os.path.join
def join_dir(dirr1, dirr2):
    return os.path.join(dirr1, dirr2)

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

        case "merge":
            dirr = ask_dir()
            merge_files(dirr)
        
        case "split":
            pass

        case "extract":
            pass

        case "scale":
            pass

        case "scale-content":
            path = ask_path()
            factor = float(input("Introduce the Factor: "))
            scale_content(path, factor)

        case "a3_to_a4":
            pass

        case "letter_to_a4":
            pass
print("Done!")