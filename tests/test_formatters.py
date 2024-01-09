import pytest
from .helpers import css_from_file
from ..hyss.format import with_linebreaks, with_indents


def test_linebreaks():
    minified_css = css_from_file('basic_sheet.css')
    linebroken_css = css_from_file('linebroken_sheet.css')
    assert with_linebreaks(minified_css) == linebroken_css 


def test_indents():
    linebroken_css = css_from_file('linebroken_sheet.css')
    indented_css = css_from_file('indented_sheet.css')
    assert with_indents(linebroken_css) == indented_css

