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
from collections import deque
from bstack_utils.constants import *
class bstack1lll1l1l11_opy_:
    def __init__(self):
        self._1lllll1l1l1_opy_ = deque()
        self._1llllll111l_opy_ = {}
        self._1llllll1ll1_opy_ = False
    def bstack1llllll1111_opy_(self, test_name, bstack1lllll1l1ll_opy_):
        bstack1llllll1lll_opy_ = self._1llllll111l_opy_.get(test_name, {})
        return bstack1llllll1lll_opy_.get(bstack1lllll1l1ll_opy_, 0)
    def bstack1llllll11ll_opy_(self, test_name, bstack1lllll1l1ll_opy_):
        bstack1llllll11l1_opy_ = self.bstack1llllll1111_opy_(test_name, bstack1lllll1l1ll_opy_)
        self.bstack1lllll1llll_opy_(test_name, bstack1lllll1l1ll_opy_)
        return bstack1llllll11l1_opy_
    def bstack1lllll1llll_opy_(self, test_name, bstack1lllll1l1ll_opy_):
        if test_name not in self._1llllll111l_opy_:
            self._1llllll111l_opy_[test_name] = {}
        bstack1llllll1lll_opy_ = self._1llllll111l_opy_[test_name]
        bstack1llllll11l1_opy_ = bstack1llllll1lll_opy_.get(bstack1lllll1l1ll_opy_, 0)
        bstack1llllll1lll_opy_[bstack1lllll1l1ll_opy_] = bstack1llllll11l1_opy_ + 1
    def bstack1ll1lll11l_opy_(self, bstack1lllll1lll1_opy_, bstack1lllllll111_opy_):
        bstack1lllll1ll11_opy_ = self.bstack1llllll11ll_opy_(bstack1lllll1lll1_opy_, bstack1lllllll111_opy_)
        bstack1lllll1ll1l_opy_ = bstack11l1l111l1_opy_[bstack1lllllll111_opy_]
        bstack1llllll1l11_opy_ = bstack11ll11_opy_ (u"ࠨࡻࡾ࠯ࡾࢁ࠲ࢁࡽࠣᑉ").format(bstack1lllll1lll1_opy_, bstack1lllll1ll1l_opy_, bstack1lllll1ll11_opy_)
        self._1lllll1l1l1_opy_.append(bstack1llllll1l11_opy_)
    def bstack1llll11l1_opy_(self):
        return len(self._1lllll1l1l1_opy_) == 0
    def bstack1lll1ll1l1_opy_(self):
        bstack1llllll1l1l_opy_ = self._1lllll1l1l1_opy_.popleft()
        return bstack1llllll1l1l_opy_
    def capturing(self):
        return self._1llllll1ll1_opy_
    def bstack1ll1l11ll_opy_(self):
        self._1llllll1ll1_opy_ = True
    def bstack1ll1l1ll11_opy_(self):
        self._1llllll1ll1_opy_ = False