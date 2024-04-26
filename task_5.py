import locale

def format_monetary_value(number, use_nepali_units=False):
    # Set the locale for Nepali or International units
    if use_nepali_units:
        locale.setlocale(locale.LC_NUMERIC, 'ne_NP.UTF-8')
    else:
        locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
    
    # Convert the number to a string with appropriate formatting
    formatted_number = locale.format_string("%.2f", number, grouping=True)
    
    return formatted_number

if __name__ == "__main__":
    number = 111625.92822
    
    # Format with International units
    international_format = format_monetary_value(number)
    print("International format:", international_format)
    
    # Format with Nepali units
    nepali_format = format_monetary_value(number, use_nepali_units=True)
    print("Nepali format:", nepali_format)


