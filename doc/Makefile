# Autor:   Evgenii Shiliaev

OUTPUT = manual

all: $(OUTPUT).pdf clean

$(OUTPUT).pdf: *.tex
	latex *.tex
	latex *.tex
	dvips -t a4 *.dvi
	ps2pdf -sPAPERSIZE=a4 *.ps
	
.PHONY: clean
clean:
	rm -f *.aux
	rm -f *.dvi
	rm -f *.log
	rm -f *.ps	
