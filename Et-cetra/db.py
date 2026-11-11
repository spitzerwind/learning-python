"""SQLite persistence helpers for a desktop habit tracker."""

from contextlib import closing
import sqlite3
from pathlib import Path
from typing import Any


DB_PATH = Path(__file__).with_name("habits.db")


def get_connection() -> sqlite3.Connection:
    """Open the local database and return rows with named-column access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the habits table if it does not already exist."""
    with closing(get_connection()) as conn:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    xp_reward INTEGER DEFAULT 10,
                    is_completed INTEGER DEFAULT 0
                )
                """
            )


def add_habit(name: str, category: str, xp_reward: int = 10) -> int:
    """Insert a habit and return its new id."""
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(
                "INSERT INTO habits (name, category, xp_reward) VALUES (?, ?, ?)",
                (name, category, xp_reward),
            )
            return int(cursor.lastrowid)


def get_all_habits() -> list[dict[str, Any]]:
    """Return every habit as a list of dictionaries."""
    with closing(get_connection()) as conn:
        rows = conn.execute(
            "SELECT id, name, category, xp_reward, is_completed FROM habits ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


def mark_habit_completed(habit_id: int) -> bool:
    """Mark a habit complete; return whether a matching row was found."""
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(
                "UPDATE habits SET is_completed = 1 WHERE id = ?", (habit_id,)
            )
            return cursor.rowcount > 0


def delete_habit(habit_id: int) -> bool:
    """Delete a habit; return whether a matching row was found."""
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
            return cursor.rowcount > 0


if __name__ == "__main__":
    init_db()

    # Even text containing SQL-looking characters is handled as ordinary data.
    sample_id = add_habit("Drink water; DROP TABLE habits; --", "Health")
    print(f"Added sample habit with id {sample_id}.")
    print("All habits:")
    for habit in get_all_habits():
        print(habit)
