
def css_from_file(filename):
    with open(f'tests/assets/{filename}', 'r') as sheet:
    #Removes trailing \n added by file.read() method
        return '\n'.join(sheet.read().split('\n')[:-1])

