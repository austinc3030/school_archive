# Makefile for LaTeX document files
# Created by Boyang Wang, xd.bywang@gmail.com, Oct. 10, 2012, Logan, Utah
# Last Modified: Oct. 10, 2012, now can embed all the fonts in pdf.

DOCUMENT=main

default: $(DOCUMENT).pdf
#default: $(DOCUMENT).ps

$(DOCUMENT).toc: $(DOCUMENT).tex
	latex $(DOCUMENT).tex

$(DOCUMENT).dvi: $(DOCUMENT).toc
	bibtex $(DOCUMENT)
	latex $(DOCUMENT).tex
	latex $(DOCUMENT).tex

$(DOCUMENT).ps: $(DOCUMENT).dvi
	dvips -Ppdf -G0 -tletter $(DOCUMENT).dvi

# $(DOCUMENT).ps: $(DOCUMENT).dvi
#	dvips -t letter -Ppdf -G0 -o $@ $<	

$(DOCUMENT).pdf: $(DOCUMENT).ps
	ps2pdf -dCompatibilityLevel=1.4 -dEmbedAllFonts=true -dPDFSETTINGS=/prepress $(DOCUMENT).ps $(DOCUMENT).pdf

#$(DOCUMENT).pdf: $(DOCUMENT).ps
#	cat $(DOCUMENT).ps | ps2pdf - > $(DOCUMENT).pdf 

all: $(DOCUMENT).pdf

clean:
	rm -rf *.aux $(DOCUMENT).log $(DOCUMENT).toc \
    $(DOCUMENT).ps $(DOCUMENT).blg figs/*.fig.bak *.bbl *.blg *.dvi *.tex.bak *.synctex
