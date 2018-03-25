from flattener import arrayFlattener


def test_answer():
    flattener = arrayFlattener()

    array = [[1,2,[3, [5, [8, 9],7, [[6]]]]],4]
    flattened = flattener.flatten(array)
    print(flattened)
    assert flattened == [1,2,3,5,8,9,7,6,4]