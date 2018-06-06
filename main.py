from flask import Flask, render_template, Markup
import markdown

app = Flask(__name__)

def get_markdown(filename):
	with open('content/{}.md'.format(filename), 'r') as f:
		md = Markup(markdown.markdown(f.read()))
	return md

# Main Routes
@app.route('/')
def index():
	return render_template('page.html')

@app.route('/about')
def about():
	content = get_markdown('about')
	return render_template('page.html', page_content=content)

@app.route('/services')
def services():
	content = get_markdown('services')
	return render_template('page.html', page_content=content)

@app.route('/products')
def products():
	content = get_markdown('products')
	return render_template('page.html', page_content=content)

@app.route('/gallery')
def gallery():
	content = get_markdown('gallery')
	return render_template('page.html', page_content=content)

@app.route('/contact')
def contact():
	content = get_markdown('contact')
	return render_template('page.html', page_content=content)

# Error Pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
