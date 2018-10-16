from script006 import mocking
from script006.mocking import class_c
from unittest import mock

_returned = 555555

# def test_classA():
#     b = mocking.B()
#     a = mocking.A(b)
#     assert a.get_param1_value() == id(a)

# def test_classA_with_mock():
#     b = mock.Mock(mocking.B)
#     b.get_value.return_value = _returned
#     a = mocking.A(b)
#     assert not a.get_param1_value() == _returned
#     assert b.get_value.call_count == 2
#
#

# def test_classA_with_context():
#     with mock.patch("script006.mocking.class_c.B") as MockedB:
#         b = mock.Mock()
#         MockedB.return_value = b
#         b.get_value.return_value = _returned
#         c = class_c.C()
#         assert c.get_value() == _returned
#         b.get_value.assert_called_once()
#         b.get_value.assert_called_with(c)



# @mock.patch("script006.mocking.class_c.B")
# def test_classA_with_mock_patch(MockedB):
#     b = mock.Mock()
#     MockedB.return_value = b
#     b.get_value.return_value = _returned
#     c = class_c.C()
#     assert c.get_value() == _returned
#     assert b.get_value.call_count == 1
#     b.get_value.assert_called_with(class_c.C())
#
#
