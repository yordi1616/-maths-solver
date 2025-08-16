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
        result = eval(expression)
        
        explanation = f"የጥያቄው ({expression}) መልስ {result} ነው።"
    except Exception as e:
        result = "ስህተት!"
        explanation = f"የተሳሳተ የሂሳብ ጥያቄ። እባክዎ ትክክለኛ የሂሳብ ቀመር ያስገቡ።"
        
    return render_template('dashboard.html', result=result, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=False)
