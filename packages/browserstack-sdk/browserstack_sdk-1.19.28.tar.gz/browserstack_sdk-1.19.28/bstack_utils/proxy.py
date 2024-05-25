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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1111ll1111_opy_
def bstack1lllll1l11l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1lllll11ll1_opy_(bstack1lllll11l1l_opy_, bstack1lllll1l111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1lllll11l1l_opy_):
        with open(bstack1lllll11l1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1lllll1l11l_opy_(bstack1lllll11l1l_opy_):
        pac = get_pac(url=bstack1lllll11l1l_opy_)
    else:
        raise Exception(bstack11ll11_opy_ (u"ࠧࡑࡣࡦࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠧᑊ").format(bstack1lllll11l1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11ll11_opy_ (u"ࠣ࠺࠱࠼࠳࠾࠮࠹ࠤᑋ"), 80))
        bstack1lllll11l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1lllll11l11_opy_ = bstack11ll11_opy_ (u"ࠩ࠳࠲࠵࠴࠰࠯࠲ࠪᑌ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1lllll1l111_opy_, bstack1lllll11l11_opy_)
    return proxy_url
def bstack1l1ll1llll_opy_(config):
    return bstack11ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᑍ") in config or bstack11ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᑎ") in config
def bstack1l11l1ll1l_opy_(config):
    if not bstack1l1ll1llll_opy_(config):
        return
    if config.get(bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᑏ")):
        return config.get(bstack11ll11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᑐ"))
    if config.get(bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᑑ")):
        return config.get(bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᑒ"))
def bstack111ll11l_opy_(config, bstack1lllll1l111_opy_):
    proxy = bstack1l11l1ll1l_opy_(config)
    proxies = {}
    if config.get(bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᑓ")) or config.get(bstack11ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᑔ")):
        if proxy.endswith(bstack11ll11_opy_ (u"ࠫ࠳ࡶࡡࡤࠩᑕ")):
            proxies = bstack1l111lll1_opy_(proxy, bstack1lllll1l111_opy_)
        else:
            proxies = {
                bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᑖ"): proxy
            }
    return proxies
def bstack1l111lll1_opy_(bstack1lllll11l1l_opy_, bstack1lllll1l111_opy_):
    proxies = {}
    global bstack1lllll11lll_opy_
    if bstack11ll11_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩᑗ") in globals():
        return bstack1lllll11lll_opy_
    try:
        proxy = bstack1lllll11ll1_opy_(bstack1lllll11l1l_opy_, bstack1lllll1l111_opy_)
        if bstack11ll11_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢᑘ") in proxy:
            proxies = {}
        elif bstack11ll11_opy_ (u"ࠣࡊࡗࡘࡕࠨᑙ") in proxy or bstack11ll11_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣᑚ") in proxy or bstack11ll11_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤᑛ") in proxy:
            bstack1lllll111ll_opy_ = proxy.split(bstack11ll11_opy_ (u"ࠦࠥࠨᑜ"))
            if bstack11ll11_opy_ (u"ࠧࡀ࠯࠰ࠤᑝ") in bstack11ll11_opy_ (u"ࠨࠢᑞ").join(bstack1lllll111ll_opy_[1:]):
                proxies = {
                    bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᑟ"): bstack11ll11_opy_ (u"ࠣࠤᑠ").join(bstack1lllll111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᑡ"): str(bstack1lllll111ll_opy_[0]).lower() + bstack11ll11_opy_ (u"ࠥ࠾࠴࠵ࠢᑢ") + bstack11ll11_opy_ (u"ࠦࠧᑣ").join(bstack1lllll111ll_opy_[1:])
                }
        elif bstack11ll11_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦᑤ") in proxy:
            bstack1lllll111ll_opy_ = proxy.split(bstack11ll11_opy_ (u"ࠨࠠࠣᑥ"))
            if bstack11ll11_opy_ (u"ࠢ࠻࠱࠲ࠦᑦ") in bstack11ll11_opy_ (u"ࠣࠤᑧ").join(bstack1lllll111ll_opy_[1:]):
                proxies = {
                    bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᑨ"): bstack11ll11_opy_ (u"ࠥࠦᑩ").join(bstack1lllll111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᑪ"): bstack11ll11_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᑫ") + bstack11ll11_opy_ (u"ࠨࠢᑬ").join(bstack1lllll111ll_opy_[1:])
                }
        else:
            proxies = {
                bstack11ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᑭ"): proxy
            }
    except Exception as e:
        print(bstack11ll11_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧᑮ"), bstack1111ll1111_opy_.format(bstack1lllll11l1l_opy_, str(e)))
    bstack1lllll11lll_opy_ = proxies
    return proxies