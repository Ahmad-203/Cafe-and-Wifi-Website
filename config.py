"""
config.py
Application configuration for Remote Cafe Finder.
Keeping configuration separate from app.py keeps the codebase modular
and makes it easy to add new environments (testing, production, etc.)
in the future.
"""

import os

# Base directory of the project, used to build absolute paths.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration shared by all environments."""

    # Secret key is required by Flask-WTF for CSRF protection.
    # In production this should be set via an environment variable.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

    # SQLite database lives inside the instance/ folder by default.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'cafes.db')}"
    )

    # Disable a feature we don't need and that adds unnecessary overhead.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination / display settings used across routes/templates.
    CAFES_PER_PAGE = 9


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
