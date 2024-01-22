import os
import time 

def file_create_delete(file_name, operation):
    data = input ("Enter the data you want to save:" )
    if operation == 'create':
        with open(file_name, 'w') as file:
            file.write(data)
        print(f"{file_name} file has been created.")
    elif operation == 'delete':
        import os
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} file has been deleted.")
        else:
            print(f"{file_name} file not found.")
    else:
        print("Invalid operation. Please specify 'create' or 'delete'.")

file_create_delete("new_file.txt", 'create')
file_create_delete("new_file.txt", 'delete')
