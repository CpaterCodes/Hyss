import pytest
from ..hyss.format import with_linebreaks

def test_linebreaks():
    before = 'div{color:white;justify-content:center;}'
    after = 'div{\ncolor:white;\njustify-content:center;\n}\n'
    
    assert with_linebreaks(before) == after


