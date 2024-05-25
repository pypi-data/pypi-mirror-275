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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack1l111l1111_opy_ import RobotHandler
from bstack_utils.capture import bstack1l111ll1l1_opy_
from bstack_utils.bstack11llllll11_opy_ import bstack1l111l1l1l_opy_, bstack1l11111ll1_opy_, bstack11lll111l1_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack1l1l111lll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lll1ll1_opy_, bstack11l11l11l_opy_, Result, \
    bstack1l1111l11l_opy_, bstack1l11l1111l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ൜"): [],
        bstack11ll11_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ൝"): [],
        bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ൞"): []
    }
    bstack11llll111l_opy_ = []
    bstack1l111lll11_opy_ = []
    @staticmethod
    def bstack11lll1l1ll_opy_(log):
        if not (log[bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨൟ")] and log[bstack11ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩൠ")].strip()):
            return
        active = bstack1l1l111lll_opy_.bstack11llll1ll1_opy_()
        log = {
            bstack11ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨൡ"): log[bstack11ll11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩൢ")],
            bstack11ll11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧൣ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠬࡠࠧ൤"),
            bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ൥"): log[bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ൦")],
        }
        if active:
            if active[bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭൧")] == bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ൨"):
                log[bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ൩")] = active[bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ൪")]
            elif active[bstack11ll11_opy_ (u"ࠬࡺࡹࡱࡧࠪ൫")] == bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࠫ൬"):
                log[bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ൭")] = active[bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ൮")]
        bstack1l1l111lll_opy_.bstack11111l1l_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._11llll1l11_opy_ = None
        self._11lllll1l1_opy_ = None
        self._1l11111l1l_opy_ = OrderedDict()
        self.bstack11lll1l111_opy_ = bstack1l111ll1l1_opy_(self.bstack11lll1l1ll_opy_)
    @bstack1l1111l11l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11lll11ll1_opy_()
        if not self._1l11111l1l_opy_.get(attrs.get(bstack11ll11_opy_ (u"ࠩ࡬ࡨࠬ൯")), None):
            self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠪ࡭ࡩ࠭൰"))] = {}
        bstack1l111ll111_opy_ = bstack11lll111l1_opy_(
                bstack11lllll11l_opy_=attrs.get(bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧ൱")),
                name=name,
                bstack1l1111111l_opy_=bstack11l11l11l_opy_(),
                file_path=os.path.relpath(attrs[bstack11ll11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ൲")], start=os.getcwd()) if attrs.get(bstack11ll11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭൳")) != bstack11ll11_opy_ (u"ࠧࠨ൴") else bstack11ll11_opy_ (u"ࠨࠩ൵"),
                framework=bstack11ll11_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨ൶")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11ll11_opy_ (u"ࠪ࡭ࡩ࠭൷"), None)
        self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧ൸"))][bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ൹")] = bstack1l111ll111_opy_
    @bstack1l1111l11l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l111l11l1_opy_()
        self._11lll11l11_opy_(messages)
        for bstack11lll1ll11_opy_ in self.bstack11llll111l_opy_:
            bstack11lll1ll11_opy_[bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨൺ")][bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ൻ")].extend(self.store[bstack11ll11_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧർ")])
            bstack1l1l111lll_opy_.bstack11llll11ll_opy_(bstack11lll1ll11_opy_)
        self.bstack11llll111l_opy_ = []
        self.store[bstack11ll11_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨൽ")] = []
    @bstack1l1111l11l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11lll1l111_opy_.start()
        if not self._1l11111l1l_opy_.get(attrs.get(bstack11ll11_opy_ (u"ࠪ࡭ࡩ࠭ൾ")), None):
            self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧൿ"))] = {}
        driver = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ඀"), None)
        bstack11llllll11_opy_ = bstack11lll111l1_opy_(
            bstack11lllll11l_opy_=attrs.get(bstack11ll11_opy_ (u"࠭ࡩࡥࠩඁ")),
            name=name,
            bstack1l1111111l_opy_=bstack11l11l11l_opy_(),
            file_path=os.path.relpath(attrs[bstack11ll11_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧං")], start=os.getcwd()),
            scope=RobotHandler.bstack11lllll1ll_opy_(attrs.get(bstack11ll11_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨඃ"), None)),
            framework=bstack11ll11_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨ඄"),
            tags=attrs[bstack11ll11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨඅ")],
            hooks=self.store[bstack11ll11_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪආ")],
            bstack11lll111ll_opy_=bstack1l1l111lll_opy_.bstack1l111l111l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11ll11_opy_ (u"ࠧࢁࡽࠡ࡞ࡱࠤࢀࢃࠢඇ").format(bstack11ll11_opy_ (u"ࠨࠠࠣඈ").join(attrs[bstack11ll11_opy_ (u"ࠧࡵࡣࡪࡷࠬඉ")]), name) if attrs[bstack11ll11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ඊ")] else name
        )
        self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠩ࡬ࡨࠬඋ"))][bstack11ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ඌ")] = bstack11llllll11_opy_
        threading.current_thread().current_test_uuid = bstack11llllll11_opy_.bstack11lll11l1l_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧඍ"), None)
        self.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ඎ"), bstack11llllll11_opy_)
    @bstack1l1111l11l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11lll1l111_opy_.reset()
        bstack1l1111l1l1_opy_ = bstack1l111l1ll1_opy_.get(attrs.get(bstack11ll11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ඏ")), bstack11ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨඐ"))
        self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠨ࡫ࡧࠫඑ"))][bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬඒ")].stop(time=bstack11l11l11l_opy_(), duration=int(attrs.get(bstack11ll11_opy_ (u"ࠪࡩࡱࡧࡰࡴࡧࡧࡸ࡮ࡳࡥࠨඓ"), bstack11ll11_opy_ (u"ࠫ࠵࠭ඔ"))), result=Result(result=bstack1l1111l1l1_opy_, exception=attrs.get(bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ඕ")), bstack1l111llll1_opy_=[attrs.get(bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧඖ"))]))
        self.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ඗"), self._1l11111l1l_opy_[attrs.get(bstack11ll11_opy_ (u"ࠨ࡫ࡧࠫ඘"))][bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ඙")], True)
        self.store[bstack11ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧක")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack1l1111l11l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11lll11ll1_opy_()
        current_test_id = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡩ࠭ඛ"), None)
        bstack11lll1llll_opy_ = current_test_id if bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡪࠧග"), None) else bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩඝ"), None)
        if attrs.get(bstack11ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬඞ"), bstack11ll11_opy_ (u"ࠨࠩඟ")).lower() in [bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨච"), bstack11ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬඡ")]:
            hook_type = bstack1l111l1lll_opy_(attrs.get(bstack11ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩජ")), bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩඣ"), None))
            hook_name = bstack11ll11_opy_ (u"࠭ࡻࡾࠩඤ").format(attrs.get(bstack11ll11_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧඥ"), bstack11ll11_opy_ (u"ࠨࠩඦ")))
            if hook_type in [bstack11ll11_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ට"), bstack11ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ඨ")]:
                hook_name = bstack11ll11_opy_ (u"ࠫࡠࢁࡽ࡞ࠢࡾࢁࠬඩ").format(bstack1l111ll11l_opy_.get(hook_type), attrs.get(bstack11ll11_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬඪ"), bstack11ll11_opy_ (u"࠭ࠧණ")))
            bstack11lll11lll_opy_ = bstack1l11111ll1_opy_(
                bstack11lllll11l_opy_=bstack11lll1llll_opy_ + bstack11ll11_opy_ (u"ࠧ࠮ࠩඬ") + attrs.get(bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ත"), bstack11ll11_opy_ (u"ࠩࠪථ")).lower(),
                name=hook_name,
                bstack1l1111111l_opy_=bstack11l11l11l_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪද")), start=os.getcwd()),
                framework=bstack11ll11_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪධ"),
                tags=attrs[bstack11ll11_opy_ (u"ࠬࡺࡡࡨࡵࠪන")],
                scope=RobotHandler.bstack11lllll1ll_opy_(attrs.get(bstack11ll11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭඲"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11lll11lll_opy_.bstack11lll11l1l_opy_()
            threading.current_thread().current_hook_id = bstack11lll1llll_opy_ + bstack11ll11_opy_ (u"ࠧ࠮ࠩඳ") + attrs.get(bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ප"), bstack11ll11_opy_ (u"ࠩࠪඵ")).lower()
            self.store[bstack11ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧබ")] = [bstack11lll11lll_opy_.bstack11lll11l1l_opy_()]
            if bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨභ"), None):
                self.store[bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩම")].append(bstack11lll11lll_opy_.bstack11lll11l1l_opy_())
            else:
                self.store[bstack11ll11_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬඹ")].append(bstack11lll11lll_opy_.bstack11lll11l1l_opy_())
            if bstack11lll1llll_opy_:
                self._1l11111l1l_opy_[bstack11lll1llll_opy_ + bstack11ll11_opy_ (u"ࠧ࠮ࠩය") + attrs.get(bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ර"), bstack11ll11_opy_ (u"ࠩࠪ඼")).lower()] = { bstack11ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ල"): bstack11lll11lll_opy_ }
            bstack1l1l111lll_opy_.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ඾"), bstack11lll11lll_opy_)
        else:
            bstack11lllllll1_opy_ = {
                bstack11ll11_opy_ (u"ࠬ࡯ࡤࠨ඿"): uuid4().__str__(),
                bstack11ll11_opy_ (u"࠭ࡴࡦࡺࡷࠫව"): bstack11ll11_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭ශ").format(attrs.get(bstack11ll11_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨෂ")), attrs.get(bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧස"), bstack11ll11_opy_ (u"ࠪࠫහ"))) if attrs.get(bstack11ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩළ"), []) else attrs.get(bstack11ll11_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬෆ")),
                bstack11ll11_opy_ (u"࠭ࡳࡵࡧࡳࡣࡦࡸࡧࡶ࡯ࡨࡲࡹ࠭෇"): attrs.get(bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬ෈"), []),
                bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ෉"): bstack11l11l11l_opy_(),
                bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵ්ࠩ"): bstack11ll11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ෋"),
                bstack11ll11_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ෌"): attrs.get(bstack11ll11_opy_ (u"ࠬࡪ࡯ࡤࠩ෍"), bstack11ll11_opy_ (u"࠭ࠧ෎"))
            }
            if attrs.get(bstack11ll11_opy_ (u"ࠧ࡭࡫ࡥࡲࡦࡳࡥࠨා"), bstack11ll11_opy_ (u"ࠨࠩැ")) != bstack11ll11_opy_ (u"ࠩࠪෑ"):
                bstack11lllllll1_opy_[bstack11ll11_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫි")] = attrs.get(bstack11ll11_opy_ (u"ࠫࡱ࡯ࡢ࡯ࡣࡰࡩࠬී"))
            if not self.bstack1l111lll11_opy_:
                self._1l11111l1l_opy_[self._1l111ll1ll_opy_()][bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨු")].add_step(bstack11lllllll1_opy_)
                threading.current_thread().current_step_uuid = bstack11lllllll1_opy_[bstack11ll11_opy_ (u"࠭ࡩࡥࠩ෕")]
            self.bstack1l111lll11_opy_.append(bstack11lllllll1_opy_)
    @bstack1l1111l11l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l111l11l1_opy_()
        self._11lll11l11_opy_(messages)
        current_test_id = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩූ"), None)
        bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫ෗"), None)
        bstack1l11111l11_opy_ = bstack1l111l1ll1_opy_.get(attrs.get(bstack11ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩෘ")), bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫෙ"))
        bstack1l1111l111_opy_ = attrs.get(bstack11ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬේ"))
        if bstack1l11111l11_opy_ != bstack11ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ෛ") and not attrs.get(bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧො")) and self._11llll1l11_opy_:
            bstack1l1111l111_opy_ = self._11llll1l11_opy_
        bstack1l1111ll11_opy_ = Result(result=bstack1l11111l11_opy_, exception=bstack1l1111l111_opy_, bstack1l111llll1_opy_=[bstack1l1111l111_opy_])
        if attrs.get(bstack11ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬෝ"), bstack11ll11_opy_ (u"ࠨࠩෞ")).lower() in [bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨෟ"), bstack11ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ෠")]:
            bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧ෡"), None)
            if bstack11lll1llll_opy_:
                bstack1l11l111l1_opy_ = bstack11lll1llll_opy_ + bstack11ll11_opy_ (u"ࠧ࠳ࠢ෢") + attrs.get(bstack11ll11_opy_ (u"࠭ࡴࡺࡲࡨࠫ෣"), bstack11ll11_opy_ (u"ࠧࠨ෤")).lower()
                self._1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ෥")].stop(time=bstack11l11l11l_opy_(), duration=int(attrs.get(bstack11ll11_opy_ (u"ࠩࡨࡰࡦࡶࡳࡦࡦࡷ࡭ࡲ࡫ࠧ෦"), bstack11ll11_opy_ (u"ࠪ࠴ࠬ෧"))), result=bstack1l1111ll11_opy_)
                bstack1l1l111lll_opy_.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭෨"), self._1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ෩")])
        else:
            bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤ࡯ࡤࠨ෪"), None)
            if bstack11lll1llll_opy_ and len(self.bstack1l111lll11_opy_) == 1:
                current_step_uuid = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡷࡩࡵࡥࡵࡶ࡫ࡧࠫ෫"), None)
                self._1l11111l1l_opy_[bstack11lll1llll_opy_][bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ෬")].bstack1l11111111_opy_(current_step_uuid, duration=int(attrs.get(bstack11ll11_opy_ (u"ࠩࡨࡰࡦࡶࡳࡦࡦࡷ࡭ࡲ࡫ࠧ෭"), bstack11ll11_opy_ (u"ࠪ࠴ࠬ෮"))), result=bstack1l1111ll11_opy_)
            else:
                self.bstack1l1111ll1l_opy_(attrs)
            self.bstack1l111lll11_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11ll11_opy_ (u"ࠫ࡭ࡺ࡭࡭ࠩ෯"), bstack11ll11_opy_ (u"ࠬࡴ࡯ࠨ෰")) == bstack11ll11_opy_ (u"࠭ࡹࡦࡵࠪ෱"):
                return
            self.messages.push(message)
            bstack11llllll1l_opy_ = []
            if bstack1l1l111lll_opy_.bstack11llll1ll1_opy_():
                bstack11llllll1l_opy_.append({
                    bstack11ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪෲ"): bstack11l11l11l_opy_(),
                    bstack11ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩෳ"): message.get(bstack11ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ෴")),
                    bstack11ll11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ෵"): message.get(bstack11ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ෶")),
                    **bstack1l1l111lll_opy_.bstack11llll1ll1_opy_()
                })
                if len(bstack11llllll1l_opy_) > 0:
                    bstack1l1l111lll_opy_.bstack11111l1l_opy_(bstack11llllll1l_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1l1l111lll_opy_.bstack11lll1l11l_opy_()
    def bstack1l1111ll1l_opy_(self, bstack11llll1lll_opy_):
        if not bstack1l1l111lll_opy_.bstack11llll1ll1_opy_():
            return
        kwname = bstack11ll11_opy_ (u"ࠬࢁࡽࠡࡽࢀࠫ෷").format(bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭෸")), bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬ෹"), bstack11ll11_opy_ (u"ࠨࠩ෺"))) if bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ෻"), []) else bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ෼"))
        error_message = bstack11ll11_opy_ (u"ࠦࡰࡽ࡮ࡢ࡯ࡨ࠾ࠥࡢࠢࡼ࠲ࢀࡠࠧࠦࡼࠡࡵࡷࡥࡹࡻࡳ࠻ࠢ࡟ࠦࢀ࠷ࡽ࡝ࠤࠣࢀࠥ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢ࡟ࠦࢀ࠸ࡽ࡝ࠤࠥ෽").format(kwname, bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ෾")), str(bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ෿"))))
        bstack1l11l11111_opy_ = bstack11ll11_opy_ (u"ࠢ࡬ࡹࡱࡥࡲ࡫࠺ࠡ࡞ࠥࡿ࠵ࢃ࡜ࠣࠢࡿࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࡢࠢࡼ࠳ࢀࡠࠧࠨ฀").format(kwname, bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨก")))
        bstack11llll1111_opy_ = error_message if bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪข")) else bstack1l11l11111_opy_
        bstack1l111l11ll_opy_ = {
            bstack11ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ฃ"): self.bstack1l111lll11_opy_[-1].get(bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨค"), bstack11l11l11l_opy_()),
            bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ฅ"): bstack11llll1111_opy_,
            bstack11ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬฆ"): bstack11ll11_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭ง") if bstack11llll1lll_opy_.get(bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨจ")) == bstack11ll11_opy_ (u"ࠩࡉࡅࡎࡒࠧฉ") else bstack11ll11_opy_ (u"ࠪࡍࡓࡌࡏࠨช"),
            **bstack1l1l111lll_opy_.bstack11llll1ll1_opy_()
        }
        bstack1l1l111lll_opy_.bstack11111l1l_opy_([bstack1l111l11ll_opy_])
    def _1l111ll1ll_opy_(self):
        for bstack11lllll11l_opy_ in reversed(self._1l11111l1l_opy_):
            bstack1l11111lll_opy_ = bstack11lllll11l_opy_
            data = self._1l11111l1l_opy_[bstack11lllll11l_opy_][bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧซ")]
            if isinstance(data, bstack1l11111ll1_opy_):
                if not bstack11ll11_opy_ (u"ࠬࡋࡁࡄࡊࠪฌ") in data.bstack1l1111lll1_opy_():
                    return bstack1l11111lll_opy_
            else:
                return bstack1l11111lll_opy_
    def _11lll11l11_opy_(self, messages):
        try:
            bstack11lll1ll1l_opy_ = BuiltIn().get_variable_value(bstack11ll11_opy_ (u"ࠨࠤࡼࡎࡒࡋࠥࡒࡅࡗࡇࡏࢁࠧญ")) in (bstack1l111l1l11_opy_.DEBUG, bstack1l111l1l11_opy_.TRACE)
            for message, bstack11lllll111_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨฎ"))
                level = message.get(bstack11ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧฏ"))
                if level == bstack1l111l1l11_opy_.FAIL:
                    self._11llll1l11_opy_ = name or self._11llll1l11_opy_
                    self._11lllll1l1_opy_ = bstack11lllll111_opy_.get(bstack11ll11_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥฐ")) if bstack11lll1ll1l_opy_ and bstack11lllll111_opy_ else self._11lllll1l1_opy_
        except:
            pass
    @classmethod
    def bstack1l1111llll_opy_(self, event: str, bstack11llll11l1_opy_: bstack1l111l1l1l_opy_, bstack11llllllll_opy_=False):
        if event == bstack11ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬฑ"):
            bstack11llll11l1_opy_.set(hooks=self.store[bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࠨฒ")])
        if event == bstack11ll11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ณ"):
            event = bstack11ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨด")
        if bstack11llllllll_opy_:
            bstack11lll1lll1_opy_ = {
                bstack11ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫต"): event,
                bstack11llll11l1_opy_.bstack1l111lll1l_opy_(): bstack11llll11l1_opy_.bstack1l1111l1ll_opy_(event)
            }
            self.bstack11llll111l_opy_.append(bstack11lll1lll1_opy_)
        else:
            bstack1l1l111lll_opy_.bstack1l1111llll_opy_(event, bstack11llll11l1_opy_)
class Messages:
    def __init__(self):
        self._1l111lllll_opy_ = []
    def bstack11lll11ll1_opy_(self):
        self._1l111lllll_opy_.append([])
    def bstack1l111l11l1_opy_(self):
        return self._1l111lllll_opy_.pop() if self._1l111lllll_opy_ else list()
    def push(self, message):
        self._1l111lllll_opy_[-1].append(message) if self._1l111lllll_opy_ else self._1l111lllll_opy_.append([message])
class bstack1l111l1l11_opy_:
    FAIL = bstack11ll11_opy_ (u"ࠨࡈࡄࡍࡑ࠭ถ")
    ERROR = bstack11ll11_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨท")
    WARNING = bstack11ll11_opy_ (u"࡛ࠪࡆࡘࡎࠨธ")
    bstack11lll1l1l1_opy_ = bstack11ll11_opy_ (u"ࠫࡎࡔࡆࡐࠩน")
    DEBUG = bstack11ll11_opy_ (u"ࠬࡊࡅࡃࡗࡊࠫบ")
    TRACE = bstack11ll11_opy_ (u"࠭ࡔࡓࡃࡆࡉࠬป")
    bstack11llll1l1l_opy_ = [FAIL, ERROR]
def bstack1l111111l1_opy_(bstack1l111111ll_opy_):
    if not bstack1l111111ll_opy_:
        return None
    if bstack1l111111ll_opy_.get(bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪผ"), None):
        return getattr(bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫฝ")], bstack11ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧพ"), None)
    return bstack1l111111ll_opy_.get(bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨฟ"), None)
def bstack1l111l1lll_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪภ"), bstack11ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧม")]:
        return
    if hook_type.lower() == bstack11ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬย"):
        if current_test_uuid is None:
            return bstack11ll11_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫร")
        else:
            return bstack11ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ฤ")
    elif hook_type.lower() == bstack11ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫล"):
        if current_test_uuid is None:
            return bstack11ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ฦ")
        else:
            return bstack11ll11_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨว")