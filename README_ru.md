# Anki Deck Generator

## Установка
После клонирования репозитория, выполните:

```bash
make init
```

Это создаст виртуальное окружение в директории `.venv` и установит туда все зависимости проекта.

## Использование
Перед использованием создайте пустую колоду в Anki и экспортируйте ее. Замените расширение файла с `.apkg` на `.zip` и распакуйте. Потребуется только файл `.anki2`, который был в архиве. Далее запустите скрипт:

```bash
python3 main.py <путь_до_файла.anki2> Goethe_A1_SD1_Wortliste.csv -n Goethe_A1 -o DEMO_Goethe_A1
```

Это создаст колоду с именем "Goethe_A1" в файле DEMO_Goethe_A1.apkg, который можно импортировать в Anki. Более подробная справка по запуску:

```bash
> python3 main.py --help
Usage: main.py [OPTIONS] INPUT_COLLECTION_PATH WORDS_CSV_PATH

Options:
  -n, --name TEXT    Name of the created deck in collection  [required]
  -o, --output TEXT  Filename to export new Anki collection to
  --help             Show this message and exit.
```

Для работы скрипта также тредуется переменная окружения `YANDEX_API_KEY` с API ключом, подробнее в [документации](https://cloud.yandex.ru/ru/docs/iam/operations/api-key/create).