import sqlite3
import pandas as pd
import os
from pathlib import Path

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos SQLite en la raíz del proyecto
    """
    # Ruta SIMPLE - la base de datos en la raíz
    db_path = 'tfm_database.db'
    
    # VERIFICACIÓN simple
    print(f"📍 Conectando a: {os.path.abspath(db_path)}")
    print(f"📍 ¿Existe el archivo? {os.path.exists(db_path)}")
        
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        print("✅ Conexión a la BD SQLite exitosa.")
        return conn
    except Exception as e:
        print(f"❌ Error conectando a la BD SQLite: {e}")
        raise

def insert_dataframe_to_table(df, table_name, conn):
    """
    Inserta un DataFrame de pandas en una tabla de SQLite.
    """
    try:
        # Primero verificar si la tabla existe
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = cursor.fetchone() is not None
        
        if not table_exists:
            print(f"❌ La tabla '{table_name}' no existe en la base de datos")
            return 0
        
        # Contar registros antes de insertar
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count_before = cursor.fetchone()[0]
        
        # Insertar datos
        df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
        
        # Contar registros después de insertar
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count_after = cursor.fetchone()[0]
        
        rows_inserted = count_after - count_before
        print(f"✅ {rows_inserted} filas insertadas en la tabla '{table_name}'.")
        return rows_inserted
        
    except Exception as e:
        print(f"❌ Error insertando datos en {table_name}: {e}")
        raise

def get_table_as_dataframe(table_name, conn):
    """
    Lee una tabla de SQLite y la devuelve como un DataFrame de pandas.
    """
    query = f"SELECT * FROM {table_name}"
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"❌ Error leyendo la tabla {table_name}: {e}")
        raise