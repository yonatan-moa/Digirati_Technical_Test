# -*- UTF-8 -*-

"""
Main function to process a small prototype simulating a call centre getting international calls. The API as for the country
code and phone number such as “+44141555555” or “44 555 512 34” etc.
The API returns:
* The Phone Number provided
* The Calling Call
* User
* Country Details
  * The default language
  * The country name
  * The name of country in user default language
  * The region
  * The flag url 
"""

import phonenumbers
import requests
from phonenumbers.phonenumberutil import NumberParseException

from sort_users import User, get_user

# Users instance initialisations
user_01 = User("User_01", ["en"])
user_02 = User("User_02", ["en"])
user_03 = User("User_03", ["en", "fr", "it", "de"])
user_04 = User("User_04", ["pl", "es", "sv", "ru"])
user_05 = User("User_05", ["en", "ra"])
user_06 = User("User_06", ["ja", "zu", "ta", "af", "sq", "en"])
user_07 = User("User_07", ["ca", "zh", "ko", "ms"])
user_08 = User("User_08", ["fr", "dk"])
user_09 = User("User_09", ["fa", "fi", "lv", "en"])
user_10 = User("User_10", ["en", "de", "fr", "da", "nl"])

# User added to a list
user_list = [
    user_01,
    user_02,
    user_03,
    user_04,
    user_05,
    user_06,
    user_07,
    user_08,
    user_09,
    user_10,
]

print("Yonatan Shahar Digirati Test")

# Url to endpoint
url = r"https://restcountries.com/v2/callingcode/"

# Input prompt to get the inputted number
input_number = input(
    "Please enter the country code and phone number to make a call. (example “+44141555555” or “44 555 512 34”): "
)
# If the number has not the + at the start of the phone number, it adds it
if input_number[0] != "+":
    input_number = f"+{input_number}"

# Parsed the input number enable to extract the code and country number
try:
    parse_phone_number = phonenumbers.parse(input_number)
    print(parse_phone_number)
except NumberParseException as e:
    print(f"The phone number provided is not a valid input, exiting {input_number}")
    exit(0)

# -----------------------------------------------------------------------------------------
# Country code and country number derived from parsed phoned number
country_code = parse_phone_number.country_code
country_number = parse_phone_number.national_number

# Url, GET request and formatting of the data returned
url_code = f"{url}{country_code}"

code_request = requests.get(url_code)

country_data = code_request.json()


# -----------------------------------------------------------------------------------------
# Extract the values as a list as few countries have several territories such as the United Kingdom and the USA
language = ""
default_lang = ""
country_names = []
default_native_names = []
country_flags_url = []
country_region = []
for item in country_data:
    language = item["languages"][0]["iso639_1"]
    default_lang = item["languages"][0]["name"]
    country_names.append(item["name"])
    default_native_names.append(item["nativeName"])
    country_flags_url.append(item["flags"]["png"])
    country_region.append(item["region"])

# ---------------------------------------------------------------------------------------------
# Find the user match according to the language in the user_list
user = get_user(language, user_list)
# If returns None, assigns the user with the most languages in its list
if user is None:
    user = user_06.name

# ----------------------------------------------------------------------------------------------
# Print out the results.
# It could be returned as a json or another required data format
print(
    f"Phone Number Provided: {input_number}\n"
    f"Calling code: {country_code}\n"
    f"User: {user}\n"
    "Country Details:\n\t"
    f"Default Language: {default_lang}\n\t"
    f"Name: {country_names[-1]}\n\t"
    f"Name of country in User default language: {default_native_names[-1]}\n\t"
    f"Region: {country_region[-1]}\n\t"
    f"Flags url: {country_flags_url[-1]}"
)
