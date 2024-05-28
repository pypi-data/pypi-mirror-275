import unittest
import data.token as auth


class TestAuthFunctions(unittest.TestCase):
    def test_get_token(self):
        token = auth.get_token("823426883@qq.com", "123456")
        print(token)
