"""
Aula extra sobre pathlib
"""
from pathlib import Path


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


project_path = Path()

print_division(text='path absolute')
print(project_path.absolute())

file_path = Path(__file__)

print_division(text='path', jump=True)
print(file_path)

print_division(text='path parent', jump=True)
print(file_path.parent)

print_division(text='path parent parent', jump=True)
print(file_path.parent.parent)

print_division(text='path parent new folder', jump=True)
idea_ = file_path.parent / 'idea'
print(idea_)
print()
print(idea_ / 'file.txt')

print_division(text='path home', jump=True)
print(Path.home())
print()
print(Path.home() / 'Desktop')
print()
print(Path.home() / 'Desktop' / 'file.txt')

print_division(text='path home file touch', jump=True)
new_file = Path.home() / 'Desktop' / 'new_file.txt'
new_file.touch()
new_file.write_text('Hello World!')

print(new_file)
print()
print(new_file.read_text())

new_file.unlink()

print_division(text='path home file with open (a+)', jump=True)
new_file_path = Path.home() / 'Desktop' / 'new_file.txt'

with new_file_path.open('a+') as new_file_:
    new_file_.write('Hello World!\n')
    new_file_.write('Hello Again!\n')
    new_file_.write('Hello Again Again!\n')

    print(new_file_path)
    print()

print(new_file_path.read_text())
new_file_path.unlink()

print_division(text='path home mkdir', jump=True)
folder_path = Path.home() / 'Desktop' / 'new_folder'
folder_path.mkdir(exist_ok=True)
subfolder_path = folder_path / 'subfolder'
subfolder_path.mkdir(exist_ok=True)

other_file_path = subfolder_path / 'file_1.txt'
other_file_path.touch()
other_file_path.write_text("Giovani, 27, Desenvolvedor")

more_file_path = folder_path / 'file_2.txt'
more_file_path.touch()
more_file_path.write_text("Luanna, 24, Professora")

# folder_path.rmdir()

files = folder_path / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Hello World\n')
        text_file.write(f'file_{i}.txt')


def rmtree(root: Path, remove_root: bool = True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(folder_path)
