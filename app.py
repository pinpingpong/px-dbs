from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST": 
        Rates = float(request.form.get("rates"))
        print(Rates)
        
        model1 = joblib.load("regression_DBS")
        pred1 = model1.predict([[Rates]])

        model2 = joblib.load("tree_DBS")
        pred2 = model2.predict([[Rates]])
        return(render_template("index.html", result1=pred1[0], result2=pred2[0]))
    else:
        return(render_template("index.html", result1="waiting", result2="waiting"))


if __name__ == "__main__": 
    app.run()

