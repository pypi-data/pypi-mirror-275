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
from uuid import uuid4
from bstack_utils.helper import bstack11l11l11l_opy_, bstack111lllll11_opy_
from bstack_utils.bstack1l1lll111l_opy_ import bstack1lllll1111l_opy_
class bstack1l111l1l1l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l1111111l_opy_=None, framework=None, tags=[], scope=[], bstack1lll1lll1ll_opy_=None, bstack1lll1ll1111_opy_=True, bstack1lll1lll111_opy_=None, bstack1l1l1l1l_opy_=None, result=None, duration=None, bstack11lllll11l_opy_=None, meta={}):
        self.bstack11lllll11l_opy_ = bstack11lllll11l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1lll1ll1111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l1111111l_opy_ = bstack1l1111111l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1lll1lll1ll_opy_ = bstack1lll1lll1ll_opy_
        self.bstack1lll1lll111_opy_ = bstack1lll1lll111_opy_
        self.bstack1l1l1l1l_opy_ = bstack1l1l1l1l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11lll11l1l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1lll1ll111l_opy_(self):
        bstack1lll1l1lll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬᓘ"): bstack1lll1l1lll1_opy_,
            bstack11ll11_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬᓙ"): bstack1lll1l1lll1_opy_,
            bstack11ll11_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᓚ"): bstack1lll1l1lll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll11_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷ࠾ࠥࠨᓛ") + key)
            setattr(self, key, val)
    def bstack1lll1l1llll_opy_(self):
        return {
            bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᓜ"): self.name,
            bstack11ll11_opy_ (u"ࠧࡣࡱࡧࡽࠬᓝ"): {
                bstack11ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᓞ"): bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᓟ"),
                bstack11ll11_opy_ (u"ࠪࡧࡴࡪࡥࠨᓠ"): self.code
            },
            bstack11ll11_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᓡ"): self.scope,
            bstack11ll11_opy_ (u"ࠬࡺࡡࡨࡵࠪᓢ"): self.tags,
            bstack11ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᓣ"): self.framework,
            bstack11ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᓤ"): self.bstack1l1111111l_opy_
        }
    def bstack1lll1ll1l11_opy_(self):
        return {
         bstack11ll11_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ᓥ"): self.meta
        }
    def bstack1llll111111_opy_(self):
        return {
            bstack11ll11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬᓦ"): {
                bstack11ll11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧᓧ"): self.bstack1lll1lll1ll_opy_
            }
        }
    def bstack1lll1ll11l1_opy_(self, bstack1lll1lll11l_opy_, details):
        step = next(filter(lambda st: st[bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧᓨ")] == bstack1lll1lll11l_opy_, self.meta[bstack11ll11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᓩ")]), None)
        step.update(details)
    def bstack1lll1llll1l_opy_(self, bstack1lll1lll11l_opy_):
        step = next(filter(lambda st: st[bstack11ll11_opy_ (u"࠭ࡩࡥࠩᓪ")] == bstack1lll1lll11l_opy_, self.meta[bstack11ll11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᓫ")]), None)
        step.update({
            bstack11ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᓬ"): bstack11l11l11l_opy_()
        })
    def bstack1l11111111_opy_(self, bstack1lll1lll11l_opy_, result, duration=None):
        bstack1lll1lll111_opy_ = bstack11l11l11l_opy_()
        if bstack1lll1lll11l_opy_ is not None and self.meta.get(bstack11ll11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓭ")):
            step = next(filter(lambda st: st[bstack11ll11_opy_ (u"ࠪ࡭ࡩ࠭ᓮ")] == bstack1lll1lll11l_opy_, self.meta[bstack11ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓯ")]), None)
            step.update({
                bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᓰ"): bstack1lll1lll111_opy_,
                bstack11ll11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᓱ"): duration if duration else bstack111lllll11_opy_(step[bstack11ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᓲ")], bstack1lll1lll111_opy_),
                bstack11ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᓳ"): result.result,
                bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᓴ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1lll1llll11_opy_):
        if self.meta.get(bstack11ll11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᓵ")):
            self.meta[bstack11ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓶ")].append(bstack1lll1llll11_opy_)
        else:
            self.meta[bstack11ll11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᓷ")] = [ bstack1lll1llll11_opy_ ]
    def bstack1lll1ll1l1l_opy_(self):
        return {
            bstack11ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᓸ"): self.bstack11lll11l1l_opy_(),
            **self.bstack1lll1l1llll_opy_(),
            **self.bstack1lll1ll111l_opy_(),
            **self.bstack1lll1ll1l11_opy_()
        }
    def bstack1lll1lll1l1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᓹ"): self.bstack1lll1lll111_opy_,
            bstack11ll11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᓺ"): self.duration,
            bstack11ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᓻ"): self.result.result
        }
        if data[bstack11ll11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᓼ")] == bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᓽ"):
            data[bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᓾ")] = self.result.bstack11ll1l111l_opy_()
            data[bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᓿ")] = [{bstack11ll11_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᔀ"): self.result.bstack111ll11l1l_opy_()}]
        return data
    def bstack1lll1ll1lll_opy_(self):
        return {
            bstack11ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᔁ"): self.bstack11lll11l1l_opy_(),
            **self.bstack1lll1l1llll_opy_(),
            **self.bstack1lll1ll111l_opy_(),
            **self.bstack1lll1lll1l1_opy_(),
            **self.bstack1lll1ll1l11_opy_()
        }
    def bstack1l1111l1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll11_opy_ (u"ࠩࡖࡸࡦࡸࡴࡦࡦࠪᔂ") in event:
            return self.bstack1lll1ll1l1l_opy_()
        elif bstack11ll11_opy_ (u"ࠪࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᔃ") in event:
            return self.bstack1lll1ll1lll_opy_()
    def bstack1l111lll1l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1lll1lll111_opy_ = time if time else bstack11l11l11l_opy_()
        self.duration = duration if duration else bstack111lllll11_opy_(self.bstack1l1111111l_opy_, self.bstack1lll1lll111_opy_)
        if result:
            self.result = result
class bstack11lll111l1_opy_(bstack1l111l1l1l_opy_):
    def __init__(self, hooks=[], bstack11lll111ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11lll111ll_opy_ = bstack11lll111ll_opy_
        super().__init__(*args, **kwargs, bstack1l1l1l1l_opy_=bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᔄ"))
    @classmethod
    def bstack1lll1llllll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll11_opy_ (u"ࠬ࡯ࡤࠨᔅ"): id(step),
                bstack11ll11_opy_ (u"࠭ࡴࡦࡺࡷࠫᔆ"): step.name,
                bstack11ll11_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨᔇ"): step.keyword,
            })
        return bstack11lll111l1_opy_(
            **kwargs,
            meta={
                bstack11ll11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩᔈ"): {
                    bstack11ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᔉ"): feature.name,
                    bstack11ll11_opy_ (u"ࠪࡴࡦࡺࡨࠨᔊ"): feature.filename,
                    bstack11ll11_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᔋ"): feature.description
                },
                bstack11ll11_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧᔌ"): {
                    bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᔍ"): scenario.name
                },
                bstack11ll11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᔎ"): steps,
                bstack11ll11_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪᔏ"): bstack1lllll1111l_opy_(test)
            }
        )
    def bstack1lll1lllll1_opy_(self):
        return {
            bstack11ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᔐ"): self.hooks
        }
    def bstack1lll1ll1ll1_opy_(self):
        if self.bstack11lll111ll_opy_:
            return {
                bstack11ll11_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩᔑ"): self.bstack11lll111ll_opy_
            }
        return {}
    def bstack1lll1ll1lll_opy_(self):
        return {
            **super().bstack1lll1ll1lll_opy_(),
            **self.bstack1lll1lllll1_opy_()
        }
    def bstack1lll1ll1l1l_opy_(self):
        return {
            **super().bstack1lll1ll1l1l_opy_(),
            **self.bstack1lll1ll1ll1_opy_()
        }
    def bstack1l111lll1l_opy_(self):
        return bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᔒ")
class bstack1l11111ll1_opy_(bstack1l111l1l1l_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1l1l1l1l_opy_=bstack11ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᔓ"))
    def bstack1l1111lll1_opy_(self):
        return self.hook_type
    def bstack1lll1ll11ll_opy_(self):
        return {
            bstack11ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᔔ"): self.hook_type
        }
    def bstack1lll1ll1lll_opy_(self):
        return {
            **super().bstack1lll1ll1lll_opy_(),
            **self.bstack1lll1ll11ll_opy_()
        }
    def bstack1lll1ll1l1l_opy_(self):
        return {
            **super().bstack1lll1ll1l1l_opy_(),
            **self.bstack1lll1ll11ll_opy_()
        }
    def bstack1l111lll1l_opy_(self):
        return bstack11ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩᔕ")