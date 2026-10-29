from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(score):
    """Example grading scale. Adjust these boundaries to match your school."""
    if score >= 70:
        return "A", "Excellent work! Keep aiming high.", "grade-a"
    elif score >= 60:
        return "B", "Very good. You're doing well!", "grade-b"
    elif score >= 50:
        return "C", "Good effort. A little more practice can help.", "grade-c"
    elif score >= 45:
        return "D", "Fair result. Review the topics you found difficult.", "grade-d"
    elif score >= 40:
        return "E", "You passed, but there's room to improve.", "grade-e"
    return "F", "Don't give up. Make a plan and try again!", "grade-f"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    score_value = ""

    if request.method == "POST":
        score_value = request.form.get("score", "").strip()
        try:
            score = float(score_value)
            if not 0 <= score <= 100:
                error = "Enter a score between 0 and 100."
            else:
                grade, message, grade_class = calculate_grade(score)
                result = {
                    "score": score,
                    "display_score": f"{score:g}",
                    "grade": grade,
                    "message": message,
                    "grade_class": grade_class,
                    "progress": score,
                }
        except ValueError:
            error = "Please enter a valid number, such as 78 or 64.5."

    return render_template(
        "index.html",
        result=result,
        error=error,
        score_value=score_value
    )


if __name__ == "__main__":
    app.run(debug=True)
