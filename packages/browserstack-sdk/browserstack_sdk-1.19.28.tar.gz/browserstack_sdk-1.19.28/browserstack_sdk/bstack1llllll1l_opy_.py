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
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll11l1l1_opy_ = {}
        bstack1l11l111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨവ"), bstack11ll11_opy_ (u"ࠨࠩശ"))
        if not bstack1l11l111ll_opy_:
            return bstack1lll11l1l1_opy_
        try:
            bstack1l11l11l11_opy_ = json.loads(bstack1l11l111ll_opy_)
            if bstack11ll11_opy_ (u"ࠤࡲࡷࠧഷ") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠥࡳࡸࠨസ")] = bstack1l11l11l11_opy_[bstack11ll11_opy_ (u"ࠦࡴࡹࠢഹ")]
            if bstack11ll11_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤഺ") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ഻") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰ഼ࠥ")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧഽ"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧാ")))
            if bstack11ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦി") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤീ") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥു")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢൂ"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧൃ")))
            if bstack11ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥൄ") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ൅") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦെ")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨേ"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨൈ")))
            if bstack11ll11_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ൉") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦൊ") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧോ")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤൌ"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫്ࠢ")))
            if bstack11ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨൎ") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ൏") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ൐")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤ൑"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ൒")))
            if bstack11ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ൓") in bstack1l11l11l11_opy_ or bstack11ll11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧൔ") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨൕ")] = bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣൖ"), bstack1l11l11l11_opy_.get(bstack11ll11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣൗ")))
            if bstack11ll11_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤ൘") in bstack1l11l11l11_opy_:
                bstack1lll11l1l1_opy_[bstack11ll11_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥ൙")] = bstack1l11l11l11_opy_[bstack11ll11_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ൚")]
        except Exception as error:
            logger.error(bstack11ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡥࡹࡧ࠺ࠡࠤ൛") +  str(error))
        return bstack1lll11l1l1_opy_