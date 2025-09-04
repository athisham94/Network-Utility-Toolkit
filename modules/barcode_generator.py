import barcode
from barcode.writer import ImageWriter

def generate_barcode(data):
    code128 = barcode.get_barcode_class('code128')
    barcode_instance = code128(data, writer=ImageWriter())
    barcode_instance.save('barcode')
    print("Barcode saved as barcode.png")
