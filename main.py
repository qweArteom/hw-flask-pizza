from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    context = {
        "name_pizza": "Піца чотири м'яса",
        "pizza_ingredients": "Перетерті томати, моцарела, бекон, маринована синя цибуля, куряче філе су-від, мисливські ковбаски, прошуто кото.",
        "name_pizza_2": "Гавайська піца",
        "pizza_ingredients_2": "Консервований ананас, ніжне куряче філе, сири моцарелла та пармезан, сирний соус, рукола та томати."

    }
    return render_template("menu.html", **context)


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html")


@app.get("/test/")
def test():
    return render_template("test.html", title="Pizzeria!")


max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]

@app.get('/results/')
def results():
  context={
     "title": "Results",
     "students": students,
     "test_name": test_name,
     "max_score": max_score,
  }
  return render_template("results_2.html", **context)


if __name__ == "__main__":
    app.run(debug=True, port=1234)