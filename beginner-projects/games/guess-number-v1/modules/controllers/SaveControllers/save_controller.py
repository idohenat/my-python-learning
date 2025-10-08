def read_save_file(file_name):
    with open(file_name, "r") as file:
        return file.read()
    
def write_save_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(str(content)) 