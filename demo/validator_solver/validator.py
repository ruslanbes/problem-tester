def validate(f_in, f_out):
    fh_in = open(f_in, 'r')
    fh_out = open(f_out, 'r')
    a, b = map(int, fh_in.readline().split())
    expected = a + b
    actual = int(fh_out.readline())
    fh_in.close()
    fh_out.close()
    if expected != actual:
        print("FAIL: Expected:", expected, "Actual:", actual)
    return expected == actual
