import unittest
from sqlalchemy.sql.expression import false, true
true=True
false=False
from . import BaseTestModel
from app.db import db
from app.models.meeting_point import MeetingPoint

class MeetingPointTest(BaseTestModel):

  def on_setup_tables(self):
    """Inicializa las tablas a utilizar en el test"""
    MeetingPoint.__table__.create(db.session.bind, checkfirst=True)


  def on_setup_data(self):
    """Inicializa los datos a utilizar en el test"""
    self.points = [
      MeetingPoint.create("punto1", "direccion1", 13, 12, 111222333, "email1@email.com", true),
      MeetingPoint.create("punto2", "direccion2", 23, 10, 222111333, "email2@email.com", false)
    ]
  

  def on_teardown_tables(self):
    """Elimina todos las tablas generados en la base de datos"""
    MeetingPoint.__table__.drop(db.session.bind, checkfirst=True)


  def test_all(self):
    """
    Dados dos punto de encuentro existente en la bd
    Cuando se consulta el tamaño de la tabla
    Se obtiene tamaño 2
    """
    self.assertEqual(len(MeetingPoint.all()), 2)


  def test_all_public(self):
    """
    Dados dos puntos donde "punto1" es público y "punto2" no existentes en la bd
    Cuando se solicitan los puntos públicos
    Entonces se retorna "punto1"
    """
    public_points = MeetingPoint.all_public()
    self.assertEqual(len(public_points), 1)
    self.assertEqual(public_points[0].name, "punto1")


  def test_all_not_public(self):
    """
    Dados dos puntos donde "punto1" es público y "punto2" no existentes en la bd
    Cuando se solicitan los puntos no públicos
    Entonces se retorna "punto2"
    """
    public_points = MeetingPoint.all_not_public()
    self.assertEqual(len(public_points), 1)
    self.assertEqual(public_points[0].name, "punto2")


  def extra_points(self):
    self.points += [
      MeetingPoint.create(
        "punto3", "direccion3", 2, 2, 333222111, "email3@email.com", true
      ),
      MeetingPoint.create(
        "punto1", "direccion4", 13, 12, 333111222, "email4@email.com", true
      )
    ]


  def test_all_paginated(self):
    pass


  def test_find_by_name(self):
    """Prueba el método find_by_name del modelo MeetingPoint"""
    
    def test_find_by_name1():
      """
      Dados 2 puntos con nombre "punto1" presentes en la bd
      Cuando se solicitan puntos por nombre "punto1"
      Entonces se obtienen los dos puntos con igual nombre
      """
      self.assertEqual(
        set([point.id for point in MeetingPoint.find_by_name("punto1")]),
        set([point.id for point in [self.points[0], self.points[3]]])
      )


    def test_find_by_name2():
      """
      Dado 1 punto con nombre "punto2" presente en la bd
      Cuando se solicitan puntos por nombre "punto2"
      Entonces se obtiene el punto con dicho nombre
      """
      self.assertEqual(
        set([point.id for point in MeetingPoint.find_by_name("punto2")]),
        set([point.id for point in self.points[1]])
      )


    self.extra_points()
    test_find_by_name1()
    test_find_by_name2()


  def test_find_by_state(self):
    """Prueba el método find_by_state del modelo MeetingPoint"""
    
    def test_find_by_name1():
      """
      Dados 3 puntos con estado público presentes en la bd
      Cuando se solicitan puntos por estado público
      Entonces se obtienen los 3 puntos con dicho estado
      """
      self.assertEqual(
        set([point.id for point in MeetingPoint.find_by_state(true)]),
        set([point.id for point in [self.points[0], self.points[2], self.points[3]]])
      )


    def test_find_by_name2():
      """
      Dado 1 punto con estado no público presente en la bd
      Cuando se solicitan puntos por estado no público
      Entonces se obtiene el punto con dicho estado
      """
      self.assertEqual(
        set([point.id for point in MeetingPoint.find_by_name(false)]),
        set([point.id for point in self.points[1]])
      )


    self.extra_points()
    test_find_by_name1()
    test_find_by_name2()


  def test_find_by_id(self):
    """
    Dado el punto con id 1 y nombre "punto1" y el punto con id 3 y nombre "punto3" presentes en la bd
    Cuando se solicitan los puntos con id 1 y 2
    Entonces se devuelven los punto con nombre "punto1" y "punto3" respectivamente
    """
    self.assertEqual(MeetingPoint.find_by_id(1).name, self.points[0].name)
    self.assertEqual(MeetingPoint.find_by_id(3).name, self.points[2].name)


  def test_update_coordinates(self):
    """
    Dado un punto con coordenadas 13 y 12 presente en la bd
    Cuando se le actualizan sus coordenadas a 3 y 4 respectivamente
    Entonces el punto en la bd pasa a tener coordenadas 3 y 4
    """
    self.assertEqual(MeetingPoint.find_by_id(1).coordinates, [13, 12])
    MeetingPoint.update_coordinates(self.points[0], 3, 4)
    self.assertEqual(MeetingPoint.find_by_id(1).coordinates, [3, 4])
