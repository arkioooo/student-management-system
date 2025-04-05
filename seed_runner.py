from db import DatabaseManager

db = DatabaseManager()

try:
    db.connect()
    
    # ✅ Fix: Open file with UTF-8 encoding
    with open("seed_data.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()
        db.cursor.execute(sql_script)
        db.connection.commit()
        print("✅ Seed data loaded successfully.")
except Exception as e:
    print(f"❌ Error loading seed data: {e}")
finally:
    db.close()
