# Исходная строка в байтовом виде
byte_str = b'r\xc3\xa9sum\xc3\xa9'

# Декодирование в строку с кодировкой по умолчанию
decoded_str_default = byte_str.decode()
print(decoded_str_default)

# Преобразование обратно в байтовую строку в кодировке 'Latin1'
byte_str_latin1 = decoded_str_default.encode('Latin1')
print(byte_str_latin1)

# Декодирование в строку с кодировкой 'Latin1'
decoded_str_latin1 = byte_str_latin1.decode('Latin1')
print(decoded_str_latin1)
