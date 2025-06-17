import re

# Function to extract emails from text
def extract_emails_from_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Regex pattern for email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)

        # Remove duplicates by converting to a set
        unique_emails = sorted(set(emails))

        # Save to output file
        with open(output_file, 'w') as out_file:
            for email in unique_emails:
                out_file.write(email + '\n')

        print(f"{len(unique_emails)} email(s) extracted and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
input_filename = input("Enter the path to the input .txt file: ").strip()
output_filename = input("Enter the name of the output file (e.g., emails.txt): ").strip()

extract_emails_from_file(input_filename, output_filename)
