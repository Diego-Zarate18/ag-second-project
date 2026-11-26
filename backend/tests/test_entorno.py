"""Pruebas de la fase F0: el entorno está listo y el grafo de diseño es legible."""

import json
from pathlib import Path

import siruga

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "SIRUGA_grafo_conocimiento.json"


def test_paquete_importa():
    assert siruga.__version__


def test_dependencias_instaladas():
    import fastapi  # noqa: F401
    import httpx  # noqa: F401
    import pydantic  # noqa: F401

    assert pydantic.VERSION.startswith("2.")


def test_grafo_tiene_valores_de_referencia():
    grafo = json.loads(GRAFO.read_text(encoding="utf-8"))
    valores = grafo["reference_values"]
    assert valores["workday"]["departure_window_start"] == "06:00"
    assert valores["workday"]["return_deadline"] == "14:00"
    assert len(valores["traffic_profile_weekday"]["bands"]) == 8
    assert grafo["genetic_algorithm"]["default_parameters"]["population_size"] == 200
