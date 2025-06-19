# Sequence Predictor

A sleek, modern web application built with Django that predicts the next number in a sequence of 10 numbers provided by the user. The interface features a futuristic design with real-time input validation and a responsive layout.

## Features

- **Input Validation**: Accepts a sequence of 10 numbers in the format `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]` with real-time feedback on input validity.
- **Prediction**: Submits the sequence to a backend (to be implemented) to predict the next number.
- **Responsive Design**: Optimized for both desktop and mobile devices with a clean, glassmorphic UI and subtle animations.
- **Modern Styling**: Uses the Inter font, a cyan-blue gradient theme, and dynamic effects like pulsing backgrounds and rotating borders.
- **Error Handling**: Displays clear error messages for invalid inputs.

## Screenshots

*Enter a 10-number sequence and get the next number in the sequence.*

## Prerequisites

- Python 3.8+
- Django 3.2+
- A modern web browser (Chrome, Firefox, Safari, etc.)

## Installation

```bash
# Clone the Repository
git clone https://github.com/yourusername/sequence-predictor.git
cd sequence-predictor

# Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Set Up Django Static Files
python manage.py collectstatic

# Apply Migrations
python manage.py makemigrations
python manage.py migrate

# Run the Development Server
python manage.py runserver
```

Then open your browser and navigate to:  
`http://127.0.0.1:8000`

## Project Structure

```
myproject/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   ├── urls.py
│   ├── onehotencoder.pkl
│   ├── sustain.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   ├── js/
│   │   │   ├── script.js
│   │   ├── images/
│   └── templates/
│       ├── index.html


```

- `templates/index.html`: The main HTML template for the Sequence Predictor interface.  
- `static/css/style.css`: Custom CSS for the futuristic UI design.  
- `requirements.txt`: Lists Python dependencies (e.g., Django).

## Usage

1. Open the application in your browser.
2. Enter a 10-number sequence in the format `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`.
3. Click the **Predict** button to submit the sequence.
4. View the predicted next number in the result card.
5. Invalid inputs will display an error message below the input field.

## Customization

- **Backend Logic**: Implement the sequence prediction logic in the Django view handling the form submission (e.g., using a machine learning model or mathematical algorithm).
- **Styling**: Modify `static/css/style.css` to adjust colors, animations, or layout.
- **Fonts**: Replace the Inter font by updating the Google Fonts import in `index.html`.

## Contributing

Contributions are welcome! Please follow these steps:

```bash
# Fork the repository
# Create a new branch
git checkout -b feature/your-feature

# Commit your changes
git commit -m "Add your feature"

# Push to the branch
git push origin feature/your-feature
```

Then open a pull request on GitHub.

