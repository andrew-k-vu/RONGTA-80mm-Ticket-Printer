from escpos.printer import Win32Raw
import datetime

ptr = Win32Raw("prod_Print") # ASSIGNS "ptr" AS REDIRECT TO USB PRINTER NAMED "prod_Print"
date_time = datetime.datetime.now()

### EPSON/RONGTA Thermal Printer 80MM(ESC/POS) ###

# Print ticket lines entered by user with date and time centered at the top of the receipt
ptr.text("^^^^^^^^^^****************************^^^^^^^^^^")
ptr.text((date_time.strftime("%B %d, %Y  |  %H%M LOCAL").center(48)))           # Print a line: centered date and time
ptr.text("\n\n")   

# Allows user to enter lines until typing 'done'
x = ''
while x != "done":                                                              # While-loop has x != 'done' for redundancy
    x = input("Enter a line then hit enter to write or type 'done' to stop: ")  # User entries into the receipt
    if x.lower() == "done" :                                                    # x.lower() add redundancy for all iterations of the word 'done'
        break                                                                   # Exit loop, print and cut when sentinal value is detected
    else :
        ptr.text((x).center(48))                                                # Prints text centered. Removing () from x causes spacing issue
        ptr.text("\n")                                                          # Placing \n with the centered print command above causes spacing issue
        continue                                                                # Redirect back to top of while-loop

ptr.text("\n")
ptr.text("^^^^^^^^^^****************************^^^^^^^^^^")
ptr.cut()