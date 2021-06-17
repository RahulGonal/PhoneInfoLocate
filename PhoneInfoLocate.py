import phonenumbers
from phonenumbers import timezone 
from phonenumbers import geocoder, carrier
import time
import webbrowser
from colorama import Fore

print(Fore.GREEN + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print(Fore.YELLOW + "P|h|o|n|e|I|n|f|o|L|o|c|a|t|e")
print(Fore.GREEN + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
time.sleep(3)
print ("Welcome to PhoneInfoLocate, created by RahulGonal")
time.sleep(3)
print("The creator/s of the tool are not responsible for any damage or misuse you the user cause")
time.sleep(3)
print("This tool is meant for only educational purposes")

# Collecting the PhoneNumber
PhoneNumber = (input("[-] Enter the PhoneNumber you want Information and Location beginning with the Plus sign and the country code >>>> "))

# Collecting Country
print("Enter the Country of the Number")
print("0 - India")
print("1 - USA")
print("3 - UK")
Country = input("[-] Choose One Option >>>> ")

# Seperate CountryCode and PhoneNumber
CountryCode = (PhoneNumber[0:3])
Number = (PhoneNumber[3:13])
AreaCode = (PhoneNumber[3:7])

#Parse Phone Number
pPhoneNumber = phonenumbers.parse(PhoneNumber)

# Validating the PhoneNumber
valid = phonenumbers.is_valid_number(pPhoneNumber)
print("Valid =",valid)

# Generating the Time Zone
timeZone = timezone.time_zones_for_number(pPhoneNumber) 
print('Timezone = ', timeZone)

# Getting the carrier
Carrier = carrier.name_for_number(pPhoneNumber, 'en') 
print("Carrier =",Carrier)

# Finding Region
Region = geocoder.description_for_number(pPhoneNumber, 'en') 
print("Region = ",Region)

# Finding Info online
print("Finding info online and redirecting you to the page in 5 seconds")
time.sleep(5)

# Opening Website for India
if "0" or "India" in Country:
  webbrowser.open_new("https://mobilenumbertracker.com/mobilenumberlocation/"+AreaCode)
 
 # Opening Website for USA
if "1" or "USA" in Country:
  webbrowser.open_new("https://www.whitepages.com/phone/"+Number)
  
# Opening 2nd Website for USA
if "1" or "USA" in Country:
	print("Found Another Website")
	print("Do you want to be redirected to that website (y/n) >>>>")
	andWeb = input("Choose One Option >>>>")
	if "y" in andWeb:
		webbrowser.open_new("https://www.searchquarry.com/phone-number-lookup/"+Number)
		
# Opening Website for UK
if "2" or "UK" in Country:
	webbrowser.open_new("https://whocalledmeuk.co.uk/phonenumber.php?numer="+Number)
	
print("Do You want to be redirected to the Truecaller Page of this phone number. (y/n)")

TruCl = input("Choose On Option >>>> ")

if "y" in TruCl:
	webbrowser.open_new("https://www.truecaller.com/search/in/"+PhoneNumber)
print("Thanks for Using the tool")  
