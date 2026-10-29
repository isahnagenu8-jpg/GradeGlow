# GradeGlow — Student Grade Calculator

A responsive student grade calculator built with Python, Flask, HTML, and CSS.

## Features
- Accepts scores from 0 to 100, including decimals
- Calculates a letter grade and gives friendly feedback
- Shows a score progress bar
- Responsive layout for desktop and mobile
- Validates incorrect or out-of-range input
- No JavaScript required

## Grading scale used
- A: 70–100
- B: 60–69
- C: 50–59
- D: 45–49
- E: 40–44
- F: 0–39

This is an example scale. Update the `calculate_grade()` function in `app.py` and the quick-reference section in `templates/index.html` to match your school's grading system.

## Run locally

1. Install Python 3.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Open the local address shown in the terminal, usually `http://127.0.0.1:5000`.

`debug=True` is for local development only. Turn debug mode off before deploying publicly.
