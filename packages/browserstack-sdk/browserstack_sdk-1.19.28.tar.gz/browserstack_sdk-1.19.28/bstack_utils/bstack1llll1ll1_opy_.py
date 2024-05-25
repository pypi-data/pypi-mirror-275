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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11l1lll11l_opy_, bstack11lllll1_opy_, get_host_info, bstack11ll11l11l_opy_, bstack11l1lllll1_opy_, bstack111lll1l1l_opy_, bstack1l11l1111l_opy_, \
    bstack111lll11l1_opy_, bstack111ll1llll_opy_, bstack1l1ll11ll_opy_, bstack111lll11ll_opy_, bstack111l1l1l_opy_, bstack1l1111l11l_opy_, bstack1ll1ll11_opy_, bstack11l11l11l_opy_
from bstack_utils.bstack1llll1l1111_opy_ import bstack1llll1l11ll_opy_
from bstack_utils.bstack11llllll11_opy_ import bstack1l111l1l1l_opy_
import bstack_utils.bstack1ll1l11ll1_opy_ as bstack1l111111l_opy_
from bstack_utils.constants import bstack11l11ll1l1_opy_
bstack1lll1l11l1l_opy_ = [
    bstack11ll11_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᔖ"), bstack11ll11_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ᔗ"), bstack11ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᔘ"), bstack11ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬᔙ"),
    bstack11ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᔚ"), bstack11ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᔛ"), bstack11ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᔜ")
]
bstack1lll11lllll_opy_ = bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡦࡳࡱࡲࡥࡤࡶࡲࡶ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᔝ")
logger = logging.getLogger(__name__)
class bstack1l1l111lll_opy_:
    bstack1llll1l1111_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lll11llll1_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll11ll1l1_opy_()
        bstack11l1lll1l1_opy_ = bstack11ll11l11l_opy_(bs_config)
        bstack11l1ll1ll1_opy_ = bstack11l1lllll1_opy_(bs_config)
        bstack111l11l1_opy_ = False
        bstack1ll111lll1_opy_ = False
        if bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࠭ᔞ") in bs_config:
            bstack111l11l1_opy_ = True
        else:
            bstack1ll111lll1_opy_ = True
        bstack111llll1_opy_ = {
            bstack11ll11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᔟ"): cls.bstack111l111l_opy_(bstack1lll11llll1_opy_.get(bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬᔠ"), bstack11ll11_opy_ (u"ࠬ࠭ᔡ"))),
            bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᔢ"): bstack1l111111l_opy_.bstack11ll11ll1_opy_(bs_config),
            bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᔣ"): bs_config.get(bstack11ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᔤ"), False),
            bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᔥ"): bstack1ll111lll1_opy_,
            bstack11ll11_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩᔦ"): bstack111l11l1_opy_
        }
        data = {
            bstack11ll11_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫᔧ"): bstack11ll11_opy_ (u"ࠬࡰࡳࡰࡰࠪᔨ"),
            bstack11ll11_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬᔩ"): bs_config.get(bstack11ll11_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᔪ"), bstack11ll11_opy_ (u"ࠨࠩᔫ")),
            bstack11ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᔬ"): bs_config.get(bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᔭ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᔮ"): bs_config.get(bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᔯ")),
            bstack11ll11_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫᔰ"): bs_config.get(bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪᔱ"), bstack11ll11_opy_ (u"ࠨࠩᔲ")),
            bstack11ll11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡠࡶ࡬ࡱࡪ࠭ᔳ"): datetime.datetime.now().isoformat(),
            bstack11ll11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᔴ"): bstack111lll1l1l_opy_(bs_config),
            bstack11ll11_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧᔵ"): get_host_info(),
            bstack11ll11_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭ᔶ"): bstack11lllll1_opy_(),
            bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᔷ"): os.environ.get(bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᔸ")),
            bstack11ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭ᔹ"): os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧᔺ"), False),
            bstack11ll11_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬᔻ"): bstack11l1lll11l_opy_(),
            bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩᔼ"): bstack111llll1_opy_,
            bstack11ll11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᔽ"): {
                bstack11ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭ᔾ"): bstack1lll11llll1_opy_.get(bstack11ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨᔿ"), bstack11ll11_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨᕀ")),
                bstack11ll11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᕁ"): bstack1lll11llll1_opy_.get(bstack11ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᕂ")),
                bstack11ll11_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᕃ"): bstack1lll11llll1_opy_.get(bstack11ll11_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪᕄ"))
            }
        }
        config = {
            bstack11ll11_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᕅ"): (bstack11l1lll1l1_opy_, bstack11l1ll1ll1_opy_),
            bstack11ll11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᕆ"): cls.default_headers()
        }
        response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᕇ"), cls.request_url(bstack11ll11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴࠩᕈ")), data, config)
        if response.status_code != 200:
            os.environ[bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᕉ")] = bstack11ll11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᕊ")
            os.environ[bstack11ll11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫᕋ")] = bstack11ll11_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬᕌ")
            os.environ[bstack11ll11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᕍ")] = bstack11ll11_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᕎ")
            os.environ[bstack11ll11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᕏ")] = bstack11ll11_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᕐ")
            os.environ[bstack11ll11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬᕑ")] = bstack11ll11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᕒ")
            bstack1lll1l111ll_opy_ = response.json()
            if bstack1lll1l111ll_opy_ and bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᕓ")]:
                error_message = bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᕔ")]
                if bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࡔࡺࡲࡨࠫᕕ")] == bstack11ll11_opy_ (u"ࠩࡈࡖࡗࡕࡒࡠࡋࡑ࡚ࡆࡒࡉࡅࡡࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙ࠧᕖ"):
                    logger.error(error_message)
                elif bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡖࡼࡴࡪ࠭ᕗ")] == bstack11ll11_opy_ (u"ࠫࡊࡘࡒࡐࡔࡢࡅࡈࡉࡅࡔࡕࡢࡈࡊࡔࡉࡆࡆࠪᕘ"):
                    logger.info(error_message)
                elif bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡘࡾࡶࡥࠨᕙ")] == bstack11ll11_opy_ (u"࠭ࡅࡓࡔࡒࡖࡤ࡙ࡄࡌࡡࡇࡉࡕࡘࡅࡄࡃࡗࡉࡉ࠭ᕚ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll11_opy_ (u"ࠢࡅࡣࡷࡥࠥࡻࡰ࡭ࡱࡤࡨࠥࡺ࡯ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᕛ"))
            return [None, None, None]
        bstack1lll1l111ll_opy_ = response.json()
        os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᕜ")] = bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᕝ")]
        if cls.bstack111l111l_opy_(bstack1lll11llll1_opy_.get(bstack11ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫᕞ"), bstack11ll11_opy_ (u"ࠫࠬᕟ"))) is True:
            logger.debug(bstack11ll11_opy_ (u"࡚ࠬࡥࡴࡶࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩᕠ"))
            os.environ[bstack11ll11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬᕡ")] = bstack11ll11_opy_ (u"ࠧࡵࡴࡸࡩࠬᕢ")
            if bstack1lll1l111ll_opy_.get(bstack11ll11_opy_ (u"ࠨ࡬ࡺࡸࠬᕣ")):
                os.environ[bstack11ll11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᕤ")] = bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠪ࡮ࡼࡺࠧᕥ")]
                os.environ[bstack11ll11_opy_ (u"ࠫࡈࡘࡅࡅࡇࡑࡘࡎࡇࡌࡔࡡࡉࡓࡗࡥࡃࡓࡃࡖࡌࡤࡘࡅࡑࡑࡕࡘࡎࡔࡇࠨᕦ")] = json.dumps({
                    bstack11ll11_opy_ (u"ࠬࡻࡳࡦࡴࡱࡥࡲ࡫ࠧᕧ"): bstack11l1lll1l1_opy_,
                    bstack11ll11_opy_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨᕨ"): bstack11l1ll1ll1_opy_
                })
            if bstack1lll1l111ll_opy_.get(bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᕩ")):
                os.environ[bstack11ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᕪ")] = bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᕫ")]
            if bstack1lll1l111ll_opy_.get(bstack11ll11_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᕬ")):
                os.environ[bstack11ll11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬᕭ")] = str(bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᕮ")])
        return [bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"࠭ࡪࡸࡶࠪᕯ")], bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᕰ")], bstack1lll1l111ll_opy_[bstack11ll11_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᕱ")]]
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def stop(cls, bstack1lll11lll1l_opy_ = None):
        if not cls.on():
            return
        if os.environ[bstack11ll11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᕲ")] == bstack11ll11_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᕳ") or os.environ[bstack11ll11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᕴ")] == bstack11ll11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᕵ"):
            print(bstack11ll11_opy_ (u"࠭ࡅ࡙ࡅࡈࡔ࡙ࡏࡏࡏࠢࡌࡒࠥࡹࡴࡰࡲࡅࡹ࡮ࡲࡤࡖࡲࡶࡸࡷ࡫ࡡ࡮ࠢࡕࡉࡖ࡛ࡅࡔࡖࠣࡘࡔࠦࡔࡆࡕࡗࠤࡔࡈࡓࡆࡔ࡙ࡅࡇࡏࡌࡊࡖ࡜ࠤ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧᕶ"))
            return {
                bstack11ll11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᕷ"): bstack11ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᕸ"),
                bstack11ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᕹ"): bstack11ll11_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨᕺ")
            }
        else:
            cls.bstack1llll1l1111_opy_.shutdown()
            data = {
                bstack11ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᕻ"): bstack11l11l11l_opy_()
            }
            if not bstack1lll11lll1l_opy_ is None:
                data[bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠩᕼ")] = [{
                    bstack11ll11_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᕽ"): bstack11ll11_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬᕾ"),
                    bstack11ll11_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨᕿ"): bstack1lll11lll1l_opy_
                }]
            config = {
                bstack11ll11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᖀ"): cls.default_headers()
            }
            bstack111l1lll1l_opy_ = bstack11ll11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫᖁ").format(os.environ[bstack11ll11_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠥᖂ")])
            bstack1lll1l11l11_opy_ = cls.request_url(bstack111l1lll1l_opy_)
            response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠬࡖࡕࡕࠩᖃ"), bstack1lll1l11l11_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll11_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯ࠧᖄ"))
    @classmethod
    def bstack11lll1l11l_opy_(cls):
        if cls.bstack1llll1l1111_opy_ is None:
            return
        cls.bstack1llll1l1111_opy_.shutdown()
    @classmethod
    def bstack1l11ll11l_opy_(cls):
        if cls.on():
            print(
                bstack11ll11_opy_ (u"ࠧࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠪᖅ").format(os.environ[bstack11ll11_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠢᖆ")]))
    @classmethod
    def bstack1lll11ll1l1_opy_(cls):
        if cls.bstack1llll1l1111_opy_ is not None:
            return
        cls.bstack1llll1l1111_opy_ = bstack1llll1l11ll_opy_(cls.bstack1lll1l11ll1_opy_)
        cls.bstack1llll1l1111_opy_.start()
    @classmethod
    def bstack11llll11ll_opy_(cls, bstack11llll11l1_opy_, bstack1lll1l1l1ll_opy_=bstack11ll11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᖇ")):
        if not cls.on():
            return
        bstack1l1l1l1l_opy_ = bstack11llll11l1_opy_[bstack11ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᖈ")]
        bstack1lll1l11111_opy_ = {
            bstack11ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᖉ"): bstack11ll11_opy_ (u"࡚ࠬࡥࡴࡶࡢࡗࡹࡧࡲࡵࡡࡘࡴࡱࡵࡡࡥࠩᖊ"),
            bstack11ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᖋ"): bstack11ll11_opy_ (u"ࠧࡕࡧࡶࡸࡤࡋ࡮ࡥࡡࡘࡴࡱࡵࡡࡥࠩᖌ"),
            bstack11ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᖍ"): bstack11ll11_opy_ (u"ࠩࡗࡩࡸࡺ࡟ࡔ࡭࡬ࡴࡵ࡫ࡤࡠࡗࡳࡰࡴࡧࡤࠨᖎ"),
            bstack11ll11_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᖏ"): bstack11ll11_opy_ (u"ࠫࡑࡵࡧࡠࡗࡳࡰࡴࡧࡤࠨᖐ"),
            bstack11ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᖑ"): bstack11ll11_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡘࡺࡡࡳࡶࡢ࡙ࡵࡲ࡯ࡢࡦࠪᖒ"),
            bstack11ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᖓ"): bstack11ll11_opy_ (u"ࠨࡊࡲࡳࡰࡥࡅ࡯ࡦࡢ࡙ࡵࡲ࡯ࡢࡦࠪᖔ"),
            bstack11ll11_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ᖕ"): bstack11ll11_opy_ (u"ࠪࡇࡇ࡚࡟ࡖࡲ࡯ࡳࡦࡪࠧᖖ")
        }.get(bstack1l1l1l1l_opy_)
        if bstack1lll1l1l1ll_opy_ == bstack11ll11_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᖗ"):
            cls.bstack1lll11ll1l1_opy_()
            cls.bstack1llll1l1111_opy_.add(bstack11llll11l1_opy_)
        elif bstack1lll1l1l1ll_opy_ == bstack11ll11_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᖘ"):
            cls.bstack1lll1l11ll1_opy_([bstack11llll11l1_opy_], bstack1lll1l1l1ll_opy_)
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def bstack1lll1l11ll1_opy_(cls, bstack11llll11l1_opy_, bstack1lll1l1l1ll_opy_=bstack11ll11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬᖙ")):
        config = {
            bstack11ll11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᖚ"): cls.default_headers()
        }
        response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᖛ"), cls.request_url(bstack1lll1l1l1ll_opy_), bstack11llll11l1_opy_, config)
        bstack11l1llll1l_opy_ = response.json()
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def bstack11111l1l_opy_(cls, bstack11llllll1l_opy_):
        bstack1lll1l1ll11_opy_ = []
        for log in bstack11llllll1l_opy_:
            bstack1lll1l11lll_opy_ = {
                bstack11ll11_opy_ (u"ࠩ࡮࡭ࡳࡪࠧᖜ"): bstack11ll11_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡎࡒࡋࠬᖝ"),
                bstack11ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᖞ"): log[bstack11ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᖟ")],
                bstack11ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᖠ"): log[bstack11ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᖡ")],
                bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡥࡲࡦࡵࡳࡳࡳࡹࡥࠨᖢ"): {},
                bstack11ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᖣ"): log[bstack11ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᖤ")],
            }
            if bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖥ") in log:
                bstack1lll1l11lll_opy_[bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖦ")] = log[bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖧ")]
            elif bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖨ") in log:
                bstack1lll1l11lll_opy_[bstack11ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᖩ")] = log[bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖪ")]
            bstack1lll1l1ll11_opy_.append(bstack1lll1l11lll_opy_)
        cls.bstack11llll11ll_opy_({
            bstack11ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᖫ"): bstack11ll11_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨᖬ"),
            bstack11ll11_opy_ (u"ࠬࡲ࡯ࡨࡵࠪᖭ"): bstack1lll1l1ll11_opy_
        })
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def bstack1lll1l1l1l1_opy_(cls, steps):
        bstack1lll1l1l11l_opy_ = []
        for step in steps:
            bstack1lll11lll11_opy_ = {
                bstack11ll11_opy_ (u"࠭࡫ࡪࡰࡧࠫᖮ"): bstack11ll11_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡔࡆࡒࠪᖯ"),
                bstack11ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᖰ"): step[bstack11ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᖱ")],
                bstack11ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᖲ"): step[bstack11ll11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᖳ")],
                bstack11ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᖴ"): step[bstack11ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᖵ")],
                bstack11ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩᖶ"): step[bstack11ll11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪᖷ")]
            }
            if bstack11ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖸ") in step:
                bstack1lll11lll11_opy_[bstack11ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖹ")] = step[bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖺ")]
            elif bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖻ") in step:
                bstack1lll11lll11_opy_[bstack11ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖼ")] = step[bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖽ")]
            bstack1lll1l1l11l_opy_.append(bstack1lll11lll11_opy_)
        cls.bstack11llll11ll_opy_({
            bstack11ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᖾ"): bstack11ll11_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᖿ"),
            bstack11ll11_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᗀ"): bstack1lll1l1l11l_opy_
        })
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def bstack1l1ll1ll11_opy_(cls, screenshot):
        cls.bstack11llll11ll_opy_({
            bstack11ll11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᗁ"): bstack11ll11_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᗂ"),
            bstack11ll11_opy_ (u"࠭࡬ࡰࡩࡶࠫᗃ"): [{
                bstack11ll11_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᗄ"): bstack11ll11_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠪᗅ"),
                bstack11ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᗆ"): bstack1l11l1111l_opy_().isoformat() + bstack11ll11_opy_ (u"ࠪ࡞ࠬᗇ"),
                bstack11ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᗈ"): screenshot[bstack11ll11_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫᗉ")],
                bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᗊ"): screenshot[bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᗋ")]
            }]
        }, bstack1lll1l1l1ll_opy_=bstack11ll11_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᗌ"))
    @classmethod
    @bstack1l1111l11l_opy_(class_method=True)
    def bstack1l1lll1l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11llll11ll_opy_({
            bstack11ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᗍ"): bstack11ll11_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧᗎ"),
            bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᗏ"): {
                bstack11ll11_opy_ (u"ࠧࡻࡵࡪࡦࠥᗐ"): cls.current_test_uuid(),
                bstack11ll11_opy_ (u"ࠨࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠧᗑ"): cls.bstack1l111l111l_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack11ll11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᗒ"), None) is None or os.environ[bstack11ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᗓ")] == bstack11ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢᗔ"):
            return False
        return True
    @classmethod
    def bstack111l111l_opy_(cls, framework=bstack11ll11_opy_ (u"ࠥࠦᗕ")):
        if framework not in bstack11l11ll1l1_opy_:
            return False
        bstack1lll1l1l111_opy_ = not bstack1ll1ll11_opy_()
        return bstack111l1l1l_opy_(cls.bs_config.get(bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᗖ"), bstack1lll1l1l111_opy_))
    @staticmethod
    def request_url(url):
        return bstack11ll11_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫᗗ").format(bstack1lll11lllll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᗘ"): bstack11ll11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᗙ"),
            bstack11ll11_opy_ (u"ࠨ࡚࠰ࡆࡘ࡚ࡁࡄࡍ࠰ࡘࡊ࡙ࡔࡐࡒࡖࠫᗚ"): bstack11ll11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᗛ")
        }
        if os.environ.get(bstack11ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᗜ"), None):
            headers[bstack11ll11_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᗝ")] = bstack11ll11_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᗞ").format(os.environ[bstack11ll11_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠢᗟ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᗠ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᗡ"), None)
    @staticmethod
    def bstack11llll1ll1_opy_():
        if getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᗢ"), None):
            return {
                bstack11ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨᗣ"): bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᗤ"),
                bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᗥ"): getattr(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᗦ"), None)
            }
        if getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᗧ"), None):
            return {
                bstack11ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᗨ"): bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᗩ"),
                bstack11ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᗪ"): getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᗫ"), None)
            }
        return None
    @staticmethod
    def bstack1l111l111l_opy_(driver):
        return {
            bstack111ll1llll_opy_(): bstack111lll11l1_opy_(driver)
        }
    @staticmethod
    def bstack1lll11ll1ll_opy_(exception_info, report):
        return [{bstack11ll11_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᗬ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll1l111l_opy_(typename):
        if bstack11ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᗭ") in typename:
            return bstack11ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᗮ")
        return bstack11ll11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᗯ")
    @staticmethod
    def bstack1lll1l111l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l111lll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11lllll1ll_opy_(test, hook_name=None):
        bstack1lll1l1ll1l_opy_ = test.parent
        if hook_name in [bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᗰ"), bstack11ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᗱ"), bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᗲ"), bstack11ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᗳ")]:
            bstack1lll1l1ll1l_opy_ = test
        scope = []
        while bstack1lll1l1ll1l_opy_ is not None:
            scope.append(bstack1lll1l1ll1l_opy_.name)
            bstack1lll1l1ll1l_opy_ = bstack1lll1l1ll1l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lll1l1111l_opy_(hook_type):
        if hook_type == bstack11ll11_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᗴ"):
            return bstack11ll11_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᗵ")
        elif hook_type == bstack11ll11_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᗶ"):
            return bstack11ll11_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᗷ")
    @staticmethod
    def bstack1lll11ll11l_opy_(bstack1l1l1111l_opy_):
        try:
            if not bstack1l1l111lll_opy_.on():
                return bstack1l1l1111l_opy_
            if os.environ.get(bstack11ll11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᗸ"), None) == bstack11ll11_opy_ (u"ࠦࡹࡸࡵࡦࠤᗹ"):
                tests = os.environ.get(bstack11ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᗺ"), None)
                if tests is None or tests == bstack11ll11_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᗻ"):
                    return bstack1l1l1111l_opy_
                bstack1l1l1111l_opy_ = tests.split(bstack11ll11_opy_ (u"ࠧ࠭ࠩᗼ"))
                return bstack1l1l1111l_opy_
        except Exception as exc:
            print(bstack11ll11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᗽ"), str(exc))
        return bstack1l1l1111l_opy_
    @classmethod
    def bstack1l1111llll_opy_(cls, event: str, bstack11llll11l1_opy_: bstack1l111l1l1l_opy_):
        bstack11lll1lll1_opy_ = {
            bstack11ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᗾ"): event,
            bstack11llll11l1_opy_.bstack1l111lll1l_opy_(): bstack11llll11l1_opy_.bstack1l1111l1ll_opy_(event)
        }
        bstack1l1l111lll_opy_.bstack11llll11ll_opy_(bstack11lll1lll1_opy_)