# Strings

Templates:

    street = '1 av de Paris'
    zip_code = 92110
    city = 'Clichy'

    address = Template("$street\n${zip} $city");
    s = address.substitute(street=street, zip=zip_code, city=city)
    print(s)

