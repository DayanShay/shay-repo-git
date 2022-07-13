def password_validator():
    """
    This function validate a password strength by sertan requirements and provides an output :

    Password Requirements:
        (1) Length – minimum of 10 characters.
        (2) Contain both alphabet and number.
        (3) Include both the small and capital case letters.

    Function Exceptions:

    (1) Color output Green or Red.
         (1.1) Green = passed the validation.
             (1.2) Red = not passed the validation.

    (2) Return exit code 0 or 1.
         (2.1) 0 = passed the validation.
             (2.2) 1 = not passed the validation.

    (3) If a validation failed provide a message explaining why.

    How to use password_validator.py
        1) Run with CMD and send a "password":
            Commend line example -> : (python ./password_validator.py "Password1!")
            function Get password as "Password1!" (wright your "password" to check)

        :return: sys.exit(code) 0 = valid ,1 = invalid.
        """
    import sys
    from colorama import init
    init(autoreset=True)
    red = "\033[31m"
    green = "\033[32m"
    if len(sys.argv) == 2:
        password_check = sys.argv[1]
    else:
        if len(sys.argv) > 2 :
            print(red + "Password InValid.")
            print("Got more then 1 arguments - can't run the Validation")
            exit(1)
        else:
            password_check = ""

    length_flag = len(password_check) > 9
    latter_flag = False
    number_flag = False
    lower_flag = False
    capital_flag = False
    for char in str(password_check):
        if char.isnumeric():
            number_flag = True
        else:
            if char.isalpha():
                latter_flag = True
                if char.isupper():
                    capital_flag = True
                else:
                    lower_flag = True
    if length_flag and latter_flag and number_flag and lower_flag and capital_flag:
        print(green + "Password Valid.")
        return exit(0)
    else:
        print(red + "Password InValid.")
        counter_msg = 1
    if not length_flag:
        print("("+str(counter_msg)+")", "Password too short - Password must have Minimum of 10 characters")
        counter_msg += 1
    if not latter_flag or not number_flag:
        print("("+str(counter_msg)+")", "Password must contain both alphabet and number")
        counter_msg += 1
    if not capital_flag or not lower_flag:
        print("("+str(counter_msg)+")", "Password must contain both small and capital case letters")
    return exit(1)


def main():
    password_validator()


if __name__ == "__main__":
    main()
