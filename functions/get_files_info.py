import os
def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."
    
    file_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(file_path)


    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    lines = []
    try:
        for f in os.listdir(full_path):
            entry_path = os.path.join(full_path, f)
            lines.append(f'- {f}: file_size={os.path.getsize(entry_path)}, is_dir={os.path.isdir(entry_path)}')
        file_string = "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
    return file_string