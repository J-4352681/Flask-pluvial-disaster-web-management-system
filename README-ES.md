# Sistema de gestión para casos de desastres pluviales

  - Sistema REST-MVC para administrar situaciones de desastres pluviales e inundaciones.

  - Fue desarrollado con Flask, SQLite, Leaflet, Bootstrap y Vue.

  - Pensado inicialmente para la ciudad de La Plata (pero también puede ser utilizado en otras localidades).
    - Se puede modificar el punto central de los mapas desde la configuración de LeafLet.

  - El sistema permite:
    - Establecer puntos de encuentro donde la gente se reuna.
    - Establecer rutas de evacuación de la ciudad o de lugares específicos.
    - Marcar zonas inundables de la ciudad.
    - Hacer denuncias y auditarlas mediante seguimientos periódicos.
    - Administrar los usuarios.
    - Modificar la configuración del sistema.

  - El sistema se compone de:
    - **Un apartado privado** de administración accesible por administradores y operadores.
      - Cuyo front-end fue desarrollado en HTML, CSS y Javascript sin utilizar Vue.

    - **Un apartado público** para los usuarios del sistema.
      - Cuyo front-end fue desarrollado en HTML, CSS y Javascript utilizando Vue.

## Login - Usuarios cargados en la base de datos de prueba:

- **Administrador:**
  - usuario: `admin`
  - contraseña: `123123`

- **Operador:**
  - usuario: `zozme@gmail.com`
  - contraseña: `234234`

## Estructura de carpetas del proyecto Flask

- Subdirectorios del directorio `app`

```bash
forms            # Módulo donde se encuentran clases que utilizan la libreria WTForms
helpers           # Módulo donde se colocan funciones auxiliares para varias partes del código
models            # Módulo con la lógica de negocio de la aplicación y la conexión a la base de datos
resources         # Módulo con los controladores de la aplicación (parte web)
static            # Módulo con los archivos estaticos (CSS, JavaScript)
templates         # Módulo con los templates
db.py             # Instancia de base de datos
__init__.py       # Instancia de la aplicación y ruteo
```

## Imágenes de la aplicación

### Aplicación privada

- **Login**

![Login de la aplicación privada](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-home.png?raw=true "Login de la aplicación privada")

- **Home**

![Página principal de la aplicación privada](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-login.png?raw=true "Página principal de la aplicación privada")

- **Listado de zonas inundables**

![Listado de zonas inundables](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-fzone.png?raw=true "Listado de zonas inundables")

- **Creación de zonas inundables**

![Creación de zonas inundables](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-new_fzone.png?raw=true "Creación de zonas inundables")

### Aplicación pública

- _A COMPLETAR_

## Cómo ejecutar

### Aplicación privada

**Para la primera ejecución:**

1. Instalar [XAMPP](https://www.apachefriends.org/es/index.html) y [Python3.9](https://www.python.org/downloads/)

2. Clonar el repositorio ejecutando:
  ```Bash
  git clone git@github.com:J-4352681/Flask-pluvial-disaster-web-managementsystem.git
  ```

3. Acceder al directorio del repositorio:
  ```Bash
  cd Flask-pluvial-disaster-web-management-system
  ```

4. Crear un entorno virtual de Python dentro del directorio del repositorio:
  ```Bash
  python -m venv venv
  ```
  - `venv` (el último de los dos) es el nombre del entorno virtual

5. Activar el entorno virtual creado ejecutando:
  ```Bash
  source venv/bin/activate
  ```

6. Instalar las dependencias ejecutando:
  ```Bash
  pip install -r requirements.txt
  ```

7. Abrir XAMPP/LAMPP y ejecutar MySQL y Apache

8. Ya no es necesario estar en el entorno virtual por consiguiente se sale deél y se lanza la app Flask:
  ```Bash
  deactivate
  ./run.sh venv
  ```
    - `venv` debe ser el nombre del entorno virtual que se haya elegido

**Para las siguientes ejecuciones:**

1. Ejecutar el script desde cualquier directorio:
  ```Bash
  [...]/Flask-pluvial-disaster-web-management-system/run.sh venv
  ```
    - `venv` debe ser el nombre del entorno virtual que se haya elegido

### Aplicación pública

9. Las instrucciones se encuentran en `web/README.md`
