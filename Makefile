.ONESHELL:

SOURCE_DIR = src
OUTPUT_DIR = output
SOURCE_FILE = $(SOURCE_DIR)/test_file.py
OUTPUT_DOT = $(OUTPUT_DIR)/output.dot
OUTPUT_PNG = $(OUTPUT_DIR)/output.png

.PHONY: visualize
visualize: $(OUTPUT_PNG)

$(OUTPUT_PNG): $(OUTPUT_DOT)
	dot -Tpng $(OUTPUT_DOT) -o $(OUTPUT_PNG)

$(OUTPUT_DOT): $(SOURCE_FILE)
	python $(SOURCE_DIR)/main.py $(SOURCE_FILE) > $(OUTPUT_DOT)

.PHONY: clean
clean:
	rm -f $(OUTPUT_DOT) $(OUTPUT_PNG)

.PHONY:  all
all: clean visualize