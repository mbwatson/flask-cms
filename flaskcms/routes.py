from flaskcms import app
from flaskcms.models import Page

# Main Routes

@app.route('/')
def index():
	page = Page('index')
	return page.build()

@app.route('/about')
def about():
	page = Page('about')
	return page.build()

@app.route('/services')
def services():
	page = Page('services')
	return page.build()

@app.route('/products')
def products():
	page = Page('products')
	return page.build()

@app.route('/contact')
def contact():
	page = Page('contact')
	return page.build()

# Error Page Routes

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
