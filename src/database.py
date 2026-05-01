"""
RateLingo Database Module
Handles SQLite3 database setup and queries for quote history
"""

import sqlite3
from datetime import datetime

DB_NAME = 'ratelingo.db'

# ==================== Table Setup ====================
def create_tables():
    """Create necessary tables if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            service TEXT NOT NULL,
            word_count INTEGER NOT NULL,
            rate REAL NOT NULL,
            total_cost REAL NOT NULL,
            text_sample TEXT
        )
    """)

    conn.commit()
    conn.close()

# ==================== Quote Operations ====================
def save_quote(service, word_count, rate, total_cost, text_sample=""):
    """
    Save a calculated quote to the database

    Args:
        service (str): Service type
        word_count (int): Number of words
        rate (float): Rate per word
        total_cost (float): Total calculated cost
        text_sample (str): First 200 characters of the text
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO quotes (date, service, word_count, rate, total_cost, text_sample)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        service,
        word_count,
        rate,
        total_cost,
        text_sample
    ))

    conn.commit()
    conn.close()
    return True

def get_all_quotes():
    """
    Retrieve all saved quotes

    Returns:
        list: List of tuples (id, date, service, word_count, rate, total_cost, text_sample)
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM quotes ORDER BY date DESC")
    rows = cur.fetchall()

    conn.close()
    return rows

def get_quote_by_id(quote_id):
    """
    Retrieve a specific quote by ID

    Args:
        quote_id (int): Quote ID

    Returns:
        tuple: Quote record or None
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM quotes WHERE id=?", (quote_id,))
    result = cur.fetchone()

    conn.close()
    return result

def delete_quote(quote_id):
    """
    Delete a quote by ID

    Args:
        quote_id (int): Quote ID to delete
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM quotes WHERE id=?", (quote_id,))

    conn.commit()
    conn.close()
    return True

def get_quotes_by_service(service):
    """
    Retrieve all quotes for a specific service

    Args:
        service (str): Service type to filter by

    Returns:
        list: Filtered list of quote records
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM quotes WHERE service=? ORDER BY date DESC", (service,))
    rows = cur.fetchall()

    conn.close()
    return rows

def get_total_earnings():
    """
    Get total earnings from all saved quotes

    Returns:
        float: Total earnings across all quotes
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT SUM(total_cost) FROM quotes")
    result = cur.fetchone()[0]

    conn.close()
    return result or 0.0

def get_quote_count():
    """
    Get total number of saved quotes

    Returns:
        int: Total quote count
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM quotes")
    result = cur.fetchone()[0]

    conn.close()
    return result or 0