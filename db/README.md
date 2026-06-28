# Legion LLM Gateway Demo Database

The SQL files are MariaDB-ready and provide schema plus sample fixtures for local evaluation.

```bash
mariadb -u root -p -e "CREATE DATABASE legion_gateway;"
mariadb -u root -p legion_gateway < db/schema.sql
mariadb -u root -p legion_gateway < db/seed_demo.sql
```

To reset the demo database:

```bash
mariadb -u root -p legion_gateway < db/reset_demo_database.sql
```

The backend tests do not require MariaDB. Leave `ENABLE_DATABASE=false` to use read-only sample data and in-memory runtime state.
