

def generate_hashtag(data: str) -> str | bool:
    if len(data) == 0:
        return False
    result = '#' + str(data.title().replace(' ', ''))
    return result if 1 < len(result) <= 140 else False

