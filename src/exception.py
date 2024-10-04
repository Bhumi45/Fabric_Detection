import sys

def error_message_detail(error, error_detail: sys):
    """
    Method to get the error details like filename, line number and error message.
    
    Parameters
    ----------
    error : Exception
        The exception raised.
    error_detail : sys
        The sys module with the exception details.
    
    Returns
    -------
    str
        The error message with filename, line number and the actual error message.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        Initializes CustomException object with error message and error details.

        Parameters
        ----------
        error_message : str
            The error message to be displayed.
        error_detail : sys
            The sys object containing the error details.

        Returns
        -------
        CustomException
            The CustomException object.
        """

        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message