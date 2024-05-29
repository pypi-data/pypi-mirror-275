from abc import ABCMeta as ABCMeta0
from builtins import str as str1, bool as bool2, int as int5, RuntimeError as RuntimeError8, Exception as Exception15, len as len_1262, list as list_1279
from types import MappingProxyType as MappingProxyType3
from typing import Callable as Callable4, TypeVar as TypeVar6, Generic as Generic7, Sequence as Sequence9, Optional as Optional10, Union as Union11, Any as Any12, MutableSequence as MutableSequence13
from temper_core import cast_by_type as cast_by_type14, Label as Label16, isinstance_int as isinstance_int17, cast_by_test as cast_by_test18, list_join as list_join_1250, generic_eq as generic_eq_1253, list_builder_add as list_builder_add_1254, string_code_points as string_code_points_1257, list_get as list_get_1263, str_cat as str_cat_1273, int_to_string as int_to_string_1274
from temper_core.regex import regex_compile_formatted as regex_compile_formatted_1246, regex_compiled_found as regex_compiled_found_1247, regex_compiled_find as regex_compiled_find_1248, regex_compiled_replace as regex_compiled_replace_1249, regex_formatter_push_capture_name as regex_formatter_push_capture_name_1255, regex_formatter_push_code_to as regex_formatter_push_code_to_1256
class RegexNode(metaclass = ABCMeta0):
  def compiled(this__8) -> 'Regex':
    return Regex(this__8)
  def found(this__9, text__125: 'str1') -> 'bool2':
    return this__9.compiled().found(text__125)
  def find(this__10, text__128: 'str1') -> 'MappingProxyType3[str1, Group]':
    return this__10.compiled().find(text__128)
  def replace(this__11, text__131: 'str1', format__132: 'Callable4[[MappingProxyType3[str1, Group]], str1]') -> 'str1':
    return this__11.compiled().replace(text__131, format__132)
class Capture(RegexNode):
  name__134: 'str1'
  item__135: 'RegexNode'
  __slots__ = ('name__134', 'item__135')
  def constructor__136(this__52, name__137: 'str1', item__138: 'RegexNode') -> 'None':
    this__52.name__134 = name__137
    this__52.item__135 = item__138
  def __init__(this__52, name__137: 'str1', item__138: 'RegexNode') -> None:
    this__52.constructor__136(name__137, item__138)
  @property
  def name(this__336) -> 'str1':
    return this__336.name__134
  @property
  def item(this__340) -> 'RegexNode':
    return this__340.item__135
class CodePart(RegexNode, metaclass = ABCMeta0):
  pass
class CodePoints(CodePart):
  value__139: 'str1'
  __slots__ = ('value__139',)
  def constructor__140(this__54, value__141: 'str1') -> 'None':
    this__54.value__139 = value__141
  def __init__(this__54, value__141: 'str1') -> None:
    this__54.constructor__140(value__141)
  @property
  def value(this__316) -> 'str1':
    return this__316.value__139
class Special(RegexNode, metaclass = ABCMeta0):
  pass
class SpecialSet(CodePart, Special, metaclass = ABCMeta0):
  pass
class CodeRange(CodePart):
  min__149: 'int5'
  max__150: 'int5'
  __slots__ = ('min__149', 'max__150')
  def constructor__151(this__70, min__152: 'int5', max__153: 'int5') -> 'None':
    this__70.min__149 = min__152
    this__70.max__150 = max__153
  def __init__(this__70, min__152: 'int5', max__153: 'int5') -> None:
    this__70.constructor__151(min__152, max__153)
  @property
  def min(this__344) -> 'int5':
    return this__344.min__149
  @property
  def max(this__348) -> 'int5':
    return this__348.max__150
ITEM__19 = TypeVar6('ITEM__19', covariant = True)
class ItemizedRegex(Generic7[ITEM__19], RegexNode, metaclass = ABCMeta0):
  @property
  def items(this__20) -> 'Sequence9[ITEM__19]':
    raise RuntimeError8()
class CodeSet(ItemizedRegex[CodePart]):
  items__156: 'Sequence9[CodePart]'
  negated__157: 'bool2'
  __slots__ = ('items__156', 'negated__157')
  def constructor__158(this__74, items__159: 'Sequence9[CodePart]', negated: Optional10['bool2'] = None) -> 'None':
    negated__160: Optional10['bool2'] = negated
    if negated__160 is None:
      negated__160 = False
    this__74.items__156 = items__159
    this__74.negated__157 = negated__160
  def __init__(this__74, items__159: 'Sequence9[CodePart]', negated: Optional10['bool2'] = None) -> None:
    negated__160: Optional10['bool2'] = negated
    this__74.constructor__158(items__159, negated__160)
  @property
  def items(this__352) -> 'Sequence9[CodePart]':
    return this__352.items__156
  @property
  def negated(this__356) -> 'bool2':
    return this__356.negated__157
class Or(ItemizedRegex[RegexNode]):
  items__161: 'Sequence9[RegexNode]'
  __slots__ = ('items__161',)
  def constructor__162(this__77, items__163: 'Sequence9[RegexNode]') -> 'None':
    this__77.items__161 = items__163
  def __init__(this__77, items__163: 'Sequence9[RegexNode]') -> None:
    this__77.constructor__162(items__163)
  @property
  def items(this__320) -> 'Sequence9[RegexNode]':
    return this__320.items__161
class Repeat(RegexNode):
  item__164: 'RegexNode'
  min__165: 'int5'
  max__166: 'Union11[int5, None]'
  reluctant__167: 'bool2'
  __slots__ = ('item__164', 'min__165', 'max__166', 'reluctant__167')
  def constructor__168(this__80, item__169: 'RegexNode', min__170: 'int5', max__171: 'Union11[int5, None]', reluctant: Optional10['bool2'] = None) -> 'None':
    reluctant__172: Optional10['bool2'] = reluctant
    if reluctant__172 is None:
      reluctant__172 = False
    this__80.item__164 = item__169
    this__80.min__165 = min__170
    this__80.max__166 = max__171
    this__80.reluctant__167 = reluctant__172
  def __init__(this__80, item__169: 'RegexNode', min__170: 'int5', max__171: 'Union11[int5, None]', reluctant: Optional10['bool2'] = None) -> None:
    reluctant__172: Optional10['bool2'] = reluctant
    this__80.constructor__168(item__169, min__170, max__171, reluctant__172)
  @property
  def item(this__360) -> 'RegexNode':
    return this__360.item__164
  @property
  def min(this__364) -> 'int5':
    return this__364.min__165
  @property
  def max(this__368) -> 'Union11[int5, None]':
    return this__368.max__166
  @property
  def reluctant(this__372) -> 'bool2':
    return this__372.reluctant__167
class Sequence(ItemizedRegex[RegexNode]):
  items__181: 'Sequence9[RegexNode]'
  __slots__ = ('items__181',)
  def constructor__182(this__86, items__183: 'Sequence9[RegexNode]') -> 'None':
    this__86.items__181 = items__183
  def __init__(this__86, items__183: 'Sequence9[RegexNode]') -> None:
    this__86.constructor__182(items__183)
  @property
  def items(this__376) -> 'Sequence9[RegexNode]':
    return this__376.items__181
class Group:
  name__184: 'str1'
  value__185: 'str1'
  codePointsBegin__186: 'int5'
  __slots__ = ('name__184', 'value__185', 'codePointsBegin__186')
  def constructor__187(this__89, name__188: 'str1', value__189: 'str1', codePointsBegin__190: 'int5') -> 'None':
    this__89.name__184 = name__188
    this__89.value__185 = value__189
    this__89.codePointsBegin__186 = codePointsBegin__190
  def __init__(this__89, name__188: 'str1', value__189: 'str1', codePointsBegin__190: 'int5') -> None:
    this__89.constructor__187(name__188, value__189, codePointsBegin__190)
  @property
  def name(this__304) -> 'str1':
    return this__304.name__184
  @property
  def value(this__308) -> 'str1':
    return this__308.value__185
  @property
  def code_points_begin(this__312) -> 'int5':
    return this__312.codePointsBegin__186
class RegexRefs__21:
  codePoints__191: 'CodePoints'
  group__192: 'Group'
  orObject__193: 'Or'
  __slots__ = ('codePoints__191', 'group__192', 'orObject__193')
  def constructor__194(this__91, code_points: Optional10['CodePoints'] = None, group: Optional10['Group'] = None, or_object: Optional10['Or'] = None) -> 'None':
    codePoints__195: Optional10['CodePoints'] = code_points
    group__196: Optional10['Group'] = group
    orObject__197: Optional10['Or'] = or_object
    t_1213: 'CodePoints'
    t_1215: 'Group'
    t_1217: 'Or'
    if codePoints__195 is None:
      t_1213 = CodePoints('')
      codePoints__195 = t_1213
    if group__196 is None:
      t_1215 = Group('', '', 0)
      group__196 = t_1215
    if orObject__197 is None:
      t_1217 = Or(())
      orObject__197 = t_1217
    this__91.codePoints__191 = codePoints__195
    this__91.group__192 = group__196
    this__91.orObject__193 = orObject__197
  def __init__(this__91, code_points: Optional10['CodePoints'] = None, group: Optional10['Group'] = None, or_object: Optional10['Or'] = None) -> None:
    codePoints__195: Optional10['CodePoints'] = code_points
    group__196: Optional10['Group'] = group
    orObject__197: Optional10['Or'] = or_object
    this__91.constructor__194(codePoints__195, group__196, orObject__197)
  @property
  def code_points(this__324) -> 'CodePoints':
    return this__324.codePoints__191
  @property
  def group(this__328) -> 'Group':
    return this__328.group__192
  @property
  def or_object(this__332) -> 'Or':
    return this__332.orObject__193
class Regex:
  data__198: 'RegexNode'
  compiled__212: 'Any12'
  __slots__ = ('data__198', 'compiled__212')
  def constructor__199(this__22, data__200: 'RegexNode') -> 'None':
    this__22.data__198 = data__200
    t_1087: 'str1' = this__22.format__231()
    t_1088: 'Any12' = regex_compile_formatted_1246(this__22, t_1087)
    this__22.compiled__212 = t_1088
  def __init__(this__22, data__200: 'RegexNode') -> None:
    this__22.constructor__199(data__200)
  def found(this__23, text__203: 'str1') -> 'bool2':
    return regex_compiled_found_1247(this__23, this__23.compiled__212, text__203)
  def find(this__24, text__206: 'str1') -> 'MappingProxyType3[str1, Group]':
    return regex_compiled_find_1248(this__24, this__24.compiled__212, text__206, regexRefs__121)
  def replace(this__25, text__209: 'str1', format__210: 'Callable4[[MappingProxyType3[str1, Group]], str1]') -> 'str1':
    return regex_compiled_replace_1249(this__25, this__25.compiled__212, text__209, format__210, regexRefs__121)
  def format__231(this__30) -> 'str1':
    return RegexFormatter__31().format(this__30.data__198)
  @property
  def data(this__414) -> 'RegexNode':
    return this__414.data__198
class RegexFormatter__31:
  out__233: 'MutableSequence13[str1]'
  __slots__ = ('out__233',)
  def format(this__32, regex__235: 'RegexNode') -> 'str1':
    this__32.pushRegex__238(regex__235)
    t_1182: 'MutableSequence13[str1]' = this__32.out__233
    def fn__1179(x__237: 'str1') -> 'str1':
      return x__237
    return list_join_1250(t_1182, '', fn__1179)
  def pushRegex__238(this__33, regex__239: 'RegexNode') -> 'None':
    t_770: 'bool2'
    t_771: 'Capture'
    t_774: 'bool2'
    t_775: 'CodePoints'
    t_778: 'bool2'
    t_779: 'CodeRange'
    t_782: 'bool2'
    t_783: 'CodeSet'
    t_786: 'bool2'
    t_787: 'Or'
    t_790: 'bool2'
    t_791: 'Repeat'
    t_794: 'bool2'
    t_795: 'Sequence'
    try:
      cast_by_type14(regex__239, Capture)
      t_770 = True
    except Exception15:
      t_770 = False
    with Label16() as s__1251_1252:
      if t_770:
        try:
          t_771 = cast_by_type14(regex__239, Capture)
        except Exception15:
          s__1251_1252.break_()
        this__33.pushCapture__241(t_771)
      else:
        try:
          cast_by_type14(regex__239, CodePoints)
          t_774 = True
        except Exception15:
          t_774 = False
        if t_774:
          try:
            t_775 = cast_by_type14(regex__239, CodePoints)
          except Exception15:
            s__1251_1252.break_()
          this__33.pushCodePoints__257(t_775, False)
        else:
          try:
            cast_by_type14(regex__239, CodeRange)
            t_778 = True
          except Exception15:
            t_778 = False
          if t_778:
            try:
              t_779 = cast_by_type14(regex__239, CodeRange)
            except Exception15:
              s__1251_1252.break_()
            this__33.pushCodeRange__262(t_779)
          else:
            try:
              cast_by_type14(regex__239, CodeSet)
              t_782 = True
            except Exception15:
              t_782 = False
            if t_782:
              try:
                t_783 = cast_by_type14(regex__239, CodeSet)
              except Exception15:
                s__1251_1252.break_()
              this__33.pushCodeSet__268(t_783)
            else:
              try:
                cast_by_type14(regex__239, Or)
                t_786 = True
              except Exception15:
                t_786 = False
              if t_786:
                try:
                  t_787 = cast_by_type14(regex__239, Or)
                except Exception15:
                  s__1251_1252.break_()
                this__33.pushOr__280(t_787)
              else:
                try:
                  cast_by_type14(regex__239, Repeat)
                  t_790 = True
                except Exception15:
                  t_790 = False
                if t_790:
                  try:
                    t_791 = cast_by_type14(regex__239, Repeat)
                  except Exception15:
                    s__1251_1252.break_()
                  this__33.pushRepeat__284(t_791)
                else:
                  try:
                    cast_by_type14(regex__239, Sequence)
                    t_794 = True
                  except Exception15:
                    t_794 = False
                  if t_794:
                    try:
                      t_795 = cast_by_type14(regex__239, Sequence)
                    except Exception15:
                      s__1251_1252.break_()
                    this__33.pushSequence__289(t_795)
                  elif generic_eq_1253(regex__239, begin):
                    try:
                      list_builder_add_1254(this__33.out__233, '^')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, dot):
                    try:
                      list_builder_add_1254(this__33.out__233, '.')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, end):
                    try:
                      list_builder_add_1254(this__33.out__233, '$')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, word_boundary):
                    try:
                      list_builder_add_1254(this__33.out__233, '\\b')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, digit):
                    try:
                      list_builder_add_1254(this__33.out__233, '\\d')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, space):
                    try:
                      list_builder_add_1254(this__33.out__233, '\\s')
                    except Exception15:
                      s__1251_1252.break_()
                  elif generic_eq_1253(regex__239, word):
                    try:
                      list_builder_add_1254(this__33.out__233, '\\w')
                    except Exception15:
                      s__1251_1252.break_()
                  else:
                    None
      return
    raise RuntimeError8()
  def pushCapture__241(this__34, capture__242: 'Capture') -> 'None':
    list_builder_add_1254(this__34.out__233, '(')
    t_765: 'MutableSequence13[str1]' = this__34.out__233
    t_1166: 'str1' = capture__242.name
    regex_formatter_push_capture_name_1255(this__34, t_765, t_1166)
    t_1167: 'RegexNode' = capture__242.item
    this__34.pushRegex__238(t_1167)
    list_builder_add_1254(this__34.out__233, ')')
  def pushCode__248(this__36, code__249: 'int5', insideCodeSet__250: 'bool2') -> 'None':
    regex_formatter_push_code_to_1256(this__36, this__36.out__233, code__249, insideCodeSet__250)
  def pushCodePoints__257(this__38, codePoints__258: 'CodePoints', insideCodeSet__259: 'bool2') -> 'None':
    t_1155: 'int5'
    t_1156: 'Any12'
    t_1160: 'Any12' = string_code_points_1257(codePoints__258.value)
    slice__261: 'Any12' = t_1160
    while True:
      if not slice__261.is_empty:
        t_1155 = slice__261.read()
        this__38.pushCode__248(t_1155, insideCodeSet__259)
        t_1156 = slice__261.advance(1)
        slice__261 = t_1156
      else:
        break
  def pushCodeRange__262(this__39, codeRange__263: 'CodeRange') -> 'None':
    list_builder_add_1254(this__39.out__233, '[')
    this__39.pushCodeRangeUnwrapped__265(codeRange__263)
    list_builder_add_1254(this__39.out__233, ']')
  def pushCodeRangeUnwrapped__265(this__40, codeRange__266: 'CodeRange') -> 'None':
    t_1148: 'int5' = codeRange__266.min
    this__40.pushCode__248(t_1148, True)
    list_builder_add_1254(this__40.out__233, '-')
    t_1150: 'int5' = codeRange__266.max
    this__40.pushCode__248(t_1150, True)
  def pushCodeSet__268(this__41, codeSet__269: 'CodeSet') -> 'None':
    t_1144: 'int5'
    t_743: 'bool2'
    t_744: 'CodeSet'
    t_749: 'CodePart'
    adjusted__271: 'RegexNode' = this__41.adjustCodeSet__273(codeSet__269, regexRefs__121)
    try:
      cast_by_type14(adjusted__271, CodeSet)
      t_743 = True
    except Exception15:
      t_743 = False
    with Label16() as s__1258_1260:
      if t_743:
        with Label16() as s__1259_1261:
          try:
            t_744 = cast_by_type14(adjusted__271, CodeSet)
            list_builder_add_1254(this__41.out__233, '[')
          except Exception15:
            s__1259_1261.break_()
          if t_744.negated:
            try:
              list_builder_add_1254(this__41.out__233, '^')
            except Exception15:
              s__1259_1261.break_()
          else:
            None
          i__272: 'int5' = 0
          while True:
            t_1144 = len_1262(t_744.items)
            if i__272 < t_1144:
              try:
                t_749 = list_get_1263(t_744.items, i__272)
              except Exception15:
                s__1259_1261.break_()
              this__41.pushCodeSetItem__277(t_749)
              i__272 = i__272 + 1
            else:
              break
          try:
            list_builder_add_1254(this__41.out__233, ']')
            s__1258_1260.break_()
          except Exception15:
            pass
        raise RuntimeError8()
      this__41.pushRegex__238(adjusted__271)
  def adjustCodeSet__273(this__42, codeSet__274: 'CodeSet', regexRefs__275: 'RegexRefs__21') -> 'RegexNode':
    return codeSet__274
  def pushCodeSetItem__277(this__43, codePart__278: 'CodePart') -> 'None':
    t_730: 'bool2'
    t_731: 'CodePoints'
    t_734: 'bool2'
    t_735: 'CodeRange'
    t_738: 'bool2'
    t_739: 'SpecialSet'
    try:
      cast_by_type14(codePart__278, CodePoints)
      t_730 = True
    except Exception15:
      t_730 = False
    with Label16() as s__1264_1265:
      if t_730:
        try:
          t_731 = cast_by_type14(codePart__278, CodePoints)
        except Exception15:
          s__1264_1265.break_()
        this__43.pushCodePoints__257(t_731, True)
      else:
        try:
          cast_by_type14(codePart__278, CodeRange)
          t_734 = True
        except Exception15:
          t_734 = False
        if t_734:
          try:
            t_735 = cast_by_type14(codePart__278, CodeRange)
          except Exception15:
            s__1264_1265.break_()
          this__43.pushCodeRangeUnwrapped__265(t_735)
        else:
          try:
            cast_by_type14(codePart__278, SpecialSet)
            t_738 = True
          except Exception15:
            t_738 = False
          if t_738:
            try:
              t_739 = cast_by_type14(codePart__278, SpecialSet)
            except Exception15:
              s__1264_1265.break_()
            this__43.pushRegex__238(t_739)
          else:
            None
      return
    raise RuntimeError8()
  def pushOr__280(this__44, or__281: 'Or') -> 'None':
    t_1128: 'int5'
    t_722: 'RegexNode'
    t_727: 'RegexNode'
    with Label16() as s__1266_1268:
      if not (not or__281.items):
        with Label16() as s__1267_1270:
          try:
            list_builder_add_1254(this__44.out__233, '(?:')
            t_722 = list_get_1263(or__281.items, 0)
          except Exception15:
            s__1267_1270.break_()
          this__44.pushRegex__238(t_722)
          i__283: 'int5' = 1
          while True:
            t_1128 = len_1262(or__281.items)
            if i__283 < t_1128:
              try:
                list_builder_add_1254(this__44.out__233, '|')
                t_727 = list_get_1263(or__281.items, i__283)
              except Exception15:
                break
              this__44.pushRegex__238(t_727)
              i__283 = i__283 + 1
            else:
              try:
                list_builder_add_1254(this__44.out__233, ')')
              except Exception15:
                s__1267_1270.break_()
              s__1266_1268.break_()
        raise RuntimeError8()
  def pushRepeat__284(this__45, repeat__285: 'Repeat') -> 'None':
    t_1118: 'RegexNode'
    t_709: 'bool2'
    t_710: 'bool2'
    t_711: 'bool2'
    t_714: 'int5'
    t_716: 'MutableSequence13[str1]'
    with Label16() as s__1271_1272:
      min__287: 'int5'
      max__288: 'Union11[int5, None]'
      try:
        list_builder_add_1254(this__45.out__233, '(?:')
        t_1118 = repeat__285.item
        this__45.pushRegex__238(t_1118)
        list_builder_add_1254(this__45.out__233, ')')
        min__287 = repeat__285.min
        max__288 = repeat__285.max
      except Exception15:
        s__1271_1272.break_()
      if min__287 == 0:
        t_709 = max__288 == 1
      else:
        t_709 = False
      if t_709:
        try:
          list_builder_add_1254(this__45.out__233, '?')
        except Exception15:
          s__1271_1272.break_()
      else:
        if min__287 == 0:
          t_710 = max__288 == None
        else:
          t_710 = False
        if t_710:
          try:
            list_builder_add_1254(this__45.out__233, '*')
          except Exception15:
            s__1271_1272.break_()
        else:
          if min__287 == 1:
            t_711 = max__288 == None
          else:
            t_711 = False
          if t_711:
            try:
              list_builder_add_1254(this__45.out__233, '+')
            except Exception15:
              s__1271_1272.break_()
          else:
            try:
              list_builder_add_1254(this__45.out__233, str_cat_1273('{', int_to_string_1274(min__287)))
            except Exception15:
              s__1271_1272.break_()
            if min__287 != max__288:
              try:
                list_builder_add_1254(this__45.out__233, ',')
              except Exception15:
                s__1271_1272.break_()
              if max__288 != None:
                t_716 = this__45.out__233
                try:
                  t_714 = cast_by_test18(max__288, isinstance_int17)
                  list_builder_add_1254(t_716, int_to_string_1274(t_714))
                except Exception15:
                  s__1271_1272.break_()
              else:
                None
            else:
              None
            try:
              list_builder_add_1254(this__45.out__233, '}')
            except Exception15:
              s__1271_1272.break_()
      if repeat__285.reluctant:
        try:
          list_builder_add_1254(this__45.out__233, '?')
        except Exception15:
          s__1271_1272.break_()
      else:
        None
      return
    raise RuntimeError8()
  def pushSequence__289(this__46, sequence__290: 'Sequence') -> 'None':
    t_1116: 'int5'
    t_703: 'RegexNode'
    i__292: 'int5' = 0
    with Label16() as s__1275_1276:
      while True:
        t_1116 = len_1262(sequence__290.items)
        if i__292 < t_1116:
          try:
            t_703 = list_get_1263(sequence__290.items, i__292)
          except Exception15:
            break
          this__46.pushRegex__238(t_703)
          i__292 = i__292 + 1
        else:
          s__1275_1276.break_()
      raise RuntimeError8()
  def max_code(this__47, codePart__294: 'CodePart') -> 'Union11[int5, None]':
    return__120: 'Union11[int5, None]'
    t_1094: 'Any12'
    t_1096: 'Any12'
    t_1101: 'Union11[int5, None]'
    t_1104: 'Union11[int5, None]'
    t_1107: 'Union11[int5, None]'
    t_1110: 'Union11[int5, None]'
    t_676: 'bool2'
    t_677: 'CodePoints'
    t_689: 'bool2'
    t_690: 'CodeRange'
    try:
      cast_by_type14(codePart__294, CodePoints)
      t_676 = True
    except Exception15:
      t_676 = False
    with Label16() as s__1277_1278:
      if t_676:
        try:
          t_677 = cast_by_type14(codePart__294, CodePoints)
        except Exception15:
          s__1277_1278.break_()
        value__296: 'str1' = t_677.value
        if not value__296:
          return__120 = None
        else:
          max__297: 'int5' = 0
          t_1094 = string_code_points_1257(value__296)
          slice__298: 'Any12' = t_1094
          while True:
            if not slice__298.is_empty:
              next__299: 'int5' = slice__298.read()
              if next__299 > max__297:
                max__297 = next__299
              else:
                None
              t_1096 = slice__298.advance(1)
              slice__298 = t_1096
            else:
              break
          return__120 = max__297
      else:
        try:
          cast_by_type14(codePart__294, CodeRange)
          t_689 = True
        except Exception15:
          t_689 = False
        if t_689:
          try:
            t_690 = cast_by_type14(codePart__294, CodeRange)
            t_1101 = t_690.max
            return__120 = t_1101
          except Exception15:
            s__1277_1278.break_()
        elif generic_eq_1253(codePart__294, digit):
          t_1104 = string_code_points_1257('9').read()
          try:
            return__120 = t_1104
          except Exception15:
            s__1277_1278.break_()
        elif generic_eq_1253(codePart__294, space):
          t_1107 = string_code_points_1257(' ').read()
          try:
            return__120 = t_1107
          except Exception15:
            s__1277_1278.break_()
        elif generic_eq_1253(codePart__294, word):
          t_1110 = string_code_points_1257('z').read()
          try:
            return__120 = t_1110
          except Exception15:
            s__1277_1278.break_()
        else:
          return__120 = None
      return return__120
    raise RuntimeError8()
  def constructor__300(this__102, out: Optional10['MutableSequence13[str1]'] = None) -> 'None':
    out__301: Optional10['MutableSequence13[str1]'] = out
    t_1090: 'MutableSequence13[str1]'
    if out__301 is None:
      t_1090 = list_1279()
      out__301 = t_1090
    this__102.out__233 = out__301
  def __init__(this__102, out: Optional10['MutableSequence13[str1]'] = None) -> None:
    out__301: Optional10['MutableSequence13[str1]'] = out
    this__102.constructor__300(out__301)
regexRefs__121: 'RegexRefs__21' = RegexRefs__21()
class Begin__12(Special):
  __slots__ = ()
  def constructor__142(this__56) -> 'None':
    None
  def __init__(this__56) -> None:
    this__56.constructor__142()
begin: 'Special' = Begin__12()
class Dot__13(Special):
  __slots__ = ()
  def constructor__143(this__58) -> 'None':
    None
  def __init__(this__58) -> None:
    this__58.constructor__143()
dot: 'Special' = Dot__13()
class End__14(Special):
  __slots__ = ()
  def constructor__144(this__60) -> 'None':
    None
  def __init__(this__60) -> None:
    this__60.constructor__144()
end: 'Special' = End__14()
class WordBoundary__15(Special):
  __slots__ = ()
  def constructor__145(this__62) -> 'None':
    None
  def __init__(this__62) -> None:
    this__62.constructor__145()
word_boundary: 'Special' = WordBoundary__15()
class Digit__16(SpecialSet):
  __slots__ = ()
  def constructor__146(this__64) -> 'None':
    None
  def __init__(this__64) -> None:
    this__64.constructor__146()
digit: 'SpecialSet' = Digit__16()
class Space__17(SpecialSet):
  __slots__ = ()
  def constructor__147(this__66) -> 'None':
    None
  def __init__(this__66) -> None:
    this__66.constructor__147()
space: 'SpecialSet' = Space__17()
class Word__18(SpecialSet):
  __slots__ = ()
  def constructor__148(this__68) -> 'None':
    None
  def __init__(this__68) -> None:
    this__68.constructor__148()
word: 'SpecialSet' = Word__18()
def entire(item__173: 'RegexNode') -> 'RegexNode':
  global begin, end
  return Sequence((begin, item__173, end))
def one_or_more(item__175: 'RegexNode', reluctant: Optional10['bool2'] = None) -> 'Repeat':
  reluctant__176: Optional10['bool2'] = reluctant
  if reluctant__176 is None:
    reluctant__176 = False
  return Repeat(item__175, 1, None, reluctant__176)
def optional(item__178: 'RegexNode', reluctant: Optional10['bool2'] = None) -> 'Repeat':
  reluctant__179: Optional10['bool2'] = reluctant
  if reluctant__179 is None:
    reluctant__179 = False
  return Repeat(item__178, 0, 1, reluctant__179)
