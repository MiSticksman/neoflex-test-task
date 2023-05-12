from task.domain_finder import find_domain

import pytest


def test_find_domain():
    assert find_domain('http://github.com/carbonfive/raygun') == 'github'
    assert find_domain('http://www.zombie-bites.com') == 'zombie-bites'
    assert find_domain('https://www.cnet.com') == 'cnet'
    assert find_domain('https://www.stackoverflow.com/') == 'stackoverflow'


def test1_invalid_url():
    with pytest.raises(Exception):
        find_domain('http:/www.cnet.com')


def test2_invalid_url():
    with pytest.raises(Exception):
        find_domain('www.stackoverflow.com/')


def test1_invalid_www():
    with pytest.raises(Exception):
        find_domain('https://ww.stackoverflow.com/')


def test2_invalid_www():
    with pytest.raises(Exception):
        find_domain('https://wwww.stackoverflow.com/')