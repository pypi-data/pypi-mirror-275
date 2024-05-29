import librds

def test_ps():
    assert librds.GroupInterface.getPS("radio95") == ("radio95 ", 4)

def test_ps_long():
    assert librds.GroupInterface.getPS("radio95 radio95") == ("radio95 ", 4)

def test_rt():
    assert librds.GroupInterface.getRT("hi!") == ("hi!\r", 1)

def test_rt2():
    assert librds.GroupInterface.getRT("hello!") == ("hello!\r ", 2)

def test_rt_full():
    assert librds.GroupInterface.getRT("hello!",True) == ("hello!\r".ljust(64), 16)

def test_ptyn():
    assert librds.GroupInterface.getPTYN("Various") == ("Various".ljust(8), 2)