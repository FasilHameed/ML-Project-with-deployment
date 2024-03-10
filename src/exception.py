import sys


def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format()
    file_name=exc_tb.tb_frame.f_code.co_filename
    