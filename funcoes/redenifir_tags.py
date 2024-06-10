
def remover_(element):
    if '_' in element.tag:
        element.tag = element.tag.split('_', 1)[1]
    for child in list(element):
        remover_(child)