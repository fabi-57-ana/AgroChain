import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Cargar variables del archivo .env
load_dotenv()


# Variables de conexión
usuario = "root"
password = os.getenv("MYSQL_ROOT_PASSWORD")
host = os.getenv("MYSQL_HOST")
puerto = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DATABASE")


# Crear conexión SQLAlchemy
conexion = create_engine(
    f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{database}"
)


def obtener_conexion():
    """
    Devuelve una conexión activa hacia MySQL.
    """
    return conexion