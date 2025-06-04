from eodbib.eodbib import Eodbib
from datetime import datetime

def test_title():
  rec = Eodbib()
  assert rec.record().title == 'Test Title 1'

def test_245_indicators():
  rec = Eodbib()
  field_245s = rec.record().get_fields('245')
  first_245 = field_245s[0]
  assert first_245.indicator1 == '0'
  assert first_245.indicator2 == '0'

def test_980_indicators():
  rec = Eodbib()
  field_980s = rec.record().get_fields('980')
  first_980 = field_980s[0]
  assert first_980.indicator1 == ' '
  assert first_980.indicator2 == ' '

def test_980_subfield_e():
  rec = Eodbib()
  field_980s = rec.record().get_fields('980')
  first_980 = field_980s[0]
  e_subfields = first_980.get_subfields('e')
  e_subfield_text = e_subfields[0]
  assert e_subfield_text == '1.00'

def test_980_subfield_g():
  rec = Eodbib()
  field_980s = rec.record().get_fields('980')
  first_980 = field_980s[0]
  g_subfields = first_980.get_subfields('g')
  g_subfield_text = g_subfields[0]
  assert g_subfield_text == '1'

def test_980_subfield_n():
  rec = Eodbib()
  field_980s = rec.record().get_fields('980')
  first_980 = field_980s[0]
  n_subfields = first_980.get_subfields('n')
  n_subfield_text = n_subfields[0]
  date = datetime.now().strftime('%Y-%m-%d')
  assert n_subfield_text == f'{date}-1'

def test_title_with_a_number():
  rec = Eodbib(3)
  assert rec.record().title == 'Test Title 3'

def test_only_one_980_field():
  rec = Eodbib(3)
  assert len(rec.record().get_fields('980')) == 1

def test_981_subfield_b_is_CLASS():
  rec = Eodbib(3)
  field_981 = rec.record().get_fields('981')
  if field_981:
    first_981 = field_981[0]
    b_subfields = first_981.get_subfields('b')
    if b_subfields:
      b_subfield_text = b_subfields[0]
  assert b_subfield_text == 'CLASS'

def test_records_title():
  rec = Eodbib()
  recs = rec.records(2)
  assert recs[0].title == 'Test Title 1'

def test_records_title2():
  rec = Eodbib()
  recs = rec.records(2)
  assert recs[1].title == 'Test Title 2'

def test_records_980_subfield_n():
  rec = Eodbib()
  recs = rec.records(2)
  field_980s = recs[1].get_fields('980')
  first_980 = field_980s[0]
  n_subfields = first_980.get_subfields('n')
  n_subfield_text = n_subfields[0]
  date = datetime.now().strftime('%Y-%m-%d')
  assert n_subfield_text == f'{date}-2'

