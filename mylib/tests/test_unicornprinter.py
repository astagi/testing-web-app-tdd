from mylib.unicornprinter import uniformat

def test_uniformat():
    assert uniformat('Hello everyone!') == '🦄 Hello everyone!'

def test_uniformat_error():
    assert uniformat('Something went wrong!', 'E') == '🚨 Something went wrong!'