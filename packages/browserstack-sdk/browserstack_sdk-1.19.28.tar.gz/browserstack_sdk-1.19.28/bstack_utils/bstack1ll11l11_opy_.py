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
class bstack1l11lll11l_opy_:
    def __init__(self, handler):
        self._1llll111l1l_opy_ = None
        self.handler = handler
        self._1llll11l111_opy_ = self.bstack1llll111lll_opy_()
        self.patch()
    def patch(self):
        self._1llll111l1l_opy_ = self._1llll11l111_opy_.execute
        self._1llll11l111_opy_.execute = self.bstack1llll111ll1_opy_()
    def bstack1llll111ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11ll11_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࠦᒢ"), driver_command, None, this, args)
            response = self._1llll111l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11ll11_opy_ (u"ࠧࡧࡦࡵࡧࡵࠦᒣ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1llll11l111_opy_.execute = self._1llll111l1l_opy_
    @staticmethod
    def bstack1llll111lll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver