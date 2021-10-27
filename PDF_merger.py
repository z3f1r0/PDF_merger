# this script merges in one unique file all pdf files that there are in working directory
from os import listdir
import PyPDF2
import os

# list of files and directory in the working directory
listFiles = listdir()

# open a pdf file for writing to merge in all others
print("How do you want to call your PDF file?\nRemember to add the '.pdf' extension")
nameFileDestination = input() # name of final pdf file
PDF_Destination = open(nameFileDestination, "wb")  # w=write, b=binary
merger = PyPDF2.PdfFileMerger() # this is a merger for all pdf files

for nameFile in listFiles:
    if nameFile.endswith(".pdf"): # choose only pdf file extension
        pdfFile = open(nameFile, "rb")  # r=read, b=binary
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        pdfFile.close()

merger.write(PDF_Destination)
PDF_Destination.close()




















