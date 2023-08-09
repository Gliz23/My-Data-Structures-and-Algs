#This function works for x(n-1) questions. Where x is a digit between 0-9.
def Big_O(expression):
    #Expansion begins
    terms = expression.split('*')

    storage =[]
    expand_form=[]
    small_storage=[]

    for term in terms:
        if '(' in term and ')' in term:
            term = term.replace('(','').replace(')','')
        storage.append(term)

    for item in storage:
        bracket_items = item.split('-')
        small_storage.append(bracket_items)
                       

    answer = f"{small_storage[0]} * {small_storage[1]} * {small_storage[2][0]} - {small_storage[0]} * {small_storage[1]} * {small_storage[2][1]}"
    answer = answer.replace('[','').replace(']','').replace("'","").replace("'","").replace('1','').replace('*','').replace(' ','').replace('nn','n^2')
    #Expansion ends

    #Finding the highest term begins.
       
     # Split the runtime function into its individual terms
    terms = answer.split('-')

     # Remove any leading or trailing whitespace from each term
    terms = [term.strip() for term in terms]

     # Initialize the highest exponent to None
    highest_exponent = None

     # Iterate over each term and update the highest exponent if necessary
    for term in terms:
         # Check if the term is a polynomial of the form an^b
        if 'n' in term and '^' in term:
             # Split the term into its coefficient and exponent
            coeff, exponent = term.split('^')

            if highest_exponent is None or exponent > highest_exponent:
                highest_exponent = exponent
            else:
                continue
    if highest_exponent is None:
        return None

             
    BigO = f"O(n^{highest_exponent})"
    # Finding the highest time ends.

    return BigO


#Your arguments should be seperated by '*' where there is multiplication.
eg = Big_O("7*n*(n-1)")
print(eg)





