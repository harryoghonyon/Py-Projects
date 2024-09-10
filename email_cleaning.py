import re
import csv


class EmailCleaner:
    def __init__(self, input_file='dirty_emails.csv', output_file='clean_emails.csv'):
        self.input_file = input_file
        self.output_file = output_file
        self.emails = []

    def read_emails(self):
        with open(self.input_file, mode='r') as file:
            csv_reader = csv.reader(file)
            self.emails = [row[0] for row in csv_reader if row]

    def clean_email(self,  email):
        email = re.sub(r'\s+', '', email)
        email = re.sub(r'\.+', '.', email)
        email = re.sub(r'@gma?i?l?[\.]*c?o?m?', '@gmail.com', email)
        return email

    def clean_emails(self):
        self.emails = [self.clean_email(email) for email in self.emails]

    def write_clean_emails(self):
        with open(self.output_file, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            for email in self.emails:
                csv_writer.writerow([email])


if __name__ == "__main__":
    cleaner = EmailCleaner()
    cleaner.read_emails()
    cleaner.clean_emails()
    cleaner.write_clean_emails()
