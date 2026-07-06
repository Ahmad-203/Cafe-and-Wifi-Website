"""
extensions.py
Holds shared extension instances (SQLAlchemy, etc.) so that both
app.py and the models/routes packages can import them without
running into circular-import problems.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
