def print_dictionay(**kargs):
    for key, value in kargs.items():
        print(key, value)

d = {"apple":20, "banan":5, "grapes":30}
print_dictionay(**d)