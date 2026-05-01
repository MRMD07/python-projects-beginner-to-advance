#In this small script we will write a function to find even numbers in the list

number_list = [1,2,3,4,5,6,7,8]

def even_number_finder(number_list): #function is choosen because probably we will need to use the same code again and again so it will be more efficient

    even_list = []
    for number in number_list:
        if number % 2 == 0: #we are using MOD(%) operator it gives the remainder however simple assumption is made which is that the list does not contain 0 as 0/2 will also give 0
            even_list.append(number)
    return even_list

even_list = even_number_finder(number_list)

print(even_list)

           
