# Form Template Matcher

## Установка

```bash
pip install -r requirements.txt
```

## Структура команды

```bash
python app.py get_tpl --kv ключ=значение ключ=значение ...
```

## Пример

```bash
python app.py get_tpl --kv f_name1=vasya@pukin.ru f_name2=27.05.2025
```

Ответ:

```
Проба
```

Если не найдено:

```json
{
  "f_name1": "email",
  "f_name2": "date"
}
```

## Тесты

```bash
pytest
```
