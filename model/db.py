import sqlite3

FILE_DB = './database/consultoria.db'


def connect():
    """Cria a conexão com o arquivo 
    do bando de dados"""
    conn = sqlite3.connect(FILE_DB)
    return conn
