from pymarc import Record, Field, Subfield, Indicators
from datetime import datetime

class Eodbib:
      def __init__(self, number = 1):
        self.number = number  
        self.date = datetime.now().strftime('%Y-%m-%d')
    
      def record(self):
        record = Record()
        record.add_field(
          Field(
              tag = '245',
              indicators = Indicators('0','0'),
              subfields = [
                  Subfield(code='a', value=f'Test Title {self.number}')
              ]),
          Field(
              tag = '980',
              indicators = Indicators(' ',' '),
              subfields = [
                  Subfield(code='e', value='1.00'),
                  Subfield(code='g', value='1'),
                  Subfield(code='n', value=f'{self.date}-{self.number}')
              ]),
          Field(
              tag = '981',
              indicators = Indicators(' ',' '),
              subfields = [
                  Subfield(code='b', value='CLASS')
              ])
          )
        return record

      def records(self, count):
        eodrecords = []
        for i in range(1, count + 1):
          self.number = i
          newrecord = self.record()
          eodrecords.append(newrecord)
        return eodrecords