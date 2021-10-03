<<<<<<< HEAD
# Grupo 38
Tomas Oliva, 17233/5 

=======
# Proyecto de Software - Aplicación de ejemplo

Aplicación de ejemplo para la cátedra de Proyecto de Software de la Facultad de Informática de la U.N.L.P.

## Iniciar ambiente

### Requisitos

- python3
- virtualenv

### Ejecución

```bash
$ virtualenv -p python3 venv
# Para iniciar el entorno virtual
$ source venv/bin/activate
# Instalar las dependencias dentro del entorno virtual
$ pip install -r requirements.txt
# En el directorio raiz
$ FLASK_ENV=development python run.py
# Otra alternativa
$ FLASK_ENV=development flask run
```

Para salir del entorno virutal, ejecutar:

```bash
$ deactivate
```

## Shell de prueba

Para iniciar una consola interactiva que nos permita interactuar con
nuestros modelos podemos ejecutar el siguiente comando:

```bash
FLASK_ENV=development flask shell
```

## Estructura de carpetas del proyecto

```bash
config            # Módulo de donde se obtienen las variables de configuración
helpers           # Módulo donde se colocan funciones auxiliares para varias partes del código
models            # Módulo con la lógica de negocio de la aplicación y la conexión a la base de datos
resources         # Módulo con los controladores de la aplicación (parte web)
templates         # Módulo con los templates
db.py             # Instancia de base de datos
__init__.py       # Instancia de la aplicación y ruteo
```

## TODO

- [ ] Usar una hoja de estilos simple para que quede de ejemplo.
>>>>>>> 684509f8757d4a9345f3b4c01b857868c0653037
