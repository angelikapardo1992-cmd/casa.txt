"""Archivo principal para mostrar el contenido de casa.txt."""

from pathlib import Path


def leer_casa(ruta: str = "casa.txt") -> str:
    """Lee y devuelve el contenido del archivo casa.txt."""
    return Path(ruta).read_text(encoding="utf-8")


if __name__ == "__main__":
    print(leer_casa())
