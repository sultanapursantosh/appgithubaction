from src.mathoperations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,6)==11
def test_sub():
    assert sub(6,5)==1
    assert sub(5,6)==-1