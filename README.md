## HW3

Импорт каталога сматрфонов в БД из CSV-файла:

```
python manage.py import_phones <название_приложения>
```

![](images/import_phones.png)

| URL                          | Описание                               |
|------------------------------|----------------------------------------|
| `/hw3/catalog/`              | Сортировка по ID                       |
| `/hw3/catalog/?sort=name`    | Сортировка по названию                 |
| `/hw3/catalog/?sort=price`   | Сортировка по цене (сначала недорогие) |
| `/hw3/catalog/?sort=-price`  | Сортировка по цене (сначала дорогие)   |
| `/hw3/catalog/<slug-phone>/` | Детальная информация                   |

![](images/catalog.gif)