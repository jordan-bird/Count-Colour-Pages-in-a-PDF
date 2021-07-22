# Count Colour Pages in a PDF

A small script to count colour and B/W pages in a PDF file. Useful for calculating printing costs for large documents.

## Requirements
pdf2image

NumPy

## Usage
```
python count-pages.py filename
```
or
```
python count-pages.py filename.pdf
```

## Sample output
```
python count-pages.py test
Counting Colour/BW pages in: test.pdf
Converting PDF to images...
Done.
Total number of pages: 8
Counting B/W and colour pages...
Analysing page 8/8

B/W: 3
Colour: 5
```
