"""Pruebas para validar la lectura del archivo casa.txt."""

import unittest

from main import leer_casa


class TestLeerCasa(unittest.TestCase):
    def test_lee_texto(self) -> None:
        contenido = leer_casa()
        self.assertIn("CASA - DISEÑO BASE", contenido)

    def test_incluye_jardin(self) -> None:
        contenido = leer_casa()
        self.assertIn("JARDÍN", contenido)


if __name__ == "__main__":
    unittest.main()
