import random
# num_to_guess = random.randint(1, 100)
# print(num_to_guess)
# user_guess = -1

# def rand_num():
#     num_to_guess = random.randint(1, 100)
#     print(num_to_guess)
#     return num_to_guess

def validation():
    is_valid_input = False
    while not is_valid_input:
        try:
            u_num = input('Guess the number: ')
            u_num = int(u_num)
            # is_valid_input = True
        except ValueError:
            print('You entered not number or left empty field')
        if u_num == 61:
            print('You are right!')
            is_valid_input = True
        else:
            print('Try again')
        print(u_num)
    return u_num

def guess(validation):
    print(validation())
    return validation()

# print(guess(rand_num()))


# while user_guess != num_to_guess:
#     user_guess = int(input('Guess the number: '))
#     if user_guess > num_to_guess:
#         print('Number must be less')
#     elif user_guess < num_to_guess:
#         print('Number must be greater')
#     else:
#         print('You guessed')
#         break

# a = rand_num()
# n = validation()
# print(n)


###


glob = -1

class guessing:
    glob = -1

    def __init__(self):
        self.number_to_guess = self.rand_num()

    def rand_num(self):
        random_number = random.randint(1, 100)
        # print(random_number)
        return random_number

    def comparison(self):
        is_valid_input = False
        while not is_valid_input:
            try:
                user_num = input('Guess the number from 1 to 100: ')
                user_num = int(user_num)
                if user_num == self.number_to_guess:
                    print('You are great!')
                    is_valid_input = True
                elif user_num in range(self.number_to_guess - 10, self.number_to_guess + 10):
                    print('Very close')
                    # if guessing.glob < self.number_to_guess:
                    #     if user_num > guessing.glob:
                    #         print('Closer')
                    #     else:
                    #         print('Further')
                    # else:
                    #     if user_num > guessing.glob:
                    #         print('Further')
                    #     else:
                    #         print('Closer')
                elif user_num in range(self.number_to_guess - 25, self.number_to_guess + 25)\
                        and user_num not in range(self.number_to_guess - 10, self.number_to_guess + 10):
                    print('Close')
                elif user_num in range(self.number_to_guess - 50, self.number_to_guess + 50)\
                        and user_num not in range(self.number_to_guess - 25, self.number_to_guess + 25):
                    print('Far')
                else:
                    print('Very far')
                if guessing.glob < self.number_to_guess:
                    if user_num > guessing.glob:
                        print('Closer')
                    else:
                        print('Further')
                else:
                    if user_num > guessing.glob:
                        print('Further')
                    else:
                        print('Closer')
                # print(guessing.glob)
                guessing.glob = user_num
                # print(guessing.glob)
            except ValueError:
                print('You entered not number or left empty field')
            # if user_num == self.number_to_guess:
            #     print('You are great!')
            #     is_valid_input = True
            # elif user_num > self.number_to_guess:
            #     print('Your number must be less')
            # elif user_num < self.number_to_guess:
            #     print('Your number must be greater')
        # print(user_num)
        return user_num

    def guess(self):
        pass


test = guessing()
test.comparison()
