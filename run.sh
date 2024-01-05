if [[ "$1" == "" ]];then
  echo "Ingrese el nombre del directorio de su entorno virtual"
  echo "Uso: ./run.sh <venv_dir_name>"
  exit 1
fi

cd "${0%/*}"
venv_dir="$(pwd)/$1"

if [[ ! -d $venv_dir ]];then
  echo "El directorio '$venv_dir' no existe"
  exit 1
fi

source $venv_dir/bin/activate
export DB_HOST="localhost"
export DB_NAME="proyecto"
export DB_PASS="root"
export DB_USER="root"
export FLASK_APP="app/__init__.py"
export FLASK_ENV="development"
flask run
