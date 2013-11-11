
import csv

class CSVParser(object):
    def __init__(self, file):
        if isinstance(file, basestring):
            fp = open(file, "rb")
        else:
            fp = file
        self.reader = csv.DictReader(fp)
        self.columns = [x.lower() for x in self.reader.fieldnames]

    def __iter__(self):
        for row in self.reader:
            yield dict((k.lower(), self._cast(v)) for k, v in row.items())
    
    def _cast(self, value):
	if self._is_float(value): 	
	   return float(value)
        if self._is_int(value):
	   return int(value)
        return value

    def _is_int(self,strvalue):
        try:
	   int(strvalue)
	   return True
        except ValueError: 
	   return False

    def _is_float(self,strvalue):
	try:
	   float(strvalue)
	   return '.' in strvalue
        except ValueError:
	   return False

