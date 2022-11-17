import pytest
from ..hyss import stylesheet

def test_basic_stylesheet():
    assert stylesheet({'display': 'flex', 'justify-content': 'center'}) == "display:flex;justify-content:center;"


def test_multiple_classes():
    classes = stylesheet({
        'body': {
            'background-color': 'yellow',
            'overflow': 'auto',
        }, 
        'div': {
            'display': 'flex',
            'color': 'red'
        }
    })
    assert classes == 'body{background-color:yellow;overflow:auto;}div{display:flex;color:red;}'

