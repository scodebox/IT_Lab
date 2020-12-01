# Function knapsack.
def knapsack(objects, profits, weights):
    cap_of_knapsack = 15
    value = 0
    ratio = []
    # Calculating the ratio.
    for i, j in zip(profits, weights):
        ratio.append(i/j)
    print('Ratio(profit/weight) : ', ratio)

    # Filling the bag with higher ratio.
    print('\nObject\tcap_of_knck\tprofit')
    print('#\t  ', cap_of_knapsack, '\t\t ', value)
    while cap_of_knapsack:
        # Getting the max ratio.
        index = ratio.index(max(ratio))
        if cap_of_knapsack > weights[index]:
            cap_of_knapsack -= weights[index]
            value += profits[index]
            print(objects[index], '\t  ', cap_of_knapsack, '\t\t ', value)
        else:
            value += (ratio[index]*cap_of_knapsack)
            cap_of_knapsack = 0
            print(objects[index], '\t  ', cap_of_knapsack, '\t\t ', value)
        del weights[index]
        del profits[index]
        del objects[index]
        del ratio[index]

    print('\nTotal profit : ', value)


# Main function.
if __name__ == '__main__':
    objects = [1, 2, 3, 4, 5, 6, 7]
    profits = [10, 5, 15, 7, 6, 18, 3]
    weights = [2, 3, 5, 7, 1, 4, 1]
    # Showing the details.
    print('Objects : ', objects)
    print('Profits : ', profits)
    print('Weights : ', weights)
    # Calling the knapsack.
    knapsack(objects, profits, weights)
