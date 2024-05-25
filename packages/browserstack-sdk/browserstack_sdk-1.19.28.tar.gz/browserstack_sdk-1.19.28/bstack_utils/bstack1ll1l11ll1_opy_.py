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
import json
import requests
import logging
from urllib.parse import urlparse
from bstack_utils.constants import bstack11ll1111l1_opy_ as bstack11ll111ll1_opy_
from bstack_utils.bstack1ll1lll1ll_opy_ import bstack1ll1lll1ll_opy_
from bstack_utils.helper import bstack11l11l11l_opy_, bstack1l11l1111l_opy_, bstack11l1lll1l_opy_, bstack11ll11l11l_opy_, bstack11l1lllll1_opy_, bstack11lllll1_opy_, get_host_info, bstack11l1lll11l_opy_, bstack1l1ll11ll_opy_, bstack1l1111l11l_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1111l11l_opy_(class_method=False)
def _11ll11l1ll_opy_(driver, bstack1llllllll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11ll11_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧ์"): caps.get(bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ํ"), None),
        bstack11ll11_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๎"): bstack1llllllll1_opy_.get(bstack11ll11_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ๏"), None),
        bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩ๐"): caps.get(bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ๑"), None),
        bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ๒"): caps.get(bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ๓"), None)
    }
  except Exception as error:
    logger.debug(bstack11ll11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ๔") + str(error))
  return response
def bstack11ll11ll1_opy_(config):
  return config.get(bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ๕"), False) or any([p.get(bstack11ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ๖"), False) == True for p in config.get(bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭๗"), [])])
def bstack111l1ll11_opy_(config, bstack1llll111ll_opy_):
  try:
    if not bstack11l1lll1l_opy_(config):
      return False
    bstack11l1ll1l11_opy_ = config.get(bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ๘"), False)
    bstack11l1ll11ll_opy_ = config[bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ๙")][bstack1llll111ll_opy_].get(bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭๚"), None)
    if bstack11l1ll11ll_opy_ != None:
      bstack11l1ll1l11_opy_ = bstack11l1ll11ll_opy_
    bstack11l1lll1ll_opy_ = os.getenv(bstack11ll11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ๛")) is not None and len(os.getenv(bstack11ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭๜"))) > 0 and os.getenv(bstack11ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ๝")) != bstack11ll11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ๞")
    return bstack11l1ll1l11_opy_ and bstack11l1lll1ll_opy_
  except Exception as error:
    logger.debug(bstack11ll11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ๟") + str(error))
  return False
def bstack1lllll1l1_opy_(bstack11l1lll111_opy_, test_tags):
  bstack11l1lll111_opy_ = os.getenv(bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭๠"))
  if bstack11l1lll111_opy_ is None:
    return True
  bstack11l1lll111_opy_ = json.loads(bstack11l1lll111_opy_)
  try:
    include_tags = bstack11l1lll111_opy_[bstack11ll11_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ๡")] if bstack11ll11_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ๢") in bstack11l1lll111_opy_ and isinstance(bstack11l1lll111_opy_[bstack11ll11_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭๣")], list) else []
    exclude_tags = bstack11l1lll111_opy_[bstack11ll11_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ๤")] if bstack11ll11_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ๥") in bstack11l1lll111_opy_ and isinstance(bstack11l1lll111_opy_[bstack11ll11_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ๦")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧ๧") + str(error))
  return False
def bstack1ll1l111_opy_(config, bstack11ll111111_opy_, bstack11l1llll11_opy_, bstack11ll11ll1l_opy_):
  bstack11l1lll1l1_opy_ = bstack11ll11l11l_opy_(config)
  bstack11l1ll1ll1_opy_ = bstack11l1lllll1_opy_(config)
  if bstack11l1lll1l1_opy_ is None or bstack11l1ll1ll1_opy_ is None:
    logger.error(bstack11ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧ๨"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ๩"), bstack11ll11_opy_ (u"ࠨࡽࢀࠫ๪")))
    data = {
        bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ๫"): config[bstack11ll11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ๬")],
        bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ๭"): config.get(bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ๮"), os.path.basename(os.getcwd())),
        bstack11ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩ๯"): bstack11l11l11l_opy_(),
        bstack11ll11_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ๰"): config.get(bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ๱"), bstack11ll11_opy_ (u"ࠩࠪ๲")),
        bstack11ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ๳"): {
            bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ๴"): bstack11ll111111_opy_,
            bstack11ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ๵"): bstack11l1llll11_opy_,
            bstack11ll11_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ๶"): __version__,
            bstack11ll11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ๷"): bstack11ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ๸"),
            bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ๹"): bstack11ll11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ๺"),
            bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ๻"): bstack11ll11ll1l_opy_
        },
        bstack11ll11_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ๼"): settings,
        bstack11ll11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧ๽"): bstack11l1lll11l_opy_(),
        bstack11ll11_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧ๾"): bstack11lllll1_opy_(),
        bstack11ll11_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪ๿"): get_host_info(),
        bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ຀"): bstack11l1lll1l_opy_(config)
    }
    headers = {
        bstack11ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩກ"): bstack11ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧຂ"),
    }
    config = {
        bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪ຃"): (bstack11l1lll1l1_opy_, bstack11l1ll1ll1_opy_),
        bstack11ll11_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧຄ"): headers
    }
    response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠧࡑࡑࡖࡘࠬ຅"), bstack11ll111ll1_opy_ + bstack11ll11_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨຆ"), data, config)
    bstack11l1llll1l_opy_ = response.json()
    if bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪງ")]:
      parsed = json.loads(os.getenv(bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫຈ"), bstack11ll11_opy_ (u"ࠫࢀࢃࠧຉ")))
      parsed[bstack11ll11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ຊ")] = bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"࠭ࡤࡢࡶࡤࠫ຋")][bstack11ll11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨຌ")]
      os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩຍ")] = json.dumps(parsed)
      bstack1ll1lll1ll_opy_.bstack11ll11ll11_opy_(bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠩࡧࡥࡹࡧࠧຎ")][bstack11ll11_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫຏ")])
      bstack1ll1lll1ll_opy_.bstack11ll111l1l_opy_(bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠫࡩࡧࡴࡢࠩຐ")][bstack11ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧຑ")])
      bstack1ll1lll1ll_opy_.store()
      return bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"࠭ࡤࡢࡶࡤࠫຒ")][bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬຓ")], bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠨࡦࡤࡸࡦ࠭ດ")][bstack11ll11_opy_ (u"ࠩ࡬ࡨࠬຕ")]
    else:
      logger.error(bstack11ll11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫຖ") + bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬທ")])
      if bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ຘ")] == bstack11ll11_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨນ"):
        for bstack11l1ll1l1l_opy_ in bstack11l1llll1l_opy_[bstack11ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧບ")]:
          logger.error(bstack11l1ll1l1l_opy_[bstack11ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩປ")])
      return None, None
  except Exception as error:
    logger.error(bstack11ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥຜ") +  str(error))
    return None, None
def bstack1lll1llll_opy_():
  if os.getenv(bstack11ll11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨຝ")) is None:
    return {
        bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫພ"): bstack11ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫຟ"),
        bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧຠ"): bstack11ll11_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭ມ")
    }
  data = {bstack11ll11_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩຢ"): bstack11l11l11l_opy_()}
  headers = {
      bstack11ll11_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩຣ"): bstack11ll11_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ຤") + os.getenv(bstack11ll11_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤລ")),
      bstack11ll11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ຦"): bstack11ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩວ")
  }
  response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠧࡑࡗࡗࠫຨ"), bstack11ll111ll1_opy_ + bstack11ll11_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪຩ"), data, { bstack11ll11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪສ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11ll11_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦຫ") + bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠫ࡟࠭ຬ"))
      return {bstack11ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬອ"): bstack11ll11_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧຮ"), bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨຯ"): bstack11ll11_opy_ (u"ࠨࠩະ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧັ") + str(error))
    return {
        bstack11ll11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪາ"): bstack11ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪຳ"),
        bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ິ"): str(error)
    }
def bstack11ll11l1l_opy_(caps, options):
  try:
    bstack11ll1111ll_opy_ = caps.get(bstack11ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧີ"), {}).get(bstack11ll11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫຶ"), caps.get(bstack11ll11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨື"), bstack11ll11_opy_ (u"ຸࠩࠪ")))
    if bstack11ll1111ll_opy_:
      logger.warn(bstack11ll11_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ູࠢ"))
      return False
    browser = caps.get(bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦ຺ࠩ"), bstack11ll11_opy_ (u"ࠬ࠭ົ")).lower()
    if browser != bstack11ll11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ຼ"):
      logger.warn(bstack11ll11_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥຽ"))
      return False
    browser_version = caps.get(bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ຾"), caps.get(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ຿")))
    if browser_version and browser_version != bstack11ll11_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪເ") and int(browser_version.split(bstack11ll11_opy_ (u"ࠫ࠳࠭ແ"))[0]) <= 94:
      logger.warn(bstack11ll11_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠹࠵࠰ࠥໂ"))
      return False
    if not options is None:
      bstack11ll11l111_opy_ = options.to_capabilities().get(bstack11ll11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫໃ"), {})
      if bstack11ll11_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫໄ") in bstack11ll11l111_opy_.get(bstack11ll11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭໅"), []):
        logger.warn(bstack11ll11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦໆ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧ໇") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11l1ll11l1_opy_ = config.get(bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ່ࠫ"), {})
    bstack11l1ll11l1_opy_[bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ້")] = os.getenv(bstack11ll11_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗ໊ࠫ"))
    bstack11l1llllll_opy_ = json.loads(os.getenv(bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ໋"), bstack11ll11_opy_ (u"ࠨࡽࢀࠫ໌"))).get(bstack11ll11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪໍ"))
    caps[bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ໎")] = True
    if bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ໏") in caps:
      caps[bstack11ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭໐")][bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭໑")] = bstack11l1ll11l1_opy_
      caps[bstack11ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ໒")][bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ໓")][bstack11ll11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ໔")] = bstack11l1llllll_opy_
    else:
      caps[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ໕")] = bstack11l1ll11l1_opy_
      caps[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ໖")][bstack11ll11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໗")] = bstack11l1llllll_opy_
  except Exception as error:
    logger.debug(bstack11ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ໘") +  str(error))
def bstack1l11ll111_opy_(driver, bstack11l1ll1lll_opy_):
  try:
    setattr(driver, bstack11ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ໙"), True)
    session = driver.session_id
    if session:
      bstack11ll111lll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll111lll_opy_ = False
      bstack11ll111lll_opy_ = url.scheme in [bstack11ll11_opy_ (u"ࠣࡪࡷࡸࡵࠨ໚"), bstack11ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ໛")]
      if bstack11ll111lll_opy_:
        if bstack11l1ll1lll_opy_:
          logger.info(bstack11ll11_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥໜ"))
      return bstack11l1ll1lll_opy_
  except Exception as e:
    logger.error(bstack11ll11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢໝ") + str(e))
    return False
def bstack1l1l111l11_opy_(driver, class_name, name, module_name, path, bstack1llllllll1_opy_):
  try:
    bstack11lll1111l_opy_ = [class_name] if not class_name is None else []
    bstack11ll11111l_opy_ = {
        bstack11ll11_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥໞ"): True,
        bstack11ll11_opy_ (u"ࠨࡴࡦࡵࡷࡈࡪࡺࡡࡪ࡮ࡶࠦໟ"): {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ໠"): name,
            bstack11ll11_opy_ (u"ࠣࡶࡨࡷࡹࡘࡵ࡯ࡋࡧࠦ໡"): os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡘࡊ࡙ࡔࡠࡔࡘࡒࡤࡏࡄࠨ໢")),
            bstack11ll11_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧ໣"): str(path),
            bstack11ll11_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࡏ࡭ࡸࡺࠢ໤"): [module_name, *bstack11lll1111l_opy_, name],
        },
        bstack11ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢ໥"): _11ll11l1ll_opy_(driver, bstack1llllllll1_opy_)
    }
    logger.debug(bstack11ll11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ໦"))
    logger.debug(driver.execute_async_script(bstack1ll1lll1ll_opy_.perform_scan, {bstack11ll11_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢ໧"): name}))
    logger.debug(driver.execute_async_script(bstack1ll1lll1ll_opy_.bstack11ll111l11_opy_, bstack11ll11111l_opy_))
    logger.info(bstack11ll11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦ໨"))
  except Exception as bstack11ll11l1l1_opy_:
    logger.error(bstack11ll11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦ໩") + str(path) + bstack11ll11_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧ໪") + str(bstack11ll11l1l1_opy_))