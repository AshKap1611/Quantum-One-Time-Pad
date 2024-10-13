import random

def ascii_string_to_bitstring(string):
    # Converts a regular string into a binary string
    res = ''.join(format(ord(i), '08b') for i in string)
    return res

def bitstring_to_ascii_string(bitstring):
    # Converts the binary string back into regular string
    if len(bitstring) % 8 != 0:
        raise ValueError("The length of the bitstring should be a multiple of 8.")
    
    byte_array = bytearray(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))
    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        return str(byte_array)

def xor_two_bitstrings(bitstring1, bitstring2):
    # XORs (adds) two binary strings to encode
    string = ""
    for i in range(len(bitstring1)):
        if bitstring1[i] == bitstring2[i]:
            string += "0"
        else:
            string += "1"
    return string
            
def main(message):
    # Creates the binary string from the message
    message_bitstring = ascii_string_to_bitstring(message)
    # Generates a random key
    key = ''.join(str(random.randint(0, 1)) for _ in range(len(message_bitstring)))

    # Creates the encoded message by adding the message and key
    encoded_message = xor_two_bitstrings(message_bitstring, key)
    # Finds the decoded message by readding (XORing) the encoded message and the key
    decoded_message = xor_two_bitstrings(encoded_message, key)

    # Outputs everything
    print("The message is:", message)
    print("The message bitstring is:", message_bitstring)
    print("The key is:", key)
    print("The encoded message bitstring is:", encoded_message)
    # Converts the decoded bitstring back into a regular string
    print("The decoded message is:", bitstring_to_ascii_string(decoded_message))

# Asks the user to input
text = input("Give me the text to encode: ")
main(text)
