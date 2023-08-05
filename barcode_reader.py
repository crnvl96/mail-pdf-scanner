from pdf2image import convert_from_path  # type: ignore
from pyzbar.pyzbar import decode  # type: ignore

from barcode_converter import barcode_converter


class BarcodeReader:
    def __init__(self, path):
        self.path = path
        self.type = "I25"
        self.utf8 = "utf-8"

    def barcode_reader(self):
        detected_barcodes = decode(convert_from_path(self.path)[0])

        if not detected_barcodes:
            return False
        else:
            for barcode in detected_barcodes:
                if barcode.data != "" and barcode.type == self.type:
                    return barcode_converter(barcode.data.decode(self.utf8))
