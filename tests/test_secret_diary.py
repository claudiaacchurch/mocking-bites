from lib.secret_diary import * 
from unittest.mock import Mock
import pytest 

# mock test unlock
def test_mock_unlock_unlocks_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.status == "unlocked"

# mock test read
def test_mock_read_raises_error_when_locked():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

def test_mock_read_returns_contents_when_unlocked():
    diary = Mock()
    diary.read.return_value = "first diary entry"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "first diary entry"

def test_mock_read_raises_error_when_locked():
    diary = Mock()
    diary.read.return_value = "first diary entry"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.status == "locked"