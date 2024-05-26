
import os, sys, argparse
from pypi_project.config import PACKAGE_NAME, EXECUTABLE_PATH, COMMAND_NAME
from pypi_project.config import PYPI_PACKAGE_NAME_PLACEHOLDER, PYPI_LICENSE_CHOICES
from pypi_project.config import RED, GREEN, CYAN, NC

def raise_error(error_message = "Unknown error happened. "): 
    print (f"{RED}Error{NC}: {error_message}")
    sys.exit(1)

def main(): 

    if (sys.argv[0] != os.path.join(EXECUTABLE_PATH, COMMAND_NAME)): 
        return

    # Capture the current terminal path
    pypi_terminal_path = os.getcwd()

    # Define the parsers and subparsers
    parser = argparse.ArgumentParser(description=f"Easier PyPI package creations, publishments and more in shell. ")
    parsers = parser.add_subparsers(dest='command')
    parser_create = parsers.add_parser('create', 
                                       description=f"Create a new PyPI package with the specified name. ", 
                                       help=f"Create a new PyPI package with the specified name. Enter {CYAN}pypi create --help{NC} for more info. ")
    parser_create_optional = parser_create.add_argument_group()
    parser_create.add_argument('name', metavar='<name>', nargs='?',
                                    help=f"(Required) The name of the new PyPI package.")
    parser_create_optional.add_argument('--path', nargs='?', 
                                    default=pypi_terminal_path, 
                                    help=f"(Optional) The path to create the new PyPI package. Default: {pypi_terminal_path}. The path/{PYPI_PACKAGE_NAME_PLACEHOLDER} should not exist prior to the packet creation. ")
    parser_create_optional.add_argument('--license', nargs='?', 
                                    choices=list(PYPI_LICENSE_CHOICES.keys()), 
                                    default=list(PYPI_LICENSE_CHOICES.keys())[0], 
                                    help=f"(Optional) The license of the new PyPI package. Default: {list(PYPI_LICENSE_CHOICES.keys())[0]}")
    parser_create_optional.add_argument('--version', nargs='?', 
                                    default="0.1.0", 
                                    help=f"(Optional) The version of the new PyPI package, following the scheme in https://peps.python.org/pep-0440/#final-releases. Default: 0.1.0")
    parser_create_optional.add_argument('--command', dest='cmd', nargs='?', 
                                    default=PYPI_PACKAGE_NAME_PLACEHOLDER, 
                                    help=f"(Optional) The command to activate the new PyPI package after installation. Default: {PYPI_PACKAGE_NAME_PLACEHOLDER}")
    parser_args = parser.parse_args()
    if (not parser_args): 
        parser.print_help()
        return

    # Capture the arguments
    if (parser_args.command == "create"): 

        if (len(sys.argv) == 2): 
            parser_create.print_help()
            return

        # Get the name of the PyPI package
        pypi_package_name = parser_args.name
        def is_valid_pypi_package_name(package_name):
            import re, keyword
            if not package_name.isascii(): return False
            if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_\-]*$", package_name): return False
            if keyword.iskeyword(package_name): return False
            return True
        if not is_valid_pypi_package_name(pypi_package_name):
            raise_error("Invalid PyPI package name. Please follow the naming rules in https://www.w3schools.com/python/gloss_python_variable_names.asp. ")

        # Get the path of the PyPI package
        pypi_package_path = os.path.join(parser_args.path, pypi_package_name)
        try: 
            os.path.normpath(pypi_package_path)
            if (os.path.exists(pypi_package_path)): raise FileExistsError
            os.makedirs(os.path.join(pypi_package_path, pypi_package_name))
        except FileExistsError:
            raise_error(f"The PyPI package path '{pypi_package_path}' already exists. Remove it to allow storing the package files without unforeseen effects. ")
        except Exception:
            raise_error(f"Invalid PyPI package path: {pypi_package_path}. ")

        # Get the version of the PyPI package
        pypi_package_version = parser_args.version
        def parse_pypi_version(version_string):
            import re
            pattern = r'^(\d+)(?:\.(\d+))?(?:\.(\d+))?.*?$'
            match = re.match(pattern, version_string)
            if match:
                major = int(match.group(1))
                minor = int(match.group(2) or '0')
                macro = int(match.group(3) or '0')
                return [major, minor, macro]
            else: return None
        pypi_package_version = parse_pypi_version(pypi_package_version)
        if (not pypi_package_version): 
            raise_error(f"Invalid PyPI version: {parser_args.version}. ")
        major, minor, macro = pypi_package_version

        pypi_package_cmd = parser_args.cmd
        if (pypi_package_cmd == PYPI_PACKAGE_NAME_PLACEHOLDER): 
            pypi_package_cmd = parser_args.name

        
        # Write the package config file
        pypi_package_name__config_content = f'''
import os, sys

pypi_PACKAGE_NAME = "{pypi_package_name}"
pypi_PACKAGE_PATH = "{os.path.join(pypi_package_path, pypi_package_name)}"
pypi_PACKAGE_VERSION = {pypi_package_version}
pypi_EXECUTABLE_PATH = os.path.dirname(sys.executable)
pypi_COMMAND_NAME = "{pypi_package_cmd}"
'''
        with open(os.path.join(pypi_package_path, pypi_package_name, "config.py"), "w") as setup_py_file:
            setup_py_file.write(pypi_package_name__config_content)

if __name__ == '__main__': 
    main()
