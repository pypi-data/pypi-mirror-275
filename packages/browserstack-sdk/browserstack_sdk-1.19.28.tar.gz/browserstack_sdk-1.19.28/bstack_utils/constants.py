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
import re
bstack1l11l11ll1_opy_ = {
	bstack11ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ་"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷ࠭༌"),
  bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭།"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡯ࡪࡿࠧ༎"),
  bstack11ll11_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ༏"): bstack11ll11_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ༐"),
  bstack11ll11_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ༑"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨ༒"),
  bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ༓"): bstack11ll11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࠫ༔"),
  bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ༕"): bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫ༖"),
  bstack11ll11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ༗"): bstack11ll11_opy_ (u"ࠧ࡯ࡣࡰࡩ༘ࠬ"),
  bstack11ll11_opy_ (u"ࠨࡦࡨࡦࡺ࡭༙ࠧ"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭ࠧ༚"),
  bstack11ll11_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨ༛"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡳࡰ࡮ࡨࠫ༜"),
  bstack11ll11_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪ༝"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪ༞"),
  bstack11ll11_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫ༟"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫ༠"),
  bstack11ll11_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨ༡"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡹ࡭ࡩ࡫࡯ࠨ༢"),
  bstack11ll11_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪ༣"): bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪ༤"),
  bstack11ll11_opy_ (u"࠭ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭༥"): bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭༦"),
  bstack11ll11_opy_ (u"ࠨࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭༧"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭༨"),
  bstack11ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡻࡱࡱࡩࠬ༩"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸ࡮ࡳࡥࡻࡱࡱࡩࠬ༪"),
  bstack11ll11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ༫"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ༬"),
  bstack11ll11_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭༭"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭༮"),
  bstack11ll11_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ༯"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ༰"),
  bstack11ll11_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫ༱"): bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫ༲"),
  bstack11ll11_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨ༳"): bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦࡰࡧࡏࡪࡿࡳࠨ༴"),
  bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡡࡪࡶ༵ࠪ"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴ࡝ࡡࡪࡶࠪ༶"),
  bstack11ll11_opy_ (u"ࠪ࡬ࡴࡹࡴࡴ༷ࠩ"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡬ࡴࡹࡴࡴࠩ༸"),
  bstack11ll11_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ༹࠭"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡦࡤࡣࡦ࡬ࡪ࠭༺"),
  bstack11ll11_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨ༻"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨ༼"),
  bstack11ll11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬ༽"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬ༾"),
  bstack11ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ༿"): bstack11ll11_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬཀ"),
  bstack11ll11_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪཁ"): bstack11ll11_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬག"),
  bstack11ll11_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨགྷ"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩང"),
  bstack11ll11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪཅ"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪཆ"),
  bstack11ll11_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ཇ"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭཈"),
  bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ཉ"): bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩཊ"),
  bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫཋ"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫཌ"),
  bstack11ll11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫཌྷ"): bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸࡵࡵࡳࡥࡨࠫཎ"),
  bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨཏ"): bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨཐ"),
  bstack11ll11_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪད"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡔࡡ࡮ࡧࠪདྷ"),
  bstack11ll11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ན"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭པ"),
  bstack11ll11_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩཕ"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩབ"),
  bstack11ll11_opy_ (u"ࠧࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬབྷ"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬམ")
}
bstack11l11ll11l_opy_ = [
  bstack11ll11_opy_ (u"ࠩࡲࡷࠬཙ"),
  bstack11ll11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ཚ"),
  bstack11ll11_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ཛ"),
  bstack11ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪཛྷ"),
  bstack11ll11_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪཝ"),
  bstack11ll11_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫཞ"),
  bstack11ll11_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨཟ"),
]
bstack1l11l1ll_opy_ = {
  bstack11ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫའ"): [bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫཡ"), bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡐࡄࡑࡊ࠭ར")],
  bstack11ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨལ"): bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩཤ"),
  bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪཥ"): bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠫས"),
  bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧཧ"): bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠨཨ"),
  bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ཀྵ"): bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧཪ"),
  bstack11ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ཫ"): bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡔࡡࡓࡉࡗࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨཬ"),
  bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ཭"): bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒࠧ཮"),
  bstack11ll11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧ཯"): bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨ཰"),
  bstack11ll11_opy_ (u"ࠬࡧࡰࡱཱࠩ"): [bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡐࡑࡡࡌࡈིࠬ"), bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡑࡒཱིࠪ")],
  bstack11ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ུࠪ"): bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡕࡇࡏࡤࡒࡏࡈࡎࡈ࡚ࡊࡒཱུࠧ"),
  bstack11ll11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧྲྀ"): bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧཷ"),
  bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩླྀ"): bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡓࡇ࡙ࡅࡓࡘࡄࡆࡎࡒࡉࡕ࡛ࠪཹ")
}
bstack1ll1llll11_opy_ = {
  bstack11ll11_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦེࠩ"): [bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡶࡤࡴࡡ࡮ࡧཻࠪ"), bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷࡔࡡ࡮ࡧོࠪ")],
  bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾཽ࠭"): [bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵࡢ࡯ࡪࡿࠧཾ"), bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧཿ")],
  bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦྀࠩ"): bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦཱྀࠩ"),
  bstack11ll11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ྂ"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ྃ"),
  bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ྄ࠬ"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ྅"),
  bstack11ll11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ྆"): [bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡶࡰࡱࠩ྇"), bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ྈ")],
  bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬྉ"): bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧྊ"),
  bstack11ll11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧྋ"): bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧྌ"),
  bstack11ll11_opy_ (u"ࠬࡧࡰࡱࠩྍ"): bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱࠩྎ"),
  bstack11ll11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩྏ"): bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩྐ"),
  bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ྑ"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ྒ")
}
bstack111l11ll1_opy_ = {
  bstack11ll11_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧྒྷ"): bstack11ll11_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩྔ"),
  bstack11ll11_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨྕ"): [bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩྖ"), bstack11ll11_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫྗ")],
  bstack11ll11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ྘"): bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨྙ"),
  bstack11ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨྚ"): bstack11ll11_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬྛ"),
  bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫྜ"): [bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨྜྷ"), bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧྞ")],
  bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪྟ"): bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬྠ"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨྡ"): bstack11ll11_opy_ (u"ࠬࡸࡥࡢ࡮ࡢࡱࡴࡨࡩ࡭ࡧࠪྡྷ"),
  bstack11ll11_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ྣ"): [bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧྤ"), bstack11ll11_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩྥ")],
  bstack11ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨྦ"): [bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࡶࠫྦྷ"), bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࠫྨ")]
}
bstack1lll1l1ll1_opy_ = [
  bstack11ll11_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫྩ"),
  bstack11ll11_opy_ (u"࠭ࡰࡢࡩࡨࡐࡴࡧࡤࡔࡶࡵࡥࡹ࡫ࡧࡺࠩྪ"),
  bstack11ll11_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ྫ"),
  bstack11ll11_opy_ (u"ࠨࡵࡨࡸ࡜࡯࡮ࡥࡱࡺࡖࡪࡩࡴࠨྫྷ"),
  bstack11ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫࡯ࡶࡶࡶࠫྭ"),
  bstack11ll11_opy_ (u"ࠪࡷࡹࡸࡩࡤࡶࡉ࡭ࡱ࡫ࡉ࡯ࡶࡨࡶࡦࡩࡴࡢࡤ࡬ࡰ࡮ࡺࡹࠨྮ"),
  bstack11ll11_opy_ (u"ࠫࡺࡴࡨࡢࡰࡧࡰࡪࡪࡐࡳࡱࡰࡴࡹࡈࡥࡩࡣࡹ࡭ࡴࡸࠧྯ"),
  bstack11ll11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪྰ"),
  bstack11ll11_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫྱ"),
  bstack11ll11_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨྲ"),
  bstack11ll11_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧླ"),
  bstack11ll11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪྴ"),
]
bstack11ll1ll1_opy_ = [
  bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧྵ"),
  bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨྶ"),
  bstack11ll11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫྷ"),
  bstack11ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ྸ"),
  bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྐྵ"),
  bstack11ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪྺ"),
  bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬྻ"),
  bstack11ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧྼ"),
  bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ྽"),
  bstack11ll11_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ྾"),
  bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ྿"),
  bstack11ll11_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩ࿀"),
  bstack11ll11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡕࡣࡪࠫ࿁"),
  bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭࿂"),
  bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ࿃"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨ࿄"),
  bstack11ll11_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠴ࠫ࿅"),
  bstack11ll11_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠶࿆ࠬ"),
  bstack11ll11_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠸࠭࿇"),
  bstack11ll11_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠺ࠧ࿈"),
  bstack11ll11_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠵ࠨ࿉"),
  bstack11ll11_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠷ࠩ࿊"),
  bstack11ll11_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠹ࠪ࿋"),
  bstack11ll11_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠻ࠫ࿌"),
  bstack11ll11_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠽ࠬ࿍"),
  bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭࿎"),
  bstack11ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ࿏"),
  bstack11ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬ࿐"),
  bstack11ll11_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬ࿑")
]
bstack11l11lllll_opy_ = [
  bstack11ll11_opy_ (u"ࠫࡺࡶ࡬ࡰࡣࡧࡑࡪࡪࡩࡢࠩ࿒"),
  bstack11ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ࿓"),
  bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ࿔"),
  bstack11ll11_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ࿕"),
  bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡖࡲࡪࡱࡵ࡭ࡹࡿࠧ࿖"),
  bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ࿗"),
  bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡖࡤ࡫ࠬ࿘"),
  bstack11ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ࿙"),
  bstack11ll11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ࿚"),
  bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ࿛"),
  bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ࿜"),
  bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ࿝"),
  bstack11ll11_opy_ (u"ࠩࡲࡷࠬ࿞"),
  bstack11ll11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭࿟"),
  bstack11ll11_opy_ (u"ࠫ࡭ࡵࡳࡵࡵࠪ࿠"),
  bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡥ࡮ࡺࠧ࿡"),
  bstack11ll11_opy_ (u"࠭ࡲࡦࡩ࡬ࡳࡳ࠭࿢"),
  bstack11ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩ࿣"),
  bstack11ll11_opy_ (u"ࠨ࡯ࡤࡧ࡭࡯࡮ࡦࠩ࿤"),
  bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡵ࡬ࡶࡶ࡬ࡳࡳ࠭࿥"),
  bstack11ll11_opy_ (u"ࠪ࡭ࡩࡲࡥࡕ࡫ࡰࡩࡴࡻࡴࠨ࿦"),
  bstack11ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡓࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨ࿧"),
  bstack11ll11_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫ࿨"),
  bstack11ll11_opy_ (u"࠭࡮ࡰࡒࡤ࡫ࡪࡒ࡯ࡢࡦࡗ࡭ࡲ࡫࡯ࡶࡶࠪ࿩"),
  bstack11ll11_opy_ (u"ࠧࡣࡨࡦࡥࡨ࡮ࡥࠨ࿪"),
  bstack11ll11_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧ࿫"),
  bstack11ll11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭࿬"),
  bstack11ll11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡩࡳࡪࡋࡦࡻࡶࠫ࿭"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨ࿮"),
  bstack11ll11_opy_ (u"ࠬࡴ࡯ࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠩ࿯"),
  bstack11ll11_opy_ (u"࠭ࡣࡩࡧࡦ࡯࡚ࡘࡌࠨ࿰"),
  bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࿱"),
  bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡄࡱࡲ࡯࡮࡫ࡳࠨ࿲"),
  bstack11ll11_opy_ (u"ࠩࡦࡥࡵࡺࡵࡳࡧࡆࡶࡦࡹࡨࠨ࿳"),
  bstack11ll11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧ࿴"),
  bstack11ll11_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ࿵"),
  bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡘࡨࡶࡸ࡯࡯࡯ࠩ࿶"),
  bstack11ll11_opy_ (u"࠭࡮ࡰࡄ࡯ࡥࡳࡱࡐࡰ࡮࡯࡭ࡳ࡭ࠧ࿷"),
  bstack11ll11_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡘ࡫࡮ࡥࡍࡨࡽࡸ࠭࿸"),
  bstack11ll11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡍࡱࡪࡷࠬ࿹"),
  bstack11ll11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡋࡧࠫ࿺"),
  bstack11ll11_opy_ (u"ࠪࡨࡪࡪࡩࡤࡣࡷࡩࡩࡊࡥࡷ࡫ࡦࡩࠬ࿻"),
  bstack11ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡔࡦࡸࡡ࡮ࡵࠪ࿼"),
  bstack11ll11_opy_ (u"ࠬࡶࡨࡰࡰࡨࡒࡺࡳࡢࡦࡴࠪ࿽"),
  bstack11ll11_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࠫ࿾"),
  bstack11ll11_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡔࡶࡴࡪࡱࡱࡷࠬ࿿"),
  bstack11ll11_opy_ (u"ࠨࡥࡲࡲࡸࡵ࡬ࡦࡎࡲ࡫ࡸ࠭က"),
  bstack11ll11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩခ"),
  bstack11ll11_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧဂ"),
  bstack11ll11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡆ࡮ࡵ࡭ࡦࡶࡵ࡭ࡨ࠭ဃ"),
  bstack11ll11_opy_ (u"ࠬࡼࡩࡥࡧࡲ࡚࠷࠭င"),
  bstack11ll11_opy_ (u"࠭࡭ࡪࡦࡖࡩࡸࡹࡩࡰࡰࡌࡲࡸࡺࡡ࡭࡮ࡄࡴࡵࡹࠧစ"),
  bstack11ll11_opy_ (u"ࠧࡦࡵࡳࡶࡪࡹࡳࡰࡕࡨࡶࡻ࡫ࡲࠨဆ"),
  bstack11ll11_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧဇ"),
  bstack11ll11_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࡇࡩࡶࠧဈ"),
  bstack11ll11_opy_ (u"ࠪࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪဉ"),
  bstack11ll11_opy_ (u"ࠫࡸࡿ࡮ࡤࡖ࡬ࡱࡪ࡝ࡩࡵࡪࡑࡘࡕ࠭ည"),
  bstack11ll11_opy_ (u"ࠬ࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪဋ"),
  bstack11ll11_opy_ (u"࠭ࡧࡱࡵࡏࡳࡨࡧࡴࡪࡱࡱࠫဌ"),
  bstack11ll11_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡑࡴࡲࡪ࡮ࡲࡥࠨဍ"),
  bstack11ll11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡏࡧࡷࡻࡴࡸ࡫ࠨဎ"),
  bstack11ll11_opy_ (u"ࠩࡩࡳࡷࡩࡥࡄࡪࡤࡲ࡬࡫ࡊࡢࡴࠪဏ"),
  bstack11ll11_opy_ (u"ࠪࡼࡲࡹࡊࡢࡴࠪတ"),
  bstack11ll11_opy_ (u"ࠫࡽࡳࡸࡋࡣࡵࠫထ"),
  bstack11ll11_opy_ (u"ࠬࡳࡡࡴ࡭ࡆࡳࡲࡳࡡ࡯ࡦࡶࠫဒ"),
  bstack11ll11_opy_ (u"࠭࡭ࡢࡵ࡮ࡆࡦࡹࡩࡤࡃࡸࡸ࡭࠭ဓ"),
  bstack11ll11_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨန"),
  bstack11ll11_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫပ"),
  bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ဖ"),
  bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩဗ"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫ࡳࡪࡩࡱࡅࡵࡶࠧဘ"),
  bstack11ll11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇ࡮ࡪ࡯ࡤࡸ࡮ࡵ࡮ࡴࠩမ"),
  bstack11ll11_opy_ (u"࠭ࡣࡢࡰࡤࡶࡾ࠭ယ"),
  bstack11ll11_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨရ"),
  bstack11ll11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨလ"),
  bstack11ll11_opy_ (u"ࠩ࡬ࡩࠬဝ"),
  bstack11ll11_opy_ (u"ࠪࡩࡩ࡭ࡥࠨသ"),
  bstack11ll11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫဟ"),
  bstack11ll11_opy_ (u"ࠬࡷࡵࡦࡷࡨࠫဠ"),
  bstack11ll11_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨအ"),
  bstack11ll11_opy_ (u"ࠧࡢࡲࡳࡗࡹࡵࡲࡦࡅࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠨဢ"),
  bstack11ll11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡄࡣࡰࡩࡷࡧࡉ࡮ࡣࡪࡩࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧဣ"),
  bstack11ll11_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡅࡹࡥ࡯ࡹࡩ࡫ࡈࡰࡵࡷࡷࠬဤ"),
  bstack11ll11_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࡊࡰࡦࡰࡺࡪࡥࡉࡱࡶࡸࡸ࠭ဥ"),
  bstack11ll11_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡅࡵࡶࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨဦ"),
  bstack11ll11_opy_ (u"ࠬࡸࡥࡴࡧࡵࡺࡪࡊࡥࡷ࡫ࡦࡩࠬဧ"),
  bstack11ll11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ဨ"),
  bstack11ll11_opy_ (u"ࠧࡴࡧࡱࡨࡐ࡫ࡹࡴࠩဩ"),
  bstack11ll11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡑࡣࡶࡷࡨࡵࡤࡦࠩဪ"),
  bstack11ll11_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡋࡲࡷࡉ࡫ࡶࡪࡥࡨࡗࡪࡺࡴࡪࡰࡪࡷࠬါ"),
  bstack11ll11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡄࡹࡩ࡯࡯ࡊࡰ࡭ࡩࡨࡺࡩࡰࡰࠪာ"),
  bstack11ll11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡵࡶ࡬ࡦࡒࡤࡽࠬိ"),
  bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ီ"),
  bstack11ll11_opy_ (u"࠭ࡷࡥ࡫ࡲࡗࡪࡸࡶࡪࡥࡨࠫု"),
  bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩူ"),
  bstack11ll11_opy_ (u"ࠨࡲࡵࡩࡻ࡫࡮ࡵࡅࡵࡳࡸࡹࡓࡪࡶࡨࡘࡷࡧࡣ࡬࡫ࡱ࡫ࠬေ"),
  bstack11ll11_opy_ (u"ࠩ࡫࡭࡬࡮ࡃࡰࡰࡷࡶࡦࡹࡴࠨဲ"),
  bstack11ll11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡓࡶࡪ࡬ࡥࡳࡧࡱࡧࡪࡹࠧဳ"),
  bstack11ll11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡗ࡮ࡳࠧဴ"),
  bstack11ll11_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩဵ"),
  bstack11ll11_opy_ (u"࠭ࡲࡦ࡯ࡲࡺࡪࡏࡏࡔࡃࡳࡴࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࡒ࡯ࡤࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫံ"),
  bstack11ll11_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦ့ࠩ"),
  bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪး"),
  bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ္ࠫ"),
  bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦ်ࠩ"),
  bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ျ"),
  bstack11ll11_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨြ"),
  bstack11ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬွ"),
  bstack11ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡴࡻࡴࡴࠩှ"),
  bstack11ll11_opy_ (u"ࠨࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡔࡷࡵ࡭ࡱࡶࡅࡩ࡭ࡧࡶࡪࡱࡵࠫဿ")
]
bstack1l11ll1l1l_opy_ = {
  bstack11ll11_opy_ (u"ࠩࡹࠫ၀"): bstack11ll11_opy_ (u"ࠪࡺࠬ၁"),
  bstack11ll11_opy_ (u"ࠫ࡫࠭၂"): bstack11ll11_opy_ (u"ࠬ࡬ࠧ၃"),
  bstack11ll11_opy_ (u"࠭ࡦࡰࡴࡦࡩࠬ၄"): bstack11ll11_opy_ (u"ࠧࡧࡱࡵࡧࡪ࠭၅"),
  bstack11ll11_opy_ (u"ࠨࡱࡱࡰࡾࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ၆"): bstack11ll11_opy_ (u"ࠩࡲࡲࡱࡿࡁࡶࡶࡲࡱࡦࡺࡥࠨ၇"),
  bstack11ll11_opy_ (u"ࠪࡪࡴࡸࡣࡦ࡮ࡲࡧࡦࡲࠧ၈"): bstack11ll11_opy_ (u"ࠫ࡫ࡵࡲࡤࡧ࡯ࡳࡨࡧ࡬ࠨ၉"),
  bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡬ࡴࡹࡴࠨ၊"): bstack11ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩ။"),
  bstack11ll11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡶ࡯ࡳࡶࠪ၌"): bstack11ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫ၍"),
  bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬ၎"): bstack11ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭၏"),
  bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡥࡸࡹࠧၐ"): bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨၑ"),
  bstack11ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻ࡫ࡳࡸࡺࠧၒ"): bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡌࡴࡹࡴࠨၓ"),
  bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡵࡲࡵࠩၔ"): bstack11ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖ࡯ࡳࡶࠪၕ"),
  bstack11ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫၖ"): bstack11ll11_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ၗ"),
  bstack11ll11_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻࡸࡷࡪࡸࠧၘ"): bstack11ll11_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨၙ"),
  bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨၚ"): bstack11ll11_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪၛ"),
  bstack11ll11_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫၜ"): bstack11ll11_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬၝ"),
  bstack11ll11_opy_ (u"ࠫࡧ࡯࡮ࡢࡴࡼࡴࡦࡺࡨࠨၞ"): bstack11ll11_opy_ (u"ࠬࡨࡩ࡯ࡣࡵࡽࡵࡧࡴࡩࠩၟ"),
  bstack11ll11_opy_ (u"࠭ࡰࡢࡥࡩ࡭ࡱ࡫ࠧၠ"): bstack11ll11_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪၡ"),
  bstack11ll11_opy_ (u"ࠨࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪၢ"): bstack11ll11_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬၣ"),
  bstack11ll11_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭ၤ"): bstack11ll11_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧၥ"),
  bstack11ll11_opy_ (u"ࠬࡲ࡯ࡨࡨ࡬ࡰࡪ࠭ၦ"): bstack11ll11_opy_ (u"࠭࡬ࡰࡩࡩ࡭ࡱ࡫ࠧၧ"),
  bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၨ"): bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၩ"),
}
bstack11l1l1111l_opy_ = bstack11ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲࡫࡮ࡺࡨࡶࡤ࠱ࡧࡴࡳ࠯ࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫࠲ࡶࡪࡲࡥࡢࡵࡨࡷ࠴ࡲࡡࡵࡧࡶࡸ࠴ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢၪ")
bstack11l1l11111_opy_ = bstack11ll11_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠲࡬ࡪࡧ࡬ࡵࡪࡦ࡬ࡪࡩ࡫ࠣၫ")
bstack11l11ll1l_opy_ = bstack11ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡽࡤ࠰ࡪࡸࡦࠬၬ")
bstack1l1ll111l1_opy_ = bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠨၭ")
bstack1ll1111l_opy_ = bstack11ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯࡯ࡧࡻࡸࡤ࡮ࡵࡣࡵࠪၮ")
bstack11l1l11l11_opy_ = {
  bstack11ll11_opy_ (u"ࠧࡤࡴ࡬ࡸ࡮ࡩࡡ࡭ࠩၯ"): 50,
  bstack11ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧၰ"): 40,
  bstack11ll11_opy_ (u"ࠩࡺࡥࡷࡴࡩ࡯ࡩࠪၱ"): 30,
  bstack11ll11_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨၲ"): 20,
  bstack11ll11_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪၳ"): 10
}
bstack11ll1lll_opy_ = bstack11l1l11l11_opy_[bstack11ll11_opy_ (u"ࠬ࡯࡮ࡧࡱࠪၴ")]
bstack1ll1lllll_opy_ = bstack11ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬၵ")
bstack1ll1l11l11_opy_ = bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬၶ")
bstack11llll11l_opy_ = bstack11ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧၷ")
bstack1l1l11lll1_opy_ = bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨၸ")
bstack1lllll11ll_opy_ = bstack11ll11_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷࠤࡦࡴࡤࠡࡲࡼࡸࡪࡹࡴ࠮ࡵࡨࡰࡪࡴࡩࡶ࡯ࠣࡴࡦࡩ࡫ࡢࡩࡨࡷ࠳ࠦࡠࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸࠥࡶࡹࡵࡧࡶࡸ࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡠࠨၹ")
bstack11l11lll1l_opy_ = [bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬၺ"), bstack11ll11_opy_ (u"ࠬ࡟ࡏࡖࡔࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬၻ")]
bstack11l11lll11_opy_ = [bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩၼ"), bstack11ll11_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩၽ")]
bstack1l1l11l11_opy_ = re.compile(bstack11ll11_opy_ (u"ࠨࡠ࡞ࡠࡡࡽ࠭࡞࠭࠽࠲࠯ࠪࠧၾ"))
bstack111111l1l_opy_ = [
  bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡔࡡ࡮ࡧࠪၿ"),
  bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬႀ"),
  bstack11ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨႁ"),
  bstack11ll11_opy_ (u"ࠬࡴࡥࡸࡅࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࠩႂ"),
  bstack11ll11_opy_ (u"࠭ࡡࡱࡲࠪႃ"),
  bstack11ll11_opy_ (u"ࠧࡶࡦ࡬ࡨࠬႄ"),
  bstack11ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪႅ"),
  bstack11ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࠩႆ"),
  bstack11ll11_opy_ (u"ࠪࡳࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨႇ"),
  bstack11ll11_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࠩႈ"),
  bstack11ll11_opy_ (u"ࠬࡴ࡯ࡓࡧࡶࡩࡹ࠭ႉ"), bstack11ll11_opy_ (u"࠭ࡦࡶ࡮࡯ࡖࡪࡹࡥࡵࠩႊ"),
  bstack11ll11_opy_ (u"ࠧࡤ࡮ࡨࡥࡷ࡙ࡹࡴࡶࡨࡱࡋ࡯࡬ࡦࡵࠪႋ"),
  bstack11ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺࡔࡪ࡯࡬ࡲ࡬ࡹࠧႌ"),
  bstack11ll11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࡒ࡯ࡨࡩ࡬ࡲ࡬ႍ࠭"),
  bstack11ll11_opy_ (u"ࠪࡳࡹ࡮ࡥࡳࡃࡳࡴࡸ࠭ႎ"),
  bstack11ll11_opy_ (u"ࠫࡵࡸࡩ࡯ࡶࡓࡥ࡬࡫ࡓࡰࡷࡵࡧࡪࡕ࡮ࡇ࡫ࡱࡨࡋࡧࡩ࡭ࡷࡵࡩࠬႏ"),
  bstack11ll11_opy_ (u"ࠬࡧࡰࡱࡃࡦࡸ࡮ࡼࡩࡵࡻࠪ႐"), bstack11ll11_opy_ (u"࠭ࡡࡱࡲࡓࡥࡨࡱࡡࡨࡧࠪ႑"), bstack11ll11_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩ႒"), bstack11ll11_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡒࡤࡧࡰࡧࡧࡦࠩ႓"), bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡇࡹࡷࡧࡴࡪࡱࡱࠫ႔"),
  bstack11ll11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ႕"),
  bstack11ll11_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡩࡸࡺࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨ႖"),
  bstack11ll11_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࠧ႗"), bstack11ll11_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࡆࡰࡧࡍࡳࡺࡥ࡯ࡶࠪ႘"),
  bstack11ll11_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬ႙"),
  bstack11ll11_opy_ (u"ࠨࡣࡧࡦࡕࡵࡲࡵࠩႚ"),
  bstack11ll11_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡕࡲࡧࡰ࡫ࡴࠨႛ"),
  bstack11ll11_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡘ࡮ࡳࡥࡰࡷࡷࠫႜ"),
  bstack11ll11_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡴࡩࠩႝ"),
  bstack11ll11_opy_ (u"ࠬࡧࡶࡥࠩ႞"), bstack11ll11_opy_ (u"࠭ࡡࡷࡦࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩ႟"), bstack11ll11_opy_ (u"ࠧࡢࡸࡧࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩႠ"), bstack11ll11_opy_ (u"ࠨࡣࡹࡨࡆࡸࡧࡴࠩႡ"),
  bstack11ll11_opy_ (u"ࠩࡸࡷࡪࡑࡥࡺࡵࡷࡳࡷ࡫ࠧႢ"), bstack11ll11_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡴࡩࠩႣ"), bstack11ll11_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡴࡵࡺࡳࡷࡪࠧႤ"),
  bstack11ll11_opy_ (u"ࠬࡱࡥࡺࡃ࡯࡭ࡦࡹࠧႥ"), bstack11ll11_opy_ (u"࠭࡫ࡦࡻࡓࡥࡸࡹࡷࡰࡴࡧࠫႦ"),
  bstack11ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩႧ"), bstack11ll11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡁࡳࡩࡶࠫႨ"), bstack11ll11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࡈ࡮ࡸࠧႩ"), bstack11ll11_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡅ࡫ࡶࡴࡳࡥࡎࡣࡳࡴ࡮ࡴࡧࡇ࡫࡯ࡩࠬႪ"), bstack11ll11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡘࡷࡪ࡙ࡹࡴࡶࡨࡱࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨႫ"),
  bstack11ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࠨႬ"), bstack11ll11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࡵࠪႭ"),
  bstack11ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡊࡩࡴࡣࡥࡰࡪࡈࡵࡪ࡮ࡧࡇ࡭࡫ࡣ࡬ࠩႮ"),
  bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࡚ࡩ࡮ࡧࡲࡹࡹ࠭Ⴏ"),
  bstack11ll11_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡃࡦࡸ࡮ࡵ࡮ࠨႰ"), bstack11ll11_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡆࡥࡹ࡫ࡧࡰࡴࡼࠫႱ"), bstack11ll11_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡊࡱࡧࡧࡴࠩႲ"), bstack11ll11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡦࡲࡉ࡯ࡶࡨࡲࡹࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨႳ"),
  bstack11ll11_opy_ (u"࠭ࡤࡰࡰࡷࡗࡹࡵࡰࡂࡲࡳࡓࡳࡘࡥࡴࡧࡷࠫႴ"),
  bstack11ll11_opy_ (u"ࠧࡶࡰ࡬ࡧࡴࡪࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩႵ"), bstack11ll11_opy_ (u"ࠨࡴࡨࡷࡪࡺࡋࡦࡻࡥࡳࡦࡸࡤࠨႶ"),
  bstack11ll11_opy_ (u"ࠩࡱࡳࡘ࡯ࡧ࡯ࠩႷ"),
  bstack11ll11_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡘࡲ࡮ࡳࡰࡰࡴࡷࡥࡳࡺࡖࡪࡧࡺࡷࠬႸ"),
  bstack11ll11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡤࡳࡱ࡬ࡨ࡜ࡧࡴࡤࡪࡨࡶࡸ࠭Ⴙ"),
  bstack11ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬႺ"),
  bstack11ll11_opy_ (u"࠭ࡲࡦࡥࡵࡩࡦࡺࡥࡄࡪࡵࡳࡲ࡫ࡄࡳ࡫ࡹࡩࡷ࡙ࡥࡴࡵ࡬ࡳࡳࡹࠧႻ"),
  bstack11ll11_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭Ⴜ"),
  bstack11ll11_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡕࡧࡴࡩࠩႽ"),
  bstack11ll11_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡖࡴࡪ࡫ࡤࠨႾ"),
  bstack11ll11_opy_ (u"ࠪ࡫ࡵࡹࡅ࡯ࡣࡥࡰࡪࡪࠧႿ"),
  bstack11ll11_opy_ (u"ࠫ࡮ࡹࡈࡦࡣࡧࡰࡪࡹࡳࠨჀ"),
  bstack11ll11_opy_ (u"ࠬࡧࡤࡣࡇࡻࡩࡨ࡚ࡩ࡮ࡧࡲࡹࡹ࠭Ⴡ"),
  bstack11ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࡙ࡣࡳ࡫ࡳࡸࠬჂ"),
  bstack11ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡉ࡫ࡶࡪࡥࡨࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫჃ"),
  bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴࡍࡲࡢࡰࡷࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠨჄ"),
  bstack11ll11_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡑࡥࡹࡻࡲࡢ࡮ࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧჅ"),
  bstack11ll11_opy_ (u"ࠪࡷࡾࡹࡴࡦ࡯ࡓࡳࡷࡺࠧ჆"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡩࡨࡈࡰࡵࡷࠫჇ"),
  bstack11ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡘࡲࡱࡵࡣ࡬ࠩ჈"), bstack11ll11_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰ࡚ࡹࡱࡧࠪ჉"), bstack11ll11_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡋࡦࡻࠪ჊"),
  bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴࡒࡡࡶࡰࡦ࡬ࠬ჋"),
  bstack11ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡦࡥࡹࡉࡡࡱࡶࡸࡶࡪ࠭჌"),
  bstack11ll11_opy_ (u"ࠪࡹࡳ࡯࡮ࡴࡶࡤࡰࡱࡕࡴࡩࡧࡵࡔࡦࡩ࡫ࡢࡩࡨࡷࠬჍ"),
  bstack11ll11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩ࡜࡯࡮ࡥࡱࡺࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳ࠭჎"),
  bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡴࡵ࡬ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ჏"),
  bstack11ll11_opy_ (u"࠭ࡥ࡯ࡨࡲࡶࡨ࡫ࡁࡱࡲࡌࡲࡸࡺࡡ࡭࡮ࠪა"),
  bstack11ll11_opy_ (u"ࠧࡦࡰࡶࡹࡷ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡳࡉࡣࡹࡩࡕࡧࡧࡦࡵࠪბ"), bstack11ll11_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡆࡨࡺࡹࡵ࡯࡭ࡵࡓࡳࡷࡺࠧგ"), bstack11ll11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡆࡨࡸࡦ࡯࡬ࡴࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠬდ"),
  bstack11ll11_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡴࡵࡹࡃࡢࡥ࡫ࡩࡑ࡯࡭ࡪࡶࠪე"),
  bstack11ll11_opy_ (u"ࠫࡨࡧ࡬ࡦࡰࡧࡥࡷࡌ࡯ࡳ࡯ࡤࡸࠬვ"),
  bstack11ll11_opy_ (u"ࠬࡨࡵ࡯ࡦ࡯ࡩࡎࡪࠧზ"),
  bstack11ll11_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭თ"),
  bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡈࡲࡦࡨ࡬ࡦࡦࠪი"), bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡅࡺࡺࡨࡰࡴ࡬ࡾࡪࡪࠧკ"),
  bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵࡁࡤࡥࡨࡴࡹࡇ࡬ࡦࡴࡷࡷࠬლ"), bstack11ll11_opy_ (u"ࠪࡥࡺࡺ࡯ࡅ࡫ࡶࡱ࡮ࡹࡳࡂ࡮ࡨࡶࡹࡹࠧმ"),
  bstack11ll11_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡳࡍ࡫ࡥࠫნ"),
  bstack11ll11_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡕࡣࡳࠫო"),
  bstack11ll11_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏ࡮ࡪࡶ࡬ࡥࡱ࡛ࡲ࡭ࠩპ"), bstack11ll11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡁ࡭࡮ࡲࡻࡕࡵࡰࡶࡲࡶࠫჟ"), bstack11ll11_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡩࡱࡳࡷ࡫ࡆࡳࡣࡸࡨ࡜ࡧࡲ࡯࡫ࡱ࡫ࠬრ"), bstack11ll11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡩࡳࡒࡩ࡯࡭ࡶࡍࡳࡈࡡࡤ࡭ࡪࡶࡴࡻ࡮ࡥࠩს"),
  bstack11ll11_opy_ (u"ࠪ࡯ࡪ࡫ࡰࡌࡧࡼࡇ࡭ࡧࡩ࡯ࡵࠪტ"),
  bstack11ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡾࡦࡨ࡬ࡦࡕࡷࡶ࡮ࡴࡧࡴࡆ࡬ࡶࠬუ"),
  bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡥࡨࡷࡸࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨფ"),
  bstack11ll11_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡐ࡫ࡹࡅࡧ࡯ࡥࡾ࠭ქ"),
  bstack11ll11_opy_ (u"ࠧࡴࡪࡲࡻࡎࡕࡓࡍࡱࡪࠫღ"),
  bstack11ll11_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡕࡷࡶࡦࡺࡥࡨࡻࠪყ"),
  bstack11ll11_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡔࡨࡷࡵࡵ࡮ࡴࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪშ"), bstack11ll11_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡗࡢ࡫ࡷࡘ࡮ࡳࡥࡰࡷࡷࠫჩ"),
  bstack11ll11_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࠧც"),
  bstack11ll11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡹࡹ࡯ࡥࡈࡼࡪࡩࡵࡵࡧࡉࡶࡴࡳࡈࡵࡶࡳࡷࠬძ"),
  bstack11ll11_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡃࡢࡲࡷࡹࡷ࡫ࠧწ"),
  bstack11ll11_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧჭ"),
  bstack11ll11_opy_ (u"ࠨࡨࡸࡰࡱࡉ࡯࡯ࡶࡨࡼࡹࡒࡩࡴࡶࠪხ"),
  bstack11ll11_opy_ (u"ࠩࡺࡥ࡮ࡺࡆࡰࡴࡄࡴࡵ࡙ࡣࡳ࡫ࡳࡸࠬჯ"),
  bstack11ll11_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡇࡴࡴ࡮ࡦࡥࡷࡖࡪࡺࡲࡪࡧࡶࠫჰ"),
  bstack11ll11_opy_ (u"ࠫࡦࡶࡰࡏࡣࡰࡩࠬჱ"),
  bstack11ll11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡙ࡌࡄࡧࡵࡸࠬჲ"),
  bstack11ll11_opy_ (u"࠭ࡴࡢࡲ࡚࡭ࡹ࡮ࡓࡩࡱࡵࡸࡕࡸࡥࡴࡵࡇࡹࡷࡧࡴࡪࡱࡱࠫჳ"),
  bstack11ll11_opy_ (u"ࠧࡴࡥࡤࡰࡪࡌࡡࡤࡶࡲࡶࠬჴ"),
  bstack11ll11_opy_ (u"ࠨࡹࡧࡥࡑࡵࡣࡢ࡮ࡓࡳࡷࡺࠧჵ"),
  bstack11ll11_opy_ (u"ࠩࡶ࡬ࡴࡽࡘࡤࡱࡧࡩࡑࡵࡧࠨჶ"),
  bstack11ll11_opy_ (u"ࠪ࡭ࡴࡹࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡷࡶࡩࠬჷ"),
  bstack11ll11_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪ࠭ჸ"),
  bstack11ll11_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡵࡶࡻࡴࡸࡤࠨჹ"),
  bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡓࡶࡪࡨࡵࡪ࡮ࡷ࡛ࡉࡇࠧჺ"),
  bstack11ll11_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡘࡆࡄࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠨ჻"),
  bstack11ll11_opy_ (u"ࠨࡹࡨࡦࡉࡸࡩࡷࡧࡵࡅ࡬࡫࡮ࡵࡗࡵࡰࠬჼ"),
  bstack11ll11_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡺࡨࠨჽ"),
  bstack11ll11_opy_ (u"ࠪࡹࡸ࡫ࡎࡦࡹ࡚ࡈࡆ࠭ჾ"),
  bstack11ll11_opy_ (u"ࠫࡼࡪࡡࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧჿ"), bstack11ll11_opy_ (u"ࠬࡽࡤࡢࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࡙࡯࡭ࡦࡱࡸࡸࠬᄀ"),
  bstack11ll11_opy_ (u"࠭ࡸࡤࡱࡧࡩࡔࡸࡧࡊࡦࠪᄁ"), bstack11ll11_opy_ (u"ࠧࡹࡥࡲࡨࡪ࡙ࡩࡨࡰ࡬ࡲ࡬ࡏࡤࠨᄂ"),
  bstack11ll11_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥ࡙ࡇࡅࡇࡻ࡮ࡥ࡮ࡨࡍࡩ࠭ᄃ"),
  bstack11ll11_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡐࡰࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡸࡴࡐࡰ࡯ࡽࠬᄄ"),
  bstack11ll11_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࡷࠬᄅ"),
  bstack11ll11_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶ࡮࡫ࡳࠨᄆ"), bstack11ll11_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷࡿࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠨᄇ"),
  bstack11ll11_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࡈࡢࡴࡧࡻࡦࡸࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩᄈ"),
  bstack11ll11_opy_ (u"ࠧ࡮ࡣࡻࡘࡾࡶࡩ࡯ࡩࡉࡶࡪࡷࡵࡦࡰࡦࡽࠬᄉ"),
  bstack11ll11_opy_ (u"ࠨࡵ࡬ࡱࡵࡲࡥࡊࡵ࡙࡭ࡸ࡯ࡢ࡭ࡧࡆ࡬ࡪࡩ࡫ࠨᄊ"),
  bstack11ll11_opy_ (u"ࠩࡸࡷࡪࡉࡡࡳࡶ࡫ࡥ࡬࡫ࡓࡴ࡮ࠪᄋ"),
  bstack11ll11_opy_ (u"ࠪࡷ࡭ࡵࡵ࡭ࡦࡘࡷࡪ࡙ࡩ࡯ࡩ࡯ࡩࡹࡵ࡮ࡕࡧࡶࡸࡒࡧ࡮ࡢࡩࡨࡶࠬᄌ"),
  bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡌ࡛ࡉࡖࠧᄍ"),
  bstack11ll11_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡴࡻࡣࡩࡋࡧࡉࡳࡸ࡯࡭࡮ࠪᄎ"),
  bstack11ll11_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪࡎࡩࡥࡦࡨࡲࡆࡶࡩࡑࡱ࡯࡭ࡨࡿࡅࡳࡴࡲࡶࠬᄏ"),
  bstack11ll11_opy_ (u"ࠧ࡮ࡱࡦ࡯ࡑࡵࡣࡢࡶ࡬ࡳࡳࡇࡰࡱࠩᄐ"),
  bstack11ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇࡱࡵࡱࡦࡺࠧᄑ"), bstack11ll11_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈ࡬ࡰࡹ࡫ࡲࡔࡲࡨࡧࡸ࠭ᄒ"),
  bstack11ll11_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡆࡨࡰࡦࡿࡁࡥࡤࠪᄓ"),
  bstack11ll11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡎࡪࡌࡰࡥࡤࡸࡴࡸࡁࡶࡶࡲࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠧᄔ")
]
bstack1l11l11l1_opy_ = bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡺࡶ࡬ࡰࡣࡧࠫᄕ")
bstack111l111l1_opy_ = [bstack11ll11_opy_ (u"࠭࠮ࡢࡲ࡮ࠫᄖ"), bstack11ll11_opy_ (u"ࠧ࠯ࡣࡤࡦࠬᄗ"), bstack11ll11_opy_ (u"ࠨ࠰࡬ࡴࡦ࠭ᄘ")]
bstack1lll111ll_opy_ = [bstack11ll11_opy_ (u"ࠩ࡬ࡨࠬᄙ"), bstack11ll11_opy_ (u"ࠪࡴࡦࡺࡨࠨᄚ"), bstack11ll11_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧᄛ"), bstack11ll11_opy_ (u"ࠬࡹࡨࡢࡴࡨࡥࡧࡲࡥࡠ࡫ࡧࠫᄜ")]
bstack11111l11l_opy_ = {
  bstack11ll11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᄝ"): bstack11ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᄞ"),
  bstack11ll11_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩᄟ"): bstack11ll11_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧᄠ"),
  bstack11ll11_opy_ (u"ࠪࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᄡ"): bstack11ll11_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬᄢ"),
  bstack11ll11_opy_ (u"ࠬ࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᄣ"): bstack11ll11_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬᄤ"),
  bstack11ll11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡏࡱࡶ࡬ࡳࡳࡹࠧᄥ"): bstack11ll11_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᄦ")
}
bstack1ll1111l1l_opy_ = [
  bstack11ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᄧ"),
  bstack11ll11_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨᄨ"),
  bstack11ll11_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬᄩ"),
  bstack11ll11_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫᄪ"),
  bstack11ll11_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧᄫ"),
]
bstack1l1111111_opy_ = bstack11ll1ll1_opy_ + bstack11l11lllll_opy_ + bstack111111l1l_opy_
bstack1ll1ll1l1_opy_ = [
  bstack11ll11_opy_ (u"ࠧ࡟࡮ࡲࡧࡦࡲࡨࡰࡵࡷࠨࠬᄬ"),
  bstack11ll11_opy_ (u"ࠨࡠࡥࡷ࠲ࡲ࡯ࡤࡣ࡯࠲ࡨࡵ࡭ࠥࠩᄭ"),
  bstack11ll11_opy_ (u"ࠩࡡ࠵࠷࠽࠮ࠨᄮ"),
  bstack11ll11_opy_ (u"ࠪࡢ࠶࠶࠮ࠨᄯ"),
  bstack11ll11_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠴࡟࠻࠳࠹࡞࠰ࠪᄰ"),
  bstack11ll11_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠶ࡠ࠶࠭࠺࡟࠱ࠫᄱ"),
  bstack11ll11_opy_ (u"࠭࡞࠲࠹࠵࠲࠸ࡡ࠰࠮࠳ࡠ࠲ࠬᄲ"),
  bstack11ll11_opy_ (u"ࠧ࡟࠳࠼࠶࠳࠷࠶࠹࠰ࠪᄳ")
]
bstack11l1l11l1l_opy_ = bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᄴ")
bstack11ll11l11_opy_ = bstack11ll11_opy_ (u"ࠩࡶࡨࡰ࠵ࡶ࠲࠱ࡨࡺࡪࡴࡴࠨᄵ")
bstack1l11l1llll_opy_ = [ bstack11ll11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᄶ") ]
bstack111lllll1_opy_ = [ bstack11ll11_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪᄷ") ]
bstack11111lll1_opy_ = [ bstack11ll11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᄸ") ]
bstack11l1l1111_opy_ = bstack11ll11_opy_ (u"࠭ࡓࡅࡍࡖࡩࡹࡻࡰࠨᄹ")
bstack1llllll1l1_opy_ = bstack11ll11_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡂࡶࡷࡩࡲࡶࡴࡦࡦࠪᄺ")
bstack1l111lll_opy_ = bstack11ll11_opy_ (u"ࠨࡕࡇࡏ࡙࡫ࡳࡵࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠬᄻ")
bstack1ll11l11l1_opy_ = bstack11ll11_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࠨᄼ")
bstack1ll1lllll1_opy_ = [
  bstack11ll11_opy_ (u"ࠪࡉࡗࡘ࡟ࡇࡃࡌࡐࡊࡊࠧᄽ"),
  bstack11ll11_opy_ (u"ࠫࡊࡘࡒࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫᄾ"),
  bstack11ll11_opy_ (u"ࠬࡋࡒࡓࡡࡅࡐࡔࡉࡋࡆࡆࡢࡆ࡞ࡥࡃࡍࡋࡈࡒ࡙࠭ᄿ"),
  bstack11ll11_opy_ (u"࠭ࡅࡓࡔࡢࡒࡊ࡚ࡗࡐࡔࡎࡣࡈࡎࡁࡏࡉࡈࡈࠬᅀ"),
  bstack11ll11_opy_ (u"ࠧࡆࡔࡕࡣࡘࡕࡃࡌࡇࡗࡣࡓࡕࡔࡠࡅࡒࡒࡓࡋࡃࡕࡇࡇࠫᅁ"),
  bstack11ll11_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡆࡐࡔ࡙ࡅࡅࠩᅂ"),
  bstack11ll11_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊ࡙ࡅࡕࠩᅃ"),
  bstack11ll11_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡗࡋࡆࡖࡕࡈࡈࠬᅄ"),
  bstack11ll11_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡇࡂࡐࡔࡗࡉࡉ࠭ᅅ"),
  bstack11ll11_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᅆ"),
  bstack11ll11_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧᅇ"),
  bstack11ll11_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤࡏࡎࡗࡃࡏࡍࡉ࠭ᅈ"),
  bstack11ll11_opy_ (u"ࠨࡇࡕࡖࡤࡇࡄࡅࡔࡈࡗࡘࡥࡕࡏࡔࡈࡅࡈࡎࡁࡃࡎࡈࠫᅉ"),
  bstack11ll11_opy_ (u"ࠩࡈࡖࡗࡥࡔࡖࡐࡑࡉࡑࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᅊ"),
  bstack11ll11_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣ࡙ࡏࡍࡆࡆࡢࡓ࡚࡚ࠧᅋ"),
  bstack11ll11_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᅌ"),
  bstack11ll11_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡓࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡎࡏࡔࡖࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨᅍ"),
  bstack11ll11_opy_ (u"࠭ࡅࡓࡔࡢࡔࡗࡕࡘ࡚ࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᅎ"),
  bstack11ll11_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡑࡓ࡙ࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࠨᅏ"),
  bstack11ll11_opy_ (u"ࠨࡇࡕࡖࡤࡔࡁࡎࡇࡢࡖࡊ࡙ࡏࡍࡗࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᅐ"),
  bstack11ll11_opy_ (u"ࠩࡈࡖࡗࡥࡍࡂࡐࡇࡅ࡙ࡕࡒ࡚ࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨᅑ"),
]
bstack1lll111l_opy_ = bstack11ll11_opy_ (u"ࠪ࠲࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡦࡸࡴࡪࡨࡤࡧࡹࡹ࠯ࠨᅒ")
bstack1l1ll11l11_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠫࢃ࠭ᅓ")), bstack11ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᅔ"), bstack11ll11_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᅕ"))
bstack11ll1111l1_opy_ = bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡩࠨᅖ")
bstack11l11ll1l1_opy_ = [ bstack11ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᅗ"), bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᅘ"), bstack11ll11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩᅙ") ]
bstack1l11ll1l11_opy_ = [ bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᅚ"), bstack11ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᅛ"), bstack11ll11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬᅜ") ]
bstack1l111l1ll1_opy_ = {
  bstack11ll11_opy_ (u"ࠧࡑࡃࡖࡗࠬᅝ"): bstack11ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᅞ"),
  bstack11ll11_opy_ (u"ࠩࡉࡅࡎࡒࠧᅟ"): bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᅠ"),
  bstack11ll11_opy_ (u"ࠫࡘࡑࡉࡑࠩᅡ"): bstack11ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᅢ")
}
bstack1ll1ll11l_opy_ = [
  bstack11ll11_opy_ (u"ࠨࡧࡦࡶࠥᅣ"),
  bstack11ll11_opy_ (u"ࠢࡨࡱࡅࡥࡨࡱࠢᅤ"),
  bstack11ll11_opy_ (u"ࠣࡩࡲࡊࡴࡸࡷࡢࡴࡧࠦᅥ"),
  bstack11ll11_opy_ (u"ࠤࡵࡩ࡫ࡸࡥࡴࡪࠥᅦ"),
  bstack11ll11_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᅧ"),
  bstack11ll11_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᅨ"),
  bstack11ll11_opy_ (u"ࠧࡹࡵࡣ࡯࡬ࡸࡊࡲࡥ࡮ࡧࡱࡸࠧᅩ"),
  bstack11ll11_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᅪ"),
  bstack11ll11_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᅫ"),
  bstack11ll11_opy_ (u"ࠣࡥ࡯ࡩࡦࡸࡅ࡭ࡧࡰࡩࡳࡺࠢᅬ"),
  bstack11ll11_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࡵࠥᅭ"),
  bstack11ll11_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠥᅮ"),
  bstack11ll11_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࡆࡹࡹ࡯ࡥࡖࡧࡷ࡯ࡰࡵࠤᅯ"),
  bstack11ll11_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦᅰ"),
  bstack11ll11_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᅱ"),
  bstack11ll11_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡕࡱࡸࡧ࡭ࡇࡣࡵ࡫ࡲࡲࠧᅲ"),
  bstack11ll11_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡏࡸࡰࡹ࡯ࡔࡰࡷࡦ࡬ࠧᅳ"),
  bstack11ll11_opy_ (u"ࠤࡶ࡬ࡦࡱࡥࠣᅴ"),
  bstack11ll11_opy_ (u"ࠥࡧࡱࡵࡳࡦࡃࡳࡴࠧᅵ")
]
bstack11l1l111ll_opy_ = [
  bstack11ll11_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࠥᅶ"),
  bstack11ll11_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᅷ"),
  bstack11ll11_opy_ (u"ࠨࡡࡶࡶࡲࠦᅸ"),
  bstack11ll11_opy_ (u"ࠢ࡮ࡣࡱࡹࡦࡲࠢᅹ"),
  bstack11ll11_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᅺ")
]
bstack1l1lll11l_opy_ = {
  bstack11ll11_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࠣᅻ"): [bstack11ll11_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᅼ")],
  bstack11ll11_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᅽ"): [bstack11ll11_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᅾ")],
  bstack11ll11_opy_ (u"ࠨࡡࡶࡶࡲࠦᅿ"): [bstack11ll11_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦᆀ"), bstack11ll11_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦᆁ"), bstack11ll11_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᆂ"), bstack11ll11_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᆃ")],
  bstack11ll11_opy_ (u"ࠦࡲࡧ࡮ࡶࡣ࡯ࠦᆄ"): [bstack11ll11_opy_ (u"ࠧࡳࡡ࡯ࡷࡤࡰࠧᆅ")],
  bstack11ll11_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᆆ"): [bstack11ll11_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᆇ")],
}
bstack11l1l111l1_opy_ = {
  bstack11ll11_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࡅ࡭ࡧࡰࡩࡳࡺࠢᆈ"): bstack11ll11_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࠣᆉ"),
  bstack11ll11_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᆊ"): bstack11ll11_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᆋ"),
  bstack11ll11_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤᆌ"): bstack11ll11_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࠣᆍ"),
  bstack11ll11_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᆎ"): bstack11ll11_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࠥᆏ"),
  bstack11ll11_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᆐ"): bstack11ll11_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᆑ")
}
bstack1l111ll11l_opy_ = {
  bstack11ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᆒ"): bstack11ll11_opy_ (u"࡙ࠬࡵࡪࡶࡨࠤࡘ࡫ࡴࡶࡲࠪᆓ"),
  bstack11ll11_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᆔ"): bstack11ll11_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࠦࡔࡦࡣࡵࡨࡴࡽ࡮ࠨᆕ"),
  bstack11ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᆖ"): bstack11ll11_opy_ (u"ࠩࡗࡩࡸࡺࠠࡔࡧࡷࡹࡵ࠭ᆗ"),
  bstack11ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᆘ"): bstack11ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡗࡩࡦࡸࡤࡰࡹࡱࠫᆙ")
}
bstack11l11llll1_opy_ = 65536
bstack11l11ll1ll_opy_ = bstack11ll11_opy_ (u"ࠬ࠴࠮࠯࡝ࡗࡖ࡚ࡔࡃࡂࡖࡈࡈࡢ࠭ᆚ")