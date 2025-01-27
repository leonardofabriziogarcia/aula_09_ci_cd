import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    value1 = 3
    value2 = 9

    output = methods.soma(value1, value2)

    assert output == 12

def test_multiplicacao():
    value1 = 4
    value2 = 5

    output = methods.multiplicacao(value1, value2)

    assert output == 20

def test_divisao():
    value1 = 10
    value2 = 5

    output = methods.divisao(value1, value2)

    assert output == 2

def test_subtracao():
    value1 = 5
    value2 = 4

    output = methods.subtracao(value1, value2)

    assert output == 1
