import unittest
from abc import abstractmethod
from app import create_app
from app.db import db


class BaseTestModel(unittest.TestCase):

  def setUp(self):
    """Inicializa el contexto en el que se prueban los modelos"""
    self.app = create_app()
    self.app.app_context().push()
    self.on_setup()


  def tearDown(self):
    """Elimina el contexto en el que se prueban los modelos"""
    db.session.remove()
    self.on_teardown_tables()


  def on_setup(self):
    """Inicializa tablas y datos de la base de datos"""
    self.on_setup_tables()
    self.on_setup_data()


  @abstractmethod
  def on_setup_tables(self):
    """Inicializa las tablas a utilizar en el test"""
    pass


  @abstractmethod
  def on_setup_data(self):
    """Inicializa los datos a utilizar en el test"""
    pass


  @abstractmethod
  def on_teardown_tables(self):
    """Elimina todos las tablas generados en la base de datos"""
    pass