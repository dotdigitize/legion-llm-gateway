from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from app.config import get_settings


def database_enabled() -> bool:
    return get_settings().enable_database


@contextmanager
def sqlite_connection() -> Iterator[sqlite3.Connection | None]:
    settings = get_settings()
    if not settings.enable_database:
        yield None
        return

    db_path = settings.database_url.removeprefix("sqlite:///")
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
