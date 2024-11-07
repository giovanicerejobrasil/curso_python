"""
os.listdir para navegar em caminhos

/home/giovani-brasil/Desktop/Development/EXEMPLE
C:\\Users\\giovani\\Desktop\\Development\\EXEMPLE
caminho = r'C:\\Users\\giovani\\Desktop\\EXEMPLE'
"""
import os


path = os.path.join('/home', 'giovani-brasil',
                    'Desktop', 'Development', 'EXEMPLE')

for dir_ in os.listdir(path):
    full_path_dir = os.path.join(path, dir_)
    if not os.path.isdir(full_path_dir):
        continue

    print(dir_)

    for item in os.listdir(full_path_dir):
        print('   -', os.path.join(full_path_dir, item))
