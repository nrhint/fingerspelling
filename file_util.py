##Nathan Hinton
##This is for opening and handeling files in a consistent manner

def open_file(file_path, file_name, file_extension):
    try:
        return open('%s/%s.%s'%(file_path, file_name, file_extension), 'r').read()
    except FileNotFoundError:
        print('File not found! Invalid path of %s/%s.%s'%(file_path, file_name, file_extension))
        return 'Error'

def write_file(file_path, file_name, file_extension, output):
    try:
        try:
            print('trying to write file at: %s'%('%s/%s.%s'%(file_path, file_name, file_extension)))
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
        except FileNotFoundError:
            import os
            os.mkdir(file_path)
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
    except Exception as e:
        print('unable to write file.\nError: %s\nPath: %s/%s.%s'%(e, file_path, file_name, file_extension))
