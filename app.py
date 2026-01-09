from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 40px;">
    <h2>Multiplication Table Generator</h2>

    <form method="POST">
        <input type="number" name="number" required>
        <button type="submit">Generate</button>
    </form>

    {% if table %}
        <h3>Table of {{ num }}</h3>
        <ul>
        {% for line in table %}
            <li>{{ line }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    num = None

    if request.method == "POST":
        num = int(request.form["number"])
        for i in range(1, 11):
            table.append(f"{num} × {i} = {num * i}")

    return render_template_string(HTML, table=table, num=num)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
