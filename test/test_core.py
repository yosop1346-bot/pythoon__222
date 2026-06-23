from importlib import import_module


TextAnalyzer = import_module(
    "\ub098\uc758_\ud328\ud0a4\uc9c0.subclass"
).TextAnalyzer


def test_word_count():
    analyzer = TextAnalyzer("Python package test")

    assert analyzer.word_count() == 3


def test_char_count():
    analyzer = TextAnalyzer("ab cd")

    assert analyzer.char_count() == 4


def test_sentence_count():
    analyzer = TextAnalyzer("Hello. Python test!")

    assert analyzer.sentence_count() == 2


def test_analyze():
    analyzer = TextAnalyzer("Hello world.")

    assert analyzer.analyze() == {
        "\글자수": 11,
        "\문자수": 1,
        "\단어수": 2,
    }
