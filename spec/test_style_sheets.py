from hyss import stylesheet
import pytest

def test_basic_stylesheet():
    assert stylesheet({'display': 'flex', 'justify-content': 'center'}) == "display:flex;justify-content:center;"

