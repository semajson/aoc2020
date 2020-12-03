import timeit


def time_algo(solver, input, *args):
    print("Testing algo", solver.__name__)
    print(
        "The algo took: ", timeit.Timer(lambda: solver(input, *args)).timeit(number=10)
    )
    print("")