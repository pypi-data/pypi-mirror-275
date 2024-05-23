from sanskritutf import sanskritutf

def test_encoding():
    # Amsterdam to Berlin
    assert sanskritutf.UtfListDecoder(['0903']) == 'ः'
