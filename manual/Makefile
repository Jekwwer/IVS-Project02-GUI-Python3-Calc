# Author:   Evgenii Shiliaev

MANUAL = dokumentace
MANUAL_FOR_HELP_WINDOW = manual_for_help_window

all: $(MANUAL).pdf $(MANUAL_FOR_HELP_WINDOW).pdf clean

$(MANUAL).pdf: $(MANUAL).tex
	latex $(MANUAL).tex
	latex $(MANUAL).tex
	dvips -t a5 $(MANUAL).dvi
	ps2pdf -sPAPERSIZE=a5 $(MANUAL).ps
	mv $(MANUAL).pdf ..

$(MANUAL_FOR_HELP_WINDOW).pdf: $(MANUAL_FOR_HELP_WINDOW).tex
	latex $(MANUAL_FOR_HELP_WINDOW).tex
	latex $(MANUAL_FOR_HELP_WINDOW).tex
	dvips -t a5 $(MANUAL_FOR_HELP_WINDOW).dvi
	ps2pdf -sPAPERSIZE=a5 $(MANUAL_FOR_HELP_WINDOW).ps
	mv $(MANUAL_FOR_HELP_WINDOW).pdf ../src

.PHONY: clean

clean:
	rm -f *.aux
	rm -f *.dvi
	rm -f *.log
	rm -f *.ps
	rm -f *.out
	rm -f *.toc