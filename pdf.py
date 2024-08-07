#pip install PyPDF2==1.26

#import PyPDF2
#rb is read binary
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file) 
#     page = reader.getPage(0)
#     # print(reader.numPages)
#     print(page.extractText())
#     # print(page.rotateClockwise(90))
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

#---------------------------------------------
    #pdf merger
# import PyPDF2
# import sys

# inputs = sys.argv[1:] 

# def pdf_merger(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('super.pdf')
#     print('all done!')
    
# pdf_merger(inputs)
#run this code in terminal

#python3 pdf.py dummy.pdf dummy2.pdf dummy3.pdf

#---------------------------------------------

#pdf watermark

import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.merge_page(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
