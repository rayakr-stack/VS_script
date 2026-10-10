def encoding(s: str) -> list:
    if not s:
        return []
    
    encoded_list = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_list.append((s[i - 1], count))
            count = 1
            
    encoded_list.append((s[-1], count))
    return encoded_list


inputTxt = str(input("Enter text: "))
endcList = encoding(inputTxt)

encodedStr = ""

for i in endcList:
    char = i[0]  
    count = i[1] 
   
    encodedStr = encodedStr + char + str(count)


print("Encoded result: ", encodedStr)
