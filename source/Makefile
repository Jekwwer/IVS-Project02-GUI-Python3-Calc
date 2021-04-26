##
# @file     Makefile
# @brief    Makefile for WaterLift Calculator
# @author   MARKO KUBRACHENKO   (xkubra00)
# @date     2021-04-24

.PHONY: all pack clean test doc run profile

PYTHON = python3
SUDO = sudo apt-get
TEAM = xshili00_xbenes58_xbrazd22_xkubra00
PYTHON_FILES := $(wildcard *.py)
MATH_FILES = math_lib.py tests.py

# cannot compile python
all: init

# installs everything required to run the calculator
init:
	$(SUDO) update
	$(SUDO) install $(PYTHON)
	$(SUDO) install $(PYTHON)-tk

# packs the project so it can be submitted
pack: clean
	cd ../.. && zip -r $(TEAM).zip $(TEAM)

# deletes all the files that should not be submitted
clean:
	rm -rf documentation

# runs tests of the math library
test: $(MATH_FILES)
	$(PYTHON) tests.py

# starts documentation generating
doc: Doxyfile
	$(SUDO) install doxygen
	doxygen Doxyfile

# runs the application
run: gui.py
	$(PYTHON) gui.py

# runs profiling
profile: profiling.py
	chmod +x profiling.py
	./profiling.py
