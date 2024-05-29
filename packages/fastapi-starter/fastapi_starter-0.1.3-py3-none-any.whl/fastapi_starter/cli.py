import sys
import os
import shutil
def create_app(app_name):
    current_dir = os.path.dirname(__file__)
    template_dir = os.path.join(current_dir, '..', 'templates', 'app_template')
    app_dir = os.path.join(os.getcwd(), app_name)

    if os.path.exists(app_dir):
        print(f"Error: Directory '{app_dir}' already exists.")
        return

    shutil.copytree(template_dir, app_dir)
    print(f"App '{app_name}' created successfully at {app_dir}.")

import os
import sys
import importlib.util
import shutil

def main():
    if len(sys.argv) < 2:
        print("Usage: fastapi_starter <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "startapp":
        if len(sys.argv) != 3:
            print("Usage: fastapi_starter startapp <app_name>")
            return
        app_name = sys.argv[2]
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', 'app_template'))
        app_dir = os.path.join(os.getcwd(), app_name)
        if not os.path.exists(template_dir):
            print(f"Error: Template directory '{template_dir}' not found.")
            return
        shutil.copytree(template_dir, app_dir)
        print(f"App '{app_name}' created successfully at {app_dir}.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

