class ComplaintValidator():
    def __init__(self, request_args):
        self._error = None
        self._request_args = request_args

    @property
    def error(self):
        return self._error

    def validate(self):
        return self