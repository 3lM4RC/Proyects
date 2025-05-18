# muros/__init__.py
from importlib import import_module
from pathlib import Path

# importa dinámicamente cada .py dentro de la carpeta (menos __init__.py)
for f in Path(__file__).parent.glob("*.py"):
    if f.stem != "__init__":
        import_module(f"muros.{f.stem}")
