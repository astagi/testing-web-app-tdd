from mylib.unicornprinter import uniformat

def test_uniformat():
    assert uniformat('Hello everyone!') == '🦄 Hello everyone!'

def test_uniformat_error():
    assert uniformat('Something went wrong!', 'E') == '🚨 Something went wrong!'

def test_uniformat_warning():
    assert uniformat('Pay attention!', 'W') == '⚠️ Pay attention!'

def test_uniformat_nonsense():
    assert uniformat('Nonsense type!', 'NNS') == '🦄 Nonsense type!'