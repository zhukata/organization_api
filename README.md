# Organization API

REST API для управления справочником организаций, зданий и деятельностей.

## Запуск

1. Склонируйте проект:
   ```bash
   git clone https://github.com/zhukata/organization_api.git
   ```

2. Создайте файл `.env` на основе `.env.example`:
   ```bash
   cp .env.example .env
   ```

3. Соберите и запустите контейнеры:
   ```bash
   docker compose up --build
   ```

Приложение будет доступно по адресу: http://localhost:8000

4. Запустите проверку функциональности:
   ```bash
   python check_functionality.py
   ```

## API Документация

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
