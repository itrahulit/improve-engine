# improve-engine
A sample website built with Flask

## Features
- Clean and modern design
- Responsive layout
- Multiple pages (Home, About)
- Easy to customize

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itrahulit/improve-engine.git
cd improve-engine
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:
```bash
python app.py
```

The website will be available at `http://localhost:5000`

**Note:** This runs Flask in debug mode for development purposes. For production deployment, use a WSGI server like Gunicorn and disable debug mode.

## Project Structure
```
improve-engine/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── index.html     # Homepage
│   └── about.html     # About page
└── static/            # Static files
    └── css/
        └── style.css  # Stylesheet
```

## Technologies Used
- Flask 3.0.0 - Python web framework
- HTML5 - Structure
- CSS3 - Styling
