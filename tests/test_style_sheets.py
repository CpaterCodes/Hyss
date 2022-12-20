import pytest
from ..hyss import stylesheet

def test_basic_stylesheet():
    css = "display:flex;justify-content:center;" 
    assert stylesheet(
            {'display': 'flex', 'justify-content': 'center'}
    ) == css


def test_multiple_classes():

    css = 'body{background-color:yellow;}div{display:flex;color:red;}' 
    assert stylesheet({
        'body': {
            'background-color': 'yellow'
        }, 
        'div': {
            'display': 'flex',
            'color': 'red'
        }
    }) == css
