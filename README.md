# Hyss - High Ympact Style Sheets

### Contents

-[Rationale](#rationale)
-[Basics](#basics)
-[Other Powers](#other-powers)
-[Animations](#animations)
-[Formatting](#formatting)
-[Future Intentions](#future-intentions)

## Rationale

Hyss is intended to allow the definition of CSS styles within python 
dictionaries, which provides a simple and flexible interface by which to 
inject python variables and re-use sets of style attributes.

Handlers also exist for formatting and animations.

## Basics

Here is a set of examples to illustrate the behaviour of functions within 
hyss. 

The `stylesheet` function can take a nested dictionary structure and 
generate minified css. Consider the following code:

```python
from hyss import stylesheet

colour = 'yellow'

example_css = stylesheet(
        {
            'body': {
                'background-color': colour,
            }, 
            'div': {
                'color': 'red'
            }
        }
```

The `example_css` variable will now contain the following css:

```css
body{background-color:yellow;}div{color:red;}
```

## Other Powers
**(Or, the use cases of css-in-python)**

### component reuse 

Say, for argument's sake, we had a number of cases where we needed to
centre text within a number of elements. A working set of CSS rules to do 
this is presented in a class `.centreText`:

```css
.centerText {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

However, instead of needing to apply these three CSS rules to all of our
components, we can simply store it as a python dictionary and include it 
into our class dictionaries as follows:

```python 

from hyss import stylesheet

center_text = {
    'display': 'flex', 
    'justify-content': 'center', 
    'align-items': 'center'
}

centered_elements = stylesheet(
    {
        '#banner':{ 
            **center_text, 
            'font-size': 'xx-large'
        },
        '.card':{ 
            **center_text, 
            'background-color': 'black', 
            'border-radius': '1rem'
        },
        'li':{ 
            **center_text 
        }
    }
)

```

### Sub Styling

Naturally, it is possible to do sub-styling as follows:

```python 
from hyss import stylesheet

sub_styled_css = stylesheet({
    'main h1': {'color': 'black'},
    'main h2': {'background-color': 'black', 'color': 'white'}
})
```

It is also possible to take advantage of CSS nesting, a CSS module explained
[here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_nesting).
However, in the scenario that CSS nesting is not supported in the target 
browser, Hyss provides the `sub_style` function for use as follows:

```python 
from hyss import stylesheet, sub_style

black_header = {'color': 'white', 'background-color': 'black'}
white_header = {'background-color': 'white', 'color': 'black'}

sub_styled_css = stylesheet({
    **sub_style('main', {
        'h1': white_header,
        'h2': black_header,
    }
})

```

As seen, the parent element name can be provided as a string, followed by a
dictionary representing CSS to be transpiled by the `stylesheet` function.

## Animations 

*Todo*

## Formatting

For some ease of reading and debugging, hyss provides utilities to provide 
linebreaks and subsequently indentation to CSS, whether produced by Hyss or 
otherwise.

### with_linebreaks

Consider the following code:

```python
from hyss.format import with_linebreaks

minified_css = "body{background-color:yellow;}div{color:red;}"

linebreak_css = with_linebreaks(minified_css)
```

The css in `linebreak_css` will look as follows in a file:

```css
body{
background-color:yellow;
}
div{
color:red;
}

```

### with_indents

Again, consider the previous code, but with `with_indents` applied:

```python
from hyss.format import with_linebreaks, with_indents

minified_css = "body{background-color:yellow;}div{color:red;}"

linebreak_css = with_linebreaks(minified_css)

indented_css = with_indents(linebreak_css)
```

The resulting CSS in `indented_css` will appear as such in a file:

```css
body{
    background-color:yellow;
}
div{
    color:red;
}
```

## Future Intentions 

Current plans are for comprehensive documentation as well as further
provisions of dedicated utilities for CSS features. 
Testing may also be refactored so as to provide a clear specification of 
expected Hyss function behaviours.

