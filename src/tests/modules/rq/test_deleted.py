from unittest import TestCase

from exe import PROJECT
from modules.SATDReviewExplore import SATDReviewExplore
from modules.review.GerritController import GerritControllerViaLocal
from modules.rq.common import mark_satd
from tests.modules.rq.test_util import exe
from tests.modules.satd.stub import SatdDetectorStub
import pandas as pd


class TestAdded(TestCase):


    def test_detect_case_N001(self):
        target = 146
        df, error = exe(target, "openstack")
        print(df.at[0, "is_deleted_satd"])
        assert df.at[0, "is_deleted_satd"] == False

    def test_detect_case_Y001(self):
        target = 156
        df, error = exe(target, "openstack")
        print(df.at[0, "is_deleted_satd"])
        assert df.at[0, "is_deleted_satd"] == True

    def test_detect_case_Y002(self):
        target = 879
        df, error = exe(target, "openstack")
        print(df.at[0, "is_deleted_satd"])
        assert df.at[0, "is_deleted_satd"] == True

    def test_detect_case_Y003(self):# TODO: not tested yet
        target = 1917
        df, error = exe(target, "openstack")
        print(df.at[0, "is_deleted_satd"])
        assert df.at[0, "is_deleted_satd"] == True

    def test_detect_case_Y004(self):# TODO: not tested yet
        target = 2269
        df, error = exe(target, "openstack")
        print(df.at[0, "is_deleted_satd"])
        assert df.at[0, "is_deleted_satd"] == True
