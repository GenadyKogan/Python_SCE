def is_ok(x):
    is_int = False
    is_pos = False
    try:
        x = float(x)
        # Check if the number is integer or not
        is_int = x.is_integer()
        if x > 0:
            is_pos = True
    except ValueError:
        print("not even a number!")

    return is_int, is_pos

print(is_ok(1))