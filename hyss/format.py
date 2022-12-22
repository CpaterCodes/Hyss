
def with_linebreaks(css: str) -> str:
    return css.replace('{', '{\n').replace('}', '}\n').replace(';', ';\n')

