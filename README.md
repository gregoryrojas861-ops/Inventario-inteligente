# Migraciones

Este proyecto está preparado para Alembic.

Inicializa Alembic si deseas generar migraciones controladas:

```bash
alembic init migrations
```

Después configura `alembic.ini` y `migrations/env.py` para importar `Base.metadata` desde `database.database`.

Ejemplo:

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```
