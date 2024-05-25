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
import re
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll1ll1ll_opy_
def bstack1lllll11111_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᑯ")):
        return bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᑰ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᑱ")):
        return bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᑲ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᑳ")):
        return bstack11ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᑴ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᑵ")):
        return bstack11ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᑶ")
def bstack1llll1lllll_opy_(fixture_name):
    return bool(re.match(bstack11ll11_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᑷ"), fixture_name))
def bstack1llll1l1lll_opy_(fixture_name):
    return bool(re.match(bstack11ll11_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᑸ"), fixture_name))
def bstack1llll1lll11_opy_(fixture_name):
    return bool(re.match(bstack11ll11_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᑹ"), fixture_name))
def bstack1lllll111l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᑺ")):
        return bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᑻ"), bstack11ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᑼ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑽ")):
        return bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᑾ"), bstack11ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᑿ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᒀ")):
        return bstack11ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᒁ"), bstack11ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᒂ")
    elif fixture_name.startswith(bstack11ll11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᒃ")):
        return bstack11ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᒄ"), bstack11ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᒅ")
    return None, None
def bstack1llll1l1l1l_opy_(hook_name):
    if hook_name in [bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᒆ"), bstack11ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᒇ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llll1llll1_opy_(hook_name):
    if hook_name in [bstack11ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᒈ"), bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᒉ")]:
        return bstack11ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᒊ")
    elif hook_name in [bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᒋ"), bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᒌ")]:
        return bstack11ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᒍ")
    elif hook_name in [bstack11ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᒎ"), bstack11ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᒏ")]:
        return bstack11ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᒐ")
    elif hook_name in [bstack11ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᒑ"), bstack11ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᒒ")]:
        return bstack11ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᒓ")
    return hook_name
def bstack1llll1l1ll1_opy_(node, scenario):
    if hasattr(node, bstack11ll11_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᒔ")):
        parts = node.nodeid.rsplit(bstack11ll11_opy_ (u"ࠧࡡࠢᒕ"))
        params = parts[-1]
        return bstack11ll11_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨᒖ").format(scenario.name, params)
    return scenario.name
def bstack1lllll1111l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11ll11_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᒗ")):
            examples = list(node.callspec.params[bstack11ll11_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧᒘ")].values())
        return examples
    except:
        return []
def bstack1llll1ll111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llll1ll11l_opy_(report):
    try:
        status = bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᒙ")
        if report.passed or (report.failed and hasattr(report, bstack11ll11_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᒚ"))):
            status = bstack11ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᒛ")
        elif report.skipped:
            status = bstack11ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᒜ")
        bstack1llll1ll1ll_opy_(status)
    except:
        pass
def bstack11lll111l_opy_(status):
    try:
        bstack1llll1ll1l1_opy_ = bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᒝ")
        if status == bstack11ll11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᒞ"):
            bstack1llll1ll1l1_opy_ = bstack11ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᒟ")
        elif status == bstack11ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᒠ"):
            bstack1llll1ll1l1_opy_ = bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᒡ")
        bstack1llll1ll1ll_opy_(bstack1llll1ll1l1_opy_)
    except:
        pass
def bstack1llll1lll1l_opy_(item=None, report=None, summary=None, extra=None):
    return