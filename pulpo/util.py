def parse_number(number_str):
    try:
        number = int(number_str)
    except:
        number = float(number_str)
    
    return number
