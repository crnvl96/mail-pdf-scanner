from mail_scanner import MailScanner


def main():
    user = input("Enter your email: ")
    password = input("Enter the relative path where your password is stored: ")

    mail_scanner = MailScanner(user, password)

    print("Downloading bills...")

    mail_scanner.download_bills()

    print("Bills downloaded!")


if __name__ == "__main__":
    main()
