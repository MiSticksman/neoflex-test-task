from task.hashtag_generator import generate_hashtag


def test_generate_hashtag_func():
    assert generate_hashtag('Hello there thanks for trying my Kata') == '#HelloThereThanksForTryingMyKata'
    assert generate_hashtag('    Hello    World   ') == '#HelloWorld'
    assert generate_hashtag('    hello  World i am  mr  robot  ') == '#HelloWorldIAmMrRobot'
    assert generate_hashtag('The Last Wish is the first volume of the literary series titled '
                            'The Witcher written by the Polish author Andrzej Sapkowski. '
                            'It consists of seven short stories with one principal character Geralt from Rivia.') is False
    assert generate_hashtag('') is False
    assert generate_hashtag('      ') is False
