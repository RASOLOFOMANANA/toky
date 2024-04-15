from itertools import product

def truth_table(func, variables):
    """Calculates the truth table for a given function."""
    table = []
    for vals in product([0, 1], repeat=len(variables)):
        row = list(vals)
        row.append(func(*vals))
        table.append(row)
    return table

def first_canonical_form(variables, minterms):
    """Calculates the first canonical form using minterms."""
    terms = []
    for i, minterm in enumerate(minterms):
        term = ""
        for j, var in enumerate(variables):
            if minterm[j] == '1':
                term += var
            elif minterm[j] == '0':
                term += var + "'"
        terms.append(term)
    return " + ".join(terms)

def second_canonical_form(variables, maxterms):
    """Calculates the second canonical form using maxterms."""
    terms = []
    for i, maxterm in enumerate(maxterms):
        term = ""
        for j, var in enumerate(variables):
            if maxterm[j] == '0':
                term += var
            elif maxterm[j] == '1':
                term += var + "'"
        terms.append(term)
    return " * ".join(terms)

def main():
    expression = input("Entrez la fonction logique (utilisez les opérateurs logiques 'and', 'or', 'not' et les variables en minuscules) : ")
    variables = sorted(set([char for char in expression if char.isalpha()]))
    func = eval(f"lambda {', '.join(variables)}: {expression}")
    
    print("\nTable de vérité :")
    table = truth_table(func, variables)
    for row in table:
        print(row)
    
    minterms = ["".join(["1" if val else "0" for val in row[:-1]]) for row in table if row[-1]]
    maxterms = ["".join(["0" if val else "1" for val in row[:-1]]) for row in table if not row[-1]]
    
    print("\nPremière forme canonique :")
    print(first_canonical_form(variables, minterms))
    
    print("\nDeuxième forme canonique :")
    print(second_canonical_form(variables, maxterms))

if __name__ == "__main__":
    main()