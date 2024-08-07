## PDF Manipulation Scripts

This repository contains Python scripts for manipulating PDF files. The available functionalities include rotating pages, merging multiple PDFs, and adding watermarks to PDFs.

## PDF Rotation

This script rotates the first page of a PDF file and saves it as a new PDF.

You can install the PyPDF2 library using pip: pip install PyPDF2==1.26

## Usage
Place your PDF file (dummy.pdf) in the working directory.
Run the script to rotate the first page of the PDF: python pdf_rotation.py

-----------------------------------------------------------------------------

## PDF Merger
This script merges multiple PDF files into a single PDF. You can install the PyPDF2 library using pip: pip install PyPDF2==1.26

## Usage
Place the PDF files you want to merge in the working directory.
Run the script with the PDF file names as command-line arguments: python pdf_merger.py dummy.pdf dummy2.pdf dummy3.pdf

-----------------------------------------------------------------------------

## PDF Watermarking

This script adds a watermark to each page of a PDF file. You can install the PyPDF2 library using pip: pip install PyPDF2==1.26

## Usage
Place your PDF files (super.pdf and wtr.pdf) in the working directory.
Run the script to add a watermark: python pdf_watermark.py

##  Made by Nishant Acharekar, under Course of Complete Python Developer 2024 by ZTM on Udemy
