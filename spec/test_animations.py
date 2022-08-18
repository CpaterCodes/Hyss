import pytest
from HYSS.hyss import stylesheet, animation

def test_default():
    style = stylesheet({
        'div': {
            'color': 'blue'
            },
        **animation(
            'move',
            ['div'],
            {'from':{'color': 'black'}, 'to': {'color': 'blue'}}
        )
        })

    intent = "div{color:blue;}@keyframes move{from{color:black;}to{color:blue;}}div{animation:move 0ms ease 0ms 1 normal none running;}"
    assert style == intent

def test_animation():
    pass

def test_multiple_targets():
    pass
