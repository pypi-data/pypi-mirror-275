def div(divider_char, divider_len):
    default_divider_len = 100
    default_divider_char = '-'

    if len(divider_char) == 0:
        print('Error: Divider character cannot be empty')
        print(f'Switching to default divider character: "{default_divider_char}"')
        divider_char = default_divider_char

    if len(str(divider_len)) == 0:
        print('Error: Divider length cannot be empty')
        print(f'Switching to default divider length: "{default_divider_len}"')
        divider_len = default_divider_len

    return divider_char * divider_len