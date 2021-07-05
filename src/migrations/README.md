Alembic code folder was generated with the following commands:

```
make venv-bash
cd src/
alembic init migrations
```

Then `migrations/env.py` was updated to load SQL Alchemy model code and db connection info.
