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
  '1':'Física',
  '2':'Matemáticas',
  '3':'Química',
  '4':'Biología',
  '5':'Educación Física',
  '6':'Castellano',
  '7':'F.S.N.',
  '8':'Inglés',
  '9':'G.H.C.',
  '10':'Ciencias de la Tierra',
  '11':'Grupo (Electiva)',
}


def dates_for_task(materias):
  print('---------- Creating Tasks ----------')
  for k, v in materias.items():
    if len(k) != 1:
      print(k, '-', v)
    else:
      print(k, '-' * 2, v)
  materia = input('Ingrese el número de la Materia: ')
  tipo_tarea = input('Ingrese el tipo de Tarea: ')
  fecha_entrega = input('Siguiendo el formato DD/MM/AAAA. Ingrese la fecha de entrega: ')
  for k, v in materias.items():
    list_k = list(k)
    k = ''.join(list_k)
    if materia == k:
      print('materia valida', v)


crear_task = input('¿Desea crear una tarea?: ')
while crear_task.lower() == 'si':
  print(dates_for_task(materias))
  crear_task = input('¿Desea crear una tarea?: ')

conexion.commit()
conexion.close()