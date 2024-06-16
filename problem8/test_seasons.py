from seasons import birth 
def test_birth():
    assert birth("2000-03-24") == "Twelve million, six hundred fifty-six thousand, one hundred sixty minutes"
    assert birth("1999-12-04") == "Twelve million, eight hundred sixteen thousand minutes"
    assert birth("1998-07-05") == ("Thirteen million, five hundred sixty thousand, four hundred eighty minutes") 
def test_invalid():
    assert birth("july 9, 1999") == "Invalid Date"
    assert birth("sahajja") == "Invalid Date"
   