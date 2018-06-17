from flask import Flask, render_template, Markup
import markdown
import yaml
import pathlib

app = Flask(__name__)

class Page():
	def __init__(self, page_name):
		self.name = page_name
		self.config = self.get_config()
		self.template = self.config['template']
		self.content = self.get_content()
	def get_config(self):
		data = { 'template': 'default' }
		config_file = pathlib.Path(f'content/{self.name}.json')
		if config_file.is_file():
			with config_file.open('r') as f:
				data = yaml.load(f)
		return data
	def get_content(self):
		content = ''
		content_file = pathlib.Path(f'content/{self.name}.md')
		if content_file.is_file():
			with open(content_file, 'r') as f:
				content = Markup(markdown.markdown(f.read()))
		return content
	def build(self):
		template = self.config['template']
		content = self.content
		return render_template(f'{template}.html', page_content=content)

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
