SOURCE_DIR = src
TESTS_DIR = tests
OUTPUT_DIR = output
SOURCE_FILE = $(TESTS_DIR)/test_file.py
OUTPUT_DOT = $(OUTPUT_DIR)/output.dot
OUTPUT_PNG = $(OUTPUT_DIR)/output.png

.PHONY: all
all: visualize

.PHONY: visualize
visualize: $(OUTPUT_PNG)

$(OUTPUT_PNG): $(OUTPUT_DOT)
	dot -Tpng $(OUTPUT_DOT) -o $(OUTPUT_PNG)

$(OUTPUT_DOT): $(SOURCE_FILE)
	python $(SOURCE_DIR)/ast_to_dot.py $(SOURCE_FILE) > $(OUTPUT_DOT)

.PHONY: clean
clean:
	rm -f $(OUTPUT_DOT) $(OUTPUT_PNG)