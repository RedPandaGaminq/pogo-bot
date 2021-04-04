class Penis:

    def __init__(self, user):
        self.user = str(user)
        self.user_id = str(user.id)
        self._length = 3

    def _get_length(self):
        return self._length

    def _set_length(self, new_length):
        self._length = new_length

    length = property(_get_length, _set_length)

