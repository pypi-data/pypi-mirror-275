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
from browserstack_sdk.bstack1lll111l11_opy_ import bstack11lll1l1_opy_
from browserstack_sdk.bstack1l111l1111_opy_ import RobotHandler
def bstack11l111l1_opy_(framework):
    if framework.lower() == bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᆛ"):
        return bstack11lll1l1_opy_.version()
    elif framework.lower() == bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ᆜ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨᆝ"):
        import behave
        return behave.__version__
    else:
        return bstack11ll11_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪᆞ")