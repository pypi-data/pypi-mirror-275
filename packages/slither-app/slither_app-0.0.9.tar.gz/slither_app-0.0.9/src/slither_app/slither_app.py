# TODO turn this into a module some day

import argparse as ap
import os
import os.path as p
import typing as typ
import datetime as dt
import pprint
import sys


def attach_to_parser(parser: ap.ArgumentParser):
    """When supplied with an existing `argparse.ArgumentParser` instance,
    adds arguments associated with run_app to it.

    Typical usage:

    .. code:: python

        parser = ap.ArgumentParser()
        attach_to_parser(parser)
        args = parser.parse_args()

    :param parser: an initialised argument
        parser
    :type parser: argparse.ArgumentParser
    """

    # add run_app arguments to parser
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="""Suppress all messages made by this program.
            Doesn't suppress python exceptions.""",
        dest="CNF_SILENT",
        default=None,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="""Increase verbosity. Shows warnings and diagnostic
            messages in addition to errors, which are displayed by
            default.""",
        dest="CNF_VERBOSE",
        default=None,
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="""Enable diagnostic code. May slow the program down
        considerably, only use if something went wrong. Enables verbosity
        as with --verbose, but also shows debug messages in addition.""",
        dest="CNF_DEBUG",
        default=None,
    )

    parser.add_argument(
        "--dir-work",
        action="store",
        help="""Override work directory, for temporary files.""",
        metavar="/path/to/workdir",
        dest="CNF_TMP",
    )

    parser.add_argument(
        "--dir-data",
        action="store",
        help="""Override data directory, for output files""",
        metavar="/path/to/datadir",
        dest="CNF_PRODUCTS",
    )


def create_parser(
    parse_args: bool = False,
) -> typ.Tuple[ap.ArgumentParser, typ.Optional[ap.Namespace]]:
    """Creates a parser with run_app arguments. If ``parse_args`` is ``True``,
    parses arguments and returns the parsed argparse.Namespace object
    along with the parser instance. If it is ``False``, returns None
    along with the parser instance.

    :param parse_args: Whether to parse arguments , defaults to False
    :type parse_args: bool, optional
    :return: A tuple containing the argument parser instance and either
        None, or the Namespace object
    :rtype: (`ap.ArgumentParser`, ``None``) or (`ap.ArgumentParser`, `ap.Namespace`)
    """

    parser = ap.ArgumentParser()

    attach_to_parser(parser)

    if parse_args:
        args = parser.parse_args()
    else:
        args = None

    return parser, args


class Env_parser:
    """An object that associates with an argument parser and its namespace when
    created. It allows you to parse environment variables and decide defaults for those arguments that
    are not explicitly set (overriden) by the user on the command line."""

    def __init__(self, arg_parser=None, parsed_args=None, defaults=None):
        # get parser and parsed args from function arguments
        self.parser = arg_parser
        self.args = parsed_args if parsed_args is not None else ap.Namespace()
        filename = sys.argv[0].split("/")[-1].split(".")[0]

        self.arglist = [
            "CNF_SILENT",
            "CNF_DEBUG",
            "CNF_VERBOSE",
            "CNF_TMP",
            "CNF_PRODUCTS",
        ]
        # set default defaults
        self.defaults = {
            "CNF_SILENT": False,
            "CNF_DEBUG": False,
            "CNF_VERBOSE": False,
            "CNF_TMP": p.expanduser(f"~/work/{filename}"),
            "CNF_PRODUCTS": p.expanduser(f"~/data/{filename}"),
        }

        # if defaults provided, overwrite default defaults with them,
        # but do it key by key, so keys that are not provided still
        # retain the default default.
        if type(defaults) == "dict":
            for key in defaults.keys():
                self.defaults[key] = defaults[key]

        # if provided defaults is not a dict, raise an error
        elif defaults is not None:
            raise TypeError(
                "Env parser instantiation argument `defaults` must be a "
                "dict. See init function docstring."
            )

    def parse_env(self):
        """Parses `run_app` env vars and sets the attached namespace variables based on them,
        unless they were set by command line arguments."""

        # create list for bool args so they can be correctly set by env vars
        bools = []

        # fill the list of bool args with the arg variable (destination) names
        # but only if parser is present.
        if self.parser is not None:
            for arg in self.parser.__dict__["_actions"]:
                if type(arg) == ap._StoreTrueAction:
                    bools.append(arg.dest)

        # go over each arg
        for arg in self.arglist:
            # if command line argument exists
            if getattr(self.args, arg, None) is not None:
                # let it be, let it be, there will be an answer, let it be
                continue

            # if not, but environment variable exists
            elif os.getenv(arg):
                # override the default value

                # if it's one of the booleans, set True regardless of value (but
                # ignore empty string too, just in case)
                if arg in bools and getattr(self.args, arg) != "":
                    setattr(self.args, arg, True)
                # otherwise use the value
                setattr(self.args, arg, os.getenv(arg))

            # if neither exists, use default
            else:
                setattr(self.args, arg, self.defaults[arg])

    def push_env(self):

        """Propagates command line arguments from the attached argparse namespace to associated
        environment variables."""

        # pushes args back to the env vars
        for arg in self.arglist:
            if arg in self.args.__dict__:
                value = getattr(self.args, arg)
                if value:
                    os.environ[arg] = str(getattr(self.args, arg))
                elif not value:
                    os.environ.pop(arg, None)
            else:
                setattr(self.args, arg, False)


########################################################################
# region Verbosity handling and other printy stuff


class Loudmouth:
    """An object that facilitates verbosity. It defines only one method,
    :func:`Loudmouth.message`. The reason why this is not a module function is to namespace it, as
    `message` is a pretty generic name.

    Typical usage:

    .. code:: python

        L = slither_app.Loudmouth(args)

        L.message("This is some command line output generated by my program!")
        L.message("something sinister is going on", "warning")

    where `args` is an argparse namespace object.
    """

    def __init__(self, args):
        self.args = args

    def _message(self, message: str, severity: str = None):
        """Prints messages to standard output. Includes date and
        time, name of the app that issued it and the severity of the message, if provided.

        :param message: The message body
        :type message: str
        :param severity: A string prepended to the message, in brackets, defaults to None
        :type severity: str, optional
        """

        stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        severity_string = " " + severity.upper() + ":" if severity else ""
        print(f"[{stamp}] grib_prep:{severity_string} {message}")

        # define message function based on verbosity options
        # nothing if silent, overrides all other verbosity

    def message(self, message: str, severity: str = None):
        """Prints messages to standard output, based on their severity values.

        Messages are displayed with the following rules:
            - **severity=None** - message displays only if verbosity or debug are enabled
            - **severity='error'** - message displays unless silent is enabled
            - **severity='warning'** - message displays unless silent is enabled
            - **severity='debug'** - message displays only if debug is enabled

        :param message: The message body
        :type message: str
        :param severity: A string which decides under which conditions (env vars or args) the message gets displayed, defaults to None, which only displays warnings and errors
        :type severity: str, optional
        """

        if self.args.CNF_SILENT:
            pass

        # print everything, overrides verbose
        elif self.args.CNF_DEBUG:
            self._message(message, severity)

        # print everything except debug messages if verbose
        elif self.args.CNF_VERBOSE and severity != "debug":
            self._message(message, severity)

        # only errors and warnings by default
        else:
            if severity in ("error", "warning"):
                self._message(message, severity)


class Loudmouth_dummy:
    """Defines the message command so that it does nothing, this is necessary if
    you use sphinx to generate docs. Having this dummy objects allows you to keep ``L.message``
    scattered across your program even if you choose not to have an argparse.Namespace object with
    parsed args present (which is the point when sphinx fails). The intended usage is:

    .. code:: python

        if __name__ == '__main__':
            # create parser, parse args and create loudmouth
            parser, args, L = slither_app.basic_init()
        else:
            # create fake loudmouth that does nothing
            L = slither_app.Loudmouth_dummy()

    This snippet creates the argument parser, parses the args and creates the regular
    :class:`Loudmouth` if the app is run. If it's imported, no argument parser is created and the
    dummy Loudmouth is instantiated instead of the regular one. Then all calls to ``L.message``
    will do nothing, but they'll also not produce any error."""

    def message(self, message=None, severity=None):
        """Does nothing."""
        pass


class Loudmouth_child(Loudmouth):
    """I forgot what this was for, so consider it deprecated, I guess."""

    def __init__(self):
        self.envparser = Env_parser()
        self.envparser.parse_env()
        self.args = self.envparser.args


# endregion
########################################################################


def basic_init():
    """Creates an argument parser, parses env vars and creates a :class:`Loudmouth` instance.
    Intended as a one-liner for when you don't need any additional arguments.

    Typical usage:

    .. code:: python

        parser, args, L = slither_app.basic_init()

    :return: (parser, args, loudmouth)
    :rtype: (argparse.ArgumentParser, argparse.Namespace, :class:`Loudmouth()`)
    """

    # argument parser
    parser, args = create_parser(parse_args=True)
    # env parser
    parser_env = Env_parser(parser, args)
    parser_env.parse_env()
    parser_env.push_env()
    # verbosity handler
    loudmouth = Loudmouth(args)

    return parser, args, loudmouth
