# fonde in un solo file tutti i pdf trovati nella cartella di lavoro
from os import listdir
import PyPDF2
import os

# elenco di files e cartelle dentro la cartella di lavoro
listaFiles = listdir()


# apriamo in scrittura il file pdf in cui fondere gli altri
print("Come vuoi chiamare il tuo file PDF?\nRicordati di aggiungere l'estensione '.pdf'")
nomeFileDestinazione = input() # diciamo come chiamare il file definitivo
PDF_Destinazione = open(nomeFileDestinazione, "wb")  # w=write, b=binary
merger = PyPDF2.PdfFileMerger() # fa da cumulatore per un file pdf e, sotto nel ciclo for, aggiunge tutte le pagine di un file della lista

for nomeFile in listaFiles:
    if nomeFile.endswith(".pdf"): #sceglie solo i file con estensione .pdf
        pdfFile = open(nomeFile, "rb")  # r=read, b=binary
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        pdfFile.close()

merger.write(PDF_Destinazione)
PDF_Destinazione.close()




















