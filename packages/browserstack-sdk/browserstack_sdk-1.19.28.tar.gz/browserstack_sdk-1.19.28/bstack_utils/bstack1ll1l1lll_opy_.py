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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack111llll11l_opy_, bstack1l111l11_opy_, bstack1l1lll1ll1_opy_, bstack1l11ll11ll_opy_, \
    bstack11l111l1ll_opy_
def bstack1ll11111ll_opy_(bstack1llll111l11_opy_):
    for driver in bstack1llll111l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11l11ll11_opy_(driver, status, reason=bstack11ll11_opy_ (u"࠭ࠧᒤ")):
    bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
    if bstack1l1l1l1l1_opy_.bstack11ll1l1l11_opy_():
        return
    bstack1ll11ll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᒥ"), bstack11ll11_opy_ (u"ࠨࠩᒦ"), status, reason, bstack11ll11_opy_ (u"ࠩࠪᒧ"), bstack11ll11_opy_ (u"ࠪࠫᒨ"))
    driver.execute_script(bstack1ll11ll11_opy_)
def bstack111111l1_opy_(page, status, reason=bstack11ll11_opy_ (u"ࠫࠬᒩ")):
    try:
        if page is None:
            return
        bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
        if bstack1l1l1l1l1_opy_.bstack11ll1l1l11_opy_():
            return
        bstack1ll11ll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᒪ"), bstack11ll11_opy_ (u"࠭ࠧᒫ"), status, reason, bstack11ll11_opy_ (u"ࠧࠨᒬ"), bstack11ll11_opy_ (u"ࠨࠩᒭ"))
        page.evaluate(bstack11ll11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᒮ"), bstack1ll11ll11_opy_)
    except Exception as e:
        print(bstack11ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣᒯ"), e)
def bstack11llll1l1_opy_(type, name, status, reason, bstack11ll1lll1_opy_, bstack11ll1l11l_opy_):
    bstack1ll11l1111_opy_ = {
        bstack11ll11_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᒰ"): type,
        bstack11ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᒱ"): {}
    }
    if type == bstack11ll11_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᒲ"):
        bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᒳ")][bstack11ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᒴ")] = bstack11ll1lll1_opy_
        bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᒵ")][bstack11ll11_opy_ (u"ࠪࡨࡦࡺࡡࠨᒶ")] = json.dumps(str(bstack11ll1l11l_opy_))
    if type == bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᒷ"):
        bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᒸ")][bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᒹ")] = name
    if type == bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᒺ"):
        bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᒻ")][bstack11ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᒼ")] = status
        if status == bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᒽ") and str(reason) != bstack11ll11_opy_ (u"ࠦࠧᒾ"):
            bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᒿ")][bstack11ll11_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᓀ")] = json.dumps(str(reason))
    bstack1ll1l11l1_opy_ = bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᓁ").format(json.dumps(bstack1ll11l1111_opy_))
    return bstack1ll1l11l1_opy_
def bstack1l1111ll_opy_(url, config, logger, bstack111111lll_opy_=False):
    hostname = bstack1l111l11_opy_(url)
    is_private = bstack1l11ll11ll_opy_(hostname)
    try:
        if is_private or bstack111111lll_opy_:
            file_path = bstack111llll11l_opy_(bstack11ll11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᓂ"), bstack11ll11_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᓃ"), logger)
            if os.environ.get(bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᓄ")) and eval(
                    os.environ.get(bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᓅ"))):
                return
            if (bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᓆ") in config and not config[bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᓇ")]):
                os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᓈ")] = str(True)
                bstack1llll1111l1_opy_ = {bstack11ll11_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪᓉ"): hostname}
                bstack11l111l1ll_opy_(bstack11ll11_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᓊ"), bstack11ll11_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨᓋ"), bstack1llll1111l1_opy_, logger)
    except Exception as e:
        pass
def bstack11lllll1l_opy_(caps, bstack1llll11111l_opy_):
    if bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᓌ") in caps:
        caps[bstack11ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓍ")][bstack11ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬᓎ")] = True
        if bstack1llll11111l_opy_:
            caps[bstack11ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᓏ")][bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᓐ")] = bstack1llll11111l_opy_
    else:
        caps[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧᓑ")] = True
        if bstack1llll11111l_opy_:
            caps[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᓒ")] = bstack1llll11111l_opy_
def bstack1llll1ll1ll_opy_(bstack1l1111l1l1_opy_):
    bstack1llll1111ll_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᓓ"), bstack11ll11_opy_ (u"ࠬ࠭ᓔ"))
    if bstack1llll1111ll_opy_ == bstack11ll11_opy_ (u"࠭ࠧᓕ") or bstack1llll1111ll_opy_ == bstack11ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᓖ"):
        threading.current_thread().testStatus = bstack1l1111l1l1_opy_
    else:
        if bstack1l1111l1l1_opy_ == bstack11ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓗ"):
            threading.current_thread().testStatus = bstack1l1111l1l1_opy_