# Flood disaster management system

  - **REST-MVC** system for managing pluvial disasters and floods.

  - Developed with **Flask**, **SQLite**, **Leaflet**, **Bootstrap**, and **Vue**.

  - Initially designed for the city of La Plata (but can also be used in other locations).
    - The central point of the maps can be modified from the Leaflet configuration.

  - The system allows:
    - Establishing meeting points where people can gather.
    - Setting evacuation routes for the city or specific places.
    - Marking flood-prone areas of the city.
    - Making complaints and auditing them through regular follow-ups.
    - Managing users.
    - Modifying the system settings.

  - The system consists of:
    - **A private section** for administration accessible by administrators and operators.
      - Whose front-end was developed in HTML, CSS, and Javascript without using Vue.

    - **A public section** for system users.
      - Whose front-end was developed in HTML, CSS, and Javascript using Vue.

## Login - Users loaded in the test database:

- **Administrator:**
  - username: `admin`
  - password: `123123`

- **Operator:**
  - username: `zozme@gmail.com`
  - password: `234234`

## Structure of the Flask project folders

- Subdirectories of the `app` directory

```bash
forms            # Module where classes that use the WTForms library are found
helpers          # Module where helper functions for various parts of the code are placed
models           # Module with the application's business logic and database connection
resources        # Module with the application's controllers (web part)
static           # Module with static files (CSS, JavaScript)
templates        # Module with the templates
db.py            # Database instance
__init__.py      # Application instance and routing
```

## Application Images

### Private section

- **Login**

![Private section login](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-home.png?raw=true "Private section login")

- **Home**

![Private section main page](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-login.png?raw=true "Private section main page")

- **List of flood-prone zones**

![List of flood-prone zones](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-fzone.png?raw=true "List of flood-prone zones")

- **Creation of flood-prone zones**

![Creation of flood-prone zones](https://github.com/J-4352681/Flask-pluvial-disaster-web-management-system/blob/master/imgs/flask_pluvial-new_fzone.png?raw=true "Creation of flood-prone zones")

### Public section

- _TO BE COMPLETED_

## How to Run

### Private section

**For the first run:**

1. Install [XAMPP](https://www.apachefriends.org/index.html) and [Python3.9](https://www.python.org/downloads/)

2. Clone the repository by executing:
  ```Bash
  git clone git@github.com:J-4352681/Flask-pluvial-disaster-web-management-system.git
  ```

3. Access the repository directory:
  ```Bash
  cd Flask-pluvial-disaster-web-management-system
  ```

4. Create a Python virtual environment within the repository directory:
  ```Bash
  python -m venv venv
  ```
  - `venv` (the last one of the two) is the name of the virtual environment

5. Activate the created virtual environment by executing:
  ```Bash
  source venv/bin/activate
  ```

6. Install the dependencies by executing:
  ```Bash
  pip install -r requirements.txt
  ```

7. Open XAMPP/LAMPP and run MySQL and Apache

8. It is no longer necessary to be in the virtual environment, so exit it and launch the Flask app:
  ```Bash
  deactivate
  ./run.sh venv
  ```

### Public section

9. The instructions can be found in `web/README.md`
