from decimal import Decimal

if __name__ == '__main__':

    def postal_code_generator(first_code, second_code):
        int_first_code = int(first_code.replace("-", "")) + 1
        int_second_code = int(second_code.replace("-", ""))

        if int_first_code > int_second_code:
            ch_int_first_code = int_first_code
            int_first_code = int_second_code
            int_second_code = ch_int_first_code

        postal_code_list = []
        while int_first_code < int_second_code:
            actual_code = str(int_first_code)
            actual_code = actual_code[:2] + '-' + actual_code[2:]
            postal_code_list.append(actual_code)
            int_first_code += 1
        return postal_code_list


    def find_missing_numbers(list_of_numbers, number_of_elements):

        number_dictionary = {}
        list_of_missing_numbers = []

        for numbers in range(1, number_of_elements + 1):
            number_dictionary[numbers] = False

        for list_numbers in list_of_numbers:
            number_dictionary[list_numbers] = True

        for key, value in number_dictionary.items():
            if not value:
                list_of_missing_numbers.append(key)

        return list_of_missing_numbers


    def generate_list_with_step(start, stop, step):
        return [Decimal(start + step * i) for i in range(stop + 2)]

print(postal_code_generator('82-100', '83-200'))
print(find_missing_numbers([7, 1, 2, 3], 10))
print((generate_list_with_step(2, 5, 0.5)))
