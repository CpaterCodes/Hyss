import pytest 
from ..hyss import sub_style, stylesheet

def test_basic_substyle():
    target = 'body{background-color:blue;}body div{color:yellow;}body p{color:white;}'
    assert stylesheet({
        'body': { 'background-color': 'blue'},
        **sub_style('body', 
            {
                'div': {'color': 'yellow'},
                'p': {'color':'white'}
            }
        ),
        }) == target
