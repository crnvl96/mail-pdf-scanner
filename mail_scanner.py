import os
import uuid
from datetime import datetime, timedelta

from imbox import Imbox  # type: ignore

from barcode_reader import BarcodeReader


class MailScanner:
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = open(password, "r").read()
        self.host = "imap.gmail.com"
        self.download_folder = "bills"
        self.thrash_folder = "thrash"

        self.make_dir(self.download_folder)
        self.make_dir(self.thrash_folder)

    def make_dir(self, path: str):
        if not os.path.exists(path):
            os.makedirs(path)

    def download_bills(self):
        mail = Imbox(
            self.host,
            username=self.user,
            password=self.password,
            ssl=True,
        )

        messages = mail.messages(
            date__gt=datetime.today() - timedelta(days=30),
            raw="has:attachment",
        )

        for _, message in messages:
            for attach in message.attachments:
                file_name = attach.get("filename")
                if ".pdf" in file_name:
                    key = str(uuid.uuid4())
                    output_path = os.path.join(
                        self.download_folder,
                        key + ".pdf",
                    )

                    file = open(output_path, "wb")
                    file.write(attach.get("content").read())

                    try:
                        barcode = BarcodeReader(output_path).barcode_reader()
                    except Exception:
                        barcode = False

                    if not barcode:
                        thrash_path = os.path.join(
                            self.thrash_folder,
                            key + ".pdf",
                        )

                        os.rename(output_path, thrash_path)
                    else:
                        with open("bills.txt", "a") as bills:
                            bills.write(
                                f"{message.subject} - {barcode}" + "\n",
                            )
