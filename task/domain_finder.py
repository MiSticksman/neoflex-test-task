from typing import Optional


def find_domain(url: str) -> Optional[str]:
    if 'http://' in url or 'https://' in url:
        domain = url.split('://')[1]
    else:
        raise Exception('invalid url format')
    if '/' in domain:
        domain = domain.split('/')[0]
    domain = domain.split('.')
    if len(domain) == 2:
        return domain[0]
    elif len(domain) == 3:
        if domain[0] == 'www':
            return domain[1]
        else:
            raise Exception('url format: invalid "www"')
