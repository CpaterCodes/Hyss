import pytest
from ..hyss import stylesheet

def test_style_attributes():
    css = 'display:flex;justify-content:center;'
    assert stylesheet(
            {'display': 'flex', 'justify-content': 'center'}
    ) == css


def test_full_stylesheet():
    
    with open('tests/assets/basic_sheet.css', 'r') as basic_sheet:
        css = basic_sheet.read().strip() 
    assert stylesheet({
        'body': {
            'background-color': 'yellow'
        }, 
        'div': {
            'display': 'flex',
            'color': 'red'
        }
    }) == css
