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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11ll1l1ll1_opy_, bstack11lll11111_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1l1ll1_opy_ = bstack11ll1l1ll1_opy_
        self.bstack11lll11111_opy_ = bstack11lll11111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11lllll1ll_opy_(bstack11ll11lll1_opy_):
        bstack11ll11llll_opy_ = []
        if bstack11ll11lll1_opy_:
            tokens = str(os.path.basename(bstack11ll11lll1_opy_)).split(bstack11ll11_opy_ (u"ࠣࡡࠥ็"))
            camelcase_name = bstack11ll11_opy_ (u"ࠤ่ࠣࠦ").join(t.title() for t in tokens)
            suite_name, bstack11ll1l1111_opy_ = os.path.splitext(camelcase_name)
            bstack11ll11llll_opy_.append(suite_name)
        return bstack11ll11llll_opy_
    @staticmethod
    def bstack11ll1l111l_opy_(typename):
        if bstack11ll11_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ้") in typename:
            return bstack11ll11_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶ๊ࠧ")
        return bstack11ll11_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ๋")