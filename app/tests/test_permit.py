import unittest
from . import BaseTestModel
from app.db import db
from app.models.permit import Permit


class PermitTest(BaseTestModel):

  def on_setup_tables(self):
    """Inicializa las tablas a utilizar en el test"""
    Permit.__table__.create(db.session.bind, checkfirst=True)


  def on_setup_data(self):
    """Inicializa los datos a utilizar en el test"""
    Permit.create("un_permiso")
  

  def on_teardown_tables(self):
    """Elimina todos las tablas generados en la base de datos"""
    Permit.__table__.drop(db.session.bind, checkfirst=True)


  def test_all(self):
    """
    Dado un permiso existente en la bd
    Cuando se consulta el tamaño de la tabla y el nombre del permiso en la misma
    Se obtiene tamaño 1 y el nombre del permiso
    """
    self.assertEqual(len(Permit.all()), 1)
    self.assertEqual(Permit.all()[0].name, "un_permiso")