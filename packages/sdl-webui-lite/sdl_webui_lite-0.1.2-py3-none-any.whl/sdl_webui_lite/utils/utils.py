import inspect
import logging

from flask_socketio import SocketIO

"""
utility functions for app.py
"""


def parse_functions(class_object=None, debug=False):
    functions = {}
    under_score = "__" if debug else "_"
    for function in dir(class_object):
        if not function.startswith(under_score) and not function.isupper():
            try:
                att = getattr(class_object, function)
                # handle getter setters
                if callable(att):
                    functions[function] = inspect.signature(att)
                else:
                    att = getattr(class_object.__class__, function)
                    if isinstance(att, property) and att.fset is not None:
                        setter = att.fset.__annotations__
                        setter.pop('return', None)
                        if setter:
                            functions[function] = setter
            except Exception:
                pass
    return functions


def convert_type(args, parameters):
    bool_dict = {"True": True, "False": False}
    arg_types = {}
    if args:
        for arg in args:
            if args[arg] == '' or args[arg] == "None":
                args[arg] = None
                arg_types[arg] = _get_type_from_parameters(arg, parameters)
            elif args[arg] == "True" or args[arg] == "False":
                args[arg] = bool_dict[args[arg]]
                arg_types[arg] = 'bool'
            elif args[arg].startswith("#"):
                args[arg] = args[arg]
                arg_types[arg] = _get_type_from_parameters(arg, parameters)
            elif type(parameters) is inspect.Signature:
                p = parameters.parameters
                if p[arg].annotation is not inspect._empty:
                    if p[arg].annotation.__module__ == 'typing':
                        arg_types[arg] = p[arg].annotation.__args__
                        for i in p[arg].annotation.__args__:
                            try:
                                args[arg] = eval(f'{i}({args[arg]})')
                                break
                            except Exception:
                                pass
                    else:
                        args[arg] = p[arg].annotation(args[arg])
                        arg_types[arg] = p[arg].annotation.__name__
                else:
                    try:
                        args[arg] = eval(args[arg])
                        arg_types[arg] = ''
                    except Exception:
                        pass
            elif type(parameters) is dict:
                if parameters[arg]:
                    if parameters[arg].__module__ == 'typing':
                        # arg_types[arg] = parameters[arg].__args__
                        for i in parameters[arg].__args__:
                            # print(i)
                            try:
                                args[arg] = eval(f'{i}({args[arg]})')
                                arg_types[arg] = i.__name__
                                break
                            except Exception:
                                pass
                    else:
                        args[arg] = parameters[arg](args[arg])
                        arg_types[arg] = parameters[arg].__name__
    return args, arg_types


def _get_type_from_parameters(arg, parameters):
    arg_type = ''
    if type(parameters) is inspect.Signature:
        p = parameters.parameters
        if p[arg].annotation is not inspect._empty:
            # print(p[arg].annotation)
            if p[arg].annotation.__module__ == 'typing':
                arg_type = p[arg].annotation.__args__
            else:
                arg_type = p[arg].annotation.__name__
            # print(arg_type)
    elif type(parameters) is dict:
        if parameters[arg]:

            if parameters[arg].__module__ == 'typing':
                arg_type = [i.__name__ for i in parameters[arg].__args__]
            else:
                arg_type = parameters[arg].__name__
    return arg_type


class SocketIOHandler(logging.Handler):
    """rewrite SocketIOHandler for logging"""

    def __init__(self, socketio: SocketIO):
        super().__init__()
        self.formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.socketio = socketio

    def emit(self, record):
        message = self.format(record)
        self.socketio.emit('log_update', {'message': message})


def start_logger(socketio: SocketIO, log_filename, logger_name):
    """start logger and configure log file and socketio handler"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(filename=log_filename)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'), )
    logger.addHandler(file_handler)
    socketio_handler = SocketIOHandler(socketio)
    logger.addHandler(socketio_handler)
