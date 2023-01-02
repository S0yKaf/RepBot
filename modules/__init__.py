import os
import importlib

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

plugins = []

# AI GENERATED CODE (minus fixing AIs dumb shits)

print("Loading modules...")
# Iterate over all files in the current directory
for file in os.listdir(current_dir):
    # If the file is a python file
    if file.endswith('.py'):
        # Get the module name by removing the '.py' extension
        module_name = file[:-3]
        # Skip the current file
        if module_name == '__init__':
            continue
        if module_name == 'Module':
            continue
        # Import the module
        module = importlib.import_module("." + module_name, "modules")
        # Iterate over all the objects in the module
        for obj in dir(module):
            # If the object is a class
            if obj == module_name:
                # Initialize the class
                plugins.append(getattr(module, obj)())
                print(f"loaded : {module_name}")
                break

print("Done loading modules!")
