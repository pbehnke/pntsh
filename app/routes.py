from flask import render_template
from pathlib import Path
from markupsafe import escape

from app import app
from app.utils import colorize

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.txt")


@app.route('/list')
def list():
    cmds_path = Path.cwd().joinpath("app","cmds")
    cmds_available = [ x.stem for x in cmds_path.glob("*.txt") if x.stem not in ["index", "list"] ]
    return render_template("list.txt", cmds_available=cmds_available)

@app.route('/<cmd>')
def get_cmd(cmd=None):
    filename = escape(cmd) + ".txt"
    cmds_path = Path.cwd().joinpath("app","cmds")
    filename_path = cmds_path.joinpath(filename)
    if filename_path.exists():
        text = filename_path.read_text()
        return colorize(text)
    else :
        return "File not accessible\n"
