def decode(encoded_str: str) -> list:
    decoded_list = []
    current_number = ""
    current_char = ""
    
    for char in encoded_str:
        if char >= '0' and char <= '9':
            current_number += char
        else:
            if current_char and current_number:
                decoded_list.append((current_char, int(current_number)))
                current_number = ""  
            current_char = char  

    if current_char and current_number:
        decoded_list.append((current_char, int(current_number)))        
    return decoded_list

inputTxt = str(input("Enter decoded text: "))
decodedList = decode(inputTxt)

decodedStr = ""

for item in decodedList:
    char = item[0]
    count = item[1]
    
    decodedStr = decodedStr + (char * count)

print("Original text:", decodedStr)