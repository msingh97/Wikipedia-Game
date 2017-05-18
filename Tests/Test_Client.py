def test(*args):
    """Runs tests and prints out their outputs in a friendly manner in the terminal. Assumes all tests take no
     arguments and throw Asserition Errors if they fail."""
    passed, failed = 0, 0
    print("-----RUNNING TESTS----- \n")
    for i in range(1, len(args) + 1):
        print("Test " + str(i) + ":")
        try:
            args[i]()
            passed += 1
            print("Passed. \n")
        except AssertionError as a:
            failed += 1
            print(a)
        except:
            failed += 1
            print("Code failed.")
    print("------------------------ \n")
    print("Results: " + str(passed) + " / " + str(len(args)) + " test cases passed.")