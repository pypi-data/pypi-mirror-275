# coding: UTF-8
import sys
bstack1111ll1_opy_ = sys.version_info [0] == 2
bstack1llllll_opy_ = 2048
bstack111lll_opy_ = 7
def bstack11ll11_opy_ (bstack1l1111l_opy_):
    global bstack111_opy_
    bstack1111111_opy_ = ord (bstack1l1111l_opy_ [-1])
    bstack11l11_opy_ = bstack1l1111l_opy_ [:-1]
    bstack1ll1111_opy_ = bstack1111111_opy_ % len (bstack11l11_opy_)
    bstack1_opy_ = bstack11l11_opy_ [:bstack1ll1111_opy_] + bstack11l11_opy_ [bstack1ll1111_opy_:]
    if bstack1111ll1_opy_:
        bstack11l11ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1llllll_opy_ - (bstack1lll1l_opy_ + bstack1111111_opy_) % bstack111lll_opy_) for bstack1lll1l_opy_, char in enumerate (bstack1_opy_)])
    else:
        bstack11l11ll_opy_ = str () .join ([chr (ord (char) - bstack1llllll_opy_ - (bstack1lll1l_opy_ + bstack1111111_opy_) % bstack111lll_opy_) for bstack1lll1l_opy_, char in enumerate (bstack1_opy_)])
    return eval (bstack11l11ll_opy_)
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1ll1l11ll1_opy_ as bstack1l111111l_opy_
from browserstack_sdk.bstack11l1ll11l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lllll11ll_opy_
class bstack11lll1l1_opy_:
    def __init__(self, args, logger, bstack11ll1l1ll1_opy_, bstack11lll11111_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1l1ll1_opy_ = bstack11ll1l1ll1_opy_
        self.bstack11lll11111_opy_ = bstack11lll11111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l1l1111l_opy_ = []
        self.bstack11ll1ll111_opy_ = None
        self.bstack111l1111l_opy_ = []
        self.bstack11ll1ll11l_opy_ = self.bstack111lll11l_opy_()
        self.bstack1111l1111_opy_ = -1
    def bstack1l1l11ll_opy_(self, bstack11ll1ll1l1_opy_):
        self.parse_args()
        self.bstack11ll1lllll_opy_()
        self.bstack11ll1llll1_opy_(bstack11ll1ll1l1_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11ll1l11ll_opy_():
        import importlib
        if getattr(importlib, bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯ࡦࡢࡰࡴࡧࡤࡦࡴࠪศ"), False):
            bstack11ll1l11l1_opy_ = importlib.find_loader(bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨษ"))
        else:
            bstack11ll1l11l1_opy_ = importlib.util.find_spec(bstack11ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩส"))
    def bstack11ll1lll11_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111l1111_opy_ = -1
        if bstack11ll11_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨห") in self.bstack11ll1l1ll1_opy_:
            self.bstack1111l1111_opy_ = int(self.bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩฬ")])
        try:
            bstack11ll1l1lll_opy_ = [bstack11ll11_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬอ"), bstack11ll11_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧฮ"), bstack11ll11_opy_ (u"ࠬ࠳ࡰࠨฯ")]
            if self.bstack1111l1111_opy_ >= 0:
                bstack11ll1l1lll_opy_.extend([bstack11ll11_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧะ"), bstack11ll11_opy_ (u"ࠧ࠮ࡰࠪั")])
            for arg in bstack11ll1l1lll_opy_:
                self.bstack11ll1lll11_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11ll1lllll_opy_(self):
        bstack11ll1ll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11ll1ll111_opy_ = bstack11ll1ll111_opy_
        return bstack11ll1ll111_opy_
    def bstack1ll1111l11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11ll1l11ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1lllll11ll_opy_)
    def bstack11ll1llll1_opy_(self, bstack11ll1ll1l1_opy_):
        bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
        if bstack11ll1ll1l1_opy_:
            self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬา"))
            self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠩࡗࡶࡺ࡫ࠧำ"))
        if bstack1l1l1l1l1_opy_.bstack11ll1l1l11_opy_():
            self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩิ"))
            self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"࡙ࠫࡸࡵࡦࠩี"))
        self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠬ࠳ࡰࠨึ"))
        self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫื"))
        self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳุࠩ"))
        self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨู"))
        if self.bstack1111l1111_opy_ > 1:
            self.bstack11ll1ll111_opy_.append(bstack11ll11_opy_ (u"ࠩ࠰ࡲฺࠬ"))
            self.bstack11ll1ll111_opy_.append(str(self.bstack1111l1111_opy_))
    def bstack11ll1ll1ll_opy_(self):
        bstack111l1111l_opy_ = []
        for spec in self.bstack1l1l1111l_opy_:
            bstack1l1111l11_opy_ = [spec]
            bstack1l1111l11_opy_ += self.bstack11ll1ll111_opy_
            bstack111l1111l_opy_.append(bstack1l1111l11_opy_)
        self.bstack111l1111l_opy_ = bstack111l1111l_opy_
        return bstack111l1111l_opy_
    def bstack111lll11l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11ll1ll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack11ll1ll11l_opy_ = False
        return self.bstack11ll1ll11l_opy_
    def bstack1lll11l11_opy_(self, bstack11ll1l1l1l_opy_, bstack1l1l11ll_opy_):
        bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ฻")] = self.bstack11ll1l1ll1_opy_
        multiprocessing.set_start_method(bstack11ll11_opy_ (u"ࠫࡸࡶࡡࡸࡰࠪ฼"))
        if bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ฽") in self.bstack11ll1l1ll1_opy_:
            bstack11l11l11_opy_ = []
            manager = multiprocessing.Manager()
            bstack1l1l1l1ll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ฾")]):
                bstack11l11l11_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack11ll1l1l1l_opy_,
                                                           args=(self.bstack11ll1ll111_opy_, bstack1l1l11ll_opy_, bstack1l1l1l1ll_opy_)))
            i = 0
            bstack11ll1lll1l_opy_ = len(self.bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ฿")])
            for t in bstack11l11l11_opy_:
                os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨเ")] = str(i)
                os.environ[bstack11ll11_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪแ")] = json.dumps(self.bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭โ")][i % bstack11ll1lll1l_opy_])
                i += 1
                t.start()
            for t in bstack11l11l11_opy_:
                t.join()
            return list(bstack1l1l1l1ll_opy_)
    @staticmethod
    def bstack1l1l1llll_opy_(driver, bstack1llllllll1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨใ"), None)
        if item and getattr(item, bstack11ll11_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧไ"), None) and not getattr(item, bstack11ll11_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨๅ"), False):
            logger.info(
                bstack11ll11_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨๆ"))
            bstack11lll1111l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l111111l_opy_.bstack1l1l111l11_opy_(driver, bstack11lll1111l_opy_, item.name, item.module.__name__, item.path, bstack1llllllll1_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)