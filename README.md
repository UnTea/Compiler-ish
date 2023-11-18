# AST to Graphviz

Этот проект представляет собой инструмент для преобразования абстрактного синтаксического дерева (AST) кода на Python в графовое представление с использованием Graphviz. Проект также включает Makefile для удобного билдирования и визуализации.

## How to use

1. Установите Graphviz: [Graphviz](https://www.graphviz.org/download/) (убедитесь, что у вас установлен Graphviz, и утилита `dot` находится в вашем `PATH`).

2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your_username/ast-to-graphviz.git
    cd ast-to-graphviz
    ```

3. Создайте и активируйте виртуальное окружение (опционально):

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    venv\Scripts\activate  # для Windows
    ```

4. Запустите [make](https://www.gnu.org/software/make/) для генерации графового представления AST и визуализации:

    ```bash
    make
    ```

   Это создаст файлы `output.dot` и `output.png` в папке `output`.

5. Чтобы очистить сгенерированные файлы, выполните:

    ```bash
    make clean
    ```

## Структура проекта

- `src`: Исходный код, включая скрипт `ast_to_dot.py`.
- `tests`: Тестовые файлы, например, `test_file.py`.
- `output`: Сгенерированные файлы, такие как `output.dot` и `output.png`.
- `Makefile`: Файл для автоматизации процесса генерации и визуализации.

## Зависимости

- Python 3.x
- Утилита [Graphviz](https://www.graphviz.org/download/)
- Утилита [make](https://www.gnu.org/software/make/)