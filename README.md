# Hyss - High Impact Style Sheets

## Rationale

Define styles as python dicts! All of the power of python, realised to create stylesheets.

## Features

- Create minified css content from a nested dictionary structure

- Helper for compound css classes (think 'div p', 'main section')  


## TODO

- Generate helpers for features such as keyframe animations.

- Create a means of generating individual styles to be scoped to specific element tags, akin to
how style sheets function in many css-in-js libraries

## Usage Demonstration

The most basic function is _stylesheet()_, which takes a structure such as that shown and creates minified css.
For ease of debugging, a second value _False_ can be passed to the function to generate a more readable format for ease of debugging. 

```
    # Basic stylesheet definition  

    stylesheet(
        {
            'body': {
                'background-color': 'yellow',
            }, 
            'div': {
                'color': 'red'
            }
        }
    ) => 'body{background-color:yellow;}div{color:red;}'

    # Debugging
    
    stylesheet(
        {
            'body': {
                'background-color': 'yellow',
            }, 
            'div': {
                'color': 'red'
            }
        },
	minify = False
    ) => 'body{
    	  background-color:yellow;
	  }
	  div{
	  color:red;
	  }'

    # This isn't intended for production use, but may be useful for debugging purposes (especially in finding or examining novel problems/challenges)
``
