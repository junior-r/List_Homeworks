import sqlite3

conexion = sqlite3.connect('Tareas.db')
cursor = conexion.cursor()

try:
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Lista (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      materia STRING,
      tipo_tarea STRING,
      fecha_entrega DATETIME,
      hecha BOOLEAN
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
  print('----------- Creating Tasks -----------')
  for k, v in materias.items():
    if len(k) != 1:
      print(k, '-', v)
    else:
      print(k, '-' * 2, v)
  print('---------- Datos Requeridos ----------')
  materia = input('Ingrese el número de la Materia: ')
  tipo_tarea = input('Ingrese el tipo de Tarea: ')
  fecha_entrega = input('Siguiendo el formato DD/MM/AAAA. Ingrese la fecha de entrega: ')
  for k, v in materias.items():
    list_k = list(k)
    k = ''.join(list_k)
    if materia == k:
      materia = v
      return create(materia, tipo_tarea, fecha_entrega)


def create(materia, tipo_tarea, fecha_entrega):
  index_task = [
    (materia, tipo_tarea, fecha_entrega, False)
  ]
  try:
    cursor.executemany('INSERT INTO Lista VALUES (NULL, ?, ?, ?, ?)', index_task)
    print('Tarea Creada Exitosamente!')
  except:
    print('No se pudo crear la Tarea!')


def read():
  cursor.execute('SELECT * FROM Lista')
  tasks = cursor.fetchall()
  print('---------- Total de Tareas ----------')
  for task in tasks:
    print(task)


def update():
  read()
  get_id = int(input('Escriba el id de la tarea a actulizar: '))
  cursor.execute(f'SELECT * FROM Lista WHERE id = {get_id}')
  get_task = cursor.fetchall()
  for i in get_task:
    i = i[0]
    print('materia | tipo_tarea | fecha_entrega | hecha')
    campo = input('¿Que desea actualizar?: ')
    campo.lower
    nuevo_valor = input('Diga el nuevo valor del campo: ')
    try:
      cursor.execute(f'UPDATE Lista SET {campo} = "{nuevo_valor}" WHERE id = {i}')
      print('Tarea Actualizada con exito!')
    except:
      return 'Ha ocurrido un error'


def delete():
  read()
  get_id = int(input('Escriba el id de la tarea a actulizar: '))
  cursor.execute(f'SELECT * FROM Lista WHERE id = {get_id}')
  get_task = cursor.fetchall()
  for i in get_task:
    i = i[0]
    prevencion = input('¿Está seguro que desea borrar permanentemente esta Tarea?: ')
    prevencion.lower
    if prevencion == 'si':
      cursor.execute(f'DELETE FROM Lista WHERE ID = {i}')
      print('Registro borrado con exito!')


def opciones():
  print('1 - Crear Tareas')
  print('2 - Ver Tareas')
  print('3 - Actualizar Tareas')
  print('4 - Borrar Tareas')
  opcion = input('¿Qué desea hacer?: ')
  if opcion == '1':
    return dates_for_task(materias)
  elif opcion == '2':
    return read()
  elif opcion == '3':
    return update()
  elif opcion == '4':
    return delete()
  else:
    print('Opción Inválida. Intente de nuevo.')
    return opciones()

opciones()

conexion.commit()
conexion.close()