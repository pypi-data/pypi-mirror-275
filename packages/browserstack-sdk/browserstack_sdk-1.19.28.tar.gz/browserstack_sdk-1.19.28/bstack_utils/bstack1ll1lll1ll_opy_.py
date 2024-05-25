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
class bstack11l1ll1111_opy_(object):
  bstack1ll11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠫࢃ࠭໫")), bstack11ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ໬"))
  bstack11l1ll111l_opy_ = os.path.join(bstack1ll11llll1_opy_, bstack11ll11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳ࠯࡬ࡶࡳࡳ࠭໭"))
  bstack11l1l1ll1l_opy_ = None
  perform_scan = None
  bstack1ll11l1lll_opy_ = None
  bstack111l11lll_opy_ = None
  bstack11ll111l11_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll11_opy_ (u"ࠧࡪࡰࡶࡸࡦࡴࡣࡦࠩ໮")):
      cls.instance = super(bstack11l1ll1111_opy_, cls).__new__(cls)
      cls.instance.bstack11l1l1llll_opy_()
    return cls.instance
  def bstack11l1l1llll_opy_(self):
    try:
      with open(self.bstack11l1ll111l_opy_, bstack11ll11_opy_ (u"ࠨࡴࠪ໯")) as bstack1l1l1ll1_opy_:
        bstack11l1l1ll11_opy_ = bstack1l1l1ll1_opy_.read()
        data = json.loads(bstack11l1l1ll11_opy_)
        if bstack11ll11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ໰") in data:
          self.bstack11ll111l1l_opy_(data[bstack11ll11_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ໱")])
        if bstack11ll11_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ໲") in data:
          self.bstack11ll11ll11_opy_(data[bstack11ll11_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭໳")])
    except:
      pass
  def bstack11ll11ll11_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11ll11_opy_ (u"࠭ࡳࡤࡣࡱࠫ໴")]
      self.bstack1ll11l1lll_opy_ = scripts[bstack11ll11_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫ໵")]
      self.bstack111l11lll_opy_ = scripts[bstack11ll11_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬ໶")]
      self.bstack11ll111l11_opy_ = scripts[bstack11ll11_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧ໷")]
  def bstack11ll111l1l_opy_(self, bstack11l1l1ll1l_opy_):
    if bstack11l1l1ll1l_opy_ != None and len(bstack11l1l1ll1l_opy_) != 0:
      self.bstack11l1l1ll1l_opy_ = bstack11l1l1ll1l_opy_
  def store(self):
    try:
      with open(self.bstack11l1ll111l_opy_, bstack11ll11_opy_ (u"ࠪࡻࠬ໸")) as file:
        json.dump({
          bstack11ll11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࠨ໹"): self.bstack11l1l1ll1l_opy_,
          bstack11ll11_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࡸࠨ໺"): {
            bstack11ll11_opy_ (u"ࠨࡳࡤࡣࡱࠦ໻"): self.perform_scan,
            bstack11ll11_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦ໼"): self.bstack1ll11l1lll_opy_,
            bstack11ll11_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧ໽"): self.bstack111l11lll_opy_,
            bstack11ll11_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢ໾"): self.bstack11ll111l11_opy_
          }
        }, file)
    except:
      pass
  def bstack1l111ll1l_opy_(self, bstack11l1l1lll1_opy_):
    try:
      return any(command.get(bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨ໿")) == bstack11l1l1lll1_opy_ for command in self.bstack11l1l1ll1l_opy_)
    except:
      return False
bstack1ll1lll1ll_opy_ = bstack11l1ll1111_opy_()