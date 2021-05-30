str1 = 'I am Boy.'
str2 = 'Niceman'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = 'Do you have a \"big collection\"'
print(escape_str1)
escape_str2 = "Tab \t Tap \t"
print(escape_str2)

raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\a"
print(raw_s2)


multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)


str_01 = "*"
str_02 = "abc"
str_03 = "def"
str_04 = "Niceman"
print(str_01 * 100)
print(str_01+str_02)
print('a' in str_04)
print('a' not in str_04)