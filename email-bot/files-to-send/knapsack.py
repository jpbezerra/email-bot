def create_matrix(rows : int, cols : int) -> list:
    matrix = []
    for i in range(rows + 1):
        matrix.append([])
        for j in range(cols + 1):
            matrix[i].append(-1)
    
    return matrix

def knapsack(itens : int, capacity : int, values : int, weights : int) -> int:
    result = create_matrix(itens, capacity)

    for i in range(itens + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                result[i][j] = 0

            elif int(weights[i]) <= j:
                result[i][j] = max(result[i - 1][j], int(values[i]) + result[i - 1][j - int(weights[i])])

            else:
                result[i][j] = result[i - 1][j]

    return result[itens][capacity]

def main():
    itens = int(input())
    capacity = int(input())

    weights = [0]
    for i in range(itens + 1):
        weights.append(int(input()))

    values = [0]
    for i in range(itens + 1):
        values.append(int(input()))

    print(f"The maximun value is: {knapsack(itens, capacity, values, weights)}")

if __name__ == "__main__":
    main()