import romanify

roman_input = input("Введите римское число: ")
arabic_input = int(input("Введите арабское число: "))

arabic_from_roman = romanify.roman2arabic(roman_input)

sum = arabic_from_roman + arabic_input
sub = arabic_from_roman - arabic_input
mul = arabic_from_roman * arabic_input
div = arabic_from_roman // arabic_input

print("Арабские:")
print(f"+: {sum}")
print(f"-: {sub}")
print(f"*: {mul}")
print(f"//: {div}")

print("Римские:")
print(f"+: {romanify.arabic2roman(sum)}")
print(f"-: {romanify.arabic2roman(sub)}")
print(f"*: {romanify.arabic2roman(mul)}")
print(f"//: {romanify.arabic2roman(div)}")