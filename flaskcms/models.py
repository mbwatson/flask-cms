from flask import Flask, render_template, Markup
from flaskcms import app
import markdown
import yaml
import pathlib

class Page():
	def __init__(self, page_name):
		self.name = page_name
		self.config = self.get_config()
		self.template = self.config['template']
		self.content = self.get_content()
	def get_config(self):
		config = { 'template': 'default' }
		config_file = pathlib.Path(f'flaskcms/content/{self.name}.yaml')
		if config_file.is_file():
			with config_file.open('r') as f:
				config = yaml.load(f)
		return config
	def get_content(self):
		content = ''
		content_file = pathlib.Path(f'flaskcms/content/{self.name}.md')
		if content_file.is_file():
			with open(content_file, 'r') as f:
				content = Markup(markdown.markdown(f.read()))
		return content
	def build(self):
		template = self.config['template']
		content = self.content
		return render_template(f'{template}.html', page_content=content)

