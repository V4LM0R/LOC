import os

def count_loc(directory):
    total_loc = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html') or filename.endswith('.css') or filename.endswith('.js'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    loc = len([line for line in lines if line.strip() != ''])
                    print(f'{filepath}: {loc} lines')
                    total_loc += loc
    return total_loc

if __name__ == "__main__":
    directory = 'Simple-html-portfolio'  
    total_loc = count_loc(directory)
    print(f'Total líneas de código: {total_loc}')
