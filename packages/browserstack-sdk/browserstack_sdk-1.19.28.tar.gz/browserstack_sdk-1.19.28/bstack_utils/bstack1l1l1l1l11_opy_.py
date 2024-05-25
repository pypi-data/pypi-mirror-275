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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11l11_opy_
import tempfile
import json
bstack1111llll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬ፭"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11ll11_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩ፮"),
      datefmt=bstack11ll11_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ፯"),
      stream=sys.stdout
    )
  return logger
def bstack1111ll1lll_opy_():
  global bstack1111llll11_opy_
  if os.path.exists(bstack1111llll11_opy_):
    os.remove(bstack1111llll11_opy_)
def bstack1llll11lll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l11l1lll1_opy_(config, log_level):
  bstack1111llllll_opy_ = log_level
  if bstack11ll11_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ፰") in config and config[bstack11ll11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩ፱")] in bstack11l1l11l11_opy_:
    bstack1111llllll_opy_ = bstack11l1l11l11_opy_[config[bstack11ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ፲")]]
  if config.get(bstack11ll11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ፳"), False):
    logging.getLogger().setLevel(bstack1111llllll_opy_)
    return bstack1111llllll_opy_
  global bstack1111llll11_opy_
  bstack1llll11lll_opy_()
  bstack1111lll11l_opy_ = logging.Formatter(
    fmt=bstack11ll11_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨ፴"),
    datefmt=bstack11ll11_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭፵")
  )
  bstack1111ll1l11_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1111llll11_opy_)
  file_handler.setFormatter(bstack1111lll11l_opy_)
  bstack1111ll1l11_opy_.setFormatter(bstack1111lll11l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1111ll1l11_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11ll11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧ፶"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1111ll1l11_opy_.setLevel(bstack1111llllll_opy_)
  logging.getLogger().addHandler(bstack1111ll1l11_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1111llllll_opy_
def bstack1111ll11l1_opy_(config):
  try:
    bstack1111lllll1_opy_ = set([
      bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ፷"), bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ፸"), bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ፹"), bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭፺"), bstack11ll11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠬ፻"),
      bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ፼"), bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ፽"), bstack11ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ፾"), bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡦࡹࡳࠨ፿")
    ])
    bstack1111ll11ll_opy_ = bstack11ll11_opy_ (u"ࠨࠩᎀ")
    with open(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬᎁ")) as bstack1111lll1l1_opy_:
      bstack1111lll111_opy_ = bstack1111lll1l1_opy_.read()
      bstack1111ll11ll_opy_ = re.sub(bstack11ll11_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫᎂ"), bstack11ll11_opy_ (u"ࠫࠬᎃ"), bstack1111lll111_opy_, flags=re.M)
      bstack1111ll11ll_opy_ = re.sub(
        bstack11ll11_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨᎄ") + bstack11ll11_opy_ (u"࠭ࡼࠨᎅ").join(bstack1111lllll1_opy_) + bstack11ll11_opy_ (u"ࠧࠪ࠰࠭ࠨࠬᎆ"),
        bstack11ll11_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪᎇ"),
        bstack1111ll11ll_opy_, flags=re.M | re.I
      )
    def bstack1111ll1l1l_opy_(dic):
      bstack1111ll1ll1_opy_ = {}
      for key, value in dic.items():
        if key in bstack1111lllll1_opy_:
          bstack1111ll1ll1_opy_[key] = bstack11ll11_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ᎈ")
        else:
          if isinstance(value, dict):
            bstack1111ll1ll1_opy_[key] = bstack1111ll1l1l_opy_(value)
          else:
            bstack1111ll1ll1_opy_[key] = value
      return bstack1111ll1ll1_opy_
    bstack1111ll1ll1_opy_ = bstack1111ll1l1l_opy_(config)
    return {
      bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ᎉ"): bstack1111ll11ll_opy_,
      bstack11ll11_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᎊ"): json.dumps(bstack1111ll1ll1_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l1l_opy_(config):
  global bstack1111llll11_opy_
  try:
    if config.get(bstack11ll11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᎋ"), False):
      return
    uuid = os.getenv(bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᎌ"))
    if not uuid or uuid == bstack11ll11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᎍ"):
      return
    bstack1111llll1l_opy_ = [bstack11ll11_opy_ (u"ࠨࡴࡨࡵࡺ࡯ࡲࡦ࡯ࡨࡲࡹࡹ࠮ࡵࡺࡷࠫᎎ"), bstack11ll11_opy_ (u"ࠩࡓ࡭ࡵ࡬ࡩ࡭ࡧࠪᎏ"), bstack11ll11_opy_ (u"ࠪࡴࡾࡶࡲࡰ࡬ࡨࡧࡹ࠴ࡴࡰ࡯࡯ࠫ᎐"), bstack1111llll11_opy_]
    bstack1llll11lll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪ᎑") + uuid + bstack11ll11_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭᎒"))
    with tarfile.open(output_file, bstack11ll11_opy_ (u"ࠨࡷ࠻ࡩࡽࠦ᎓")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1111llll1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1111ll11l1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1111lll1ll_opy_ = data.encode()
        tarinfo.size = len(bstack1111lll1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1111lll1ll_opy_))
    bstack11ll11111_opy_ = MultipartEncoder(
      fields= {
        bstack11ll11_opy_ (u"ࠧࡥࡣࡷࡥࠬ᎔"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11ll11_opy_ (u"ࠨࡴࡥࠫ᎕")), bstack11ll11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧ᎖")),
        bstack11ll11_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ᎗"): uuid
      }
    )
    response = requests.post(
      bstack11ll11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡻࡰ࡭ࡱࡤࡨ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡥ࡯࡭ࡪࡴࡴ࠮࡮ࡲ࡫ࡸ࠵ࡵࡱ࡮ࡲࡥࡩࠨ᎘"),
      data=bstack11ll11111_opy_,
      headers={bstack11ll11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ᎙"): bstack11ll11111_opy_.content_type},
      auth=(config[bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ᎚")], config[bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ᎛")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧ᎜") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11ll11_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨ᎝") + str(e))
  finally:
    try:
      bstack1111ll1lll_opy_()
    except:
      pass