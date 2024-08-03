from flask import Flask, render_template
import random

app = Flask(__name__)

fun_facts = [
    "Bananas are berries, but strawberries aren't.",
    "Honey never spoils.",
    "Octopuses have three hearts.",
    "Humans and giraffes have the same number of neck vertebrae.",
    "A group of flamingos is called a 'flamboyance'.",
]

@app.route('/')
def index():
    fact_of_the_day = random.choice(fun_facts)
    return render_template('index.html', fact=fact_of_the_day)

if __name__ == '__main__':
    app.run(debug=True)