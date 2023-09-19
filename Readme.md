### Работа с миграциями

#### Инициализации миграций
```
alembic init migrations
```

#### Запуск миграций
```
alembic revision --autogenerate -m "migration_name"
```

#### Миграция
```
alembic upgrade *migration hash*
```
Взять хэш можно из migration/versions/migration_name
