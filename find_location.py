import phonenumbers
from phonenumbers import geocoder, timezone, carrier

# Input a phone number
mobileNo = input("Enter a phone number: ")  # Provide a valid phone number here as a string

try:
    mobileNo = phonenumbers.parse(mobileNo)

    # Get the timezone of the phone number
    timezone_info = timezone.time_zones_for_number(mobileNo)
    print("Timezone: ", timezone_info)

    # Get carrier information of the phone number
    carrier_info = carrier.name_for_number(mobileNo, "en")
    print("Carrier: ", carrier_info)

    # Get region information of the phone number
    region_info = geocoder.description_for_number(mobileNo, "en")
    print("Region: ", region_info)

    # Validate phone number
    is_valid = phonenumbers.is_valid_number(mobileNo)
    print("Valid Mobile Number: ", is_valid)

    # Check the possibility of the phone number
    is_possible = phonenumbers.is_possible_number(mobileNo)
    print("Checking possibility of a number: ", is_possible)

    # Get the last known location (if available)
    last_location = geocoder.description_for_number(mobileNo, "en")
    print("Last Known Location: ", last_location)

except phonenumbers.phonenumberutil.NumberFormatException:
    print("Invalid phone number format")