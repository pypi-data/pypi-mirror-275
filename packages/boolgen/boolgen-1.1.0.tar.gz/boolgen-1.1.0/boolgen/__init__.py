"""
boolgen -- generate Boolean expressions from truth tables.
(c) 2024 Schuyler Erle. See LICENSE.md for more details.
"""
import re, sys
from itertools import combinations, product
from typing import List, Tuple

# Helper function to parse the input table
def parse_input(input_string: str) -> Tuple[List[str], List[str], List[List[int]]]:
    """
    Parse the input data into variables and truth table.

    :param input_data: A string containing the input data
    :return: A tuple containing the list of input variables, list of output variables, and the truth table
    """

    def is_output_var(v):
        return bool(re.search(r'^(?:out|=)|=$', v, re.I))

    # Split the input string by non-alphanumeric characters
    rows = [re.split(r'(?!=)\W+', row.strip()) for row in input_string.strip().split('\n')]
    
    # Extract the header (variables) and the rest of the rows (values)
    variables = rows[0]
    truth_table = [list(map(int, row)) for row in rows[1:]]
    
    # Determine the input variables and output variables
    input_vars = [var for var in variables if not is_output_var(var)]
    output_vars = [var.replace('=', '') for var in variables if is_output_var(var)]

    # If no output variables were explicitly declared using pre/postfix '=',
    # assume that the last column is meant to be an output.
    if not output_vars:
        output_vars.append(input_vars.pop())
    
    return input_vars, output_vars, truth_table

# Helper function to convert minterms to binary format
def minterm_to_binary(minterm, num_vars):
    return format(minterm, f'0{num_vars}b')

# Function to find prime implicants using Quine-McCluskey method
def find_prime_implicants(num_vars: int, minterms: List[int]) -> List[str]:
    """
    Find prime implicants for the given minterms using the Quine-McCluskey algorithm.

    :param num_vars: Number of input variables
    :param minterms: List of minterm indices
    :return: A list of strings representing the prime implicants
    """
    def combine_terms(term1, term2):
        diff = sum(1 for a, b in zip(term1, term2) if a != b)
        if diff == 1:
            combined = ''.join(a if a == b else '-' for a, b in zip(term1, term2))
            return combined
        return None

    def term_to_indices(term):
        indices = []
        for i in range(1 << num_vars):
            bin_rep = f"{i:0{num_vars}b}"
            if all(a == b or a == '-' for a, b in zip(term, bin_rep)):
                indices.append(i)
        return indices

    groups = {i: [] for i in range(num_vars + 1)}
    for minterm in minterms:
        bin_rep = f"{minterm:0{num_vars}b}"
        groups[bin_rep.count('1')].append(bin_rep)

    prime_implicants = set()
    while True:
        new_groups = {i: [] for i in range(num_vars + 1)}
        marked = set()
        for i in range(num_vars):
            for term1 in groups[i]:
                for term2 in groups[i + 1]:
                    combined = combine_terms(term1, term2)
                    if combined:
                        new_groups[i].append(combined)
                        marked.add(term1)
                        marked.add(term2)
        new_groups = {i: list(set(terms)) for i, terms in new_groups.items()}

        for i in range(num_vars + 1):
            for term in groups[i]:
                if term not in marked:
                    prime_implicants.add(term)

        if not any(new_groups.values()):
            break
        groups = new_groups

    # Essential Prime Implicant Reduction
    prime_implicant_chart = {term: set(term_to_indices(term)) for term in prime_implicants}
    minterm_chart = {minterm: [] for minterm in minterms}
    for term, indices in prime_implicant_chart.items():
        for index in indices:
            if index in minterm_chart:
                minterm_chart[index].append(term)

    essential_prime_implicants = set()
    while minterm_chart:
        for minterm, terms in minterm_chart.items():
            if len(terms) == 1:
                essential_prime_implicant = terms[0]
                break
        else:
            essential_prime_implicant = max(prime_implicant_chart, key=lambda t: len(prime_implicant_chart[t]))

        essential_prime_implicants.add(essential_prime_implicant)
        covered_minterms = prime_implicant_chart.pop(essential_prime_implicant)
        minterm_chart = {m: terms for m, terms in minterm_chart.items() if m not in covered_minterms}

        for minterm, terms in minterm_chart.items():
            terms = [t for t in terms if t != essential_prime_implicant]
            if terms:
                minterm_chart[minterm] = terms
            else:
                del minterm_chart[minterm]

    return essential_prime_implicants


# Function to simplify Boolean expressions
def simplify_expression(input_vars: List[str], truth_table: List[List[int]], output_index: int) -> str:
    """
    Simplify the boolean expression based on the truth table.

    :param input_vars: List of input variable names
    :param truth_table: The truth table as a list of lists of integers
    :param output_index: The index of the output variable to simplify for
    :return: A string representing the simplified boolean expression
    """
    num_vars = len(input_vars)
    output_values = [row[num_vars + output_index] for row in truth_table]
    
    if all(v == 1 for v in output_values):
        return '1'
    if all(v == 0 for v in output_values):
        return '0'
    
    minterms = [i for i, row in enumerate(truth_table) if row[num_vars + output_index] == 1]
    prime_implicants = find_prime_implicants(num_vars, minterms)

    def term_to_expression(term):
        parts = []
        for var, bit in zip(input_vars, term):
            if bit == '0':
                parts.append(f"~{var}")
            elif bit == '1':
                parts.append(var)
        return ' & '.join(sorted(parts))

    expressions = [term_to_expression(term) for term in prime_implicants]
    return ' | '.join(sorted(expressions))


# Main function
def evaluate_table(input_string):
    input_vars, output_vars, truth_table = parse_input(input_string)
    output_expressions = []
    for output_index, output_var in enumerate(output_vars):
        expression = simplify_expression(input_vars, truth_table, output_index)
        output_expressions.append((output_var, expression))
    return output_expressions

def main():
    if len(sys.argv) > 1:
        table = open(sys.argv[1]).read()
    else:
        table = sys.stdin.read()
    for output_var, expression in evaluate_table(table):
        print(f"{output_var} = {expression}")

if __name__ == "__main__":
    main()
