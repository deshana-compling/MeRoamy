import sqlite3

DB = 'meroamy_packages.db'

def create_database():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS packages (
        id INTEGER PRIMARY KEY,
        name TEXT,
        destination TEXT,
        country TEXT,
        duration_days INTEGER,
        includes TEXT,
        price INTEGER,
        tourist_spots TEXT)
    """)

    packages = [
        ('Lavish Lakshwadeep', 'Lakshwadeep Islands, India','India', 8, 
        'Cruise Hotel, meals, resort tickets', 699, 'Agatti Island, Bangaram Island, Kavaratti'),
        
        ('Paris Explorer', 'Paris, France','France', 5,
        'Hotel, meals, city tour', 899, 'Eiffel Tower, Louvre Museum, Montmartre'),
        
        ('Japan Jewels', 'Tokyo, Kyoto, Osaka','Japan', 10,
        'Hotels, meals, railpass', 2199, 'Shibuya, Fushimi Inari Shrine, Arashiyama, Osaka Castle'),
        
        ('Bali Escape', 'Bali, Indonesia','Indonesia', 6,
        'Hotel, meals, airport transfer, resort tickets', 799, 'Uluwatu Temple, Ubud, Tegallalang Rice Terrace')
        ]

    cursor.executemany("""
    INSERT INTO packages (name, destination, country, duration_days, includes, price, tourist_spots)
    VALUES(?, ?, ?, ?, ?, ?, ?)""", packages)

    conn.commit()
    cursor.execute("SELECT * FROM packages")
    for row in cursor.fetchall():
        print(row)
    conn.close()

#Function used by the AI assistant

def search_packages(place):
    print(f"DATABASE TOOL CALLED. Searching {place}", flush=True)

    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name, destination, country, duration_days, includes, price, tourist_spots
            FROM packages
            WHERE destination LIKE ?
            OR country LIKE ?
            OR tourist_spots LIKE ?
            """, (f'%{place}%', f'%{place}%', f'%{place}%')
        )
    results = cursor.fetchall()
    if results:
        return results
    else:
        return 'No packages found for this destination'
