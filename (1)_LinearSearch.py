# The function enables you to reuse the code.
def linear_search(list, key):
    for i in list:
        if i == key:
            return key
    return "Key not found"


# The commented code is a sample of how the fuction works.
# My_list = [2,5,8,2,9]

# Example = linear_search( My_list, 5)
# print (Example)


#You can input your own list and key in the terminal.
Your_list = input("Provide a list: ")
Your_key = input("Provide a key: ")

Your_example = linear_search( Your_list, Your_key)
print (Your_example)




# //        This confirms whether the key is in the list.
        # String confirm = (linearSearchConfirm(array,4));
    #     //This method verifies whether the search key is in the array or not.
    # private static String linearSearchConfirm(int[] array, int key) {
    #     for(int i:array) {
    #         if(i == key) {
    #             return Integer.toString(i);
    #         }
    #     } return "Key not found." ;
    # }