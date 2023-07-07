#문자열 뒤집는 함수
def reverse_string(string):
    return string[::-1]

#주어진 리스트에서 짝수만 반환하는 함수:
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

#문자열에서 중복된 문자를 제거하는 함수:
def remove_duplicates(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result

#섭씨 온도를 화씨 온도로 변환하는 함수
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit