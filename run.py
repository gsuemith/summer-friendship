from flask import Flask, render_template, flash, redirect, url_for
from forms import (CreateAccountForm, CreateParentForm, LoginForm,
                ParentRegistrationForm, ChildRegistrationForm)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b61c061b27638c88e2c19d40de59a84d'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/user/parent", methods=['GET', 'POST'])
def user_parent():
    form = CreateParentForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home', _anchor='continue'))
    return render_template('user_parent.html',
            title='Create Parent Account',
            form=form)

@app.route("/user/youth", methods=['GET', 'POST'])
def user_youth():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home', _anchor='continue'))
    return render_template('user_youth.html',
            title='Create Youth Account',
            form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@sf.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home', _anchor='continue'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Log In', form=form)

@app.route("/register/parent", methods=['GET', 'POST'])
def register_parent():
    form = ParentRegistrationForm()
    return render_template('register_parent.html', form=form, title='Register Family')

@app.route("/register/child", methods=['GET', 'POST'])
def register_child():
    form = ChildRegistrationForm()
    return render_template('register_parent.html', form=form, title='Register Family')

if __name__ == '__main__':
    app.run(debug=True)
