from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """የመጀመሪያውን ገጽ ያሳያል።"""
    return render_template('home.html')

@app.route('/start')
def start_page():
    """የሒሳብ ጥያቄ ማስገቢያ ገጽን ያሳያል።"""
    return render_template('dashboard.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """የሒሳብ ጥያቄን አስልቶ መልሱን ያብራራል (ግንባታ)።"""
    try:
        expression = request.form['question']
        # eval() በጥንቃቄ መጠቀም አለበት። ለቀላል ፕሮጀክት ጥሩ ነው።
        result = eval(expression)
        
        explanation = f"የጥያቄው ({expression}) መልስ {result} ነው።"
    except Exception as e:
        result = "ስህተት!"
        explanation = f"የተሳሳተ የሂሳብ ጥያቄ። እባክዎ ትክክለኛ የሂሳብ ቀመር ያስገቡ።"
        
    return render_template('dashboard.html', result=result, explanation=explanation)

if __name__ == '__main__':
    # ለሙከራ debug=True ማድረግ ትችላለህ። ለደፕሎይመንት ግን False መሆን አለበት።
    app.run(debug=False)<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liyo's Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #a7d9f2;
            color: #333;
            margin: 0;
            text-align: center;
        }
        .header {
            font-size: 2em;
            color: #0056b3;
            margin-bottom: 20px;
        }
        .btn {
            padding: 15px 30px;
            font-size: 1.2em;
            color: white;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="header">
        Created by Liyo
    </div>
    <a href="/start" class="btn">Start</a>
</body>
</html><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #e0f2f7;
            color: #333;
            margin: 0;
            text-align: center;
        }
        .dashboard-container {
            width: 80%;
            max-width: 600px;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input[type="text"] {
            width: 90%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1em;
        }
        button {
            padding: 10px 20px;
            font-size: 1em;
            color: white;
            background-color: #28a745;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #218838;
        }
        .result-box {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #0056b3;
            border-radius: 5px;
            background-color: #eaf6ff;
            text-align: left;
        }
        .result-box h3 {
            margin-top: 0;
            color: #0056b3;
        }
        .explanation {
            margin-top: 10px;
            font-size: 1em;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <h1>ሒሳብ ለመስራት ጥያቄ አስገባ</h1>
        <form action="/calculate" method="post">
            <input type="text" name="question" placeholder="ለምሳሌ: (25 + 10) * 2" required>
            <button type="submit">መልስ</button>
        </form>

        {% if result %}
        <div class="result-box">
            <h3>መልስ: {{ result }}</h3>
            <p class="explanation">{{ explanation }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
