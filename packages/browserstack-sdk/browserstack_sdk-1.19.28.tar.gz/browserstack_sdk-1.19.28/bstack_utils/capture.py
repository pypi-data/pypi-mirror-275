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
import sys
class bstack1l111ll1l1_opy_:
    def __init__(self, handler):
        self._11l1l1l1l1_opy_ = sys.stdout.write
        self._11l1l1l111_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l1l1l11l_opy_
        sys.stdout.error = self.bstack11l1l1l1ll_opy_
    def bstack11l1l1l11l_opy_(self, _str):
        self._11l1l1l1l1_opy_(_str)
        if self.handler:
            self.handler({bstack11ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪༀ"): bstack11ll11_opy_ (u"ࠬࡏࡎࡇࡑࠪ༁"), bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ༂"): _str})
    def bstack11l1l1l1ll_opy_(self, _str):
        self._11l1l1l111_opy_(_str)
        if self.handler:
            self.handler({bstack11ll11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭༃"): bstack11ll11_opy_ (u"ࠨࡇࡕࡖࡔࡘࠧ༄"), bstack11ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ༅"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l1l1l1l1_opy_
        sys.stderr.write = self._11l1l1l111_opy_