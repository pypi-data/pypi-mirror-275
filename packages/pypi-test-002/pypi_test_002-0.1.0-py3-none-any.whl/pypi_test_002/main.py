
import os, sys, argparse
from pypi_test_002.config import pypi_PACKAGE_NAME, pypi_PACKAGE_PATH, pypi_PACKAGE_VERSION, pypi_EXECUTABLE_PATH, pypi_COMMAND_NAME
from pypi_test_002.config import RED, GREEN, CYAN, NC

def main(): 

    # only handle the commands starting with pypi_COMMAND_NAME
    if (not sys.argv[0] == os.path.join(pypi_EXECUTABLE_PATH, pypi_COMMAND_NAME)): 
        return
    
    print ("Hello World! ")
    print (f'''
New PyPI package name: {pypi_PACKAGE_NAME}
New PyPI package path: {pypi_PACKAGE_PATH}
New PyPI package version: {'.'.join(pypi_PACKAGE_VERSION)}

Congratulations 🚀🤩! You have successfully created and uploaded the {pypi_PACKAGE_NAME} package. 
To start, open the main.py file (/Applications/GitHub Projects/PyPI-Project/pypi_test_002/pypi_test_002/main.py)

Define more conditions in the main() function to add functions to commands starting with {pypi_COMMAND_NAME}. For example, if you want the command "{pypi_COMMAND_NAME} greet" to greet the user, define main.py as follows: 

{CYAN}
import os, sys, argparse
from {pypi_PACKAGE_NAME}.config import pypi_PACKAGE_NAME, pypi_PACKAGE_PATH, pypi_EXECUTABLE_PATH, pypi_COMMAND_NAME
from pypi_project.config import RED, GREEN, CYAN, NC

def raise_error(error_message = "Unknown error happened. "): 
    print (f"{{RED}}Error{{NC}}: error_message")
    sys.exit(1)

def main(): 
    
    # only handle the commands starting with pypi_COMMAND_NAME
    if (not sys.argv[0] == os.path.join(pypi_EXECUTABLE_PATH, pypi_COMMAND_NAME)): 
        return
    
    # Define the main parser
    parser = argparse.ArgumentParser(description=f"Description of the new PyPI package. ")
    parsers = parser.add_subparsers(dest='command')
           
    # Define the sub parser for the greet command
    parser_greet = parsers.add_parser('greet', 
                                       description=f"Greet the user. ", 
                                       help=f"Greet the user. Enter pypi create --help for more info. ")
    parser_greet_optional = parser_greet.add_argument_group()
    parser_create_optional.add_argument('--name', nargs='?', 
                                    default=None, 
                                    help=f"(Optional) The name of the user to greet. ")
        
    # Parse the args
    parser_args = parser.parse_args()

    # Display the help info if no args
    if (not parser_args): 
        parser.print_help()
        return

    # The greet argument
    if (parser_args.command == "greet"): 

        # Display the help info if no args
        if (len(sys.argv) == 2): 
            parser_greet.print_help()
            return
        
        # Greet the user differently depending on whether the name is available
        if (parser_args.name): 
            print ("Nice to meet you, {pypi_test_002}! ")
        else: 
            print ("Nice to meet you! ")

{NC}
    
        ''')

