#creat static method to validate if a number is even.
class Number:
    @staticmethod
    def is_even(number):
        if number % 2==0:
            return True
        else:
            return False
print(Number.is_even(10))

