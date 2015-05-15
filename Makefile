# Jan Wuyts 20120730 (c) Pronota NV
#
.PHONY: pdf docx all clean

RST2PDF=/Users/jan/dev_python/IT8_epd/bin/rst2pdf
PANDOC=/home/jan/.cabal/bin/pandoc

all: docx html

html:  $(notdir $(patsubst %.markdown,%.html,$(wildcard ./*.markdown)))

docx:  $(notdir $(patsubst %.markdown,%.docx,$(wildcard ./*.markdown)))

plain:  $(notdir $(patsubst %.markdown,%.txt,$(wildcard ./*.markdown)))

clean:
	rm -f *.html
	rm -f *.docx
	rm -f *.txt

%.html: %.markdown
	$(PANDOC) -f markdown -t html -o $@ $< 

%.docx: %.markdown
	$(PANDOC) -f markdown -t docx -o $@ $< 

%.txt: %.markdown
	$(PANDOC) -f markdown -t plain -o $@ $< 

