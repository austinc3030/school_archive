class ErrorHandler(object):

    def __init__(self):
        """
        During initialization, create class variables to hold error count and exit message
        """
        self.error_count = 0  # Indicates success
        self.exit_message = ""  # Empty exit message