# Organization API

REST API для управления справочником организаций, зданий и деятельностей.

## Запуск приложения

### Локальный запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Создайте файл `.env` на основе `.env.example` и настройте переменные окружения:
   ```bash
   cp .env.example .env
   ```

3. Примените миграции:
   ```bash
   alembic upgrade head
   ```

4. Запустите приложение:
   ```bash
   uvicorn app.main:app --reload
   ```

### Запуск с Docker

1. Соберите и запустите контейнеры с помощью Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Приложение будет доступно по адресу: http://localhost:8000

## API Документация

После запуска приложения документация будет доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Аутентификация

Все запросы требуют API ключ в заголовке:
```
X-API-KEY: secret-key
```

## Endpoints

### Здания
- `GET /buildings/` - Список всех зданий
- `POST /buildings/` - Создать здание
- `GET /buildings/{building_id}` - Получить здание по ID

### Деятельности
- `GET /activities/` - Список всех деятельностей
- `POST /activities/` - Создать деятельность
- `GET /activities/{activity_id}` - Получить деятельность по ID
- `GET /activities/tree/{activity_id}` - Получить дерево деятельности

### Организации
- `GET /organizations/` - Список всех организаций
- `POST /organizations/` - Создать организацию
- `GET /organizations/{organization_id}` - Получить организацию по ID
- `GET /organizations/by_building/{building_id}` - Организации в здании
- `GET /organizations/by_activity/{activity_id}` - Организации по деятельности (включая дочерние)
- `GET /organizations/by_name/{name}` - Поиск организаций по названию
- `GET /organizations/in_radius/` - Организации в радиусе (параметры: latitude, longitude, radius_km)
