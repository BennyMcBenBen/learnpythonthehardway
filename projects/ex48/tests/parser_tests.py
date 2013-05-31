from nose.tools import *
from ex48 import lexicon, parser
from ex48.parser import ParserError

def parse_sentence(sentence):
    return parser.parse_sentence(lexicon.scan(sentence))

def test_none_word_list():
    assert_is_none(parser.match(None, 'noun'))

def test_match_not_expecting():
    assert_is_none(parser.match([('error', 'SPAM')], 'noun'))

def test_go_north():
    sentence = parse_sentence("go north")
    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "go")
    assert_equal(sentence.object, "north")
    
def test_kill_the_princess():
    sentence = parse_sentence("kill the princess")
    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "kill")
    assert_equal(sentence.object, "princess")
    
def test_eat_the_bear():
    sentence = parse_sentence("eat the bear")
    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "eat")
    assert_equal(sentence.object, "bear")

def test_bear_eat_the_princess():
    sentence = parse_sentence("bear eat the princess")
    assert_equal(sentence.subject, "bear")
    assert_equal(sentence.verb, "eat")
    assert_equal(sentence.object, "princess")

def test_empty():
    assert_raises(ParserError, parse_sentence, "")
    
def test_subject_error():
    assert_raises(ParserError, parse_sentence, "SPAM go north")

def test_verb_error():
    assert_raises(ParserError, parse_sentence, "princess SPAM north")
    
def test_object_error():
    assert_raises(ParserError, parse_sentence, "go SPAM")
