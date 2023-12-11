import csv

# Replace 'your_data.csv' with the path to your CSV file
file1 = 'hremails.csv'

# Create an empty list to store email addresses
emails = set()
def getEmails(csv_file):
    # Open the CSV file and read email addresses from a specific column
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Split the column value by commas and remove spaces from each email
            email_list = row['Email'].split(',')
            cleaned_emails = [email.strip() for email in email_list if '@' in email.strip()]
            for mail in cleaned_emails:
                mail= mail.strip()
                if mail and len(mail)>0 and mail[0]!=' ':
                    emails.add(mail)

# getEmails(file1)
getEmails(file1)
# Print the valid email addresses
output_file = 'cleaned_emails.txt'

# Write the valid email addresses to the output file
emails = sorted(emails)
with open(output_file, 'w') as out_file:
    for email in emails:
        out_file.write(email + '\n')
