import cgitb; cgitb.enable();
import sys;
import re;
import time;

class PymlParser:
    def __init__(self, pyml):
        regex = re.compile('<\?py[\s]([^\?>]*)[\s]\?>');
        self.source = "print '''"+ pyml +"'''";
        self.parsestring = regex.sub(r"''';\g<1>\nprint '''", self.source);
        exec(self.parsestring);

print 'Status: 200 OK';
print 'Content-type: text/html';
print;

file = sys.argv[1].replace('\\', '\\\\');
pyml = open(file, 'r');
py = PymlParser(pyml.read());