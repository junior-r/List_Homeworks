import sqlite3

conexion = sqlite3.connect('Tareas.db')
cursor = conexion.cursor()

try:
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Lista (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      materia STRING,
      tipo_tarea STRING,
      fecha_entrega DATETIME
    )
  '''
  )
except sqlite3.OperationalError:
  pass

materias = {
  'Física': '1',
  'Matemáticas': '2',
  'Química': '3',
  'Biología': '4',
  'Educación Física': '5',
  'Castellano': '6',
  'F.S.N.': '7',
  'Inglés': '8',
  'G.H.C.': '9',
  'Ciencias de la Tierra': '10',
  'Grupo (Electiva)': '11',
}

conexion.commit()
conexion.close()