def generate_slug(string: str) -> str:
    return '-'.join(string.lower().split(' '))
