# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.status = "locked"
        self.diary = diary

    def read(self):
        if self.status == "locked":
            raise Exception("Go away!")
        else:
            return self.diary.read()
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        pass

    def lock(self):
        self.status = "locked"

    def unlock(self):
        self.status = "unlocked"