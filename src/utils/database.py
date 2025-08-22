import sqlite3
import pandas as pd
import os

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos SQLite.
    La ruta a la BD ahora es relativa al proyecto.
    """
    # Navega dos niveles arriba desde 'src/utils' para llegar a la raíz del proyecto
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    db_path = os.path.join(project_root, 'tfm_database.db')
    
    try:
        conn = sqlite3.connect(db_path)
        # Habilitar claves foráneas
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
        # Usar el método de pandas 'to_sql' que es muy eficiente para SQLite
        df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
        print(f"✅ Datos insertados en la tabla '{table_name}'.")
    except Exception as e:
        print(f"❌ Error insertando datos en {table_name}: {e}")
        raise

# Función útil para leer datos de una tabla y convertirlos en un DataFrame
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