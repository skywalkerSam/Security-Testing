logo = """
______ _
| ___ (_)
| |_/ /_ _ __   __ _ _ __ _   _
| ___ \ | '_ \ / _` | '__| | | |
| |_/ / | | | | (_| | |  | |_| |
\____/|_|_| |_|\__,_|_|   \__, |
                           __/ |
                          |___/

 _____                               _
/  __ \                             (_)
| /  \/ ___  _ ____   _____ _ __ ___ _  ___  _ ___
| |    / _ \| '_ \ \ / / _ \ '__/ __| |/ _ \| '_  |
| \__/\ (_) | | | \ V /  __/ |  \__ \ | (_) | | | |
 \____/\___/|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|


"""
print(logo)


def binary_conversion():
    try:
        user_text = input("\nEnter some text: ")
        binary_format = ' '.join(format(x, 'b') for x in bytearray(user_text, 'utf-8'))
        print(f"\nBinary Conversion: {binary_format}")
    except Exception as e:
        #print(e)
        print("\n\t Something went wrong!  Please Try Again :( \n")


if __name__ == "__main__":
    binary_conversion()
