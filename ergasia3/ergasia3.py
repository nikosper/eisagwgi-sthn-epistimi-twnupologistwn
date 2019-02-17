import re
import sys
#####
def remove_comments(text):

    pattern = r"""
          #
          
    """
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(noncomments)

if __name__ == '__ergasia3_':
    filename = sys.argv[1]
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments)
    fh = open(filename+".nocomments", "w")
    fh.write(code_wo_comments)
    fh.close()