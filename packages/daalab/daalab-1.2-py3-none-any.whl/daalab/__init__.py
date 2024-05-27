from .codes import print_react_form, print_react_timetable, print_react_func, print_react_sp, print_react_routes, print_react_es5_es6, print_form_validation, print_bootstrap_table

# Import functions from the codes module
form = print_react_form
table = print_react_timetable
func_class = print_react_func
states_props = print_react_sp
routes = print_react_routes
es5_es6 = print_react_es5_es6
form_valid = print_form_validation
bootstrap_table = print_bootstrap_table

def list_functions():
    functions = {
        "form": "Print React Form",
        "table": "Print React Timetable",
        "func_class": "Print React Function and Class",
        "states_props": "Print React States and Props",
        "routes": "Print React Routes",
        "es5_es6": "Print React ES5 and ES6",
        "form_valid": "Print Form Validation",
        "bootstrap_table": "Print Bootstrap Table"
    }

    print("Available functions in the daalab library:")
    for name, description in functions.items():
        print(f"{name}: {description}")

# Call the list_functions function to display available functions
list_functions()
