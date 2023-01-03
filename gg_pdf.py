import PyPDF2
import sys

def main(pdf_name):
    pdfFile = open(pdf_name,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    original_stdout = sys.stdout
    with open('./MFL.txt','w') as f:
        sys.stdout = f
        pages=pdfReader.numPages
        for i in range(1,pages):
            pageObj = pdfReader.getPage(i)
            print("Page No: ",i+1)
            text = pageObj.extractText().split("  ")
            for i in range(len(text)):
                print(text[i],end="\n\n")
            print()
        pdfFile.close()
        sys.stdout = original_stdout

if __name__ == '__main__':
    main()
