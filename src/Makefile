##
# @file     Makefile
# @brief    Makefile for WaterLift Calculator
# @author   MARKO KUBRACHENKO   (xkubra00)
# @date     2021-04-24

.PHONY: all init pack folder clean test doc run profile install

PYTHON = python3
SUDO = sudo apt-get
TEAM = IVS_BHitW
LOGIN = xshili00_xbenes58_xbrazd22_xkubra00
REPOSITORY = https://github.com/Jekwwer/IVS_BHitW.git
INSTALL_FILES := $(filter-out tests.py, $(wildcard *.py))
MATH_FILES = math_lib.py tests.py

# cannot compile python
all: init

# installs everything required to run the calculator
init:
	$(SUDO) update
	$(SUDO) install $(PYTHON)
	$(SUDO) install $(PYTHON)-tk
	$(SUDO) install $(PYTHON)-pip
	$(PIP)  install tkDocViewer

# packs the project so it can be submitted
pack: folder
	cd ../.. && zip -r $(LOGIN).zip $(LOGIN)
	cd ../.. && rm -rf $(LOGIN)

# creates a folder to be zipped
folder: doc install clean
	mkdir ../../$(LOGIN) && cd ../../$(LOGIN) && git clone $(REPOSITORY) && mv IVS_BHitW repo
	cp -a ../doc ../../$(LOGIN)/ && rm -rf ../doc
	cp -a ../install ../../$(LOGIN)/ && rm -rf ../install/*.deb

# deletes all the files that should not be submitted
clean:
	rm -rf __pycache__

# runs tests of the math library
test: $(MATH_FILES)
	$(PYTHON) tests.py

# starts documentation generating
doc: Doxyfile
	$(SUDO) install doxygen
	rm -rf ../doc
	doxygen Doxyfile

# runs the application
run: gui.py
	$(PYTHON) gui.py

# runs profiling
profile: profiling.py
	chmod +x profiling.py
	./profiling.py

# creates a deb file
install: $(INSTALL_FILES)
	rm -rf ../install/*.deb
	bash install.sh
