# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.

    current_frame = currentframe()
   
    if current_frame:
        current_frame = current_frame.f_back

    while hasattr(current_frame, "f_code"):
        frame_code = current_frame.f_code
        filename = os.path.normcase(frame_code.co_filename)

        if filename == _srcfile:
            current_frame = current_frame.f_back
        else:
            return (frame_code.co_filename, frame_code.f_lineno, frame_code.co_name)
        

    return "(unknown file)", 0, "(unknown function)"

# How can we make this code better?
