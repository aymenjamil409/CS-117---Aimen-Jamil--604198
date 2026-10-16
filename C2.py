def parallel_r(resistors):
    reciprocal_sum = 0
    for r in resistors:
        reciprocal_sum = reciprocal_sum + (1 / r)
    r_eq = 1 / reciprocal_sum
    return r_eq
test_1 = [10, 10,15 ,60 ]
result_1 = parallel_r(test_1)
print("parallel_r([10, 10]) ->", result_1)
test_2 = [100, 200, 300 , 400]
result_2 = parallel_r(test_2)
print("parallel_r([100, 200, 300]) ->", result_2)
