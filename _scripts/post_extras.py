"""Después de generar_extras.py (se puede volver a correr): el formulario no pide email y se envía por WhatsApp."""
from pathlib import Path
p = Path(__file__).resolve().parent.parent / "privacidad.html"
t = p.read_text(encoding="utf8")
t = t.replace("nombre, teléfono, email y el mensaje que escribís o al escribirnos por WhatsApp.",
              "nombre, teléfono, el área de consulta y el mensaje que escribís en el formulario (que se envía por WhatsApp) o al escribirnos por ese medio.")
p.write_text(t, encoding="utf8", newline="\n"); print("ok privacidad")
