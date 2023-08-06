# mail-pdf-scanner
Python script to quickly scan your email for bills with barcodes

## Usage
- This guide assumes you have an Gmail account
- Clone the repo
  ```bash
  git clone https://github.com/crnvl96/mail-pdf-scanner.git && cd mail-pdf-scanner
  ```
- Configure an [app password](https://support.google.com/mail/answer/185833?hl=en) for your google account
- save your password in a file
  ```bash
  echo [YOUR_PASS] > password/pass
  ```
- Create a virtual environment and install the dependencies
  ```bash
  python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
  ```
- Run the project
  ```bash
  python3 main.py
  ```
  - Your barcodes, with the related mail subjects will be saved in a file called `bills.txt`, at project root
  - There will be created two folders: `thrash` will contain attachments that do not contains barcodes, and `bills` will contain attachments that have.
  
