from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User, Posting
from market.forms import RegisterForm, LoginForm, UploadForm
from market import db
from flask_login import login_user, logout_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    postings = Posting.query.all()
    return render_template('market.html', postings=postings)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
	form = RegisterForm()
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data,
							  email_address=form.email_address.data,
							  password=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('market_page'))
	if form.errors != {}: # if there are not errors from the validations
		for err_msg in form.errors.values():
			flash(f'There was an error with creating a user: {err_msg}', category='danger')
	return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.check_password_correction(
				attempted_password=form.password.data
		):
			login_user(attempted_user)
			flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
			return redirect(url_for('market_page'))
		else:
			flash('Username and password are not matched! Please try again', category='danger')
			
	return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
	logout_user()
	flash("Successfully logged out!", category='info')
	return redirect(url_for("home_page"))

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
	form = UploadForm()
	# flash("You can upload your baobei's info now!", category='info')
	if form.validate_on_submit():
		posting_to_create = Posting(image = form.image.data,
							itemname = form.itemname.data,
							email_address = form.email_address.data,
							phone = form.phone.data,
							date = form.date.data,
							pick_address = form.pick_address.data,
							price = form.price.data,
							description = form.description.data,
							)
		db.session.add(posting_to_create)
		db.session.commit()
		flash(f'Successfully uploaded!', category='success')
		return redirect(url_for('profile_page'))
	if form.errors != {}: # if there are not errors from the validations
		for err_msg in form.errors.values():
			flash(f'There was an error with posting an item: {err_msg}', category='danger')
	return render_template('upload.html', form=form)


@app.route('/info/<string:id>', methods=['GET', 'POST'])
def info_page(id):
	form = UploadForm()
	posting = Posting.query.filter_by(id=int(id)).one()
	# flash(f'Information of item {itemid}')
	return render_template('moreinfo.html', form=form, posting=posting)

@app.route('/profile/<string:userid>', methods=['GET', 'POST'])
def profile_page(userid):
	user = User.query.filter_by(id=int(userid)).one()
	return render_template('profile.html', user=user)