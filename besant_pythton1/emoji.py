## unicode of emojis
print('\U0001F602')
print('\U0001F603')
print('\U0001F605')
print('\U0001F60D')
print('\U0001F92A')
print('\U0001F92B')
print('\U0001F648')
print("I",'\U00002764',"you")
print('\U0001F494')
## convert ordinal value to binary code
ord_value = 65
binary_code = bin(ord_value)
with_out_prefix = binary_code[2:]
print(with_out_prefix)
## convert binary to letter
binary_value = "1000001"
letter = int(binary_value,2)
result = chr(letter)
print(result)
