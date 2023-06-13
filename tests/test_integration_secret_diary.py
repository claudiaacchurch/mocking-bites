from lib.secret_diary import * 
from lib.diary import * 

# read returns contents if diary is unlocked
def test_read_returns_contents_unlocked():
    diary = Diary("this is my first diary entry")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    result = secret_diary.read()
    assert result == "this is my first diary entry"


