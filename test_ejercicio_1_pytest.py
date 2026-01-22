# prueba para comprobar funcionamiento de la funcion capital_case:

import pytest

def capital_case(x):  
    if not isinstance(x, str):  
        raise TypeError('Debes de proporcionar un string')         
    return x.capitalize() 

def test_capital_case():
    assert capital_case('semáforo') == 'Semáforo' 

# segundo test donde se comprueba si nuestra funcion capital_test tiene alguna comprobación respescto a los tipos de entrada

def test_raises_exception_on_non_string_arguments(): 
    with  pytest.raises(TypeError):  
        capital_case(9)