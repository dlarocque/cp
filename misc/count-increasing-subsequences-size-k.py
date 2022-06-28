def num_increasing_subsequences(a, k) -> int:
    n = len(a)
    num_subs = [1] * n
    
    for _ in range(2, k+1):
        for j in range(n-1, -1, -1):
            num_subs[j] = 0
            for i in range(j-1, -1, -1):
                if a[i] < a[j]:
                    num_subs[j] += num_subs[i]

        print(num_subs, sum(num_subs))

    return sum(num_subs)

print(num_increasing_subsequences([1, 2, 3, 4, 5], 4))
