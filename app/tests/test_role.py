import unittest
from sqlalchemy import Table
from . import BaseTestModel
from app.db import db
from app.models.role import Role
from app.models.permit import Permit


class RoleTest(BaseTestModel):

  def on_setup_tables(self):
    """Inicializa las tablas a utilizar en el test"""
    Permit.__table__.create(db.session.bind, checkfirst=True)
    Role.__table__.create(db.session.bind, checkfirst=True)
    Table('role_has_permit', db.Model.metadata, extend_existing=True).create(db.session.bind, checkfirst=True)


  def on_setup_data(self):
    """Inicializa los datos a utilizar en el test"""
    permiso1 = "permiso1"
    permiso2 = "permiso2"
    self.permisos = [
      Permit.create(permiso1),
      Permit.create(permiso2)
    ]
    
    role1 = "role1"
    role2 = "role2"
    self.roles = [
      Role.create(role1, self.permisos),
      Role.create(role2, self.permisos)
    ]


  def on_teardown_tables(self):
    """Elimina todos los datos generados en la base de datos"""
    Table('role_has_permit', db.Model.metadata, extend_existing=True).drop(db.session.bind, checkfirst=True)
    Role.__table__.drop(db.session.bind, checkfirst=True)
    Permit.__table__.drop(db.session.bind, checkfirst=True)


  def test_all(self):
    """Prueba el método all del modelo Role"""

    def test_all1():
      """
      Dado un rol existente en la bd
      Cuando se consulta el tamaño de la tabla y el nombre del rol en la misma
      Se obtiene tamaño 1 y el nombre del rol
      """
      self.assertEqual(len(Role.all()), 2)
      self.assertEqual(Role.all()[0].name, "role1")


    def test_all2():
      """
      Dado un rol inexistente en la bd
      Cuando se inserta el rol en la bd
      Se obtiene tamaño 2 y los dos nombres de los roles insertados
      """
      self.roles += [Role.create("role3")]
      self.assertEqual(len(Role.all()), 3)
      self.assertEqual(len(Role.all()), len(self.roles))


    test_all1()
    test_all2()


  def test_get_admin(self):
    """Prueba el método get_admin del modelo Role"""

    def test_get_admin1():
      """
      Dado el rol "admin" no presente en la bd
      Cuando se solicita por nombre el rol "admin"
      Entonces no se encuentra ningún elemento
      """
      self.assertFalse(Role.get_admin())


    def test_get_admin2():
      """
      Dado el rol "admin" no presente en la bd
      Cuando se solicita por nombre el rol "admin"
      Entonces no se encuentra ningún elemento
      """
      self.roles += [Role.create("admin")]
      self.assertTrue(Role.get_admin())


    test_get_admin1()
    test_get_admin2()


  def test_get_by_name(self):
    """Prueba el método get_by_name del modelo Role"""

    def test_get_by_name1():
      """
      Dado el rol "role1234" no presente en la bd
      Cuando se solicita por nombre el rol "role1234"
      Entonces no se encuentra ningún elemento
      """
      self.assertFalse(Role.get_by_name("role1234"))


    def test_get_by_name2():
      """
      Dado el rol "role10" presente en la bd
      Cuando se solicita por nombre el rol "rol10"
      Entonces se encuentra y retorna el elemento
      """
      self.roles += [Role.create("role10")]
      self.assertTrue(Role.get_by_name("role10"))


    test_get_by_name1()
    test_get_by_name2()


  def test_get_operator(self):
    """Prueba el método get_operator del modelo Role"""

    def test_get_operator1():
      """
      Dado el rol "operator" no presente en la bd
      Cuando se solicita por nombre el rol "operator"
      Entonces no se encuentra ningún elemento
      """
      self.assertFalse(Role.get_operator())


    def test_get_operator2():
      """
      Dado el rol "operator" presente en la bd
      Cuando se solicita por nombre el rol "operator"
      Entonces se encuentra y retorna el elemento
      """
      self.roles += [Role.create("operator")]
      self.assertTrue(Role.get_operator())


    test_get_operator1()
    test_get_operator2()


  def test_get_by_ids(self):
    """Prueba el método get_by_ids del modelo Role"""

    def test_get_by_ids1():
      """
      Dados dos roles con id 9 y 10 no presentes en la bd
      Cuando se solicitan roles con id 9 y 10
      Entonces no se encuentra ningún elemento
      """
      self.assertFalse(Role.get_by_ids([9, 10]))


    def test_get_by_ids2():
      """
      Dados dos roles con id 1 y 2 no presentes en la bd
      Cuando se solicitan roles con id 1 y 2
      Entonces se encuentran y retornan los elementos
      """
      roles_id = [1, 2]
      self.assertEqual(set([role.id for role in Role.get_by_ids(roles_id)]), set(roles_id))


    test_get_by_ids1()
    test_get_by_ids2()