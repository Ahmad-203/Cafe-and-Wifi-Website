# Remote Cafe Finder ☕

A full-stack Flask web application that helps remote workers, freelancers,
and students discover work-friendly cafes — places with good coffee, fast
WiFi, plenty of power sockets, and comfortable seating.

---

## Features

- **Home page** with a hero section, live stats, and featured cafes
- **Browse all cafes** in a responsive Bootstrap card grid
- **Cafe details page** with seating, WiFi, sockets, calls, price, and rating
- **Add a cafe** via a validated form (Flask-WTF + WTForms)
- **Edit a cafe** with the same validated form, pre-filled
- **Delete a cafe** with a confirmation modal
- **Search** by name or location, with WiFi / sockets / calls filters
- **Sorting** by name, rating, or coffee price
- **About** and **Contact** pages
- **Dark mode toggle** that remembers your preference via `localStorage`
- **Custom 404 and 500 error pages**
- Server-side and client-side **form validation**
- Modular project structure: `models/`, `forms/`, `routes/` (Flask blueprints)

---

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy (ORM over SQLite)
- Flask-WTF / WTForms (forms & validation)
- Jinja2 templates
- Bootstrap 5 + Bootstrap Icons
- Vanilla JavaScript (dark mode, client-side validation hooks)

---

## Project Structure

```text
remote_cafe_finder/
├── app.py                 # App factory, blueprint registration, seed data
├── config.py              # Configuration classes
├── extensions.py          # Shared SQLAlchemy() instance
├── requirements.txt
├── README.md
│
├── instance/
│   └── cafes.db            # SQLite database (auto-created on first run)
│
├── models/
│   └── cafe.py             # Cafe ORM model
│
├── forms/
│   └── cafe_form.py        # Flask-WTF form for add/edit
│
├── routes/
│   ├── home.py              # / , /about , /contact
│   ├── cafes.py              # /cafes , /cafe/<id> , /add-cafe , /edit/<id> , /delete/<id>
│   └── search.py             # /search
│
├── templates/
│   ├── base.html, index.html, cafes.html, cafe_details.html,
│   ├── add_cafe.html, edit_cafe.html, search_results.html,
│   └── about.html, contact.html, 404.html, 500.html
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/             # (uses hosted Unsplash URLs by default)
│
└── screenshots/           # Add your own app screenshots here
```

---

## Installation & Setup

### 1. Clone / unzip the project

```bash
cd remote_cafe_finder
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Set a secret key

```bash
export SECRET_KEY="your-own-secret-key"     # Windows: set SECRET_KEY=...
```

If skipped, a development default is used — fine for local testing, not for production.

---

## Running Locally

```bash
python app.py
```

The app will:
1. Create the `instance/` folder and `cafes.db` SQLite database if they don't exist.
2. Seed the database with 6 sample cafes on first run.
3. Start the dev server at **http://127.0.0.1:5000**

---

## Database Notes

- The `Cafe` model lives in `models/cafe.py` and includes:
  `id, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price, rating`.
- `db.create_all()` runs automatically inside the app factory — no manual migration step is needed for this demo.
- For schema changes in a real project, consider adding **Flask-Migrate**.

---

## Screenshots

> Add your own screenshots to the `screenshots/` folder and reference them here, e.g.:
>
> ![Home Page](screenshots/home.png)
> ![Cafe List](screenshots/cafes.png)
> ![Cafe Details](screenshots/details.png)

---

## Future Improvements

- User accounts & authentication (so only owners can edit/delete their cafes)
- Image uploads instead of external image URLs
- Pagination on the cafes list for large datasets
- Map view (e.g. Leaflet/Google Maps embed) showing all cafes at once
- User reviews and comments per cafe
- REST API endpoints (JSON) alongside the HTML views
- Flask-Migrate for proper schema migrations
- Automated tests (pytest) for routes and models

---

## License

This project is provided as a demonstration/template and is free to use and modify.
