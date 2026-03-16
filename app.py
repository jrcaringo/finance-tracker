from flask import Flask, render_template, request, redirect
from database import db
from models import Transaction

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def dashboard():
    transactions = Transaction.query.all()

    total = sum(t.amount for t in transactions)

    return render_template(
        "dashboard.html",
        transactions=transactions,
        total=total
    )


@app.route("/add", methods=["GET", "POST"])
def add_transaction():

    if request.method == "POST":

        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]

        transaction = Transaction(
            amount=amount,
            category=category,
            description=description
        )

        db.session.add(transaction)
        db.session.commit()

        return redirect("/")

    return render_template("add_transaction.html")


@app.route("/delete/<int:id>")
def delete(id):

    transaction = Transaction.query.get(id)

    db.session.delete(transaction)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)