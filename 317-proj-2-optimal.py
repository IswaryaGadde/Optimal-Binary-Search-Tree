import sys
def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        probabilities = [int(line) for line in file]
    return n, probabilities

def optimal_bst(n, probabilities):
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    roots = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 2):
        dp[i][i - 1] = 0  # Initialize the diagonal elements.

    for cl in range(1, n + 1):
        for i in range(1, n - cl + 2):
            j = i + cl - 1
            dp[i][j] = float('inf')
            for k in range(i, j + 1):
                cost = dp[i][k - 1] + dp[k + 1][j] + sum(probabilities[i - 1:j])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    roots[i][j] = k

    return dp, roots

def print_dynamic_table(dp,roots, n):
    print("Table:")
    header = "       "+ " ".join(f"    {i:02d}    " for i in range(1, n + 1))
    print(header)
    for i in range(1, n + 1):       
        row = f"{i:02d}         "
        for j in range(1, n + 1):
            value = dp[i][j]
            if value == 0:
                row += "  -        "
            else:
                row += (f"{value:05d}      ")              
        print(row)

    print("\nRoots:")
    header = "       " + " ".join(f"    {i:02d}    " for i in range(1, n + 1))
    print(header)
    for i in range(1, n + 1):       
        row = f"{i:02d}          "
        for j in range(1, n + 1):
            root = roots[i][j]
            if root == 0:
                row += "  -        "
            else:
                row += f"{root:05d}      "       
        print(row)

def print_tree(roots, i, j, space_needed):
     if i <= j:
        mid = roots[i][j]
        if mid == 0:
            node = "  -  "
        else:
            node = f"{mid:02d} "
        
        left_child = roots[i][mid - 1] if mid > i else 0
        right_child = roots[mid + 1][j] if mid < j else 0
        
        if left_child == 0:
            left_node = "-"
        else:
            left_node = ""
        
        if right_child == 0:
            right_node = "-"
        else:
            right_node = ""
        
        print(" " * space_needed + f"{left_node} {right_node}")
        print(" " * space_needed + node)
        print_tree(roots, i, mid - 1, space_needed + 4)
        print_tree(roots, mid + 1, j, space_needed + 4)


def main():
    n, probabilities = read_input("c:/Users/gadde/UAH/Python/project-one/input-317.txt")
    dp, roots = optimal_bst(n, probabilities)

    with open("c:/Users/gadde/UAH/Python/project-one/ig0026.txt", "w") as output_file:
        sys.stdout = output_file  # Redirect standard output to the output file

        # Print the dynamic programming table and tree
        print_dynamic_table(dp, roots, n)
        print("\nBinary Tree:")
        print_tree(roots, 1, n, 0)

    sys.stdout = sys.__stdout__  # Reset standard output to the console

    

if __name__ == "__main__":
    main()
