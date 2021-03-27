reversort(lst):
    rlst = []
    for k in range(1, len(lst) + 1):
        rlst += [lst[-k]]
    return rlst


def get_cost(length, lst):
    cost = 0
    for i in range(length-1):
        j = lst.index(min(lst[i:]))
        cost += j-i+1
        lst = lst[:i] + reversort(lst[i:j+1]) + lst[j+1:]
    return cost


def main():
    T = int(input())
    for case in range(1, T + 1):
        length = int(input())
        lst = [int(s) for s in input().split(" ")]
        print("Case #{}: {}".format(case, get_cost(length, lst)))


if __name__ == '__main__':
    main()
