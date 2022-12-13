from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(iterable, chunk_size):
    if not hasattr(iterable, '__iter__'):
        yield iterable
    else:
        i = 0
        chunk = []
        for item in iterable:
            chunk.append(item)
            i += 1
            if not i % chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
