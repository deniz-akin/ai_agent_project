import os, subprocess
def run_python_file(working_directory, file_path):
    if file_path is None:
        file_path = "."
    
    full_path = os.path.abspath(os.path.join(working_directory,file_path))
    if os.path.commonpath([full_path, os.path.abspath(working_directory)]) != os.path.abspath(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.lower().endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python", full_path],
                                capture_output=True,
                                text=True,
                                timeout=30,
                                cwd=working_directory,
                                )
        if not result.stdout and not result.stderr:
            return "No output produced."
        if result.returncode != 0:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nProcess exited with code {result.returncode}\n"
        else:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
