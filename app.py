"""
app.py
Application factory and entry point for Remote Cafe Finder.

Run locally with:
    python app.py
"""

import os
from flask import Flask, render_template

from config import config_by_name
from extensions import db
from models.cafe import Cafe

from routes.home import home_bp
from routes.cafes import cafes_bp
from routes.search import search_bp


def create_app(config_name="development"):
    """Application factory: builds and configures the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name["development"]))

    # Initialize extensions.
    db.init_app(app)

    # Register blueprints (modular route groups).
    app.register_blueprint(home_bp)
    app.register_blueprint(cafes_bp)
    app.register_blueprint(search_bp)

    # Make "now" available to all templates (used in the footer for the year).
    @app.context_processor
    def inject_globals():
        from datetime import datetime
        return {"current_year": datetime.utcnow().year}

    # --- Error handlers -----------------------------------------------
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        db.session.rollback()
        return render_template("500.html"), 500

    # --- Database setup & seed data ------------------------------------
    with app.app_context():
        os.makedirs(os.path.join(os.path.dirname(__file__), "instance"), exist_ok=True)
        db.create_all()
        seed_database_if_empty()

    return app


def seed_database_if_empty():
    """Populate the database with a handful of sample cafes on first run."""
    if Cafe.query.first() is not None:
        return

    sample_cafes = [
        Cafe(
            name="The Workshop Coffee Co.",
            map_url="https://maps.google.com/?q=Workshop+Coffee+London",
            img_url="https://images.unsplash.com/photo-1559925393-8be0ec4767c8?w=800",
            location="London",
            seats="20-30",
            has_toilet=True,
            has_wifi=True,
            has_sockets=True,
            can_take_calls=True,
            coffee_price="£3.20",
            rating=4.5,
        ),
        Cafe(
            name="Bean There Cafe",
            map_url="https://maps.google.com/?q=Bean+There+Cafe+Manchester",
            img_url="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
            location="Manchester",
            seats="10-20",
            has_toilet=True,
            has_wifi=True,
            has_sockets=False,
            can_take_calls=False,
            coffee_price="£2.80",
            rating=4.0,
        ),
        Cafe(
            name="Remote Roast",
            map_url="https://maps.google.com/?q=Remote+Roast+Edinburgh",
            img_url="https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=800",
            location="Edinburgh",
            seats="30-40",
            has_toilet=True,
            has_wifi=True,
            has_sockets=True,
            can_take_calls=True,
            coffee_price="£3.50",
            rating=5.0,
        ),
        Cafe(
            name="Quiet Corner",
            map_url="https://maps.google.com/?q=Quiet+Corner+Bristol",
            img_url="https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800",
            location="Bristol",
            seats="0-10",
            has_toilet=False,
            has_wifi=True,
            has_sockets=True,
            can_take_calls=False,
            coffee_price="£2.50",
            rating=3.5,
        ),
        Cafe(
            name="Laptop & Latte",
            map_url="https://maps.google.com/?q=Laptop+and+Latte+Leeds",
            img_url="https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=800",
            location="Leeds",
            seats="40-50",
            has_toilet=True,
            has_wifi=True,
            has_sockets=True,
            can_take_calls=True,
            coffee_price="£3.00",
            rating=4.2,
        ),
        Cafe(
            name="The Daily Grind",
            map_url="https://maps.google.com/?q=The+Daily+Grind+Birmingham",
            img_url="https://images.unsplash.com/photo-1559925393-8be0ec4767c8?w=800",
            location="Birmingham",
            seats="10-20",
            has_toilet=True,
            has_wifi=False,
            has_sockets=False,
            can_take_calls=False,
            coffee_price="£2.40",
            rating=3.0,
        ),
    ]

    db.session.add_all(sample_cafes)
    db.session.commit()


# Create the app at module level so `flask run` and gunicorn can find it.
app = create_app(os.environ.get("FLASK_ENV", "development"))


if __name__ == "__main__":
    app.run(debug=True)
