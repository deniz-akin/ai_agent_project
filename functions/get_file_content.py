import os

def get_file_content(working_directory, file_path):
    if file_path is None:
        file_path = "."
    
    full_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    try:
        if os.path.getsize(full_path) > MAX_CHARS:
            with open(full_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                return f'{file_content_string}[... File "{file_path}" truncated at 10000 characters]'
        else:
            with open(full_path, "r") as f:
                file_content_string = f.read()
                return file_content_string
    except Exception as e:
        return f'Error: {e}'
        
