from typing import Any as Any12, MutableSequence as MutableSequence13, Callable as Callable4, Sequence as Sequence9, Union as Union11, Optional as Optional10
from temper_core import LoggingConsole as LoggingConsole19, Pair as Pair_1283, Label as Label16, list_builder_add as list_builder_add_1254, list_join as list_join_1250, list_map as list_map_1284, list_get as list_get_1263, str_cat as str_cat_1273
from builtins import bool as bool2, str as str1, Exception as Exception15, int as int5, RuntimeError as RuntimeError8, tuple as tuple_1282, list as list_1279, len as len_1262
console_88: 'Any12' = LoggingConsole19(__name__)
class Test:
  passing__16: 'bool2'
  failedOnAssert__17: 'bool2'
  hasUnhandledFail__18: 'bool2'
  _failedOnAssert__58: 'bool2'
  _passing__59: 'bool2'
  _messages__60: 'MutableSequence13[str1]'
  __slots__ = ('passing__16', 'failedOnAssert__17', 'hasUnhandledFail__18', '_failedOnAssert__58', '_passing__59', '_messages__60')
  def assert_(this__7, success__36: 'bool2', message__37: 'Callable4[[], str1]') -> 'None':
    if not success__36:
      this__7._passing__59 = False
      list_builder_add_1254(this__7._messages__60, message__37())
    else:
      None
  def assert_hard(this__8, success__40: 'bool2', message__41: 'Callable4[[], str1]') -> 'None':
    this__8.assert_(success__40, message__41)
    if not success__40:
      this__8._failedOnAssert__58 = True
      assert False, str1(this__8.messages_combined())
    else:
      None
  def soft_fail_to_hard(this__9) -> 'None':
    if this__9.has_unhandled_fail:
      this__9._failedOnAssert__58 = True
      assert False, str1(this__9.messages_combined())
    else:
      None
  @property
  def passing(this__11) -> 'bool2':
    return this__11._passing__59
  def messages(this__12) -> 'Sequence9[str1]':
    return tuple_1282(this__12._messages__60)
  @property
  def failed_on_assert(this__13) -> 'bool2':
    return this__13._failedOnAssert__58
  @property
  def has_unhandled_fail(this__14) -> 'bool2':
    t_186: 'bool2'
    if this__14._failedOnAssert__58:
      t_186 = True
    else:
      t_186 = this__14._passing__59
    return not t_186
  def messages_combined(this__15) -> 'Union11[str1, None]':
    return__30: 'Union11[str1, None]'
    t_291: 'MutableSequence13[str1]'
    t_292: 'Union11[str1, None]'
    if not this__15._messages__60:
      return__30 = None
    else:
      t_291 = this__15._messages__60
      def fn__288(it__57: 'str1') -> 'str1':
        return it__57
      t_292 = list_join_1250(t_291, ', ', fn__288)
      return__30 = t_292
    return return__30
  def constructor__61(this__19, failed_on_assert: Optional10['bool2'] = None, passing: Optional10['bool2'] = None, messages: Optional10['MutableSequence13[str1]'] = None) -> 'None':
    _failedOnAssert__62: Optional10['bool2'] = failed_on_assert
    _passing__63: Optional10['bool2'] = passing
    _messages__64: Optional10['MutableSequence13[str1]'] = messages
    t_285: 'MutableSequence13[str1]'
    if _failedOnAssert__62 is None:
      _failedOnAssert__62 = False
    if _passing__63 is None:
      _passing__63 = True
    if _messages__64 is None:
      t_285 = list_1279()
      _messages__64 = t_285
    this__19._failedOnAssert__58 = _failedOnAssert__62
    this__19._passing__59 = _passing__63
    this__19._messages__60 = _messages__64
  def __init__(this__19, failed_on_assert: Optional10['bool2'] = None, passing: Optional10['bool2'] = None, messages: Optional10['MutableSequence13[str1]'] = None) -> None:
    _failedOnAssert__62: Optional10['bool2'] = failed_on_assert
    _passing__63: Optional10['bool2'] = passing
    _messages__64: Optional10['MutableSequence13[str1]'] = messages
    this__19.constructor__61(_failedOnAssert__62, _passing__63, _messages__64)
test_name: 'Any12' = ('<<lang.temper.value.TType: Type, lang.temper.value.Value: String: Type>>', NotImplemented)[1]
test_fun: 'Any12' = ('<<lang.temper.value.TType: Type, lang.temper.value.Value: fn (Test): (Void | Bubble): Type>>', NotImplemented)[1]
test_case: 'Any12' = ('<<lang.temper.value.TType: Type, lang.temper.value.Value: Pair<String, fn (Test): (Void | Bubble)>: Type>>', NotImplemented)[1]
test_failure_message: 'Any12' = ('<<lang.temper.value.TType: Type, lang.temper.value.Value: String: Type>>', NotImplemented)[1]
test_result: 'Any12' = ('<<lang.temper.value.TType: Type, lang.temper.value.Value: Pair<String, List<String>>: Type>>', NotImplemented)[1]
def process_test_cases(testCases__65: 'Sequence9[(Pair_1283[str1, (Callable4[[Test], None])])]') -> 'Sequence9[(Pair_1283[str1, (Sequence9[str1])])]':
  global list_map_1284
  def fn__278(testCase__67: 'Pair_1283[str1, (Callable4[[Test], None])]') -> 'Pair_1283[str1, (Sequence9[str1])]':
    global Pair_1283, tuple_1282
    t_269: 'bool2'
    t_271: 'Sequence9[str1]'
    t_168: 'bool2'
    key__69: 'str1' = testCase__67.key
    fun__70: 'Callable4[[Test], None]' = testCase__67.value
    test__71: 'Test' = Test()
    hadBubble__72: 'bool2'
    try:
      fun__70(test__71)
      hadBubble__72 = False
    except Exception15:
      hadBubble__72 = True
    messages__73: 'Sequence9[str1]' = test__71.messages()
    failures__74: 'Sequence9[str1]'
    if test__71.passing:
      failures__74 = ()
    else:
      if hadBubble__72:
        t_269 = test__71.failed_on_assert
        t_168 = not t_269
      else:
        t_168 = False
      if t_168:
        allMessages__75: 'MutableSequence13[str1]' = list_1279(messages__73)
        list_builder_add_1254(allMessages__75, 'Bubble')
        t_271 = tuple_1282(allMessages__75)
        failures__74 = t_271
      else:
        failures__74 = messages__73
    return Pair_1283(key__69, failures__74)
  return list_map_1284(testCases__65, fn__278)
def report_test_results(testResults__76: 'Sequence9[(Pair_1283[str1, (Sequence9[str1])])]') -> 'None':
  global console_88
  t_256: 'int5'
  t_257: 'str1'
  t_261: 'str1'
  t_154: 'Pair_1283[str1, (Sequence9[str1])]'
  i__78: 'int5' = 0
  with Label16() as s__1285_1286:
    while True:
      t_256 = len_1262(testResults__76)
      if i__78 < t_256:
        try:
          t_154 = list_get_1263(testResults__76, i__78)
        except Exception15:
          break
        testResult__79: 'Pair_1283[str1, (Sequence9[str1])]' = t_154
        failureMessages__80: 'Sequence9[str1]' = testResult__79.value
        if not failureMessages__80:
          t_261 = testResult__79.key
          console_88.log(str_cat_1273(t_261, ': Passed'))
        else:
          def fn__254(it__82: 'str1') -> 'str1':
            return it__82
          message__81: 'str1' = list_join_1250(failureMessages__80, ', ', fn__254)
          t_257 = testResult__79.key
          console_88.log(str_cat_1273(t_257, ': Failed ', message__81))
        i__78 = i__78 + 1
      else:
        s__1285_1286.break_()
    raise RuntimeError8()
def run_test_cases(testCases__83: 'Sequence9[(Pair_1283[str1, (Callable4[[Test], None])])]') -> 'None':
  global process_test_cases, report_test_results
  report_test_results(process_test_cases(testCases__83))
def run_test(testFun__85: 'Callable4[[Test], None]') -> 'None':
  test__87: 'Test' = Test()
  testFun__85(test__87)
  test__87.soft_fail_to_hard()
