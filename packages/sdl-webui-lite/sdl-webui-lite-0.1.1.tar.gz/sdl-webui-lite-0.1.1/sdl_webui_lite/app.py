import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from flask import Flask, render_template, request, flash
from utils import utils
from utils import scheduler
from flask_socketio import SocketIO

global deck
deck = None
app = Flask(__name__)
app.secret_key = 'key'

app.config['DEBUG'] = False
app.config['TITLE'] = "Self-Driving Lab"
app.config['LOG_FILENAME'] = "example.log"

socketio = SocketIO(app)
task_manager = scheduler.TaskManager()


@socketio.on('connect')
def handle_connect():
    # Fetch log messages from local file
    filename = app.config['LOG_FILENAME']
    with open(filename, 'r') as log_file:
        log_history = log_file.readlines()
    for message in log_history:
        socketio.emit('log_update', {'message': message})


@socketio.on('abort_action')
def handle_abort_action():
    task_manager.cancel_current_task()


@app.route('/home')
def index():
    return render_template("home.html", title=app.config['TITLE'])


def make_grid(row: int = 1, col: int = 1):
    """
    return the tray index str list by defining the size
    :param row: 1 to 26
    :param col: 1 to 26
    :return: return the tray index
    """
    letter_list = [chr(i) for i in range(65, 90)]
    return [[i + str(j + 1) for j in range(col)] for i in letter_list[:row]]


@app.route('/', methods=['GET', 'POST'])
def experiment():
    global deck
    grid = make_grid(5, 6)
    functions = utils.parse_functions(deck, debug=app.config['DEBUG'])
    if request.method == "POST":
        args = request.form.to_dict()
        function_name = args.pop('action')
        # vials = request.form.get()
        function_executable = getattr(deck, function_name)
        try:
            args, _ = utils.convert_type(args, functions[function_name])
        except Exception as e:
            flash(e)
            return render_template('experiment.html', functions=functions)
        if type(functions[function_name]) is dict:
            args = list(args.values())[0]
        try:
            output = ''
            if callable(function_executable):
                task_manager.add_task(function_executable, args)
            else:
                # for setter
                function_executable = args
            # flash(f"\nRun Success! Output value: {output}.")
        except Exception as e:
            flash(e)
    return render_template("experiment.html", functions=functions, title=app.config['TITLE'])


def start_gui(module, logger: str | list = None, host="0.0.0.0", port=8000, debug=app.config['DEBUG']):
    global deck
    deck = module
    logger_list = [task_manager.__class__.__name__]
    if type(logger) is str:
        logger_list.append(logger)
    elif type(logger) is list:
        logger_list.extend(logger)
    for log in logger_list:
        utils.start_logger(socketio, log_filename=app.config['LOG_FILENAME'], logger_name=log)
    socketio.run(app, host=host, port=port, debug=debug, use_reloader=False, allow_unsafe_werkzeug=True)


if __name__ == '__main__':
    # start_logger()
    # app.run()
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True, debug=True)
