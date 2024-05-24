import os
import logging
import time
import traceback
import json

# import threading
# from .logged_requests import LoggedRequests

from pprint import pformat
from pprint import pprint
from jsoncomparison import Compare
import requests

try:
    import settings
except ImportError:
    traceback.print_exc()


class BaseTestCase(object):
    """
BaseTestCase is the superclass for all the backend(Non UI) and frontend(UI) Testcases and Mobile Testcases
@author: Wang Lin
"""

    # TestEngineCaseInput from gitHub Action (test-engine目前只支持单线程)
    TestEngineCaseInput = {}

    # GlobalObjData 是全局数据对象（各个不同的thread发起的不同的testcase直接共享该数据）
    GlobalObjData = {}

    # 框架提供的全局数据列表: GlobalDataList
    GlobalDataList = []

    GlobalTotalCaseCount = 0
    GlobalExecutedCaseList = []

    priority = None

    def __init__(self):
        self.pprint = pprint
        self.pformat = pformat
        self.logger = logging

        # self.requests = LoggedRequests
        self.requests = requests

        self.testcase_id = None

        self.TestEngineCaseInput = BaseTestCase.TestEngineCaseInput

        # TestEngineTestEngineCaseOutput: case由test-engine触发执行结束后call-back时传入的参数（ test-engine目前只支持单线程）
        self.TestEngineCaseOutput = {}

        self.GlobalObjData = BaseTestCase.GlobalObjData

        # self.DataList = BaseTestCase.DataList
        self.GlobalTotalCaseCount = BaseTestCase.GlobalTotalCaseCount
        self.GlobalExecutedCaseList = BaseTestCase.GlobalExecutedCaseList

        # # todo: 此处用于 构建多线程时 每个线程独立的 TestEngineCaseInput(线程id作为key)
        # print("===================+++++++++++++==========threading.currentThread().ident")
        # print(threading.currentThread().ident)

        # self.CaseData 用于记录 case执行过程中产生的数据（多数情况用于 某个 testcase chain中, 某个Testcase中有调用了 另外一个Testcase.run_test() 则此case 被定义一个 TestcaseChain）
        # eg:
        # from linktest.api_testcase import APITestCase
        # from tests.api.testcase_demo.testcase1 import Testcase1
        # from tests.api.testcase_demo.testcase2 import Testcase2
        #
        # class Testcase3(APITestCase):
        #     tag = 'case3'
        #
        #     def run_test(self):
        #         # 如下调用方式 Testcase1 & Testcase2 的log 不会 被保存到 Testcase3 的log 中
        #         # Testcase1().run_test()
        #         # Testcase2().run_test()
        #         # print(self.CaseData)
        #
        #         # 如下调用方式 Testcase1 & Testcase2 的log  会  被保存到 Testcase3 的log 中
        #
        #         # 比如： TestAdd1.run_test(self)中会设置 username, self.CaseData['username'] = 'lin'
        #         Testcase1.run_test(self)
        #
        #         # TestAdd2.run_test(self)中会设置 password, self.CaseData['password'] = res['password'], 其中 res可能是某个方法或方法的返回值
        #         Testcase2.run_test(self)
        #
        #         # 此时可以在 TestAdd3 直接通过 self.CaseData 获取 对应的 username & password
        #         self.logger.info(self.CaseData)
        #         self.logger.info(self.CaseData['username'])
        #         self.logger.info(self.CaseData['password'])
        #
        #         # login(self.CaseData['username']), self.CaseData['password']))
        self.CaseData = {}

    # now timeout only support integer seconds, default value is 1200 seconds
    timeout = getattr(settings, "TESTCASE_TIMEOUT", 1200)

    def sleep(self, sleep_seconds):
        time.sleep(sleep_seconds)

    def run_test(self):
        """
        this method must be implement by all backend test cases,
        each test case must encapsulate its business logic into a specific method which called run_test():
        def run_test(self):
            ...
        """
        raise NotImplementedError(" - subclass: %s must implement this method: run_test(self)!" % self)

    def teardown(self):
        """
        def teardown(self):
            ...
        """
        pass

    def setup(self):
        """
        def teardown(self):
            ...
        """
        pass

    def assert_equals(self, actual_val, expect_val):
        try:
            assert actual_val == expect_val
            self.logger.info("Assertion Passed: actual_val(%s) == expect_val(%s)", actual_val, expect_val)

        except AssertionError as e:
            e.args += ('expected value is %s' % expect_val, 'actual_val is %s' % actual_val)
            self.logger.info("Assertion Failed: actual_val(%s) == expect_val(%s)", actual_val, expect_val)
            raise

    def assert_contains(self, source_val, target_val):
        try:
            if (
                    (type(source_val) == type(target_val)) and
                    (
                            type(source_val) == str or type(source_val) == int or type(source_val) == float
                    )
            ):
                source_val_str = str(source_val)
                target_val_str = str(target_val)
                if source_val_str.__contains__(target_val_str):
                    self.logger.info(
                        "assert_contains Passed => source_val: %s, target_val: %s" % (source_val, target_val))
                else:
                    self.logger.error(
                        "assert_contains Failed => source_val: %s, target_val: %s " % (source_val, target_val))
                    raise RuntimeError(
                        "assert_contains Failed => source_val: %s, target_val: %s " % (source_val, target_val))
            else:
                self.logger.error(
                    "assert_contains Failed => source_val: %s, target_val: %s, "
                    "the type of params should be on of [str, int, float] " % (source_val, target_val))
                raise RuntimeError(
                    "assert_contains Failed => source_val: %s, target_val: %s , "
                    "the type of params should be on of [str, int, float] " % (source_val, target_val))

        except AssertionError as e:
            e.args += ('assert_contains => source_val is %s' % source_val, 'target_val is %s' % target_val)
            self.logger.error(
                "assert_contains Failed => source_val: %s, target_val: %s " % (source_val, target_val))
            raise RuntimeError(
                "assert_contains Failed => source_val: %s, target_val: %s " % (source_val, target_val))

    def assert_is_not_none(self, actual_val):
        try:
            assert actual_val is not None
            self.logger.info("assert Passed %s is not None" % (actual_val))
        except AssertionError as e:
            e.args += ('expected value is not None', 'actual_val is %s' % actual_val)
            self.logger.info("assert_is_not_none Failed => assert_is_not_none(%s)" % (actual_val))
            raise

    def compare_json_and_return_diff(self, expected_json, actual_json, rules=None):
        """
        忽视JSON对象内部的键值对的顺序，即对象包含相同的键值对，即使顺序不同，也被视为相同的JSON对象。JSON对象的比较忽略键值对的顺序。
        例如，以下两个JSON对象包含相同的键值对，即使顺序不同，也被视为相同的JSON对象：
        json1 = {
            "name": "linktest",
            "Company": {
                "name": "IKEA",
                "No": 1
            },
            "version": "1.0"
        }
        json2 = {
            "version": "1.0",
            "name": "linktest",
            "Company": {
                "name": "IKEA",
                "No": 1
            }
        }
        """

        self.logger.info("========================= Compare JSON Objects =========================")
        self.logger.info("Expected JSON: "+ os.linesep + json.dumps(expected_json, ensure_ascii=False, indent=2))
        self.logger.info("Expected JSON: "+ os.linesep + json.dumps(actual_json, ensure_ascii=False, indent=2))

        if rules:
            self.logger.info("Compare Rules:")
            self.logger.info(rules)

        diff = Compare(rules=rules).check(expected_json, actual_json)
        self.logger.info("========================= JSON diff ========================= ")
        self.logger.info(self.pformat(diff))

        # 判断逻辑交给用户，这里直接返回diff
        return diff

    def compare_json_and_assert_equal(self, expected_json, actual_json, rules=None):
        diff = self.compare_json_and_return_diff(expected_json, actual_json, rules)
        self.pprint(diff)
        assert diff == {}

    def compare_json_with_strict_mode(self, expected_json, actual_json):
        """
        JSON对象内部的键值对顺序是有意义的，即使对象包含相同的键值对，但顺序不同，也应该被视为不同的对象。JSON对象的比较不应该忽略键值对的顺序。
        例如，以下两个JSON对象虽然包含相同的键值对，但由于顺序不同，应该被视为不同的对象：
        ```
        { "name": "linktest", "version": 1.0 }
        {"version": 1.0, "name": "linktest" }
        ```
        :param expected_json:
        :param actual_json:
        :return:
        """

        self.logger.info("========================= Compare JSON Objects With Strict Mode =========================")
        v1 = json.dumps(expected_json, sort_keys=False)
        v2 = json.dumps(actual_json, sort_keys=False)

        self.logger.info("Expected JSON: ")
        self.logger.info(self.pformat(v1))

        self.logger.info("Actual JSON: ")
        self.logger.info(self.pformat(v2))

        print("Expected JSON:: ")
        self.pprint(v1)
        print("Actual JSON: ")
        self.pprint(v2)

        assert v1 == v2
