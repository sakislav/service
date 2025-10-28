from datetime import date
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
import os
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "vnrevewvjiowvow"
Bootstrap5(app)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u9b6kdrnigq1i2:p36247ef0676403b4975ce71402371fe5f531f06837b9e4f62b67c9635772f8c0@c7itisjfjj8ril.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d58bnbpgd036r4'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Repair(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client: Mapped[str] = mapped_column(String(64), nullable=False)
    device: Mapped[str] = mapped_column(String(64), nullable=False)
    phone: Mapped[str] = mapped_column(String(100), nullable=False)
    problem: Mapped[str] = mapped_column(String(250), nullable=False)
    fix: Mapped[str] = mapped_column(String(250), nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    result = db.session.execute(db.select(Repair))
    repairs = result.scalars().all()
    return render_template('index.html', repairs=repairs)

@app.route('/repairs', methods=['GET', 'POST'])
def repairs():
    form = CreateRepairForm()
    if form.validate_on_submit():
        repair = Repair(
            client=form.client.data,
            device=form.device.data,
            phone=form.phone.data,
            problem=form.problem.data,
            fix=form.fix.data,
            cost=form.cost.data,
            date=date.today().strftime("%d/%m/%Y")
        )
        db.session.add(repair)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('repairs.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
