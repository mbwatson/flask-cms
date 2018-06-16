# Flask CMS

This is simply a general exploration into how one may create a flask-based cms from scratch.

## A few details:

* Pages are objects.
* Page content is stored in external markdown files.
* Page attributes are stored in external files in JSON format, such as which template to use. (Obviously more configurations will be necessary to implement in the future.)

## To Use

Clone this repo, and fire up your python development server by executing `python main.py` and pointing your browser at `localhost:5000`. You'll need to `pip install` the following packages: `markdown`, `pathlib`, and `flask`.