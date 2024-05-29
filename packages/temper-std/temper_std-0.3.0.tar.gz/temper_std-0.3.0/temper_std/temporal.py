from typing import Sequence as Sequence9, Any as Any12
from builtins import int as int5, bool as bool2, str as str1
from temper_core import int_to_string as int_to_string_1274, string_code_points as string_code_points_1257, str_cat as str_cat_1273
# Type nym`std//temporal.temper.md`.Date connected to datetime.date
daysInMonth__26: 'Sequence9[int5]' = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def isLeapYear__24(year__29: 'int5') -> 'bool2':
  return__16: 'bool2'
  t_168: 'int5'
  if year__29 % 4 == 0:
    if year__29 % 100 != 0:
      return__16 = True
    else:
      t_168 = year__29 % 400
      return__16 = t_168 == 0
  else:
    return__16 = False
  return return__16
def pad__25(padding__31: 'str1', num__32: 'int5') -> 'str1':
  'If the decimal representation of \\|num\\| is longer than [padding],\nthen that representation.\nOtherwise any sign for [num] followed by the prefix of [padding]\nthat would bring the integer portion up to the length of [padding].\n\n```temper\npad("0000", 123) == "0123") &&\npad("000", 123) == "123") &&\npad("00", 123) == "123") &&\npad("0000", -123) == "-0123") &&\npad("000", -123) == "-123") &&\npad("00", -123) == "-123")\n```'
  return__17: 'str1'
  t_228: 'Any12'
  decimal__34: 'str1' = int_to_string_1274(num__32, 10)
  t_224: 'Any12' = string_code_points_1257(decimal__34)
  decimalCodePoints__35: 'Any12' = t_224
  sign__36: 'str1'
  if decimalCodePoints__35.read() == 45:
    sign__36 = '-'
    t_228 = decimalCodePoints__35.advance(1)
    decimalCodePoints__35 = t_228
  else:
    sign__36 = ''
  paddingCp__37: 'Any12' = string_code_points_1257(padding__31)
  nNeeded__38: 'int5' = paddingCp__37.length - decimalCodePoints__35.length
  if nNeeded__38 <= 0:
    return__17 = decimal__34
  else:
    pad__39: 'str1' = paddingCp__37.limit(nNeeded__38).to_string()
    decimalOnly__40: 'str1' = decimalCodePoints__35.to_string()
    return__17 = str_cat_1273(sign__36, pad__39, decimalOnly__40)
  return return__17
dayOfWeekLookupTableLeapy__27: 'Sequence9[int5]' = (0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)
dayOfWeekLookupTableNotLeapy__28: 'Sequence9[int5]' = (0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)
