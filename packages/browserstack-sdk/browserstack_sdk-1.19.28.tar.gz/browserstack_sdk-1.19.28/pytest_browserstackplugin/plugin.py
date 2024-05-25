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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11l11l1l_opy_, bstack1ll1l11111_opy_, update, bstack1ll1ll1l_opy_,
                                       bstack11llll11_opy_, bstack1lll1l11l_opy_, bstack1ll11l11l_opy_, bstack1llllllll_opy_,
                                       bstack1ll1lll11_opy_, bstack1lll11l1l_opy_, bstack11l1llll_opy_, bstack1l1l1llll1_opy_,
                                       bstack1l1lll11l1_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1l11llll_opy_)
from browserstack_sdk.bstack1lll111l11_opy_ import bstack11lll1l1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l1l1l1l11_opy_
from bstack_utils.capture import bstack1l111ll1l1_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack11ll1lll_opy_, bstack1ll11l11l1_opy_, bstack1ll1lllll1_opy_, \
    bstack1l1l11lll1_opy_
from bstack_utils.helper import bstack1l1lll1ll1_opy_, bstack111ll11l11_opy_, bstack1l11l1111l_opy_, bstack11111llll_opy_, bstack111lll1l11_opy_, bstack11l11l11l_opy_, \
    bstack11l1111lll_opy_, \
    bstack111ll11ll1_opy_, bstack111ll1l11_opy_, bstack1llllll11_opy_, bstack11l111ll1l_opy_, bstack1l1ll11l1_opy_, Notset, \
    bstack111111ll1_opy_, bstack111lllll11_opy_, bstack11l111l1l1_opy_, Result, bstack111ll1l111_opy_, bstack111llllll1_opy_, bstack1l1111l11l_opy_, \
    bstack11llll1ll_opy_, bstack1ll1llll1l_opy_, bstack111l1l1l_opy_, bstack11l11ll111_opy_
from bstack_utils.bstack111l111ll1_opy_ import bstack111l111l1l_opy_
from bstack_utils.messages import bstack1l1ll11l_opy_, bstack1lll1ll11_opy_, bstack1111l1l11_opy_, bstack1l1l1ll1ll_opy_, bstack1lllll11ll_opy_, \
    bstack1111l1l1_opy_, bstack1l1ll1lll1_opy_, bstack1111lllll_opy_, bstack11l111l1l_opy_, bstack111ll11ll_opy_, \
    bstack11111l1ll_opy_, bstack1l1l111l1_opy_
from bstack_utils.proxy import bstack1l11l1ll1l_opy_, bstack1l111lll1_opy_
from bstack_utils.bstack1l1lll111l_opy_ import bstack1llll1lll1l_opy_, bstack1llll1l1l1l_opy_, bstack1llll1llll1_opy_, bstack1llll1l1lll_opy_, \
    bstack1llll1lll11_opy_, bstack1llll1l1ll1_opy_, bstack1llll1ll111_opy_, bstack11lll111l_opy_, bstack1llll1ll11l_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l11lll11l_opy_
from bstack_utils.bstack1ll1l1lll_opy_ import bstack11llll1l1_opy_, bstack1l1111ll_opy_, bstack11lllll1l_opy_, \
    bstack11l11ll11_opy_, bstack111111l1_opy_
from bstack_utils.bstack11llllll11_opy_ import bstack11lll111l1_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack1l1l111lll_opy_
import bstack_utils.bstack1ll1l11ll1_opy_ as bstack1l111111l_opy_
from bstack_utils.bstack1ll1lll1ll_opy_ import bstack1ll1lll1ll_opy_
bstack1lll1ll11l_opy_ = None
bstack1l1l11lll_opy_ = None
bstack11l11l1l1_opy_ = None
bstack1llll111l1_opy_ = None
bstack11lll1l11_opy_ = None
bstack1l1ll11l1l_opy_ = None
bstack1lll111l1l_opy_ = None
bstack11ll1ll11_opy_ = None
bstack1lllll1lll_opy_ = None
bstack1llllll111_opy_ = None
bstack1l1llllll_opy_ = None
bstack111l1ll1l_opy_ = None
bstack11l11l1ll_opy_ = None
bstack1l11llll1_opy_ = bstack11ll11_opy_ (u"ࠪࠫᗿ")
CONFIG = {}
bstack11llll1l_opy_ = False
bstack1l11l1l1l1_opy_ = bstack11ll11_opy_ (u"ࠫࠬᘀ")
bstack111111ll_opy_ = bstack11ll11_opy_ (u"ࠬ࠭ᘁ")
bstack1l11lll1_opy_ = False
bstack1l111l11l_opy_ = []
bstack1l1l11l11l_opy_ = bstack11ll1lll_opy_
bstack1ll1llll1l1_opy_ = bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᘂ")
bstack1lll111ll1l_opy_ = False
bstack1ll1llll1_opy_ = {}
bstack1ll1llllll_opy_ = False
logger = bstack1l1l1l1l11_opy_.get_logger(__name__, bstack1l1l11l11l_opy_)
store = {
    bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᘃ"): []
}
bstack1lll11l1ll1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11111l1l_opy_ = {}
current_test_uuid = None
def bstack1l1l11l111_opy_(page, bstack1ll111l1_opy_):
    try:
        page.evaluate(bstack11ll11_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᘄ"),
                      bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᘅ") + json.dumps(
                          bstack1ll111l1_opy_) + bstack11ll11_opy_ (u"ࠥࢁࢂࠨᘆ"))
    except Exception as e:
        print(bstack11ll11_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᘇ"), e)
def bstack1lll11lll1_opy_(page, message, level):
    try:
        page.evaluate(bstack11ll11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᘈ"), bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫᘉ") + json.dumps(
            message) + bstack11ll11_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪᘊ") + json.dumps(level) + bstack11ll11_opy_ (u"ࠨࡿࢀࠫᘋ"))
    except Exception as e:
        print(bstack11ll11_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧᘌ"), e)
def pytest_configure(config):
    bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
    config.args = bstack1l1l111lll_opy_.bstack1lll11ll11l_opy_(config.args)
    bstack1l1l1l1l1_opy_.bstack1l11l1l11l_opy_(bstack111l1l1l_opy_(config.getoption(bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᘍ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1lll11l1l1l_opy_ = item.config.getoption(bstack11ll11_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᘎ"))
    plugins = item.config.getoption(bstack11ll11_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨᘏ"))
    report = outcome.get_result()
    bstack1lll11l111l_opy_(item, call, report)
    if bstack11ll11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠦᘐ") not in plugins or bstack1l1ll11l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack11ll11_opy_ (u"ࠢࡠࡦࡵ࡭ࡻ࡫ࡲࠣᘑ"), None)
    page = getattr(item, bstack11ll11_opy_ (u"ࠣࡡࡳࡥ࡬࡫ࠢᘒ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1ll1lllllll_opy_(item, report, summary, bstack1lll11l1l1l_opy_)
    if (page is not None):
        bstack1ll1lllll1l_opy_(item, report, summary, bstack1lll11l1l1l_opy_)
def bstack1ll1lllllll_opy_(item, report, summary, bstack1lll11l1l1l_opy_):
    if report.when == bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᘓ") and report.skipped:
        bstack1llll1ll11l_opy_(report)
    if report.when in [bstack11ll11_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘔ"), bstack11ll11_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘕ")]:
        return
    if not bstack111lll1l11_opy_():
        return
    try:
        if (str(bstack1lll11l1l1l_opy_).lower() != bstack11ll11_opy_ (u"ࠬࡺࡲࡶࡧࠪᘖ")):
            item._driver.execute_script(
                bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫᘗ") + json.dumps(
                    report.nodeid) + bstack11ll11_opy_ (u"ࠧࡾࡿࠪᘘ"))
        os.environ[bstack11ll11_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᘙ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11ll11_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨ࠾ࠥࢁ࠰ࡾࠤᘚ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll11_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᘛ")))
    bstack1l1ll1l11_opy_ = bstack11ll11_opy_ (u"ࠦࠧᘜ")
    bstack1llll1ll11l_opy_(report)
    if not passed:
        try:
            bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11ll11_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᘝ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1l11_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11ll11_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᘞ")))
        bstack1l1ll1l11_opy_ = bstack11ll11_opy_ (u"ࠢࠣᘟ")
        if not passed:
            try:
                bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll11_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᘠ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1l11_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭ᘡ")
                    + json.dumps(bstack11ll11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠤࠦᘢ"))
                    + bstack11ll11_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᘣ")
                )
            else:
                item._driver.execute_script(
                    bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪᘤ")
                    + json.dumps(str(bstack1l1ll1l11_opy_))
                    + bstack11ll11_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤᘥ")
                )
        except Exception as e:
            summary.append(bstack11ll11_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡧ࡮࡯ࡱࡷࡥࡹ࡫࠺ࠡࡽ࠳ࢁࠧᘦ").format(e))
def bstack1lll1111ll1_opy_(test_name, error_message):
    try:
        bstack1lll11l11ll_opy_ = []
        bstack1llll111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᘧ"), bstack11ll11_opy_ (u"ࠩ࠳ࠫᘨ"))
        bstack1lll111111_opy_ = {bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᘩ"): test_name, bstack11ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᘪ"): error_message, bstack11ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᘫ"): bstack1llll111ll_opy_}
        bstack1ll1lll1ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᘬ"))
        if os.path.exists(bstack1ll1lll1ll1_opy_):
            with open(bstack1ll1lll1ll1_opy_) as f:
                bstack1lll11l11ll_opy_ = json.load(f)
        bstack1lll11l11ll_opy_.append(bstack1lll111111_opy_)
        with open(bstack1ll1lll1ll1_opy_, bstack11ll11_opy_ (u"ࠧࡸࠩᘭ")) as f:
            json.dump(bstack1lll11l11ll_opy_, f)
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡪࡸࡳࡪࡵࡷ࡭ࡳ࡭ࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡵࡿࡴࡦࡵࡷࠤࡪࡸࡲࡰࡴࡶ࠾ࠥ࠭ᘮ") + str(e))
def bstack1ll1lllll1l_opy_(item, report, summary, bstack1lll11l1l1l_opy_):
    if report.when in [bstack11ll11_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᘯ"), bstack11ll11_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᘰ")]:
        return
    if (str(bstack1lll11l1l1l_opy_).lower() != bstack11ll11_opy_ (u"ࠫࡹࡸࡵࡦࠩᘱ")):
        bstack1l1l11l111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll11_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᘲ")))
    bstack1l1ll1l11_opy_ = bstack11ll11_opy_ (u"ࠨࠢᘳ")
    bstack1llll1ll11l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll11_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢᘴ").format(e)
                )
        try:
            if passed:
                bstack111111l1_opy_(getattr(item, bstack11ll11_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᘵ"), None), bstack11ll11_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤᘶ"))
            else:
                error_message = bstack11ll11_opy_ (u"ࠪࠫᘷ")
                if bstack1l1ll1l11_opy_:
                    bstack1lll11lll1_opy_(item._page, str(bstack1l1ll1l11_opy_), bstack11ll11_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥᘸ"))
                    bstack111111l1_opy_(getattr(item, bstack11ll11_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᘹ"), None), bstack11ll11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᘺ"), str(bstack1l1ll1l11_opy_))
                    error_message = str(bstack1l1ll1l11_opy_)
                else:
                    bstack111111l1_opy_(getattr(item, bstack11ll11_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭ᘻ"), None), bstack11ll11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᘼ"))
                bstack1lll1111ll1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11ll11_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾ࠴ࢂࠨᘽ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11ll11_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᘾ"), default=bstack11ll11_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥᘿ"), help=bstack11ll11_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦᙀ"))
    parser.addoption(bstack11ll11_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᙁ"), default=bstack11ll11_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨᙂ"), help=bstack11ll11_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢᙃ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11ll11_opy_ (u"ࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦᙄ"), action=bstack11ll11_opy_ (u"ࠥࡷࡹࡵࡲࡦࠤᙅ"), default=bstack11ll11_opy_ (u"ࠦࡨ࡮ࡲࡰ࡯ࡨࠦᙆ"),
                         help=bstack11ll11_opy_ (u"ࠧࡊࡲࡪࡸࡨࡶࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶࠦᙇ"))
def bstack11lll1l1ll_opy_(log):
    if not (log[bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᙈ")] and log[bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᙉ")].strip()):
        return
    active = bstack11llll1ll1_opy_()
    log = {
        bstack11ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᙊ"): log[bstack11ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᙋ")],
        bstack11ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᙌ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠫ࡟࠭ᙍ"),
        bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᙎ"): log[bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᙏ")],
    }
    if active:
        if active[bstack11ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬᙐ")] == bstack11ll11_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᙑ"):
            log[bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᙒ")] = active[bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᙓ")]
        elif active[bstack11ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩᙔ")] == bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࠪᙕ"):
            log[bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᙖ")] = active[bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᙗ")]
    bstack1l1l111lll_opy_.bstack11111l1l_opy_([log])
def bstack11llll1ll1_opy_():
    if len(store[bstack11ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᙘ")]) > 0 and store[bstack11ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᙙ")][-1]:
        return {
            bstack11ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨᙚ"): bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᙛ"),
            bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᙜ"): store[bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᙝ")][-1]
        }
    if store.get(bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᙞ"), None):
        return {
            bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᙟ"): bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺࠧᙠ"),
            bstack11ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᙡ"): store[bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᙢ")]
        }
    return None
bstack11lll1l111_opy_ = bstack1l111ll1l1_opy_(bstack11lll1l1ll_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1lll111ll1l_opy_
        item._1ll1llll11l_opy_ = True
        bstack1ll111l1l_opy_ = bstack1l111111l_opy_.bstack1lllll1l1_opy_(CONFIG, bstack111ll11ll1_opy_(item.own_markers))
        item._a11y_test_case = bstack1ll111l1l_opy_
        if bstack1lll111ll1l_opy_:
            driver = getattr(item, bstack11ll11_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᙣ"), None)
            item._a11y_started = bstack1l111111l_opy_.bstack1l11ll111_opy_(driver, bstack1ll111l1l_opy_)
        if not bstack1l1l111lll_opy_.on() or bstack1ll1llll1l1_opy_ != bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᙤ"):
            return
        global current_test_uuid, bstack11lll1l111_opy_
        bstack11lll1l111_opy_.start()
        bstack1l111111ll_opy_ = {
            bstack11ll11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᙥ"): uuid4().__str__(),
            bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᙦ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠩ࡝ࠫᙧ")
        }
        current_test_uuid = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙨ")]
        store[bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᙩ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪᙪ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11111l1l_opy_[item.nodeid] = {**_1l11111l1l_opy_[item.nodeid], **bstack1l111111ll_opy_}
        bstack1lll1111l1l_opy_(item, _1l11111l1l_opy_[item.nodeid], bstack11ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᙫ"))
    except Exception as err:
        print(bstack11ll11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩᙬ"), str(err))
def pytest_runtest_setup(item):
    global bstack1lll11l1ll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11l111ll1l_opy_():
        atexit.register(bstack1ll11111ll_opy_)
        if not bstack1lll11l1ll1_opy_:
            try:
                bstack1lll11111l1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l11ll111_opy_():
                    bstack1lll11111l1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll11111l1_opy_:
                    signal.signal(s, bstack1ll1llllll1_opy_)
                bstack1lll11l1ll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11ll11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪ࡭ࡩࡴࡶࡨࡶࠥࡹࡩࡨࡰࡤࡰࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡹ࠺ࠡࠤ᙭") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llll1lll1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᙮")
    try:
        if not bstack1l1l111lll_opy_.on():
            return
        bstack11lll1l111_opy_.start()
        uuid = uuid4().__str__()
        bstack1l111111ll_opy_ = {
            bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙯ"): uuid,
            bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᙰ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠬࡠࠧᙱ"),
            bstack11ll11_opy_ (u"࠭ࡴࡺࡲࡨࠫᙲ"): bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᙳ"),
            bstack11ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᙴ"): bstack11ll11_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᙵ"),
            bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᙶ"): bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᙷ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᙸ")] = item
        store[bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᙹ")] = [uuid]
        if not _1l11111l1l_opy_.get(item.nodeid, None):
            _1l11111l1l_opy_[item.nodeid] = {bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᙺ"): [], bstack11ll11_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᙻ"): []}
        _1l11111l1l_opy_[item.nodeid][bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᙼ")].append(bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙽ")])
        _1l11111l1l_opy_[item.nodeid + bstack11ll11_opy_ (u"ࠫ࠲ࡹࡥࡵࡷࡳࠫᙾ")] = bstack1l111111ll_opy_
        bstack1lll111l1ll_opy_(item, bstack1l111111ll_opy_, bstack11ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᙿ"))
    except Exception as err:
        print(bstack11ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩ "), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1ll1llll1_opy_
        if CONFIG.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᚁ"), False):
            if CONFIG.get(bstack11ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᚂ"), bstack11ll11_opy_ (u"ࠤࡤࡹࡹࡵࠢᚃ")) == bstack11ll11_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᚄ"):
                bstack1lll11l1l11_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᚅ"), None)
                bstack1ll11lll11_opy_ = bstack1lll11l1l11_opy_ + bstack11ll11_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᚆ")
                driver = getattr(item, bstack11ll11_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᚇ"), None)
                PercySDK.screenshot(driver, bstack1ll11lll11_opy_)
        if getattr(item, bstack11ll11_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧᚈ"), False):
            bstack11lll1l1_opy_.bstack1l1l1llll_opy_(getattr(item, bstack11ll11_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᚉ"), None), bstack1ll1llll1_opy_, logger, item)
        if not bstack1l1l111lll_opy_.on():
            return
        bstack1l111111ll_opy_ = {
            bstack11ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᚊ"): uuid4().__str__(),
            bstack11ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᚋ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠫ࡟࠭ᚌ"),
            bstack11ll11_opy_ (u"ࠬࡺࡹࡱࡧࠪᚍ"): bstack11ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᚎ"),
            bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᚏ"): bstack11ll11_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᚐ"),
            bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᚑ"): bstack11ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᚒ")
        }
        _1l11111l1l_opy_[item.nodeid + bstack11ll11_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧᚓ")] = bstack1l111111ll_opy_
        bstack1lll111l1ll_opy_(item, bstack1l111111ll_opy_, bstack11ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᚔ"))
    except Exception as err:
        print(bstack11ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬᚕ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l1l111lll_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1llll1l1lll_opy_(fixturedef.argname):
        store[bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᚖ")] = request.node
    elif bstack1llll1lll11_opy_(fixturedef.argname):
        store[bstack11ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭ᚗ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack11ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᚘ"): fixturedef.argname,
            bstack11ll11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᚙ"): bstack11l1111lll_opy_(outcome),
            bstack11ll11_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᚚ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ᚛")]
        if not _1l11111l1l_opy_.get(current_test_item.nodeid, None):
            _1l11111l1l_opy_[current_test_item.nodeid] = {bstack11ll11_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ᚜"): []}
        _1l11111l1l_opy_[current_test_item.nodeid][bstack11ll11_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ᚝")].append(fixture)
    except Exception as err:
        logger.debug(bstack11ll11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫ᚞"), str(err))
if bstack1l1ll11l1_opy_() and bstack1l1l111lll_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _1l11111l1l_opy_[request.node.nodeid][bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ᚟")].bstack1lll1llll1l_opy_(id(step))
        except Exception as err:
            print(bstack11ll11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨᚠ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _1l11111l1l_opy_[request.node.nodeid][bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᚡ")].bstack1l11111111_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11ll11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᚢ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11llllll11_opy_: bstack11lll111l1_opy_ = _1l11111l1l_opy_[request.node.nodeid][bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᚣ")]
            bstack11llllll11_opy_.bstack1l11111111_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11ll11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᚤ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1ll1llll1l1_opy_
        try:
            if not bstack1l1l111lll_opy_.on() or bstack1ll1llll1l1_opy_ != bstack11ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᚥ"):
                return
            global bstack11lll1l111_opy_
            bstack11lll1l111_opy_.start()
            driver = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨᚦ"), None)
            if not _1l11111l1l_opy_.get(request.node.nodeid, None):
                _1l11111l1l_opy_[request.node.nodeid] = {}
            bstack11llllll11_opy_ = bstack11lll111l1_opy_.bstack1lll1llllll_opy_(
                scenario, feature, request.node,
                name=bstack1llll1l1ll1_opy_(request.node, scenario),
                bstack1l1111111l_opy_=bstack11l11l11l_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11ll11_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᚧ"),
                tags=bstack1llll1ll111_opy_(feature, scenario),
                bstack11lll111ll_opy_=bstack1l1l111lll_opy_.bstack1l111l111l_opy_(driver) if driver and driver.session_id else {}
            )
            _1l11111l1l_opy_[request.node.nodeid][bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᚨ")] = bstack11llllll11_opy_
            bstack1lll11111ll_opy_(bstack11llllll11_opy_.uuid)
            bstack1l1l111lll_opy_.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᚩ"), bstack11llllll11_opy_)
        except Exception as err:
            print(bstack11ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨᚪ"), str(err))
def bstack1lll1111111_opy_(bstack1lll11ll111_opy_):
    if bstack1lll11ll111_opy_ in store[bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᚫ")]:
        store[bstack11ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᚬ")].remove(bstack1lll11ll111_opy_)
def bstack1lll11111ll_opy_(bstack1lll111l11l_opy_):
    store[bstack11ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᚭ")] = bstack1lll111l11l_opy_
    threading.current_thread().current_test_uuid = bstack1lll111l11l_opy_
@bstack1l1l111lll_opy_.bstack1lll1l111l1_opy_
def bstack1lll11l111l_opy_(item, call, report):
    global bstack1ll1llll1l1_opy_
    bstack1ll1111lll_opy_ = bstack11l11l11l_opy_()
    if hasattr(report, bstack11ll11_opy_ (u"ࠪࡷࡹࡵࡰࠨᚮ")):
        bstack1ll1111lll_opy_ = bstack111ll1l111_opy_(report.stop)
    elif hasattr(report, bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪᚯ")):
        bstack1ll1111lll_opy_ = bstack111ll1l111_opy_(report.start)
    try:
        if getattr(report, bstack11ll11_opy_ (u"ࠬࡽࡨࡦࡰࠪᚰ"), bstack11ll11_opy_ (u"࠭ࠧᚱ")) == bstack11ll11_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᚲ"):
            bstack11lll1l111_opy_.reset()
        if getattr(report, bstack11ll11_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᚳ"), bstack11ll11_opy_ (u"ࠩࠪᚴ")) == bstack11ll11_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᚵ"):
            if bstack1ll1llll1l1_opy_ == bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᚶ"):
                _1l11111l1l_opy_[item.nodeid][bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᚷ")] = bstack1ll1111lll_opy_
                bstack1lll1111l1l_opy_(item, _1l11111l1l_opy_[item.nodeid], bstack11ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᚸ"), report, call)
                store[bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᚹ")] = None
            elif bstack1ll1llll1l1_opy_ == bstack11ll11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᚺ"):
                bstack11llllll11_opy_ = _1l11111l1l_opy_[item.nodeid][bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᚻ")]
                bstack11llllll11_opy_.set(hooks=_1l11111l1l_opy_[item.nodeid].get(bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᚼ"), []))
                exception, bstack1l111llll1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l111llll1_opy_ = [call.excinfo.exconly(), getattr(report, bstack11ll11_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪᚽ"), bstack11ll11_opy_ (u"ࠬ࠭ᚾ"))]
                bstack11llllll11_opy_.stop(time=bstack1ll1111lll_opy_, result=Result(result=getattr(report, bstack11ll11_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᚿ"), bstack11ll11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᛀ")), exception=exception, bstack1l111llll1_opy_=bstack1l111llll1_opy_))
                bstack1l1l111lll_opy_.bstack1l1111llll_opy_(bstack11ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᛁ"), _1l11111l1l_opy_[item.nodeid][bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᛂ")])
        elif getattr(report, bstack11ll11_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᛃ"), bstack11ll11_opy_ (u"ࠫࠬᛄ")) in [bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᛅ"), bstack11ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᛆ")]:
            bstack1l11l111l1_opy_ = item.nodeid + bstack11ll11_opy_ (u"ࠧ࠮ࠩᛇ") + getattr(report, bstack11ll11_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᛈ"), bstack11ll11_opy_ (u"ࠩࠪᛉ"))
            if getattr(report, bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᛊ"), False):
                hook_type = bstack11ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᛋ") if getattr(report, bstack11ll11_opy_ (u"ࠬࡽࡨࡦࡰࠪᛌ"), bstack11ll11_opy_ (u"࠭ࠧᛍ")) == bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᛎ") else bstack11ll11_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᛏ")
                _1l11111l1l_opy_[bstack1l11l111l1_opy_] = {
                    bstack11ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᛐ"): uuid4().__str__(),
                    bstack11ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᛑ"): bstack1ll1111lll_opy_,
                    bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᛒ"): hook_type
                }
            _1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛓ")] = bstack1ll1111lll_opy_
            bstack1lll1111111_opy_(_1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᛔ")])
            bstack1lll111l1ll_opy_(item, _1l11111l1l_opy_[bstack1l11l111l1_opy_], bstack11ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᛕ"), report, call)
            if getattr(report, bstack11ll11_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᛖ"), bstack11ll11_opy_ (u"ࠩࠪᛗ")) == bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᛘ"):
                if getattr(report, bstack11ll11_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᛙ"), bstack11ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᛚ")) == bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᛛ"):
                    bstack1l111111ll_opy_ = {
                        bstack11ll11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᛜ"): uuid4().__str__(),
                        bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᛝ"): bstack11l11l11l_opy_(),
                        bstack11ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᛞ"): bstack11l11l11l_opy_()
                    }
                    _1l11111l1l_opy_[item.nodeid] = {**_1l11111l1l_opy_[item.nodeid], **bstack1l111111ll_opy_}
                    bstack1lll1111l1l_opy_(item, _1l11111l1l_opy_[item.nodeid], bstack11ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᛟ"))
                    bstack1lll1111l1l_opy_(item, _1l11111l1l_opy_[item.nodeid], bstack11ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᛠ"), report, call)
    except Exception as err:
        print(bstack11ll11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡼࡿࠪᛡ"), str(err))
def bstack1lll1111lll_opy_(test, bstack1l111111ll_opy_, result=None, call=None, bstack1l1l1l1l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11llllll11_opy_ = {
        bstack11ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᛢ"): bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᛣ")],
        bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᛤ"): bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺࠧᛥ"),
        bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᛦ"): test.name,
        bstack11ll11_opy_ (u"ࠫࡧࡵࡤࡺࠩᛧ"): {
            bstack11ll11_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᛨ"): bstack11ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᛩ"),
            bstack11ll11_opy_ (u"ࠧࡤࡱࡧࡩࠬᛪ"): inspect.getsource(test.obj)
        },
        bstack11ll11_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᛫"): test.name,
        bstack11ll11_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨ᛬"): test.name,
        bstack11ll11_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪ᛭"): bstack1l1l111lll_opy_.bstack11lllll1ll_opy_(test),
        bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧᛮ"): file_path,
        bstack11ll11_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧᛯ"): file_path,
        bstack11ll11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᛰ"): bstack11ll11_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᛱ"),
        bstack11ll11_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᛲ"): file_path,
        bstack11ll11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᛳ"): bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᛴ")],
        bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᛵ"): bstack11ll11_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᛶ"),
        bstack11ll11_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩᛷ"): {
            bstack11ll11_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫᛸ"): test.nodeid
        },
        bstack11ll11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭᛹"): bstack111ll11ll1_opy_(test.own_markers)
    }
    if bstack1l1l1l1l_opy_ in [bstack11ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ᛺"), bstack11ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᛻")]:
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠫࡲ࡫ࡴࡢࠩ᛼")] = {
            bstack11ll11_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ᛽"): bstack1l111111ll_opy_.get(bstack11ll11_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ᛾"), [])
        }
    if bstack1l1l1l1l_opy_ == bstack11ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ᛿"):
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᜀ")] = bstack11ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᜁ")
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᜂ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᜃ")]
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᜄ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᜅ")]
    if result:
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᜆ")] = result.outcome
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᜇ")] = result.duration * 1000
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᜈ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜉ")]
        if result.failed:
            bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᜊ")] = bstack1l1l111lll_opy_.bstack11ll1l111l_opy_(call.excinfo.typename)
            bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᜋ")] = bstack1l1l111lll_opy_.bstack1lll11ll1ll_opy_(call.excinfo, result)
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᜌ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᜍ")]
    if outcome:
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᜎ")] = bstack11l1111lll_opy_(outcome)
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᜏ")] = 0
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜐ")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᜑ")]
        if bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᜒ")] == bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᜓ"):
            bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ᜔࠭")] = bstack11ll11_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳ᜕ࠩ")  # bstack1lll1111l11_opy_
            bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ᜖")] = [{bstack11ll11_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭᜗"): [bstack11ll11_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨ᜘")]}]
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ᜙")] = bstack1l111111ll_opy_[bstack11ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ᜚")]
    return bstack11llllll11_opy_
def bstack1ll1lllll11_opy_(test, bstack11lll11lll_opy_, bstack1l1l1l1l_opy_, result, call, outcome, bstack1lll11l1111_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ᜛")]
    hook_name = bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ᜜")]
    hook_data = {
        bstack11ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᜝"): bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᜞")],
        bstack11ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩᜟ"): bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᜠ"),
        bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜡ"): bstack11ll11_opy_ (u"ࠧࡼࡿࠪᜢ").format(bstack1llll1l1l1l_opy_(hook_name)),
        bstack11ll11_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᜣ"): {
            bstack11ll11_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᜤ"): bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᜥ"),
            bstack11ll11_opy_ (u"ࠫࡨࡵࡤࡦࠩᜦ"): None
        },
        bstack11ll11_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫᜧ"): test.name,
        bstack11ll11_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ᜨ"): bstack1l1l111lll_opy_.bstack11lllll1ll_opy_(test, hook_name),
        bstack11ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᜩ"): file_path,
        bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᜪ"): file_path,
        bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᜫ"): bstack11ll11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᜬ"),
        bstack11ll11_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᜭ"): file_path,
        bstack11ll11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᜮ"): bstack11lll11lll_opy_[bstack11ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᜯ")],
        bstack11ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᜰ"): bstack11ll11_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪᜱ") if bstack1ll1llll1l1_opy_ == bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᜲ") else bstack11ll11_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᜳ"),
        bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫᜴ࠧ"): hook_type
    }
    bstack1lll111llll_opy_ = bstack1l111111l1_opy_(_1l11111l1l_opy_.get(test.nodeid, None))
    if bstack1lll111llll_opy_:
        hook_data[bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪ᜵")] = bstack1lll111llll_opy_
    if result:
        hook_data[bstack11ll11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᜶")] = result.outcome
        hook_data[bstack11ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ᜷")] = result.duration * 1000
        hook_data[bstack11ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᜸")] = bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᜹")]
        if result.failed:
            hook_data[bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ᜺")] = bstack1l1l111lll_opy_.bstack11ll1l111l_opy_(call.excinfo.typename)
            hook_data[bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ᜻")] = bstack1l1l111lll_opy_.bstack1lll11ll1ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᜼")] = bstack11l1111lll_opy_(outcome)
        hook_data[bstack11ll11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ᜽")] = 100
        hook_data[bstack11ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᜾")] = bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᜿")]
        if hook_data[bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᝀ")] == bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᝁ"):
            hook_data[bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᝂ")] = bstack11ll11_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭ᝃ")  # bstack1lll1111l11_opy_
            hook_data[bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᝄ")] = [{bstack11ll11_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᝅ"): [bstack11ll11_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬᝆ")]}]
    if bstack1lll11l1111_opy_:
        hook_data[bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᝇ")] = bstack1lll11l1111_opy_.result
        hook_data[bstack11ll11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᝈ")] = bstack111lllll11_opy_(bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᝉ")], bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᝊ")])
        hook_data[bstack11ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᝋ")] = bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᝌ")]
        if hook_data[bstack11ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᝍ")] == bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᝎ"):
            hook_data[bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᝏ")] = bstack1l1l111lll_opy_.bstack11ll1l111l_opy_(bstack1lll11l1111_opy_.exception_type)
            hook_data[bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᝐ")] = [{bstack11ll11_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᝑ"): bstack11l111l1l1_opy_(bstack1lll11l1111_opy_.exception)}]
    return hook_data
def bstack1lll1111l1l_opy_(test, bstack1l111111ll_opy_, bstack1l1l1l1l_opy_, result=None, call=None, outcome=None):
    bstack11llllll11_opy_ = bstack1lll1111lll_opy_(test, bstack1l111111ll_opy_, result, call, bstack1l1l1l1l_opy_, outcome)
    driver = getattr(test, bstack11ll11_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᝒ"), None)
    if bstack1l1l1l1l_opy_ == bstack11ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᝓ") and driver:
        bstack11llllll11_opy_[bstack11ll11_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧ᝔")] = bstack1l1l111lll_opy_.bstack1l111l111l_opy_(driver)
    if bstack1l1l1l1l_opy_ == bstack11ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ᝕"):
        bstack1l1l1l1l_opy_ = bstack11ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᝖")
    bstack11lll1lll1_opy_ = {
        bstack11ll11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ᝗"): bstack1l1l1l1l_opy_,
        bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ᝘"): bstack11llllll11_opy_
    }
    bstack1l1l111lll_opy_.bstack11llll11ll_opy_(bstack11lll1lll1_opy_)
def bstack1lll111l1ll_opy_(test, bstack1l111111ll_opy_, bstack1l1l1l1l_opy_, result=None, call=None, outcome=None, bstack1lll11l1111_opy_=None):
    hook_data = bstack1ll1lllll11_opy_(test, bstack1l111111ll_opy_, bstack1l1l1l1l_opy_, result, call, outcome, bstack1lll11l1111_opy_)
    bstack11lll1lll1_opy_ = {
        bstack11ll11_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ᝙"): bstack1l1l1l1l_opy_,
        bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩ᝚"): hook_data
    }
    bstack1l1l111lll_opy_.bstack11llll11ll_opy_(bstack11lll1lll1_opy_)
def bstack1l111111l1_opy_(bstack1l111111ll_opy_):
    if not bstack1l111111ll_opy_:
        return None
    if bstack1l111111ll_opy_.get(bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ᝛"), None):
        return getattr(bstack1l111111ll_opy_[bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ᝜")], bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᝝"), None)
    return bstack1l111111ll_opy_.get(bstack11ll11_opy_ (u"ࠫࡺࡻࡩࡥࠩ᝞"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l1l111lll_opy_.on():
            return
        places = [bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᝟"), bstack11ll11_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᝠ"), bstack11ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᝡ")]
        bstack11llllll1l_opy_ = []
        for bstack1lll111111l_opy_ in places:
            records = caplog.get_records(bstack1lll111111l_opy_)
            bstack1ll1lll1lll_opy_ = bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᝢ") if bstack1lll111111l_opy_ == bstack11ll11_opy_ (u"ࠩࡦࡥࡱࡲࠧᝣ") else bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᝤ")
            bstack1lll111l111_opy_ = request.node.nodeid + (bstack11ll11_opy_ (u"ࠫࠬᝥ") if bstack1lll111111l_opy_ == bstack11ll11_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᝦ") else bstack11ll11_opy_ (u"࠭࠭ࠨᝧ") + bstack1lll111111l_opy_)
            bstack1lll111l11l_opy_ = bstack1l111111l1_opy_(_1l11111l1l_opy_.get(bstack1lll111l111_opy_, None))
            if not bstack1lll111l11l_opy_:
                continue
            for record in records:
                if bstack111llllll1_opy_(record.message):
                    continue
                bstack11llllll1l_opy_.append({
                    bstack11ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᝨ"): bstack111ll11l11_opy_(record.created).isoformat() + bstack11ll11_opy_ (u"ࠨ࡜ࠪᝩ"),
                    bstack11ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᝪ"): record.levelname,
                    bstack11ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᝫ"): record.message,
                    bstack1ll1lll1lll_opy_: bstack1lll111l11l_opy_
                })
        if len(bstack11llllll1l_opy_) > 0:
            bstack1l1l111lll_opy_.bstack11111l1l_opy_(bstack11llllll1l_opy_)
    except Exception as err:
        print(bstack11ll11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨᝬ"), str(err))
def bstack1l11l1111_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1ll1llllll_opy_
    bstack1111l11ll_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ᝭"), None) and bstack1l1lll1ll1_opy_(
            threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᝮ"), None)
    bstack1l1l111111_opy_ = getattr(driver, bstack11ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧᝯ"), None) != None and getattr(driver, bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨᝰ"), None) == True
    if sequence == bstack11ll11_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ᝱") and driver != None:
      if not bstack1ll1llllll_opy_ and bstack111lll1l11_opy_() and bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᝲ") in CONFIG and CONFIG[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᝳ")] == True and bstack1ll1lll1ll_opy_.bstack1l111ll1l_opy_(driver_command) and (bstack1l1l111111_opy_ or bstack1111l11ll_opy_) and not bstack1l11llll_opy_(args):
        try:
          bstack1ll1llllll_opy_ = True
          logger.debug(bstack11ll11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ᝴").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11ll11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫ᝵").format(str(err)))
        bstack1ll1llllll_opy_ = False
    if sequence == bstack11ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭᝶"):
        if driver_command == bstack11ll11_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ᝷"):
            bstack1l1l111lll_opy_.bstack1l1ll1ll11_opy_({
                bstack11ll11_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ᝸"): response[bstack11ll11_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ᝹")],
                bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᝺"): store[bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᝻")]
            })
def bstack1ll11111ll_opy_():
    global bstack1l111l11l_opy_
    bstack1l1l1l1l11_opy_.bstack1llll11lll_opy_()
    logging.shutdown()
    bstack1l1l111lll_opy_.bstack11lll1l11l_opy_()
    for driver in bstack1l111l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1llllll1_opy_(*args):
    global bstack1l111l11l_opy_
    bstack1l1l111lll_opy_.bstack11lll1l11l_opy_()
    for driver in bstack1l111l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1lll_opy_(self, *args, **kwargs):
    bstack1ll1l11l1l_opy_ = bstack1lll1ll11l_opy_(self, *args, **kwargs)
    bstack1l1l111lll_opy_.bstack1l1lll1l1_opy_(self)
    return bstack1ll1l11l1l_opy_
def bstack1lll1llll1_opy_(framework_name):
    global bstack1l11llll1_opy_
    global bstack1llll111l_opy_
    bstack1l11llll1_opy_ = framework_name
    logger.info(bstack1l1l111l1_opy_.format(bstack1l11llll1_opy_.split(bstack11ll11_opy_ (u"࠭࠭ࠨ᝼"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack111lll1l11_opy_():
            Service.start = bstack1ll11l11l_opy_
            Service.stop = bstack1llllllll_opy_
            webdriver.Remote.__init__ = bstack1l1l11l1l1_opy_
            webdriver.Remote.get = bstack1llll1111_opy_
            if not isinstance(os.getenv(bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨ᝽")), str):
                return
            WebDriver.close = bstack1ll1lll11_opy_
            WebDriver.quit = bstack1lll11l1ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack111lll1l11_opy_() and bstack1l1l111lll_opy_.on():
            webdriver.Remote.__init__ = bstack1lll1lll_opy_
        bstack1llll111l_opy_ = True
    except Exception as e:
        pass
    bstack1lll1l1l1_opy_()
    if os.environ.get(bstack11ll11_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭᝾")):
        bstack1llll111l_opy_ = eval(os.environ.get(bstack11ll11_opy_ (u"ࠩࡖࡉࡑࡋࡎࡊࡗࡐࡣࡔࡘ࡟ࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡎࡔࡓࡕࡃࡏࡐࡊࡊࠧ᝿")))
    if not bstack1llll111l_opy_:
        bstack11l1llll_opy_(bstack11ll11_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧក"), bstack11111l1ll_opy_)
    if bstack1llll1l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1ll1llll_opy_
        except Exception as e:
            logger.error(bstack1111l1l1_opy_.format(str(e)))
    if bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫខ") in str(framework_name).lower():
        if not bstack111lll1l11_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11llll11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1lll1l11l_opy_
            Config.getoption = bstack1l1l1l11l1_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1lll1l1111_opy_
        except Exception as e:
            pass
def bstack1lll11l1ll_opy_(self):
    global bstack1l11llll1_opy_
    global bstack1l11llll11_opy_
    global bstack1l1l11lll_opy_
    try:
        if bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬគ") in bstack1l11llll1_opy_ and self.session_id != None and bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪឃ"), bstack11ll11_opy_ (u"ࠧࠨង")) != bstack11ll11_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩច"):
            bstack1l1lllll1_opy_ = bstack11ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩឆ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪជ")
            bstack1ll1llll1l_opy_(logger, True)
            if self != None:
                bstack11l11ll11_opy_(self, bstack1l1lllll1_opy_, bstack11ll11_opy_ (u"ࠫ࠱ࠦࠧឈ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩញ"), None)
        if item is not None and bstack1lll111ll1l_opy_:
            bstack11lll1l1_opy_.bstack1l1l1llll_opy_(self, bstack1ll1llll1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11ll11_opy_ (u"࠭ࠧដ")
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣឋ") + str(e))
    bstack1l1l11lll_opy_(self)
    self.session_id = None
def bstack1l1l11l1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l11llll11_opy_
    global bstack1lll1ll111_opy_
    global bstack1l11lll1_opy_
    global bstack1l11llll1_opy_
    global bstack1lll1ll11l_opy_
    global bstack1l111l11l_opy_
    global bstack1l11l1l1l1_opy_
    global bstack111111ll_opy_
    global bstack1lll111ll1l_opy_
    global bstack1ll1llll1_opy_
    CONFIG[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪឌ")] = str(bstack1l11llll1_opy_) + str(__version__)
    command_executor = bstack1llllll11_opy_(bstack1l11l1l1l1_opy_)
    logger.debug(bstack1l1l1ll1ll_opy_.format(command_executor))
    proxy = bstack1l1lll11l1_opy_(CONFIG, proxy)
    bstack1llll111ll_opy_ = 0
    try:
        if bstack1l11lll1_opy_ is True:
            bstack1llll111ll_opy_ = int(os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩឍ")))
    except:
        bstack1llll111ll_opy_ = 0
    bstack1ll111l1l1_opy_ = bstack11l11l1l_opy_(CONFIG, bstack1llll111ll_opy_)
    logger.debug(bstack1111lllll_opy_.format(str(bstack1ll111l1l1_opy_)))
    bstack1ll1llll1_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ណ"))[bstack1llll111ll_opy_]
    if bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨត") in CONFIG and CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩថ")]:
        bstack11lllll1l_opy_(bstack1ll111l1l1_opy_, bstack111111ll_opy_)
    if bstack1l111111l_opy_.bstack111l1ll11_opy_(CONFIG, bstack1llll111ll_opy_) and bstack1l111111l_opy_.bstack11ll11l1l_opy_(bstack1ll111l1l1_opy_, options):
        bstack1lll111ll1l_opy_ = True
        bstack1l111111l_opy_.set_capabilities(bstack1ll111l1l1_opy_, CONFIG)
    if desired_capabilities:
        bstack111ll1ll1_opy_ = bstack1ll1l11111_opy_(desired_capabilities)
        bstack111ll1ll1_opy_[bstack11ll11_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ទ")] = bstack111111ll1_opy_(CONFIG)
        bstack1llll111_opy_ = bstack11l11l1l_opy_(bstack111ll1ll1_opy_)
        if bstack1llll111_opy_:
            bstack1ll111l1l1_opy_ = update(bstack1llll111_opy_, bstack1ll111l1l1_opy_)
        desired_capabilities = None
    if options:
        bstack1lll11l1l_opy_(options, bstack1ll111l1l1_opy_)
    if not options:
        options = bstack1ll1ll1l_opy_(bstack1ll111l1l1_opy_)
    if proxy and bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧធ")):
        options.proxy(proxy)
    if options and bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧន")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack111ll1l11_opy_() < version.parse(bstack11ll11_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨប")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1ll111l1l1_opy_)
    logger.info(bstack1111l1l11_opy_)
    if bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪផ")):
        bstack1lll1ll11l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪព")):
        bstack1lll1ll11l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬភ")):
        bstack1lll1ll11l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1lll1ll11l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l11lll11_opy_ = bstack11ll11_opy_ (u"࠭ࠧម")
        if bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨយ")):
            bstack1l11lll11_opy_ = self.caps.get(bstack11ll11_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣរ"))
        else:
            bstack1l11lll11_opy_ = self.capabilities.get(bstack11ll11_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤល"))
        if bstack1l11lll11_opy_:
            bstack11llll1ll_opy_(bstack1l11lll11_opy_)
            if bstack111ll1l11_opy_() <= version.parse(bstack11ll11_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪវ")):
                self.command_executor._url = bstack11ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧឝ") + bstack1l11l1l1l1_opy_ + bstack11ll11_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤឞ")
            else:
                self.command_executor._url = bstack11ll11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣស") + bstack1l11lll11_opy_ + bstack11ll11_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣហ")
            logger.debug(bstack1lll1ll11_opy_.format(bstack1l11lll11_opy_))
        else:
            logger.debug(bstack1l1ll11l_opy_.format(bstack11ll11_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤឡ")))
    except Exception as e:
        logger.debug(bstack1l1ll11l_opy_.format(e))
    bstack1l11llll11_opy_ = self.session_id
    if bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩអ") in bstack1l11llll1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧឣ"), None)
        if item:
            bstack1lll111l1l1_opy_ = getattr(item, bstack11ll11_opy_ (u"ࠫࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࡠࡵࡷࡥࡷࡺࡥࡥࠩឤ"), False)
            if not getattr(item, bstack11ll11_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ឥ"), None) and bstack1lll111l1l1_opy_:
                setattr(store[bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪឦ")], bstack11ll11_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨឧ"), self)
        bstack1l1l111lll_opy_.bstack1l1lll1l1_opy_(self)
    bstack1l111l11l_opy_.append(self)
    if bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫឨ") in CONFIG and bstack11ll11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧឩ") in CONFIG[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ឪ")][bstack1llll111ll_opy_]:
        bstack1lll1ll111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧឫ")][bstack1llll111ll_opy_][bstack11ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪឬ")]
    logger.debug(bstack111ll11ll_opy_.format(bstack1l11llll11_opy_))
def bstack1llll1111_opy_(self, url):
    global bstack1lllll1lll_opy_
    global CONFIG
    try:
        bstack1l1111ll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11l111l1l_opy_.format(str(err)))
    try:
        bstack1lllll1lll_opy_(self, url)
    except Exception as e:
        try:
            bstack1ll1111111_opy_ = str(e)
            if any(err_msg in bstack1ll1111111_opy_ for err_msg in bstack1ll1lllll1_opy_):
                bstack1l1111ll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11l111l1l_opy_.format(str(err)))
        raise e
def bstack1lll1l1l_opy_(item, when):
    global bstack111l1ll1l_opy_
    try:
        bstack111l1ll1l_opy_(item, when)
    except Exception as e:
        pass
def bstack1lll1l1111_opy_(item, call, rep):
    global bstack11l11l1ll_opy_
    global bstack1l111l11l_opy_
    name = bstack11ll11_opy_ (u"࠭ࠧឭ")
    try:
        if rep.when == bstack11ll11_opy_ (u"ࠧࡤࡣ࡯ࡰࠬឮ"):
            bstack1l11llll11_opy_ = threading.current_thread().bstackSessionId
            bstack1lll11l1l1l_opy_ = item.config.getoption(bstack11ll11_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪឯ"))
            try:
                if (str(bstack1lll11l1l1l_opy_).lower() != bstack11ll11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧឰ")):
                    name = str(rep.nodeid)
                    bstack1ll11ll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫឱ"), name, bstack11ll11_opy_ (u"ࠫࠬឲ"), bstack11ll11_opy_ (u"ࠬ࠭ឳ"), bstack11ll11_opy_ (u"࠭ࠧ឴"), bstack11ll11_opy_ (u"ࠧࠨ឵"))
                    os.environ[bstack11ll11_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫា")] = name
                    for driver in bstack1l111l11l_opy_:
                        if bstack1l11llll11_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll11ll11_opy_)
            except Exception as e:
                logger.debug(bstack11ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩិ").format(str(e)))
            try:
                bstack11lll111l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫី"):
                    status = bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫឹ") if rep.outcome.lower() == bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬឺ") else bstack11ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ុ")
                    reason = bstack11ll11_opy_ (u"ࠧࠨូ")
                    if status == bstack11ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨួ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11ll11_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧើ") if status == bstack11ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪឿ") else bstack11ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪៀ")
                    data = name + bstack11ll11_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧេ") if status == bstack11ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ែ") else name + bstack11ll11_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪៃ") + reason
                    bstack1lllllll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪោ"), bstack11ll11_opy_ (u"ࠩࠪៅ"), bstack11ll11_opy_ (u"ࠪࠫំ"), bstack11ll11_opy_ (u"ࠫࠬះ"), level, data)
                    for driver in bstack1l111l11l_opy_:
                        if bstack1l11llll11_opy_ == driver.session_id:
                            driver.execute_script(bstack1lllllll11_opy_)
            except Exception as e:
                logger.debug(bstack11ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩៈ").format(str(e)))
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪ៉").format(str(e)))
    bstack11l11l1ll_opy_(item, call, rep)
notset = Notset()
def bstack1l1l1l11l1_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1llllll_opy_
    if str(name).lower() == bstack11ll11_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧ៊"):
        return bstack11ll11_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ់")
    else:
        return bstack1l1llllll_opy_(self, name, default, skip)
def bstack1ll1llll_opy_(self):
    global CONFIG
    global bstack1lll111l1l_opy_
    try:
        proxy = bstack1l11l1ll1l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11ll11_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ៌")):
                proxies = bstack1l111lll1_opy_(proxy, bstack1llllll11_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1l1lll_opy_ = proxies.popitem()
                    if bstack11ll11_opy_ (u"ࠥ࠾࠴࠵ࠢ៍") in bstack1l1l1lll_opy_:
                        return bstack1l1l1lll_opy_
                    else:
                        return bstack11ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ៎") + bstack1l1l1lll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤ៏").format(str(e)))
    return bstack1lll111l1l_opy_(self)
def bstack1llll1l1_opy_():
    return (bstack11ll11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ័") in CONFIG or bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ៑") in CONFIG) and bstack11111llll_opy_() and bstack111ll1l11_opy_() >= version.parse(
        bstack1ll11l11l1_opy_)
def bstack1l1ll111_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1lll1ll111_opy_
    global bstack1l11lll1_opy_
    global bstack1l11llll1_opy_
    CONFIG[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ្ࠪ")] = str(bstack1l11llll1_opy_) + str(__version__)
    bstack1llll111ll_opy_ = 0
    try:
        if bstack1l11lll1_opy_ is True:
            bstack1llll111ll_opy_ = int(os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ៓")))
    except:
        bstack1llll111ll_opy_ = 0
    CONFIG[bstack11ll11_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ។")] = True
    bstack1ll111l1l1_opy_ = bstack11l11l1l_opy_(CONFIG, bstack1llll111ll_opy_)
    logger.debug(bstack1111lllll_opy_.format(str(bstack1ll111l1l1_opy_)))
    if CONFIG.get(bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ៕")):
        bstack11lllll1l_opy_(bstack1ll111l1l1_opy_, bstack111111ll_opy_)
    if bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ៖") in CONFIG and bstack11ll11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫៗ") in CONFIG[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ៘")][bstack1llll111ll_opy_]:
        bstack1lll1ll111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ៙")][bstack1llll111ll_opy_][bstack11ll11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ៚")]
    import urllib
    import json
    bstack11lll111_opy_ = bstack11ll11_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ៛") + urllib.parse.quote(json.dumps(bstack1ll111l1l1_opy_))
    browser = self.connect(bstack11lll111_opy_)
    return browser
def bstack1lll1l1l1_opy_():
    global bstack1llll111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l1ll111_opy_
        bstack1llll111l_opy_ = True
    except Exception as e:
        pass
def bstack1ll1llll1ll_opy_():
    global CONFIG
    global bstack11llll1l_opy_
    global bstack1l11l1l1l1_opy_
    global bstack111111ll_opy_
    global bstack1l11lll1_opy_
    global bstack1l1l11l11l_opy_
    CONFIG = json.loads(os.environ.get(bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪៜ")))
    bstack11llll1l_opy_ = eval(os.environ.get(bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭៝")))
    bstack1l11l1l1l1_opy_ = os.environ.get(bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭៞"))
    bstack1l1l1llll1_opy_(CONFIG, bstack11llll1l_opy_)
    bstack1l1l11l11l_opy_ = bstack1l1l1l1l11_opy_.bstack1l11l1lll1_opy_(CONFIG, bstack1l1l11l11l_opy_)
    global bstack1lll1ll11l_opy_
    global bstack1l1l11lll_opy_
    global bstack11l11l1l1_opy_
    global bstack1llll111l1_opy_
    global bstack11lll1l11_opy_
    global bstack1l1ll11l1l_opy_
    global bstack11ll1ll11_opy_
    global bstack1lllll1lll_opy_
    global bstack1lll111l1l_opy_
    global bstack1l1llllll_opy_
    global bstack111l1ll1l_opy_
    global bstack11l11l1ll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1lll1ll11l_opy_ = webdriver.Remote.__init__
        bstack1l1l11lll_opy_ = WebDriver.quit
        bstack11ll1ll11_opy_ = WebDriver.close
        bstack1lllll1lll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ៟") in CONFIG or bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ០") in CONFIG) and bstack11111llll_opy_():
        if bstack111ll1l11_opy_() < version.parse(bstack1ll11l11l1_opy_):
            logger.error(bstack1l1ll1lll1_opy_.format(bstack111ll1l11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1lll111l1l_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1111l1l1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l1llllll_opy_ = Config.getoption
        from _pytest import runner
        bstack111l1ll1l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1lllll11ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack11l11l1ll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ១"))
    bstack111111ll_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ២"), {}).get(bstack11ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭៣"))
    bstack1l11lll1_opy_ = True
    bstack1lll1llll1_opy_(bstack1l1l11lll1_opy_)
if (bstack11l111ll1l_opy_()):
    bstack1ll1llll1ll_opy_()
@bstack1l1111l11l_opy_(class_method=False)
def bstack1lll111ll11_opy_(hook_name, event, bstack1ll1llll111_opy_=None):
    if hook_name not in [bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭៤"), bstack11ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ៥"), bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭៦"), bstack11ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ៧"), bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ៨"), bstack11ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ៩"), bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪ៪"), bstack11ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧ៫")]:
        return
    node = store[bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ៬")]
    if hook_name in [bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭៭"), bstack11ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ៮")]:
        node = store[bstack11ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨ៯")]
    elif hook_name in [bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ៰"), bstack11ll11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ៱")]:
        node = store[bstack11ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪ៲")]
    if event == bstack11ll11_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭៳"):
        hook_type = bstack1llll1llll1_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11lll11lll_opy_ = {
            bstack11ll11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ៴"): uuid,
            bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ៵"): bstack11l11l11l_opy_(),
            bstack11ll11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ៶"): bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ៷"),
            bstack11ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ៸"): hook_type,
            bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ៹"): hook_name
        }
        store[bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ៺")].append(uuid)
        bstack1lll111lll1_opy_ = node.nodeid
        if hook_type == bstack11ll11_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ៻"):
            if not _1l11111l1l_opy_.get(bstack1lll111lll1_opy_, None):
                _1l11111l1l_opy_[bstack1lll111lll1_opy_] = {bstack11ll11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ៼"): []}
            _1l11111l1l_opy_[bstack1lll111lll1_opy_][bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ៽")].append(bstack11lll11lll_opy_[bstack11ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ៾")])
        _1l11111l1l_opy_[bstack1lll111lll1_opy_ + bstack11ll11_opy_ (u"ࠫ࠲࠭៿") + hook_name] = bstack11lll11lll_opy_
        bstack1lll111l1ll_opy_(node, bstack11lll11lll_opy_, bstack11ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭᠀"))
    elif event == bstack11ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ᠁"):
        bstack1l11l111l1_opy_ = node.nodeid + bstack11ll11_opy_ (u"ࠧ࠮ࠩ᠂") + hook_name
        _1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᠃")] = bstack11l11l11l_opy_()
        bstack1lll1111111_opy_(_1l11111l1l_opy_[bstack1l11l111l1_opy_][bstack11ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᠄")])
        bstack1lll111l1ll_opy_(node, _1l11111l1l_opy_[bstack1l11l111l1_opy_], bstack11ll11_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᠅"), bstack1lll11l1111_opy_=bstack1ll1llll111_opy_)
def bstack1lll11l1lll_opy_():
    global bstack1ll1llll1l1_opy_
    if bstack1l1ll11l1_opy_():
        bstack1ll1llll1l1_opy_ = bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨ᠆")
    else:
        bstack1ll1llll1l1_opy_ = bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᠇")
@bstack1l1l111lll_opy_.bstack1lll1l111l1_opy_
def bstack1lll11l11l1_opy_():
    bstack1lll11l1lll_opy_()
    if bstack11111llll_opy_():
        bstack1l11lll11l_opy_(bstack1l11l1111_opy_)
    try:
        bstack111l111l1l_opy_(bstack1lll111ll11_opy_)
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢ᠈").format(e))
bstack1lll11l11l1_opy_()