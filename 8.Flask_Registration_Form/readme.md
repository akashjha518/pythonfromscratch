## Installation

1. Create and activate a virtual environment.
2. Install Flask:

```bash
pip install flask
```

## How To Run

1. Start the app:

```bash
python task.py
```

2. Open your browser and go to:

```text
http://127.0.0.1:5000/
```

## Usage

- The `/register` route shows the registration form.
- Submitting the form sends a `POST` request to `/confirm`.
- The confirmation page displays:
  - Name
  - City
  - Phone number

## Routes

- `/` or `/register` - renders the registration form
- `/confirm` - handles submitted form data and renders the confirmation page