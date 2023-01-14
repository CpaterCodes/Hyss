import pytest
from ..hyss.format import with_linebreaks, with_indents

def test_linebreaks():
    before = 'div{color:white;justify-content:center;}'
    after = 'div{\ncolor:white;\njustify-content:center;\n}\n'
    
    assert with_linebreaks(before) == after


def test_indents():
    before = 'div{\ncolor:white;\n}\np{\ncolor:black;\n}\n'
    after = 'div{\n\tcolor:white;\n}\np{\n\tcolor:black;\n}\n'

    assert with_indents(before) == after

