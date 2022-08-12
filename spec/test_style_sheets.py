import pytest
from HYSS.hyss import stylesheet

def test_basic_stylesheet():
    assert stylesheet({'display': 'flex', 'justify-content': 'center'}) == "display:flex;justify-content:center;"

