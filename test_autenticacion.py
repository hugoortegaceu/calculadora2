# tests/test_autenticacion.py
from modulos_utiles.autenticacion import Autenticacion 
 
def test_credenciales_validas():
    auth = Autenticacion()
    assert auth.verificar_credenciales("admin", "1234") is True
 
def test_credenciales_invalidas():
    auth = Autenticacion()
    assert auth.verificar_credenciales("admin", "wrong") is False
 
def test_usuario_inexistente():
    auth = Autenticacion()
    assert auth.verificar_credenciales("unknown", "password") is False
 
