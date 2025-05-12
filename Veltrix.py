#! python3
# Veltrix.py

import pyperclip
import re
from colorama import Fore
import pyfiglet
import phonenumbers
from phonenumbers import PhoneNumberMatcher, PhoneNumberFormat, carrier, timezone

class ContactInfoExtractor:
    def __init__(self, default_region='US'):
        self.default_region = default_region  # Default country

        self.email_regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+       # username
            @                       # @ symbol
            [a-zA-Z0-9.-]+          # domain name
            (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)

    def extract_phone_numbers(self, text):
        phone_infos = []

        for match in PhoneNumberMatcher(text, self.default_region):
            number = match.number
            formatted_number = phonenumbers.format_number(number, PhoneNumberFormat.INTERNATIONAL)

            # Get carrier name (may be empty for some numbers)
            number_carrier = carrier.name_for_number(number, 'en')

            # Get timezones
            number_timezones = timezone.time_zones_for_number(number)

            info = f"{formatted_number}"
            if number_carrier:
                info += f" | Carrier: {number_carrier}"
            if number_timezones:
                info += f" | Timezones: {', '.join(number_timezones)}"

            phone_infos.append(info)

        return phone_infos

    def extract_emails(self, text):
        return [match[0] for match in self.email_regex.findall(text)]

    def extract_from_text(self, text):
        matches = []
        matches.extend(self.extract_phone_numbers(text))
        matches.extend(self.extract_emails(text))
        return matches

    def extract_from_clipboard(self):
        text = pyperclip.paste()
        return self.extract_from_text(text)

    def run(self):
        matches = self.extract_from_clipboard()
        if matches:
            pyperclip.copy('\n'.join(matches))
            print(Fore.GREEN, '>Copied to clipboard~#')
            print("\n".join(matches))
        else:
            print(Fore.RED, ">No phone numbers or email addresses found!")

if __name__ == "__main__":
    extractor = ContactInfoExtractor(default_region='US')  
    header=pyfiglet.figlet_format('veltrix',font= 'isometric1', width=100)
    print(Fore.BLUE + header)
    extractor.run()

