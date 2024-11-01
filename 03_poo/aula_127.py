"""
Mantendo estados dentro da classe
"""


class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.name} já está filmando...')
            return

        print(f'{self.name} está filmando...')
        self.recording = True

    def stop_record(self):
        if not self.recording:
            print(f'{self.name} não está filmando...')
            return

        print(f'{self.name} está parando de filmar...')
        self.recording = False

    def take_photo(self):
        if self.recording:
            print(f'{self.name} não pode fotografar filmando...')
            return

        print(f'{self.name} está tirando uma foto...')


def print_division(num_repeat=50):
    print('', '=' * num_repeat, '', sep='\n')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.record()
c1.record()
c1.take_photo()
c1.stop_record()
c1.take_photo()

print_division()

c2.stop_record()
c2.record()
c2.take_photo()
c2.record()
c2.stop_record()
c2.take_photo()
