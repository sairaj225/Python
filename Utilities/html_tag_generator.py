
def tag( name, *content, cls = None, **attrs ):
    
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join( f' {attrs} = "{value}"'
                    for attrs, value in
                    sorted( attrs.items()))
                
    else:
        attr_str = ''

    if content:
        return '\n'.join(f'  <{name}{attr_str}>{c}</{name}>'
                for c in content)

    else:
        return f'<{name}{attr_str}/>'

print(tag("p", "hellow", "world", cls="one"))