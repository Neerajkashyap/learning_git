import pdb
num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']

pdb.set_trace()
def nested():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested()