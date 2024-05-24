import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import shutil
def convert_to_whl():
    os.chdir(file_path)
    subprocess.run(['python', f'{file_path}\setup.py', 'bdist_wheel'], shell=True)
    for file in os.listdir('dist'):
        if file.endswith('.whl'):
            shutil.move(os.path.join('dist', file), os.path.join(file_path, file))
    shutil.rmtree('dist')
    shutil.rmtree('build')
    os.remove(f'{package_name}.bat')
    os.remove('setup.py')
    shutil.rmtree(f'{package_name}.egg-info')
def distribute_win():
    complete.destroy()
    def distribute():
        token = token_entry.get()
        command = f'twine upload --repository-url https://upload.pypi.org/legacy/ --username __token__ --password {token} {file_path}\{package_name}-0.0.0-py3-none-any.whl'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        messagebox.showinfo("Disrtibution Complete!", f"Project posted on PyPI install it with 'pip install {package_name}'")
    root = tk.Tk()
    token_label = tk.Label(root, text="Enter your PyPI API token:")
    token_label.pack()
    token_entry = tk.Entry(root)
    token_entry.pack()
    distribute_button = tk.Button(root, text="Distribute", command=distribute)
    distribute_button.pack()
    root.mainloop()
def generate_bat(package_name):
    batch_file_content = f"""
@echo off
setlocal
cd /d "%~dp0"
python __init__.py %*
endlocal
"""
    with open(f'{file_path}\{package_name}.bat', 'w') as batch_file:
        batch_file.write(batch_file_content)
def generate_setup_py(package_name):
    setup_content = f"""
from setuptools import setup, find_packages
setup(
    name='{package_name}',
    packages=['{file_path}'],
    scripts=[f'{package_name}.bat', '__init__.py']
)
"""
    with open(f'{file_path}\setup.py', 'w') as setup_file:
        setup_file.write(setup_content)
def browse_script():
    global file_path, package_name
    file_path = filedialog.askdirectory()
    script_entry.delete(0, tk.END)
    script_entry.insert(0, file_path)
    package_name = os.path.basename(file_path)
    package_name = package_name.replace("-", "_")
def convert_button_click():
    global complete
    generate_bat(package_name)
    generate_setup_py(package_name)
    convert_to_whl()
    root.destroy()
    messagebox.showinfo("Conversion Complete", "Conversion to .whl completed successfully!")
    complete = tk.Tk()
    complete.title("Distribute")
    distribute_button = tk.Button(complete, text="Distribute on PyPI", command=distribute_win)
    distribute_button.pack()
root = tk.Tk()
root.title("Python to .whl Converter")
script_label = tk.Label(root, text="Python Script:")
script_entry = tk.Entry(root)
browse_button = tk.Button(root, text="Browse", command=browse_script)
convert_button = tk.Button(root, text="Convert to .whl", command=convert_button_click)
script_label.grid(row=0, column=0)
script_entry.grid(row=0, column=1)
browse_button.grid(row=0, column=2)
convert_button.grid(row=2, columnspan=3)
root.mainloop()
