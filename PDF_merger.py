# this script merges in one unique file all pdf files that there are in working directory
from os import listdir
import PyPDF2
import os

# list of files and directory in the working directory
listaFiles = listdir()

# open a pdf file for writing to merge in all others
print("Come vuoi chiamare il tuo file PDF?\nRicordati di aggiungere l'estensione '.pdf'")
nomeFileDestinazione = input() # name of final pdf file
PDF_Destinazione = open(nomeFileDestinazione, "wb")  # w=write, b=binary
merger = PyPDF2.PdfFileMerger() # this is a merger for all pdf files

for nomeFile in listaFiles:
    if nomeFile.endswith(".pdf"): # choose only pdf file extension
        pdfFile = open(nomeFile, "rb")  # r=read, b=binary
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        pdfFile.close()

merger.write(PDF_Destinazione)
PDF_Destinazione.close()




















