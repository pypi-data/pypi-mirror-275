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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1llllll1l_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1lll11l11l_opy_ import bstack1lll1l1l11_opy_
import time
import requests
def bstack1l1l11l1l_opy_():
  global CONFIG
  headers = {
        bstack11ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack11ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack111ll11l_opy_(CONFIG, bstack1ll1111l_opy_)
  try:
    response = requests.get(bstack1ll1111l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1lll1111ll_opy_ = response.json()[bstack11ll11_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1l11l1l1ll_opy_.format(response.json()))
      return bstack1lll1111ll_opy_
    else:
      logger.debug(bstack1lllllll1_opy_.format(bstack11ll11_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack1lllllll1_opy_.format(e))
def bstack1ll11llll_opy_(hub_url):
  global CONFIG
  url = bstack11ll11_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack11ll11_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack11ll11_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack11ll11_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack111ll11l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111l1lll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll1ll1l_opy_.format(hub_url, e))
def bstack1lll11ll1l_opy_():
  try:
    global bstack1l11l1l1l1_opy_
    bstack1lll1111ll_opy_ = bstack1l1l11l1l_opy_()
    bstack1l1ll1l1_opy_ = []
    results = []
    for bstack11111ll1l_opy_ in bstack1lll1111ll_opy_:
      bstack1l1ll1l1_opy_.append(bstack1l11ll1l_opy_(target=bstack1ll11llll_opy_,args=(bstack11111ll1l_opy_,)))
    for t in bstack1l1ll1l1_opy_:
      t.start()
    for t in bstack1l1ll1l1_opy_:
      results.append(t.join())
    bstack111lllll_opy_ = {}
    for item in results:
      hub_url = item[bstack11ll11_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack11ll11_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack111lllll_opy_[hub_url] = latency
    bstack1lll1111_opy_ = min(bstack111lllll_opy_, key= lambda x: bstack111lllll_opy_[x])
    bstack1l11l1l1l1_opy_ = bstack1lll1111_opy_
    logger.debug(bstack1l1ll11lll_opy_.format(bstack1lll1111_opy_))
  except Exception as e:
    logger.debug(bstack11l111lll_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1l1l1l1l11_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack1l1l1lll11_opy_, bstack1l1ll11ll_opy_, bstack11l1ll1ll_opy_, bstack1l1lll1ll1_opy_, bstack11l1lll1l_opy_, \
  Notset, bstack111111ll1_opy_, \
  bstack11l11l111_opy_, bstack1llll1llll_opy_, bstack1111l11l1_opy_, bstack11lllll1_opy_, bstack1l1ll11l1_opy_, bstack11111llll_opy_, \
  bstack1ll1ll11_opy_, \
  bstack1ll11l11ll_opy_, bstack11111l111_opy_, bstack11llll1ll_opy_, bstack1ll1l1l1ll_opy_, \
  bstack1ll1llll1l_opy_, bstack11lllllll_opy_, bstack111l1l1l_opy_
from bstack_utils.bstack111l1l11_opy_ import bstack11l111l1_opy_
from bstack_utils.bstack1ll11l11_opy_ import bstack1l11lll11l_opy_
from bstack_utils.bstack1ll1l1lll_opy_ import bstack11l11ll11_opy_, bstack111111l1_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack1l1l111lll_opy_
from bstack_utils.bstack1ll1lll1ll_opy_ import bstack1ll1lll1ll_opy_
from bstack_utils.proxy import bstack1l111lll1_opy_, bstack111ll11l_opy_, bstack1l11l1ll1l_opy_, bstack1l1ll1llll_opy_
import bstack_utils.bstack1ll1l11ll1_opy_ as bstack1l111111l_opy_
from browserstack_sdk.bstack1lll111l11_opy_ import *
from browserstack_sdk.bstack11l1ll11l_opy_ import *
from bstack_utils.bstack1l1lll111l_opy_ import bstack11lll111l_opy_
bstack11l1111l1_opy_ = bstack11ll11_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack1l1llllll1_opy_ = bstack11ll11_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack1l1l1lllll_opy_ = None
CONFIG = {}
bstack1ll1l111l1_opy_ = {}
bstack111ll1l1l_opy_ = {}
bstack1l11llll11_opy_ = None
bstack111lll1ll_opy_ = None
bstack1lll1ll111_opy_ = None
bstack1ll1l1l1l1_opy_ = -1
bstack1l11lll111_opy_ = 0
bstack1l1l11l11l_opy_ = bstack11ll1lll_opy_
bstack1111llll1_opy_ = 1
bstack1l11lll1_opy_ = False
bstack1l11ll11l1_opy_ = False
bstack1l11llll1_opy_ = bstack11ll11_opy_ (u"ࠨࠩࢂ")
bstack111111ll_opy_ = bstack11ll11_opy_ (u"ࠩࠪࢃ")
bstack11llll1l_opy_ = False
bstack1l111ll1_opy_ = True
bstack111lll1l1_opy_ = bstack11ll11_opy_ (u"ࠪࠫࢄ")
bstack1l111l11l_opy_ = []
bstack1l11l1l1l1_opy_ = bstack11ll11_opy_ (u"ࠫࠬࢅ")
bstack1llll111l_opy_ = False
bstack1l11ll11_opy_ = None
bstack1l111l1ll_opy_ = None
bstack1ll11l1ll_opy_ = None
bstack11ll1111_opy_ = -1
bstack1ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠬࢄࠧࢆ")), bstack11ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack11ll11_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack1ll1ll1ll_opy_ = 0
bstack11l1l11l1_opy_ = 0
bstack1ll11lllll_opy_ = []
bstack111111111_opy_ = []
bstack1ll1ll1ll1_opy_ = []
bstack1llll11111_opy_ = []
bstack1ll1l1l111_opy_ = bstack11ll11_opy_ (u"ࠨࠩࢉ")
bstack1lll11lll_opy_ = bstack11ll11_opy_ (u"ࠩࠪࢊ")
bstack1111l1lll_opy_ = False
bstack1l1ll1111_opy_ = False
bstack1ll1llll1_opy_ = {}
bstack1lll1ll11l_opy_ = None
bstack1l1l11lll_opy_ = None
bstack11lll1ll1_opy_ = None
bstack1llll1l1l1_opy_ = None
bstack1ll1111ll_opy_ = None
bstack1l1l111ll1_opy_ = None
bstack11l11l1l1_opy_ = None
bstack1llll111l1_opy_ = None
bstack1l11l1l11_opy_ = None
bstack11lll1l11_opy_ = None
bstack1l1ll11l1l_opy_ = None
bstack1lll111l1l_opy_ = None
bstack11ll1ll11_opy_ = None
bstack1lllll1lll_opy_ = None
bstack1llllll111_opy_ = None
bstack1l1llllll_opy_ = None
bstack111l1ll1l_opy_ = None
bstack1llll1111l_opy_ = None
bstack11l11l1ll_opy_ = None
bstack1l111l111_opy_ = None
bstack1lll11ll11_opy_ = None
bstack1ll1llllll_opy_ = False
bstack1lllll1l11_opy_ = bstack11ll11_opy_ (u"ࠥࠦࢋ")
logger = bstack1l1l1l1l11_opy_.get_logger(__name__, bstack1l1l11l11l_opy_)
bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
percy = bstack1lllll1ll1_opy_()
bstack1l1l11111l_opy_ = bstack1lll1l1l11_opy_()
def bstack11lll1111_opy_():
  global CONFIG
  global bstack1111l1lll_opy_
  global bstack1l1l1l1l1_opy_
  bstack1ll1ll1l1l_opy_ = bstack1lll1lll11_opy_(CONFIG)
  if (bstack11ll11_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ࢌ") in bstack1ll1ll1l1l_opy_ and str(bstack1ll1ll1l1l_opy_[bstack11ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ")]).lower() == bstack11ll11_opy_ (u"࠭ࡴࡳࡷࡨࠫࢎ")):
    bstack1111l1lll_opy_ = True
  bstack1l1l1l1l1_opy_.bstack1l11l1l11l_opy_(bstack1ll1ll1l1l_opy_.get(bstack11ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ࢏"), False))
def bstack1ll1lll1l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack111ll1l11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11l1l1l1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11ll11_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack11ll11_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack111lll1l1_opy_
      bstack111lll1l1_opy_ += bstack11ll11_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1lllll111_opy_ = re.compile(bstack11ll11_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack1111l1ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1lllll111_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11ll11_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack11ll11_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack111llll1l_opy_():
  bstack1ll1l1ll1l_opy_ = bstack11l1l1l1_opy_()
  if bstack1ll1l1ll1l_opy_ and os.path.exists(os.path.abspath(bstack1ll1l1ll1l_opy_)):
    fileName = bstack1ll1l1ll1l_opy_
  if bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack11ll111_opy_ = os.path.abspath(fileName)
  else:
    bstack11ll111_opy_ = bstack11ll11_opy_ (u"࢛ࠬ࠭")
  bstack1ll1111ll1_opy_ = os.getcwd()
  bstack1l1ll1l1ll_opy_ = bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack11lll11l1_opy_ = bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack11ll111_opy_)) and bstack1ll1111ll1_opy_ != bstack11ll11_opy_ (u"ࠣࠤ࢞"):
    bstack11ll111_opy_ = os.path.join(bstack1ll1111ll1_opy_, bstack1l1ll1l1ll_opy_)
    if not os.path.exists(bstack11ll111_opy_):
      bstack11ll111_opy_ = os.path.join(bstack1ll1111ll1_opy_, bstack11lll11l1_opy_)
    if bstack1ll1111ll1_opy_ != os.path.dirname(bstack1ll1111ll1_opy_):
      bstack1ll1111ll1_opy_ = os.path.dirname(bstack1ll1111ll1_opy_)
    else:
      bstack1ll1111ll1_opy_ = bstack11ll11_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack11ll111_opy_):
    bstack1111ll1l1_opy_(
      bstack1l1l1l11l_opy_.format(os.getcwd()))
  try:
    with open(bstack11ll111_opy_, bstack11ll11_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack11ll11_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1lllll111_opy_)
      yaml.add_constructor(bstack11ll11_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack1111l1ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11ll111_opy_, bstack11ll11_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1111ll1l1_opy_(bstack1l1ll11ll1_opy_.format(str(exc)))
def bstack11l11lll_opy_(config):
  bstack1ll11l1l11_opy_ = bstack111l1l1l1_opy_(config)
  for option in list(bstack1ll11l1l11_opy_):
    if option.lower() in bstack1l11ll1l1l_opy_ and option != bstack1l11ll1l1l_opy_[option.lower()]:
      bstack1ll11l1l11_opy_[bstack1l11ll1l1l_opy_[option.lower()]] = bstack1ll11l1l11_opy_[option]
      del bstack1ll11l1l11_opy_[option]
  return config
def bstack111l1l11l_opy_():
  global bstack111ll1l1l_opy_
  for key, bstack1l11111l1_opy_ in bstack1l11l1ll_opy_.items():
    if isinstance(bstack1l11111l1_opy_, list):
      for var in bstack1l11111l1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111ll1l1l_opy_[key] = os.environ[var]
          break
    elif bstack1l11111l1_opy_ in os.environ and os.environ[bstack1l11111l1_opy_] and str(os.environ[bstack1l11111l1_opy_]).strip():
      bstack111ll1l1l_opy_[key] = os.environ[bstack1l11111l1_opy_]
  if bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack111ll1l1l_opy_[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack111ll1l1l_opy_[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack11ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack1111l111l_opy_():
  global bstack1ll1l111l1_opy_
  global bstack111lll1l1_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack11ll11_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1ll1l111l1_opy_[bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1ll1l111l1_opy_[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1l11ll1lll_opy_ in bstack1ll1llll11_opy_.items():
    if isinstance(bstack1l11ll1lll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1l11ll1lll_opy_:
          if idx < len(sys.argv) and bstack11ll11_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1ll1l111l1_opy_:
            bstack1ll1l111l1_opy_[key] = sys.argv[idx + 1]
            bstack111lll1l1_opy_ += bstack11ll11_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack11ll11_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack11ll11_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack1l11ll1lll_opy_.lower() == val.lower() and not key in bstack1ll1l111l1_opy_:
          bstack1ll1l111l1_opy_[key] = sys.argv[idx + 1]
          bstack111lll1l1_opy_ += bstack11ll11_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack1l11ll1lll_opy_ + bstack11ll11_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1ll1l11111_opy_(config):
  bstack11l1ll1l1_opy_ = config.keys()
  for bstack11l11ll1_opy_, bstack1ll11111_opy_ in bstack1l11l11ll1_opy_.items():
    if bstack1ll11111_opy_ in bstack11l1ll1l1_opy_:
      config[bstack11l11ll1_opy_] = config[bstack1ll11111_opy_]
      del config[bstack1ll11111_opy_]
  for bstack11l11ll1_opy_, bstack1ll11111_opy_ in bstack111l11ll1_opy_.items():
    if isinstance(bstack1ll11111_opy_, list):
      for bstack1ll111111l_opy_ in bstack1ll11111_opy_:
        if bstack1ll111111l_opy_ in bstack11l1ll1l1_opy_:
          config[bstack11l11ll1_opy_] = config[bstack1ll111111l_opy_]
          del config[bstack1ll111111l_opy_]
          break
    elif bstack1ll11111_opy_ in bstack11l1ll1l1_opy_:
      config[bstack11l11ll1_opy_] = config[bstack1ll11111_opy_]
      del config[bstack1ll11111_opy_]
  for bstack1ll111111l_opy_ in list(config):
    for bstack1l1llll1ll_opy_ in bstack1l1111111_opy_:
      if bstack1ll111111l_opy_.lower() == bstack1l1llll1ll_opy_.lower() and bstack1ll111111l_opy_ != bstack1l1llll1ll_opy_:
        config[bstack1l1llll1ll_opy_] = config[bstack1ll111111l_opy_]
        del config[bstack1ll111111l_opy_]
  bstack11l111111_opy_ = []
  if bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ") in config:
    bstack11l111111_opy_ = config[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")]
  for platform in bstack11l111111_opy_:
    for bstack1ll111111l_opy_ in list(platform):
      for bstack1l1llll1ll_opy_ in bstack1l1111111_opy_:
        if bstack1ll111111l_opy_.lower() == bstack1l1llll1ll_opy_.lower() and bstack1ll111111l_opy_ != bstack1l1llll1ll_opy_:
          platform[bstack1l1llll1ll_opy_] = platform[bstack1ll111111l_opy_]
          del platform[bstack1ll111111l_opy_]
  for bstack11l11ll1_opy_, bstack1ll11111_opy_ in bstack111l11ll1_opy_.items():
    for platform in bstack11l111111_opy_:
      if isinstance(bstack1ll11111_opy_, list):
        for bstack1ll111111l_opy_ in bstack1ll11111_opy_:
          if bstack1ll111111l_opy_ in platform:
            platform[bstack11l11ll1_opy_] = platform[bstack1ll111111l_opy_]
            del platform[bstack1ll111111l_opy_]
            break
      elif bstack1ll11111_opy_ in platform:
        platform[bstack11l11ll1_opy_] = platform[bstack1ll11111_opy_]
        del platform[bstack1ll11111_opy_]
  for bstack1111llll_opy_ in bstack11111l11l_opy_:
    if bstack1111llll_opy_ in config:
      if not bstack11111l11l_opy_[bstack1111llll_opy_] in config:
        config[bstack11111l11l_opy_[bstack1111llll_opy_]] = {}
      config[bstack11111l11l_opy_[bstack1111llll_opy_]].update(config[bstack1111llll_opy_])
      del config[bstack1111llll_opy_]
  for platform in bstack11l111111_opy_:
    for bstack1111llll_opy_ in bstack11111l11l_opy_:
      if bstack1111llll_opy_ in list(platform):
        if not bstack11111l11l_opy_[bstack1111llll_opy_] in platform:
          platform[bstack11111l11l_opy_[bstack1111llll_opy_]] = {}
        platform[bstack11111l11l_opy_[bstack1111llll_opy_]].update(platform[bstack1111llll_opy_])
        del platform[bstack1111llll_opy_]
  config = bstack11l11lll_opy_(config)
  return config
def bstack1l11l1l1_opy_(config):
  global bstack111111ll_opy_
  if bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࢵ") in config and str(config[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ")]).lower() != bstack11ll11_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࢷ"):
    if not bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢸ") in config:
      config[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ")] = {}
    if not bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢺ") in config[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")]:
      bstack11l11l11l_opy_ = datetime.datetime.now()
      bstack111ll1111_opy_ = bstack11l11l11l_opy_.strftime(bstack11ll11_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧࢼ"))
      hostname = socket.gethostname()
      bstack1lllllll1l_opy_ = bstack11ll11_opy_ (u"ࠫࠬࢽ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11ll11_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧࢾ").format(bstack111ll1111_opy_, hostname, bstack1lllllll1l_opy_)
      config[bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")][bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣀ")] = identifier
    bstack111111ll_opy_ = config[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣁ")][bstack11ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣂ")]
  return config
def bstack11l11111l_opy_():
  bstack111l11ll_opy_ =  bstack11lllll1_opy_()[bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩࣃ")]
  return bstack111l11ll_opy_ if bstack111l11ll_opy_ else -1
def bstack11l1ll1l_opy_(bstack111l11ll_opy_):
  global CONFIG
  if not bstack11ll11_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣄ") in CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣅ")]:
    return
  CONFIG[bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")] = CONFIG[bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")].replace(
    bstack11ll11_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ"),
    str(bstack111l11ll_opy_)
  )
def bstack1lll111lll_opy_():
  global CONFIG
  if not bstack11ll11_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨࣉ") in CONFIG[bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")]:
    return
  bstack11l11l11l_opy_ = datetime.datetime.now()
  bstack111ll1111_opy_ = bstack11l11l11l_opy_.strftime(bstack11ll11_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ࣋"))
  CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌")] = CONFIG[bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")].replace(
    bstack11ll11_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭࣎"),
    bstack111ll1111_opy_
  )
def bstack1111l1ll1_opy_():
  global CONFIG
  if bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ") in CONFIG and not bool(CONFIG[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")]):
    del CONFIG[bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")]
    return
  if not bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭") in CONFIG:
    CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")] = bstack11ll11_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣔ")
  if bstack11ll11_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭ࣕ") in CONFIG[bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ")]:
    bstack1lll111lll_opy_()
    os.environ[bstack11ll11_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ࣗ")] = CONFIG[bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣘ")]
  if not bstack11ll11_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣙ") in CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    return
  bstack111l11ll_opy_ = bstack11ll11_opy_ (u"࠭ࠧࣛ")
  bstack1l1llll111_opy_ = bstack11l11111l_opy_()
  if bstack1l1llll111_opy_ != -1:
    bstack111l11ll_opy_ = bstack11ll11_opy_ (u"ࠧࡄࡋࠣࠫࣜ") + str(bstack1l1llll111_opy_)
  if bstack111l11ll_opy_ == bstack11ll11_opy_ (u"ࠨࠩࣝ"):
    bstack1lllll1111_opy_ = bstack11llllll_opy_(CONFIG[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬࣞ")])
    if bstack1lllll1111_opy_ != -1:
      bstack111l11ll_opy_ = str(bstack1lllll1111_opy_)
  if bstack111l11ll_opy_:
    bstack11l1ll1l_opy_(bstack111l11ll_opy_)
    os.environ[bstack11ll11_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧࣟ")] = CONFIG[bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")]
def bstack1lll111l1_opy_(bstack1l1111l1_opy_, bstack11111111_opy_, path):
  bstack1lll11llll_opy_ = {
    bstack11ll11_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣡"): bstack11111111_opy_
  }
  if os.path.exists(path):
    bstack1ll1l1ll1_opy_ = json.load(open(path, bstack11ll11_opy_ (u"࠭ࡲࡣࠩ࣢")))
  else:
    bstack1ll1l1ll1_opy_ = {}
  bstack1ll1l1ll1_opy_[bstack1l1111l1_opy_] = bstack1lll11llll_opy_
  with open(path, bstack11ll11_opy_ (u"ࠢࡸࣣ࠭ࠥ")) as outfile:
    json.dump(bstack1ll1l1ll1_opy_, outfile)
def bstack11llllll_opy_(bstack1l1111l1_opy_):
  bstack1l1111l1_opy_ = str(bstack1l1111l1_opy_)
  bstack1ll11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠨࢀࠪࣤ")), bstack11ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩࣥ"))
  try:
    if not os.path.exists(bstack1ll11llll1_opy_):
      os.makedirs(bstack1ll11llll1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠪࢂࣦࠬ")), bstack11ll11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫࣧ"), bstack11ll11_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧࣨ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11ll11_opy_ (u"࠭ࡷࠨࣩ")):
        pass
      with open(file_path, bstack11ll11_opy_ (u"ࠢࡸ࠭ࠥ࣪")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11ll11_opy_ (u"ࠨࡴࠪ࣫")) as bstack1l1l1ll1_opy_:
      bstack11ll1l1ll_opy_ = json.load(bstack1l1l1ll1_opy_)
    if bstack1l1111l1_opy_ in bstack11ll1l1ll_opy_:
      bstack1l111l1l1_opy_ = bstack11ll1l1ll_opy_[bstack1l1111l1_opy_][bstack11ll11_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣬")]
      bstack1l11l1ll1_opy_ = int(bstack1l111l1l1_opy_) + 1
      bstack1lll111l1_opy_(bstack1l1111l1_opy_, bstack1l11l1ll1_opy_, file_path)
      return bstack1l11l1ll1_opy_
    else:
      bstack1lll111l1_opy_(bstack1l1111l1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l11llllll_opy_.format(str(e)))
    return -1
def bstack1l1lll1l_opy_(config):
  if not config[bstack11ll11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ࣭ࠬ")] or not config[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ࣮ࠧ")]:
    return True
  else:
    return False
def bstack1l111llll_opy_(config, index=0):
  global bstack11llll1l_opy_
  bstack11l1l111_opy_ = {}
  caps = bstack11ll1ll1_opy_ + bstack1lll1l1ll1_opy_
  if bstack11llll1l_opy_:
    caps += bstack111111l1l_opy_
  for key in config:
    if key in caps + [bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࣯")]:
      continue
    bstack11l1l111_opy_[key] = config[key]
  if bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ") in config:
    for bstack1ll1l1ll_opy_ in config[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")][index]:
      if bstack1ll1l1ll_opy_ in caps + [bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣲ࠭"), bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪࣳ")]:
        continue
      bstack11l1l111_opy_[bstack1ll1l1ll_opy_] = config[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ")][index][bstack1ll1l1ll_opy_]
  bstack11l1l111_opy_[bstack11ll11_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࣵ")] = socket.gethostname()
  if bstack11ll11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࣶ࠭") in bstack11l1l111_opy_:
    del (bstack11l1l111_opy_[bstack11ll11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ")])
  return bstack11l1l111_opy_
def bstack1l11l11ll_opy_(config):
  global bstack11llll1l_opy_
  bstack1l1llll11l_opy_ = {}
  caps = bstack1lll1l1ll1_opy_
  if bstack11llll1l_opy_:
    caps += bstack111111l1l_opy_
  for key in caps:
    if key in config:
      bstack1l1llll11l_opy_[key] = config[key]
  return bstack1l1llll11l_opy_
def bstack111l1llll_opy_(bstack11l1l111_opy_, bstack1l1llll11l_opy_):
  bstack11lll11ll_opy_ = {}
  for key in bstack11l1l111_opy_.keys():
    if key in bstack1l11l11ll1_opy_:
      bstack11lll11ll_opy_[bstack1l11l11ll1_opy_[key]] = bstack11l1l111_opy_[key]
    else:
      bstack11lll11ll_opy_[key] = bstack11l1l111_opy_[key]
  for key in bstack1l1llll11l_opy_:
    if key in bstack1l11l11ll1_opy_:
      bstack11lll11ll_opy_[bstack1l11l11ll1_opy_[key]] = bstack1l1llll11l_opy_[key]
    else:
      bstack11lll11ll_opy_[key] = bstack1l1llll11l_opy_[key]
  return bstack11lll11ll_opy_
def bstack11l11l1l_opy_(config, index=0):
  global bstack11llll1l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l11lll1l1_opy_ = bstack1l1l1lll11_opy_(bstack1l1l11l11_opy_, config, logger)
  bstack1l1llll11l_opy_ = bstack1l11l11ll_opy_(config)
  bstack1ll11l1l_opy_ = bstack1lll1l1ll1_opy_
  bstack1ll11l1l_opy_ += bstack1ll1111l1l_opy_
  bstack1l1llll11l_opy_ = update(bstack1l1llll11l_opy_, bstack1l11lll1l1_opy_)
  if bstack11llll1l_opy_:
    bstack1ll11l1l_opy_ += bstack111111l1l_opy_
  if bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ") in config:
    if bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣹ࠭") in config[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࣺࠬ")][index]:
      caps[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣻ")] = config[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ")][index][bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ")]
    if bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣾ") in config[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣿ")][index]:
      caps[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऀ")] = str(config[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬँ")][index][bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं")])
    bstack111ll1l1_opy_ = bstack1l1l1lll11_opy_(bstack1l1l11l11_opy_, config[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index], logger)
    bstack1ll11l1l_opy_ += list(bstack111ll1l1_opy_.keys())
    for bstack1111lll1l_opy_ in bstack1ll11l1l_opy_:
      if bstack1111lll1l_opy_ in config[bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऄ")][index]:
        if bstack1111lll1l_opy_ == bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨअ"):
          try:
            bstack111ll1l1_opy_[bstack1111lll1l_opy_] = str(config[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪआ")][index][bstack1111lll1l_opy_] * 1.0)
          except:
            bstack111ll1l1_opy_[bstack1111lll1l_opy_] = str(config[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack1111lll1l_opy_])
        else:
          bstack111ll1l1_opy_[bstack1111lll1l_opy_] = config[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack1111lll1l_opy_]
        del (config[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1111lll1l_opy_])
    bstack1l1llll11l_opy_ = update(bstack1l1llll11l_opy_, bstack111ll1l1_opy_)
  bstack11l1l111_opy_ = bstack1l111llll_opy_(config, index)
  for bstack1ll111111l_opy_ in bstack1lll1l1ll1_opy_ + [bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऊ"), bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऋ")] + list(bstack1l11lll1l1_opy_.keys()):
    if bstack1ll111111l_opy_ in bstack11l1l111_opy_:
      bstack1l1llll11l_opy_[bstack1ll111111l_opy_] = bstack11l1l111_opy_[bstack1ll111111l_opy_]
      del (bstack11l1l111_opy_[bstack1ll111111l_opy_])
  if bstack111111ll1_opy_(config):
    bstack11l1l111_opy_[bstack11ll11_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ऌ")] = True
    caps.update(bstack1l1llll11l_opy_)
    caps[bstack11ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨऍ")] = bstack11l1l111_opy_
  else:
    bstack11l1l111_opy_[bstack11ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨऎ")] = False
    caps.update(bstack111l1llll_opy_(bstack11l1l111_opy_, bstack1l1llll11l_opy_))
    if bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧए") in caps:
      caps[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫऐ")] = caps[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऑ")]
      del (caps[bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ")])
    if bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧओ") in caps:
      caps[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩऔ")] = caps[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩक")]
      del (caps[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख")])
  return caps
def bstack1llllll11_opy_():
  global bstack1l11l1l1l1_opy_
  if bstack111ll1l11_opy_() <= version.parse(bstack11ll11_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪग")):
    if bstack1l11l1l1l1_opy_ != bstack11ll11_opy_ (u"ࠫࠬघ"):
      return bstack11ll11_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨङ") + bstack1l11l1l1l1_opy_ + bstack11ll11_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥच")
    return bstack1l1ll111l1_opy_
  if bstack1l11l1l1l1_opy_ != bstack11ll11_opy_ (u"ࠧࠨछ"):
    return bstack11ll11_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥज") + bstack1l11l1l1l1_opy_ + bstack11ll11_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥझ")
  return bstack11l11ll1l_opy_
def bstack1l11111ll_opy_(options):
  return hasattr(options, bstack11ll11_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫञ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1111l111_opy_(options, bstack1l1l1ll1l1_opy_):
  for bstack111lll1l_opy_ in bstack1l1l1ll1l1_opy_:
    if bstack111lll1l_opy_ in [bstack11ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩट"), bstack11ll11_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩठ")]:
      continue
    if bstack111lll1l_opy_ in options._experimental_options:
      options._experimental_options[bstack111lll1l_opy_] = update(options._experimental_options[bstack111lll1l_opy_],
                                                         bstack1l1l1ll1l1_opy_[bstack111lll1l_opy_])
    else:
      options.add_experimental_option(bstack111lll1l_opy_, bstack1l1l1ll1l1_opy_[bstack111lll1l_opy_])
  if bstack11ll11_opy_ (u"࠭ࡡࡳࡩࡶࠫड") in bstack1l1l1ll1l1_opy_:
    for arg in bstack1l1l1ll1l1_opy_[bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬढ")]:
      options.add_argument(arg)
    del (bstack1l1l1ll1l1_opy_[bstack11ll11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ण")])
  if bstack11ll11_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭त") in bstack1l1l1ll1l1_opy_:
    for ext in bstack1l1l1ll1l1_opy_[bstack11ll11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ")]:
      options.add_extension(ext)
    del (bstack1l1l1ll1l1_opy_[bstack11ll11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨद")])
def bstack1lll1l11_opy_(options, bstack1l1l1111l1_opy_):
  if bstack11ll11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫध") in bstack1l1l1111l1_opy_:
    for bstack1lllll1l1l_opy_ in bstack1l1l1111l1_opy_[bstack11ll11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन")]:
      if bstack1lllll1l1l_opy_ in options._preferences:
        options._preferences[bstack1lllll1l1l_opy_] = update(options._preferences[bstack1lllll1l1l_opy_], bstack1l1l1111l1_opy_[bstack11ll11_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")][bstack1lllll1l1l_opy_])
      else:
        options.set_preference(bstack1lllll1l1l_opy_, bstack1l1l1111l1_opy_[bstack11ll11_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप")][bstack1lllll1l1l_opy_])
  if bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧफ") in bstack1l1l1111l1_opy_:
    for arg in bstack1l1l1111l1_opy_[bstack11ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨब")]:
      options.add_argument(arg)
def bstack1lllllllll_opy_(options, bstack1111111l_opy_):
  if bstack11ll11_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬभ") in bstack1111111l_opy_:
    options.use_webview(bool(bstack1111111l_opy_[bstack11ll11_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭म")]))
  bstack1111l111_opy_(options, bstack1111111l_opy_)
def bstack1l1l1l11ll_opy_(options, bstack1ll1l1l11l_opy_):
  for bstack11111ll1_opy_ in bstack1ll1l1l11l_opy_:
    if bstack11111ll1_opy_ in [bstack11ll11_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪय"), bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬर")]:
      continue
    options.set_capability(bstack11111ll1_opy_, bstack1ll1l1l11l_opy_[bstack11111ll1_opy_])
  if bstack11ll11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ") in bstack1ll1l1l11l_opy_:
    for arg in bstack1ll1l1l11l_opy_[bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧल")]:
      options.add_argument(arg)
  if bstack11ll11_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧळ") in bstack1ll1l1l11l_opy_:
    options.bstack1111l11l_opy_(bool(bstack1ll1l1l11l_opy_[bstack11ll11_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨऴ")]))
def bstack11l1111l_opy_(options, bstack1lllll11l1_opy_):
  for bstack1ll111l11_opy_ in bstack1lllll11l1_opy_:
    if bstack1ll111l11_opy_ in [bstack11ll11_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩव"), bstack11ll11_opy_ (u"࠭ࡡࡳࡩࡶࠫश")]:
      continue
    options._options[bstack1ll111l11_opy_] = bstack1lllll11l1_opy_[bstack1ll111l11_opy_]
  if bstack11ll11_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫष") in bstack1lllll11l1_opy_:
    for bstack1l11l1l1l_opy_ in bstack1lllll11l1_opy_[bstack11ll11_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस")]:
      options.bstack1lll11111_opy_(
        bstack1l11l1l1l_opy_, bstack1lllll11l1_opy_[bstack11ll11_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ह")][bstack1l11l1l1l_opy_])
  if bstack11ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨऺ") in bstack1lllll11l1_opy_:
    for arg in bstack1lllll11l1_opy_[bstack11ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩऻ")]:
      options.add_argument(arg)
def bstack11l11lll1_opy_(options, caps):
  if not hasattr(options, bstack11ll11_opy_ (u"ࠬࡑࡅ़࡚ࠩ")):
    return
  if options.KEY == bstack11ll11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫऽ") and options.KEY in caps:
    bstack1111l111_opy_(options, caps[bstack11ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬा")])
  elif options.KEY == bstack11ll11_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ि") and options.KEY in caps:
    bstack1lll1l11_opy_(options, caps[bstack11ll11_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧी")])
  elif options.KEY == bstack11ll11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫु") and options.KEY in caps:
    bstack1l1l1l11ll_opy_(options, caps[bstack11ll11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬू")])
  elif options.KEY == bstack11ll11_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ृ") and options.KEY in caps:
    bstack1lllllllll_opy_(options, caps[bstack11ll11_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॄ")])
  elif options.KEY == bstack11ll11_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ॅ") and options.KEY in caps:
    bstack11l1111l_opy_(options, caps[bstack11ll11_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॆ")])
def bstack1ll1ll1l_opy_(caps):
  global bstack11llll1l_opy_
  if isinstance(os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪे")), str):
    bstack11llll1l_opy_ = eval(os.getenv(bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫै")))
  if bstack11llll1l_opy_:
    if bstack1ll1lll1l1_opy_() < version.parse(bstack11ll11_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪॉ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬॊ")
    if bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫो") in caps:
      browser = caps[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬौ")]
    elif bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ्ࠩ") in caps:
      browser = caps[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪॎ")]
    browser = str(browser).lower()
    if browser == bstack11ll11_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪॏ") or browser == bstack11ll11_opy_ (u"ࠫ࡮ࡶࡡࡥࠩॐ"):
      browser = bstack11ll11_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ॑")
    if browser == bstack11ll11_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭॒ࠧ"):
      browser = bstack11ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ॓")
    if browser not in [bstack11ll11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ॔"), bstack11ll11_opy_ (u"ࠩࡨࡨ࡬࡫ࠧॕ"), bstack11ll11_opy_ (u"ࠪ࡭ࡪ࠭ॖ"), bstack11ll11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॗ"), bstack11ll11_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭क़")]:
      return None
    try:
      package = bstack11ll11_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨख़").format(browser)
      name = bstack11ll11_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨग़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l11111ll_opy_(options):
        return None
      for bstack1ll111111l_opy_ in caps.keys():
        options.set_capability(bstack1ll111111l_opy_, caps[bstack1ll111111l_opy_])
      bstack11l11lll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll11l1l_opy_(options, bstack1ll111l1l1_opy_):
  if not bstack1l11111ll_opy_(options):
    return
  for bstack1ll111111l_opy_ in bstack1ll111l1l1_opy_.keys():
    if bstack1ll111111l_opy_ in bstack1ll1111l1l_opy_:
      continue
    if bstack1ll111111l_opy_ in options._caps and type(options._caps[bstack1ll111111l_opy_]) in [dict, list]:
      options._caps[bstack1ll111111l_opy_] = update(options._caps[bstack1ll111111l_opy_], bstack1ll111l1l1_opy_[bstack1ll111111l_opy_])
    else:
      options.set_capability(bstack1ll111111l_opy_, bstack1ll111l1l1_opy_[bstack1ll111111l_opy_])
  bstack11l11lll1_opy_(options, bstack1ll111l1l1_opy_)
  if bstack11ll11_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧज़") in options._caps:
    if options._caps[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")] and options._caps[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨढ़")].lower() != bstack11ll11_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬफ़"):
      del options._caps[bstack11ll11_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫय़")]
def bstack11l1ll111_opy_(proxy_config):
  if bstack11ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪॠ") in proxy_config:
    proxy_config[bstack11ll11_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩॡ")] = proxy_config[bstack11ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬॢ")]
    del (proxy_config[bstack11ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ")])
  if bstack11ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭।") in proxy_config and proxy_config[bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ॥")].lower() != bstack11ll11_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ०"):
    proxy_config[bstack11ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ१")] = bstack11ll11_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧ२")
  if bstack11ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭३") in proxy_config:
    proxy_config[bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ४")] = bstack11ll11_opy_ (u"ࠪࡴࡦࡩࠧ५")
  return proxy_config
def bstack1l1lll11l1_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ६") in config:
    return proxy
  config[bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७")] = bstack11l1ll111_opy_(config[bstack11ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")])
  if proxy == None:
    proxy = Proxy(config[bstack11ll11_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९")])
  return proxy
def bstack1ll1llll_opy_(self):
  global CONFIG
  global bstack1lll111l1l_opy_
  try:
    proxy = bstack1l11l1ll1l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11ll11_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭॰")):
        proxies = bstack1l111lll1_opy_(proxy, bstack1llllll11_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l1lll_opy_ = proxies.popitem()
          if bstack11ll11_opy_ (u"ࠤ࠽࠳࠴ࠨॱ") in bstack1l1l1lll_opy_:
            return bstack1l1l1lll_opy_
          else:
            return bstack11ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦॲ") + bstack1l1l1lll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣॳ").format(str(e)))
  return bstack1lll111l1l_opy_(self)
def bstack1llll1l1_opy_():
  global CONFIG
  return bstack1l1ll1llll_opy_(CONFIG) and bstack11111llll_opy_() and bstack111ll1l11_opy_() >= version.parse(bstack1ll11l11l1_opy_)
def bstack1ll11lll1_opy_():
  global CONFIG
  return (bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨॴ") in CONFIG or bstack11ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪॵ") in CONFIG) and bstack1ll1ll11_opy_()
def bstack111l1l1l1_opy_(config):
  bstack1ll11l1l11_opy_ = {}
  if bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॶ") in config:
    bstack1ll11l1l11_opy_ = config[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॷ")]
  if bstack11ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॸ") in config:
    bstack1ll11l1l11_opy_ = config[bstack11ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩॹ")]
  proxy = bstack1l11l1ll1l_opy_(config)
  if proxy:
    if proxy.endswith(bstack11ll11_opy_ (u"ࠫ࠳ࡶࡡࡤࠩॺ")) and os.path.isfile(proxy):
      bstack1ll11l1l11_opy_[bstack11ll11_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨॻ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11ll11_opy_ (u"࠭࠮ࡱࡣࡦࠫॼ")):
        proxies = bstack111ll11l_opy_(config, bstack1llllll11_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l1lll_opy_ = proxies.popitem()
          if bstack11ll11_opy_ (u"ࠢ࠻࠱࠲ࠦॽ") in bstack1l1l1lll_opy_:
            parsed_url = urlparse(bstack1l1l1lll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11ll11_opy_ (u"ࠣ࠼࠲࠳ࠧॾ") + bstack1l1l1lll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll11l1l11_opy_[bstack11ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬॿ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll11l1l11_opy_[bstack11ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ঀ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll11l1l11_opy_[bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧঁ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll11l1l11_opy_[bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨং")] = str(parsed_url.password)
  return bstack1ll11l1l11_opy_
def bstack1lll1lll11_opy_(config):
  if bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫঃ") in config:
    return config[bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ঄")]
  return {}
def bstack11lllll1l_opy_(caps):
  global bstack111111ll_opy_
  if bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঅ") in caps:
    caps[bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪআ")][bstack11ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩই")] = True
    if bstack111111ll_opy_:
      caps[bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬঈ")][bstack11ll11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧউ")] = bstack111111ll_opy_
  else:
    caps[bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫঊ")] = True
    if bstack111111ll_opy_:
      caps[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঋ")] = bstack111111ll_opy_
def bstack1lll1111l1_opy_():
  global CONFIG
  if bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬঌ") in CONFIG and bstack111l1l1l_opy_(CONFIG[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭঍")]):
    bstack1ll11l1l11_opy_ = bstack111l1l1l1_opy_(CONFIG)
    bstack1lllll11l_opy_(CONFIG[bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭঎")], bstack1ll11l1l11_opy_)
def bstack1lllll11l_opy_(key, bstack1ll11l1l11_opy_):
  global bstack1l1l1lllll_opy_
  logger.info(bstack1ll1l111l_opy_)
  try:
    bstack1l1l1lllll_opy_ = Local()
    bstack11ll1l111_opy_ = {bstack11ll11_opy_ (u"ࠫࡰ࡫ࡹࠨএ"): key}
    bstack11ll1l111_opy_.update(bstack1ll11l1l11_opy_)
    logger.debug(bstack1l1l11l1_opy_.format(str(bstack11ll1l111_opy_)))
    bstack1l1l1lllll_opy_.start(**bstack11ll1l111_opy_)
    if bstack1l1l1lllll_opy_.isRunning():
      logger.info(bstack1ll1lll1l_opy_)
  except Exception as e:
    bstack1111ll1l1_opy_(bstack1l1ll1lll_opy_.format(str(e)))
def bstack1lll11111l_opy_():
  global bstack1l1l1lllll_opy_
  if bstack1l1l1lllll_opy_.isRunning():
    logger.info(bstack1llll1ll1l_opy_)
    bstack1l1l1lllll_opy_.stop()
  bstack1l1l1lllll_opy_ = None
def bstack1l1llll1l_opy_(bstack1111l1l1l_opy_=[]):
  global CONFIG
  bstack1lll1l1l1l_opy_ = []
  bstack1ll1ll1l11_opy_ = [bstack11ll11_opy_ (u"ࠬࡵࡳࠨঐ"), bstack11ll11_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ঑"), bstack11ll11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ঒"), bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪও"), bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧঔ"), bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫক")]
  try:
    for err in bstack1111l1l1l_opy_:
      bstack1ll11ll11l_opy_ = {}
      for k in bstack1ll1ll1l11_opy_:
        val = CONFIG[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧখ")][int(err[bstack11ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫগ")])].get(k)
        if val:
          bstack1ll11ll11l_opy_[k] = val
      if(err[bstack11ll11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬঘ")] != bstack11ll11_opy_ (u"ࠧࠨঙ")):
        bstack1ll11ll11l_opy_[bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹࡹࠧচ")] = {
          err[bstack11ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧছ")]: err[bstack11ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩজ")]
        }
        bstack1lll1l1l1l_opy_.append(bstack1ll11ll11l_opy_)
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡰࡴࡰࡥࡹࡺࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷ࠾ࠥ࠭ঝ") + str(e))
  finally:
    return bstack1lll1l1l1l_opy_
def bstack1l1l1l11_opy_(file_name):
  bstack1ll11l1ll1_opy_ = []
  try:
    bstack111l1lll1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack111l1lll1_opy_):
      with open(bstack111l1lll1_opy_) as f:
        bstack1l1l1ll111_opy_ = json.load(f)
        bstack1ll11l1ll1_opy_ = bstack1l1l1ll111_opy_
      os.remove(bstack111l1lll1_opy_)
    return bstack1ll11l1ll1_opy_
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡࡧࡵࡶࡴࡸࠠ࡭࡫ࡶࡸ࠿ࠦࠧঞ") + str(e))
def bstack1ll11111ll_opy_():
  global bstack1lllll1l11_opy_
  global bstack1l111l11l_opy_
  global bstack1ll11lllll_opy_
  global bstack111111111_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack1lll11lll_opy_
  global CONFIG
  bstack11ll111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧট"))
  if bstack11ll111ll_opy_ in [bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ঠ"), bstack11ll11_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧড")]:
    bstack1ll111ll1l_opy_()
  percy.shutdown()
  if bstack1lllll1l11_opy_:
    logger.warning(bstack1111111l1_opy_.format(str(bstack1lllll1l11_opy_)))
  else:
    try:
      bstack1ll1l1ll1_opy_ = bstack11l11l111_opy_(bstack11ll11_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨঢ"), logger)
      if bstack1ll1l1ll1_opy_.get(bstack11ll11_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨণ")) and bstack1ll1l1ll1_opy_.get(bstack11ll11_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩত")).get(bstack11ll11_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧথ")):
        logger.warning(bstack1111111l1_opy_.format(str(bstack1ll1l1ll1_opy_[bstack11ll11_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫদ")][bstack11ll11_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩধ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1lll1lll1l_opy_)
  global bstack1l1l1lllll_opy_
  if bstack1l1l1lllll_opy_:
    bstack1lll11111l_opy_()
  try:
    for driver in bstack1l111l11l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11llllll1_opy_)
  if bstack1lll11lll_opy_ == bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧন"):
    bstack1ll1ll1ll1_opy_ = bstack1l1l1l11_opy_(bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ঩"))
  if bstack1lll11lll_opy_ == bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪপ") and len(bstack111111111_opy_) == 0:
    bstack111111111_opy_ = bstack1l1l1l11_opy_(bstack11ll11_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩফ"))
    if len(bstack111111111_opy_) == 0:
      bstack111111111_opy_ = bstack1l1l1l11_opy_(bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫব"))
  bstack1l1l111l_opy_ = bstack11ll11_opy_ (u"࠭ࠧভ")
  if len(bstack1ll11lllll_opy_) > 0:
    bstack1l1l111l_opy_ = bstack1l1llll1l_opy_(bstack1ll11lllll_opy_)
  elif len(bstack111111111_opy_) > 0:
    bstack1l1l111l_opy_ = bstack1l1llll1l_opy_(bstack111111111_opy_)
  elif len(bstack1ll1ll1ll1_opy_) > 0:
    bstack1l1l111l_opy_ = bstack1l1llll1l_opy_(bstack1ll1ll1ll1_opy_)
  elif len(bstack1llll11111_opy_) > 0:
    bstack1l1l111l_opy_ = bstack1l1llll1l_opy_(bstack1llll11111_opy_)
  if bool(bstack1l1l111l_opy_):
    bstack1l1lllllll_opy_(bstack1l1l111l_opy_)
  else:
    bstack1l1lllllll_opy_()
  bstack1llll1llll_opy_(bstack1l1ll11l11_opy_, logger)
  bstack1l1l1l1l11_opy_.bstack11111l1l_opy_(CONFIG)
  if len(bstack1ll1ll1ll1_opy_) > 0:
    sys.exit(len(bstack1ll1ll1ll1_opy_))
def bstack1ll1l111ll_opy_(bstack111l11l1l_opy_, frame):
  global bstack1l1l1l1l1_opy_
  logger.error(bstack11ll1111l_opy_)
  bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪম"), bstack111l11l1l_opy_)
  if hasattr(signal, bstack11ll11_opy_ (u"ࠨࡕ࡬࡫ࡳࡧ࡬ࡴࠩয")):
    bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩর"), signal.Signals(bstack111l11l1l_opy_).name)
  else:
    bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ঱"), bstack11ll11_opy_ (u"ࠫࡘࡏࡇࡖࡐࡎࡒࡔ࡝ࡎࠨল"))
  bstack11ll111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭঳"))
  if bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭঴"):
    bstack1l1l111lll_opy_.stop(bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ঵")))
  bstack1ll11111ll_opy_()
  sys.exit(1)
def bstack1111ll1l1_opy_(err):
  logger.critical(bstack1ll11ll1_opy_.format(str(err)))
  bstack1l1lllllll_opy_(bstack1ll11ll1_opy_.format(str(err)), True)
  atexit.unregister(bstack1ll11111ll_opy_)
  bstack1ll111ll1l_opy_()
  sys.exit(1)
def bstack11l1llll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1lllllll_opy_(message, True)
  atexit.unregister(bstack1ll11111ll_opy_)
  bstack1ll111ll1l_opy_()
  sys.exit(1)
def bstack1l11lll1ll_opy_():
  global CONFIG
  global bstack1ll1l111l1_opy_
  global bstack111ll1l1l_opy_
  global bstack1l111ll1_opy_
  CONFIG = bstack111llll1l_opy_()
  load_dotenv(CONFIG.get(bstack11ll11_opy_ (u"ࠨࡧࡱࡺࡋ࡯࡬ࡦࠩশ")))
  bstack111l1l11l_opy_()
  bstack1111l111l_opy_()
  CONFIG = bstack1ll1l11111_opy_(CONFIG)
  update(CONFIG, bstack111ll1l1l_opy_)
  update(CONFIG, bstack1ll1l111l1_opy_)
  CONFIG = bstack1l11l1l1_opy_(CONFIG)
  bstack1l111ll1_opy_ = bstack11l1lll1l_opy_(CONFIG)
  bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪষ"), bstack1l111ll1_opy_)
  if (bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭স") in CONFIG and bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧহ") in bstack1ll1l111l1_opy_) or (
          bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ঺") in CONFIG and bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঻") not in bstack111ll1l1l_opy_):
    if os.getenv(bstack11ll11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇ়ࠫ")):
      CONFIG[bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪঽ")] = os.getenv(bstack11ll11_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭া"))
    else:
      bstack1111l1ll1_opy_()
  elif (bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ি") not in CONFIG and bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ী") in CONFIG) or (
          bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨু") in bstack111ll1l1l_opy_ and bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩূ") not in bstack1ll1l111l1_opy_):
    del (CONFIG[bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩৃ")])
  if bstack1l1lll1l_opy_(CONFIG):
    bstack1111ll1l1_opy_(bstack1111ll1l_opy_)
  bstack1l1l1l111l_opy_()
  bstack1ll111l111_opy_()
  if bstack11llll1l_opy_:
    CONFIG[bstack11ll11_opy_ (u"ࠨࡣࡳࡴࠬৄ")] = bstack1l111111_opy_(CONFIG)
    logger.info(bstack1l1l1l1ll1_opy_.format(CONFIG[bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࠭৅")]))
  if not bstack1l111ll1_opy_:
    CONFIG[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆")] = [{}]
def bstack1l1l1llll1_opy_(config, bstack11l1l11ll_opy_):
  global CONFIG
  global bstack11llll1l_opy_
  CONFIG = config
  bstack11llll1l_opy_ = bstack11l1l11ll_opy_
def bstack1ll111l111_opy_():
  global CONFIG
  global bstack11llll1l_opy_
  if bstack11ll11_opy_ (u"ࠫࡦࡶࡰࠨে") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11l1llll_opy_(e, bstack11l1l1l11_opy_)
    bstack11llll1l_opy_ = True
    bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫৈ"), True)
def bstack1l111111_opy_(config):
  bstack11ll11ll_opy_ = bstack11ll11_opy_ (u"࠭ࠧ৉")
  app = config[bstack11ll11_opy_ (u"ࠧࡢࡲࡳࠫ৊")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l111l1_opy_:
      if os.path.exists(app):
        bstack11ll11ll_opy_ = bstack1l1l11l1ll_opy_(config, app)
      elif bstack1llll1l1ll_opy_(app):
        bstack11ll11ll_opy_ = app
      else:
        bstack1111ll1l1_opy_(bstack1llll11l11_opy_.format(app))
    else:
      if bstack1llll1l1ll_opy_(app):
        bstack11ll11ll_opy_ = app
      elif os.path.exists(app):
        bstack11ll11ll_opy_ = bstack1l1l11l1ll_opy_(app)
      else:
        bstack1111ll1l1_opy_(bstack1l1lllll11_opy_)
  else:
    if len(app) > 2:
      bstack1111ll1l1_opy_(bstack1l11ll1l1_opy_)
    elif len(app) == 2:
      if bstack11ll11_opy_ (u"ࠨࡲࡤࡸ࡭࠭ো") in app and bstack11ll11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬৌ") in app:
        if os.path.exists(app[bstack11ll11_opy_ (u"ࠪࡴࡦࡺࡨࠨ্")]):
          bstack11ll11ll_opy_ = bstack1l1l11l1ll_opy_(config, app[bstack11ll11_opy_ (u"ࠫࡵࡧࡴࡩࠩৎ")], app[bstack11ll11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ৏")])
        else:
          bstack1111ll1l1_opy_(bstack1llll11l11_opy_.format(app))
      else:
        bstack1111ll1l1_opy_(bstack1l11ll1l1_opy_)
    else:
      for key in app:
        if key in bstack1lll111ll_opy_:
          if key == bstack11ll11_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ৐"):
            if os.path.exists(app[key]):
              bstack11ll11ll_opy_ = bstack1l1l11l1ll_opy_(config, app[key])
            else:
              bstack1111ll1l1_opy_(bstack1llll11l11_opy_.format(app))
          else:
            bstack11ll11ll_opy_ = app[key]
        else:
          bstack1111ll1l1_opy_(bstack1lllll1ll_opy_)
  return bstack11ll11ll_opy_
def bstack1llll1l1ll_opy_(bstack11ll11ll_opy_):
  import re
  bstack1ll1ll111l_opy_ = re.compile(bstack11ll11_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢ৑"))
  bstack1lllll111l_opy_ = re.compile(bstack11ll11_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰࠯࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ৒"))
  if bstack11ll11_opy_ (u"ࠩࡥࡷ࠿࠵࠯ࠨ৓") in bstack11ll11ll_opy_ or re.fullmatch(bstack1ll1ll111l_opy_, bstack11ll11ll_opy_) or re.fullmatch(bstack1lllll111l_opy_, bstack11ll11ll_opy_):
    return True
  else:
    return False
def bstack1l1l11l1ll_opy_(config, path, bstack1llll11ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11ll11_opy_ (u"ࠪࡶࡧ࠭৔")).read()).hexdigest()
  bstack1111ll11l_opy_ = bstack111l1l111_opy_(md5_hash)
  bstack11ll11ll_opy_ = None
  if bstack1111ll11l_opy_:
    logger.info(bstack1l1l1lll1_opy_.format(bstack1111ll11l_opy_, md5_hash))
    return bstack1111ll11l_opy_
  bstack11ll11111_opy_ = MultipartEncoder(
    fields={
      bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࠩ৕"): (os.path.basename(path), open(os.path.abspath(path), bstack11ll11_opy_ (u"ࠬࡸࡢࠨ৖")), bstack11ll11_opy_ (u"࠭ࡴࡦࡺࡷ࠳ࡵࡲࡡࡪࡰࠪৗ")),
      bstack11ll11_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ৘"): bstack1llll11ll_opy_
    }
  )
  response = requests.post(bstack1l11l11l1_opy_, data=bstack11ll11111_opy_,
                           headers={bstack11ll11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ৙"): bstack11ll11111_opy_.content_type},
                           auth=(config[bstack11ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ৚")], config[bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭৛")]))
  try:
    res = json.loads(response.text)
    bstack11ll11ll_opy_ = res[bstack11ll11_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰࠬড়")]
    logger.info(bstack11111ll11_opy_.format(bstack11ll11ll_opy_))
    bstack11l1l111l_opy_(md5_hash, bstack11ll11ll_opy_)
  except ValueError as err:
    bstack1111ll1l1_opy_(bstack1lll11l111_opy_.format(str(err)))
  return bstack11ll11ll_opy_
def bstack1l1l1l111l_opy_():
  global CONFIG
  global bstack1111llll1_opy_
  bstack1lll11l1l1_opy_ = 0
  bstack1l1l1l1l1l_opy_ = 1
  if bstack11ll11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬঢ়") in CONFIG:
    bstack1l1l1l1l1l_opy_ = CONFIG[bstack11ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭৞")]
  if bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪয়") in CONFIG:
    bstack1lll11l1l1_opy_ = len(CONFIG[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৠ")])
  bstack1111llll1_opy_ = int(bstack1l1l1l1l1l_opy_) * int(bstack1lll11l1l1_opy_)
def bstack111l1l111_opy_(md5_hash):
  bstack1l1ll1ll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠩࢁࠫৡ")), bstack11ll11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪৢ"), bstack11ll11_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬৣ"))
  if os.path.exists(bstack1l1ll1ll1_opy_):
    bstack1l11l1l111_opy_ = json.load(open(bstack1l1ll1ll1_opy_, bstack11ll11_opy_ (u"ࠬࡸࡢࠨ৤")))
    if md5_hash in bstack1l11l1l111_opy_:
      bstack1ll1111l1_opy_ = bstack1l11l1l111_opy_[md5_hash]
      bstack1ll1111lll_opy_ = datetime.datetime.now()
      bstack1l1l1l1lll_opy_ = datetime.datetime.strptime(bstack1ll1111l1_opy_[bstack11ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ৥")], bstack11ll11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ০"))
      if (bstack1ll1111lll_opy_ - bstack1l1l1l1lll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll1111l1_opy_[bstack11ll11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭১")]):
        return None
      return bstack1ll1111l1_opy_[bstack11ll11_opy_ (u"ࠩ࡬ࡨࠬ২")]
  else:
    return None
def bstack11l1l111l_opy_(md5_hash, bstack11ll11ll_opy_):
  bstack1ll11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠪࢂࠬ৩")), bstack11ll11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ৪"))
  if not os.path.exists(bstack1ll11llll1_opy_):
    os.makedirs(bstack1ll11llll1_opy_)
  bstack1l1ll1ll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠬࢄࠧ৫")), bstack11ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭৬"), bstack11ll11_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ৭"))
  bstack1l1l111l1l_opy_ = {
    bstack11ll11_opy_ (u"ࠨ࡫ࡧࠫ৮"): bstack11ll11ll_opy_,
    bstack11ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ৯"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll11_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧৰ")),
    bstack11ll11_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩৱ"): str(__version__)
  }
  if os.path.exists(bstack1l1ll1ll1_opy_):
    bstack1l11l1l111_opy_ = json.load(open(bstack1l1ll1ll1_opy_, bstack11ll11_opy_ (u"ࠬࡸࡢࠨ৲")))
  else:
    bstack1l11l1l111_opy_ = {}
  bstack1l11l1l111_opy_[md5_hash] = bstack1l1l111l1l_opy_
  with open(bstack1l1ll1ll1_opy_, bstack11ll11_opy_ (u"ࠨࡷࠬࠤ৳")) as outfile:
    json.dump(bstack1l11l1l111_opy_, outfile)
def bstack1ll11l11l_opy_(self):
  return
def bstack1llllllll_opy_(self):
  return
def bstack1ll1lll11_opy_(self):
  global bstack11ll1ll11_opy_
  bstack11ll1ll11_opy_(self)
def bstack1l1l11ll1_opy_():
  global bstack1ll11l1ll_opy_
  bstack1ll11l1ll_opy_ = True
def bstack1lll11l1ll_opy_(self):
  global bstack1l11llll1_opy_
  global bstack1l11llll11_opy_
  global bstack1l1l11lll_opy_
  try:
    if bstack11ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ৴") in bstack1l11llll1_opy_ and self.session_id != None and bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ৵"), bstack11ll11_opy_ (u"ࠩࠪ৶")) != bstack11ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ৷"):
      bstack1l1lllll1_opy_ = bstack11ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ৸") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ৹")
      if bstack1l1lllll1_opy_ == bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭৺"):
        bstack1ll1llll1l_opy_(logger)
      if self != None:
        bstack11l11ll11_opy_(self, bstack1l1lllll1_opy_, bstack11ll11_opy_ (u"ࠧ࠭ࠢࠪ৻").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11ll11_opy_ (u"ࠨࠩৼ")
    if bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ৽") in bstack1l11llll1_opy_ and getattr(threading.current_thread(), bstack11ll11_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ৾"), None):
      bstack11lll1l1_opy_.bstack1l1l1llll_opy_(self, bstack1ll1llll1_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧ৿") + str(e))
  bstack1l1l11lll_opy_(self)
  self.session_id = None
def bstack1lll1lll_opy_(self, command_executor=bstack11ll11_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ਀"), *args, **kwargs):
  bstack1ll1l11l1l_opy_ = bstack1lll1ll11l_opy_(self, command_executor, *args, **kwargs)
  try:
    logger.debug(bstack11ll11_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪਁ").format(str(command_executor)))
    logger.debug(bstack11ll11_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩਂ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫਃ") in command_executor._url:
      bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ਄"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ਅ") in command_executor):
    bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬਆ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1l111lll_opy_.bstack1l1lll1l1_opy_(self)
  return bstack1ll1l11l1l_opy_
def bstack1l11llll_opy_(args):
  return bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭ਇ") in str(args)
def bstack1ll1l1l1l_opy_(self, driver_command, *args, **kwargs):
  global bstack1l111l111_opy_
  global bstack1ll1llllll_opy_
  bstack1111l11ll_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪਈ"), None) and bstack1l1lll1ll1_opy_(
          threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ਉ"), None)
  bstack1l1l111111_opy_ = getattr(self, bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨਊ"), None) != None and getattr(self, bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ਋"), None) == True
  if not bstack1ll1llllll_opy_ and bstack1l111ll1_opy_ and bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ਌") in CONFIG and CONFIG[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ਍")] == True and bstack1ll1lll1ll_opy_.bstack1l111ll1l_opy_(driver_command) and (bstack1l1l111111_opy_ or bstack1111l11ll_opy_) and not bstack1l11llll_opy_(args):
    try:
      bstack1ll1llllll_opy_ = True
      logger.debug(bstack11ll11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ਎").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11ll11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫਏ").format(str(err)))
    bstack1ll1llllll_opy_ = False
  response = bstack1l111l111_opy_(self, driver_command, *args, **kwargs)
  if bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ਐ") in str(bstack1l11llll1_opy_).lower() and bstack1l1l111lll_opy_.on():
    try:
      if driver_command == bstack11ll11_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ਑"):
        bstack1l1l111lll_opy_.bstack1l1ll1ll11_opy_({
            bstack11ll11_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ਒"): response[bstack11ll11_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩਓ")],
            bstack11ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫਔ"): bstack1l1l111lll_opy_.current_test_uuid() if bstack1l1l111lll_opy_.current_test_uuid() else bstack1l1l111lll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack1l1l11l1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1l11llll11_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack1lll1ll111_opy_
  global bstack1l11lll1_opy_
  global bstack1l11ll11l1_opy_
  global bstack1l11llll1_opy_
  global bstack1lll1ll11l_opy_
  global bstack1l111l11l_opy_
  global bstack11ll1111_opy_
  global bstack1ll1llll1_opy_
  CONFIG[bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧਕ")] = str(bstack1l11llll1_opy_) + str(__version__)
  command_executor = bstack1llllll11_opy_()
  logger.debug(bstack1l1l1ll1ll_opy_.format(command_executor))
  proxy = bstack1l1lll11l1_opy_(CONFIG, proxy)
  bstack1llll111ll_opy_ = 0 if bstack1ll1l1l1l1_opy_ < 0 else bstack1ll1l1l1l1_opy_
  try:
    if bstack1l11lll1_opy_ is True:
      bstack1llll111ll_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l11ll11l1_opy_ is True:
      bstack1llll111ll_opy_ = int(threading.current_thread().name)
  except:
    bstack1llll111ll_opy_ = 0
  bstack1ll111l1l1_opy_ = bstack11l11l1l_opy_(CONFIG, bstack1llll111ll_opy_)
  logger.debug(bstack1111lllll_opy_.format(str(bstack1ll111l1l1_opy_)))
  if bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਖ") in CONFIG and bstack111l1l1l_opy_(CONFIG[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫਗ")]):
    bstack11lllll1l_opy_(bstack1ll111l1l1_opy_)
  if bstack1l111111l_opy_.bstack111l1ll11_opy_(CONFIG, bstack1llll111ll_opy_) and bstack1l111111l_opy_.bstack11ll11l1l_opy_(bstack1ll111l1l1_opy_, options):
    threading.current_thread().a11yPlatform = True
    bstack1l111111l_opy_.set_capabilities(bstack1ll111l1l1_opy_, CONFIG)
  if desired_capabilities:
    bstack111ll1ll1_opy_ = bstack1ll1l11111_opy_(desired_capabilities)
    bstack111ll1ll1_opy_[bstack11ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨਘ")] = bstack111111ll1_opy_(CONFIG)
    bstack1llll111_opy_ = bstack11l11l1l_opy_(bstack111ll1ll1_opy_)
    if bstack1llll111_opy_:
      bstack1ll111l1l1_opy_ = update(bstack1llll111_opy_, bstack1ll111l1l1_opy_)
    desired_capabilities = None
  if options:
    bstack1lll11l1l_opy_(options, bstack1ll111l1l1_opy_)
  if not options:
    options = bstack1ll1ll1l_opy_(bstack1ll111l1l1_opy_)
  bstack1ll1llll1_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਙ"))[bstack1llll111ll_opy_]
  if proxy and bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪਚ")):
    options.proxy(proxy)
  if options and bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪਛ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack111ll1l11_opy_() < version.parse(bstack11ll11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫਜ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1ll111l1l1_opy_)
  logger.info(bstack1111l1l11_opy_)
  if bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ਝ")):
    bstack1lll1ll11l_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ਞ")):
    bstack1lll1ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨਟ")):
    bstack1lll1ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1lll1ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l11lll11_opy_ = bstack11ll11_opy_ (u"ࠩࠪਠ")
    if bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫਡ")):
      bstack1l11lll11_opy_ = self.caps.get(bstack11ll11_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦਢ"))
    else:
      bstack1l11lll11_opy_ = self.capabilities.get(bstack11ll11_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧਣ"))
    if bstack1l11lll11_opy_:
      bstack11llll1ll_opy_(bstack1l11lll11_opy_)
      if bstack111ll1l11_opy_() <= version.parse(bstack11ll11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ਤ")):
        self.command_executor._url = bstack11ll11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣਥ") + bstack1l11l1l1l1_opy_ + bstack11ll11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧਦ")
      else:
        self.command_executor._url = bstack11ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦਧ") + bstack1l11lll11_opy_ + bstack11ll11_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦਨ")
      logger.debug(bstack1lll1ll11_opy_.format(bstack1l11lll11_opy_))
    else:
      logger.debug(bstack1l1ll11l_opy_.format(bstack11ll11_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧ਩")))
  except Exception as e:
    logger.debug(bstack1l1ll11l_opy_.format(e))
  if bstack11ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਪ") in bstack1l11llll1_opy_:
    bstack1l1ll1111l_opy_(bstack1ll1l1l1l1_opy_, bstack11ll1111_opy_)
  bstack1l11llll11_opy_ = self.session_id
  if bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ਫ") in bstack1l11llll1_opy_ or bstack11ll11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧਬ") in bstack1l11llll1_opy_ or bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧਭ") in bstack1l11llll1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l1l111lll_opy_.bstack1l1lll1l1_opy_(self)
  bstack1l111l11l_opy_.append(self)
  if bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਮ") in CONFIG and bstack11ll11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਯ") in CONFIG[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧਰ")][bstack1llll111ll_opy_]:
    bstack1lll1ll111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ਱")][bstack1llll111ll_opy_][bstack11ll11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਲ")]
  logger.debug(bstack111ll11ll_opy_.format(bstack1l11llll11_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1lll1ll1ll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1llll111l_opy_
      if(bstack11ll11_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤਲ਼") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠨࢀࠪ਴")), bstack11ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩਵ"), bstack11ll11_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬਸ਼")), bstack11ll11_opy_ (u"ࠫࡼ࠭਷")) as fp:
          fp.write(bstack11ll11_opy_ (u"ࠧࠨਸ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11ll11_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣਹ")))):
          with open(args[1], bstack11ll11_opy_ (u"ࠧࡳࠩ਺")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11ll11_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧ਻") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11l1111l1_opy_)
            lines.insert(1, bstack1l1llllll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11ll11_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶ਼ࠦ")), bstack11ll11_opy_ (u"ࠪࡻࠬ਽")) as bstack11l1lll11_opy_:
              bstack11l1lll11_opy_.writelines(lines)
        CONFIG[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ਾ")] = str(bstack1l11llll1_opy_) + str(__version__)
        bstack1llll111ll_opy_ = 0 if bstack1ll1l1l1l1_opy_ < 0 else bstack1ll1l1l1l1_opy_
        try:
          if bstack1l11lll1_opy_ is True:
            bstack1llll111ll_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l11ll11l1_opy_ is True:
            bstack1llll111ll_opy_ = int(threading.current_thread().name)
        except:
          bstack1llll111ll_opy_ = 0
        CONFIG[bstack11ll11_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧਿ")] = False
        CONFIG[bstack11ll11_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧੀ")] = True
        bstack1ll111l1l1_opy_ = bstack11l11l1l_opy_(CONFIG, bstack1llll111ll_opy_)
        logger.debug(bstack1111lllll_opy_.format(str(bstack1ll111l1l1_opy_)))
        if CONFIG.get(bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫੁ")):
          bstack11lllll1l_opy_(bstack1ll111l1l1_opy_)
        if bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫੂ") in CONFIG and bstack11ll11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ੃") in CONFIG[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭੄")][bstack1llll111ll_opy_]:
          bstack1lll1ll111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ੅")][bstack1llll111ll_opy_][bstack11ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੆")]
        args.append(os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"࠭ࡾࠨੇ")), bstack11ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧੈ"), bstack11ll11_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪ੉")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1ll111l1l1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11ll11_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ੊"))
      bstack1llll111l_opy_ = True
      return bstack1llllll111_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1l1ll111_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1ll1l1l1l1_opy_
    global bstack1lll1ll111_opy_
    global bstack1l11lll1_opy_
    global bstack1l11ll11l1_opy_
    global bstack1l11llll1_opy_
    CONFIG[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬੋ")] = str(bstack1l11llll1_opy_) + str(__version__)
    bstack1llll111ll_opy_ = 0 if bstack1ll1l1l1l1_opy_ < 0 else bstack1ll1l1l1l1_opy_
    try:
      if bstack1l11lll1_opy_ is True:
        bstack1llll111ll_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l11ll11l1_opy_ is True:
        bstack1llll111ll_opy_ = int(threading.current_thread().name)
    except:
      bstack1llll111ll_opy_ = 0
    CONFIG[bstack11ll11_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥੌ")] = True
    bstack1ll111l1l1_opy_ = bstack11l11l1l_opy_(CONFIG, bstack1llll111ll_opy_)
    logger.debug(bstack1111lllll_opy_.format(str(bstack1ll111l1l1_opy_)))
    if CONFIG.get(bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭੍ࠩ")):
      bstack11lllll1l_opy_(bstack1ll111l1l1_opy_)
    if bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੎") in CONFIG and bstack11ll11_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ੏") in CONFIG[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੐")][bstack1llll111ll_opy_]:
      bstack1lll1ll111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬੑ")][bstack1llll111ll_opy_][bstack11ll11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ੒")]
    import urllib
    import json
    bstack11lll111_opy_ = bstack11ll11_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭੓") + urllib.parse.quote(json.dumps(bstack1ll111l1l1_opy_))
    browser = self.connect(bstack11lll111_opy_)
    return browser
except Exception as e:
    pass
def bstack1lll1l1l1_opy_():
    global bstack1llll111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l1ll111_opy_
        bstack1llll111l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lll1ll1ll_opy_
      bstack1llll111l_opy_ = True
    except Exception as e:
      pass
def bstack1l1l11l111_opy_(context, bstack1ll111l1_opy_):
  try:
    context.page.evaluate(bstack11ll11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ੔"), bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ੕")+ json.dumps(bstack1ll111l1_opy_) + bstack11ll11_opy_ (u"ࠢࡾࡿࠥ੖"))
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ੗"), e)
def bstack1lll11lll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11ll11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ੘"), bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨਖ਼") + json.dumps(message) + bstack11ll11_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧਗ਼") + json.dumps(level) + bstack11ll11_opy_ (u"ࠬࢃࡽࠨਜ਼"))
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤੜ"), e)
def bstack1llll1111_opy_(self, url):
  global bstack1lllll1lll_opy_
  try:
    bstack1l1111ll_opy_(url)
  except Exception as err:
    logger.debug(bstack11l111l1l_opy_.format(str(err)))
  try:
    bstack1lllll1lll_opy_(self, url)
  except Exception as e:
    try:
      bstack1ll1111111_opy_ = str(e)
      if any(err_msg in bstack1ll1111111_opy_ for err_msg in bstack1ll1lllll1_opy_):
        bstack1l1111ll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l111l1l_opy_.format(str(err)))
    raise e
def bstack1ll111ll_opy_(self):
  global bstack1l111l1ll_opy_
  bstack1l111l1ll_opy_ = self
  return
def bstack1l1l1lll1l_opy_(self):
  global bstack1l11ll11_opy_
  bstack1l11ll11_opy_ = self
  return
def bstack1lll111ll1_opy_(test_name, bstack1l1lll1lll_opy_):
  global CONFIG
  if CONFIG.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭੝"), False):
    bstack1l1ll111ll_opy_ = os.path.relpath(bstack1l1lll1lll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l1ll111ll_opy_)
    bstack1l1lllll1l_opy_ = suite_name + bstack11ll11_opy_ (u"ࠣ࠯ࠥਫ਼") + test_name
    threading.current_thread().percySessionName = bstack1l1lllll1l_opy_
def bstack1llll1lll1_opy_(self, test, *args, **kwargs):
  global bstack11lll1ll1_opy_
  test_name = None
  bstack1l1lll1lll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1lll1lll_opy_ = str(test.source)
  bstack1lll111ll1_opy_(test_name, bstack1l1lll1lll_opy_)
  bstack11lll1ll1_opy_(self, test, *args, **kwargs)
def bstack1ll1ll11l1_opy_(driver, bstack1l1lllll1l_opy_):
  if not bstack1111l1lll_opy_ and bstack1l1lllll1l_opy_:
      bstack1ll11l1111_opy_ = {
          bstack11ll11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ੟"): bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੠"),
          bstack11ll11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ੡"): {
              bstack11ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ੢"): bstack1l1lllll1l_opy_
          }
      }
      bstack1ll1l11l1_opy_ = bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੣").format(json.dumps(bstack1ll11l1111_opy_))
      driver.execute_script(bstack1ll1l11l1_opy_)
  if bstack111lll1ll_opy_:
      bstack111llllll_opy_ = {
          bstack11ll11_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ੤"): bstack11ll11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ੥"),
          bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ੦"): {
              bstack11ll11_opy_ (u"ࠪࡨࡦࡺࡡࠨ੧"): bstack1l1lllll1l_opy_ + bstack11ll11_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭੨"),
              bstack11ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ੩"): bstack11ll11_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ੪")
          }
      }
      if bstack111lll1ll_opy_.status == bstack11ll11_opy_ (u"ࠧࡑࡃࡖࡗࠬ੫"):
          bstack11ll11lll_opy_ = bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭੬").format(json.dumps(bstack111llllll_opy_))
          driver.execute_script(bstack11ll11lll_opy_)
          bstack11l11ll11_opy_(driver, bstack11ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ੭"))
      elif bstack111lll1ll_opy_.status == bstack11ll11_opy_ (u"ࠪࡊࡆࡏࡌࠨ੮"):
          reason = bstack11ll11_opy_ (u"ࠦࠧ੯")
          bstack11l111ll1_opy_ = bstack1l1lllll1l_opy_ + bstack11ll11_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭ੰ")
          if bstack111lll1ll_opy_.message:
              reason = str(bstack111lll1ll_opy_.message)
              bstack11l111ll1_opy_ = bstack11l111ll1_opy_ + bstack11ll11_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭ੱ") + reason
          bstack111llllll_opy_[bstack11ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪੲ")] = {
              bstack11ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧੳ"): bstack11ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨੴ"),
              bstack11ll11_opy_ (u"ࠪࡨࡦࡺࡡࠨੵ"): bstack11l111ll1_opy_
          }
          bstack11ll11lll_opy_ = bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੶").format(json.dumps(bstack111llllll_opy_))
          driver.execute_script(bstack11ll11lll_opy_)
          bstack11l11ll11_opy_(driver, bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ੷"), reason)
          bstack11lllllll_opy_(reason, str(bstack111lll1ll_opy_), str(bstack1ll1l1l1l1_opy_), logger)
def bstack1ll1l1lll1_opy_(driver, test):
  if CONFIG.get(bstack11ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ੸"), False) and CONFIG.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪ੹"), bstack11ll11_opy_ (u"ࠣࡣࡸࡸࡴࠨ੺")) == bstack11ll11_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ੻"):
      bstack1ll11lll11_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭੼"), None)
      bstack1l1lll1111_opy_(driver, bstack1ll11lll11_opy_)
  if bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ੽"), None) and bstack1l1lll1ll1_opy_(
          threading.current_thread(), bstack11ll11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ੾"), None):
      logger.info(bstack11ll11_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨ੿"))
      bstack1l111111l_opy_.bstack1l1l111l11_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack1llllllll1_opy_=bstack1ll1llll1_opy_)
def bstack1ll111llll_opy_(test, bstack1l1lllll1l_opy_):
    try:
      data = {}
      if test:
        data[bstack11ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ઀")] = bstack1l1lllll1l_opy_
      if bstack111lll1ll_opy_:
        if bstack111lll1ll_opy_.status == bstack11ll11_opy_ (u"ࠨࡒࡄࡗࡘ࠭ઁ"):
          data[bstack11ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩં")] = bstack11ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪઃ")
        elif bstack111lll1ll_opy_.status == bstack11ll11_opy_ (u"ࠫࡋࡇࡉࡍࠩ઄"):
          data[bstack11ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬઅ")] = bstack11ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭આ")
          if bstack111lll1ll_opy_.message:
            data[bstack11ll11_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧઇ")] = str(bstack111lll1ll_opy_.message)
      user = CONFIG[bstack11ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪઈ")]
      key = CONFIG[bstack11ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬઉ")]
      url = bstack11ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨઊ").format(user, key, bstack1l11llll11_opy_)
      headers = {
        bstack11ll11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪઋ"): bstack11ll11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨઌ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1111ll111_opy_.format(str(e)))
def bstack1ll11l1l1l_opy_(test, bstack1l1lllll1l_opy_):
  global CONFIG
  global bstack1l11ll11_opy_
  global bstack1l111l1ll_opy_
  global bstack1l11llll11_opy_
  global bstack111lll1ll_opy_
  global bstack1lll1ll111_opy_
  global bstack1llll1l1l1_opy_
  global bstack1ll1111ll_opy_
  global bstack1l1l111ll1_opy_
  global bstack1lll11ll11_opy_
  global bstack1l111l11l_opy_
  global bstack1ll1llll1_opy_
  try:
    if not bstack1l11llll11_opy_:
      with open(os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"࠭ࡾࠨઍ")), bstack11ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ઎"), bstack11ll11_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪએ"))) as f:
        bstack1llll1ll11_opy_ = json.loads(bstack11ll11_opy_ (u"ࠤࡾࠦઐ") + f.read().strip() + bstack11ll11_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬઑ") + bstack11ll11_opy_ (u"ࠦࢂࠨ઒"))
        bstack1l11llll11_opy_ = bstack1llll1ll11_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l111l11l_opy_:
    for driver in bstack1l111l11l_opy_:
      if bstack1l11llll11_opy_ == driver.session_id:
        if test:
          bstack1ll1l1lll1_opy_(driver, test)
        bstack1ll1ll11l1_opy_(driver, bstack1l1lllll1l_opy_)
  elif bstack1l11llll11_opy_:
    bstack1ll111llll_opy_(test, bstack1l1lllll1l_opy_)
  if bstack1l11ll11_opy_:
    bstack1ll1111ll_opy_(bstack1l11ll11_opy_)
  if bstack1l111l1ll_opy_:
    bstack1l1l111ll1_opy_(bstack1l111l1ll_opy_)
  if bstack1ll11l1ll_opy_:
    bstack1lll11ll11_opy_()
def bstack1lll1lllll_opy_(self, test, *args, **kwargs):
  bstack1l1lllll1l_opy_ = None
  if test:
    bstack1l1lllll1l_opy_ = str(test.name)
  bstack1ll11l1l1l_opy_(test, bstack1l1lllll1l_opy_)
  bstack1llll1l1l1_opy_(self, test, *args, **kwargs)
def bstack1ll1lll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l11l1l1_opy_
  global CONFIG
  global bstack1l111l11l_opy_
  global bstack1l11llll11_opy_
  bstack1111lll11_opy_ = None
  try:
    if bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫઓ"), None):
      try:
        if not bstack1l11llll11_opy_:
          with open(os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"࠭ࡾࠨઔ")), bstack11ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧક"), bstack11ll11_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪખ"))) as f:
            bstack1llll1ll11_opy_ = json.loads(bstack11ll11_opy_ (u"ࠤࡾࠦગ") + f.read().strip() + bstack11ll11_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬઘ") + bstack11ll11_opy_ (u"ࠦࢂࠨઙ"))
            bstack1l11llll11_opy_ = bstack1llll1ll11_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1l111l11l_opy_:
        for driver in bstack1l111l11l_opy_:
          if bstack1l11llll11_opy_ == driver.session_id:
            bstack1111lll11_opy_ = driver
    bstack1ll111l1l_opy_ = bstack1l111111l_opy_.bstack1lllll1l1_opy_(CONFIG, test.tags)
    if bstack1111lll11_opy_:
      threading.current_thread().isA11yTest = bstack1l111111l_opy_.bstack1l11ll111_opy_(bstack1111lll11_opy_, bstack1ll111l1l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll111l1l_opy_
  except:
    pass
  bstack11l11l1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111lll1ll_opy_
  bstack111lll1ll_opy_ = self._test
def bstack1111ll11_opy_():
  global bstack1ll1l1l11_opy_
  try:
    if os.path.exists(bstack1ll1l1l11_opy_):
      os.remove(bstack1ll1l1l11_opy_)
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨચ") + str(e))
def bstack1l1llll1_opy_():
  global bstack1ll1l1l11_opy_
  bstack1ll1l1ll1_opy_ = {}
  try:
    if not os.path.isfile(bstack1ll1l1l11_opy_):
      with open(bstack1ll1l1l11_opy_, bstack11ll11_opy_ (u"࠭ࡷࠨછ")):
        pass
      with open(bstack1ll1l1l11_opy_, bstack11ll11_opy_ (u"ࠢࡸ࠭ࠥજ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1ll1l1l11_opy_):
      bstack1ll1l1ll1_opy_ = json.load(open(bstack1ll1l1l11_opy_, bstack11ll11_opy_ (u"ࠨࡴࡥࠫઝ")))
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫઞ") + str(e))
  finally:
    return bstack1ll1l1ll1_opy_
def bstack1l1ll1111l_opy_(platform_index, item_index):
  global bstack1ll1l1l11_opy_
  try:
    bstack1ll1l1ll1_opy_ = bstack1l1llll1_opy_()
    bstack1ll1l1ll1_opy_[item_index] = platform_index
    with open(bstack1ll1l1l11_opy_, bstack11ll11_opy_ (u"ࠥࡻ࠰ࠨટ")) as outfile:
      json.dump(bstack1ll1l1ll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩઠ") + str(e))
def bstack1ll11l111_opy_(bstack1ll1lll111_opy_):
  global CONFIG
  bstack11l1l1l1l_opy_ = bstack11ll11_opy_ (u"ࠬ࠭ડ")
  if not bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઢ") in CONFIG:
    logger.info(bstack11ll11_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫણ"))
  try:
    platform = CONFIG[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫત")][bstack1ll1lll111_opy_]
    if bstack11ll11_opy_ (u"ࠩࡲࡷࠬથ") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"ࠪࡳࡸ࠭દ")]) + bstack11ll11_opy_ (u"ࠫ࠱ࠦࠧધ")
    if bstack11ll11_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨન") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ઩")]) + bstack11ll11_opy_ (u"ࠧ࠭ࠢࠪપ")
    if bstack11ll11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬફ") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭બ")]) + bstack11ll11_opy_ (u"ࠪ࠰ࠥ࠭ભ")
    if bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭મ") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧય")]) + bstack11ll11_opy_ (u"࠭ࠬࠡࠩર")
    if bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ઱") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭લ")]) + bstack11ll11_opy_ (u"ࠩ࠯ࠤࠬળ")
    if bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ઴") in platform:
      bstack11l1l1l1l_opy_ += str(platform[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬવ")]) + bstack11ll11_opy_ (u"ࠬ࠲ࠠࠨશ")
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ષ") + str(e))
  finally:
    if bstack11l1l1l1l_opy_[len(bstack11l1l1l1l_opy_) - 2:] == bstack11ll11_opy_ (u"ࠧ࠭ࠢࠪસ"):
      bstack11l1l1l1l_opy_ = bstack11l1l1l1l_opy_[:-2]
    return bstack11l1l1l1l_opy_
def bstack1lll1l111l_opy_(path, bstack11l1l1l1l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1lllll11_opy_ = ET.parse(path)
    bstack11ll1l1l_opy_ = bstack1lllll11_opy_.getroot()
    bstack11l1lll1_opy_ = None
    for suite in bstack11ll1l1l_opy_.iter(bstack11ll11_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧહ")):
      if bstack11ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ઺") in suite.attrib:
        suite.attrib[bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨ઻")] += bstack11ll11_opy_ (u"઼ࠫࠥ࠭") + bstack11l1l1l1l_opy_
        bstack11l1lll1_opy_ = suite
    bstack1l11llll1l_opy_ = None
    for robot in bstack11ll1l1l_opy_.iter(bstack11ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫઽ")):
      bstack1l11llll1l_opy_ = robot
    bstack1lll11ll_opy_ = len(bstack1l11llll1l_opy_.findall(bstack11ll11_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬા")))
    if bstack1lll11ll_opy_ == 1:
      bstack1l11llll1l_opy_.remove(bstack1l11llll1l_opy_.findall(bstack11ll11_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭િ"))[0])
      bstack1l1lll11_opy_ = ET.Element(bstack11ll11_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧી"), attrib={bstack11ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧુ"): bstack11ll11_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪૂ"), bstack11ll11_opy_ (u"ࠫ࡮ࡪࠧૃ"): bstack11ll11_opy_ (u"ࠬࡹ࠰ࠨૄ")})
      bstack1l11llll1l_opy_.insert(1, bstack1l1lll11_opy_)
      bstack1l11l111l_opy_ = None
      for suite in bstack1l11llll1l_opy_.iter(bstack11ll11_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬૅ")):
        bstack1l11l111l_opy_ = suite
      bstack1l11l111l_opy_.append(bstack11l1lll1_opy_)
      bstack1l1lll1l1l_opy_ = None
      for status in bstack11l1lll1_opy_.iter(bstack11ll11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ૆")):
        bstack1l1lll1l1l_opy_ = status
      bstack1l11l111l_opy_.append(bstack1l1lll1l1l_opy_)
    bstack1lllll11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭ે") + str(e))
def bstack1l1lll1l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1llll1111l_opy_
  global CONFIG
  if bstack11ll11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨૈ") in options:
    del options[bstack11ll11_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢૉ")]
  bstack1lll11llll_opy_ = bstack1l1llll1_opy_()
  for bstack1l11ll1111_opy_ in bstack1lll11llll_opy_.keys():
    path = os.path.join(os.getcwd(), bstack11ll11_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ૊"), str(bstack1l11ll1111_opy_), bstack11ll11_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩો"))
    bstack1lll1l111l_opy_(path, bstack1ll11l111_opy_(bstack1lll11llll_opy_[bstack1l11ll1111_opy_]))
  bstack1111ll11_opy_()
  return bstack1llll1111l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111lll11_opy_(self, ff_profile_dir):
  global bstack1llll111l1_opy_
  if not ff_profile_dir:
    return None
  return bstack1llll111l1_opy_(self, ff_profile_dir)
def bstack111l1111_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111111ll_opy_
  bstack1ll1l1111l_opy_ = []
  if bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૌ") in CONFIG:
    bstack1ll1l1111l_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ્ࠪ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11ll11_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ૎")],
      pabot_args[bstack11ll11_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ૏")],
      argfile,
      pabot_args.get(bstack11ll11_opy_ (u"ࠥ࡬࡮ࡼࡥࠣૐ")),
      pabot_args[bstack11ll11_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ૑")],
      platform[0],
      bstack111111ll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11ll11_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ૒")] or [(bstack11ll11_opy_ (u"ࠨࠢ૓"), None)]
    for platform in enumerate(bstack1ll1l1111l_opy_)
  ]
def bstack111ll111_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l1l11llll_opy_=bstack11ll11_opy_ (u"ࠧࠨ૔")):
  global bstack11lll1l11_opy_
  self.platform_index = platform_index
  self.bstack1l1l1111ll_opy_ = bstack1l1l11llll_opy_
  bstack11lll1l11_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll11111l1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1ll11l1l_opy_
  global bstack111lll1l1_opy_
  if not bstack11ll11_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૕") in item.options:
    item.options[bstack11ll11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૖")] = []
  for v in item.options[bstack11ll11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ૗")]:
    if bstack11ll11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪ૘") in v:
      item.options[bstack11ll11_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ૙")].remove(v)
    if bstack11ll11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭૚") in v:
      item.options[bstack11ll11_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ૛")].remove(v)
    if bstack11ll11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ૜") in v:
      item.options[bstack11ll11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૝")].remove(v)
  item.options[bstack11ll11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ૞")].insert(0, bstack11ll11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ࠭૟").format(item.platform_index))
  item.options[bstack11ll11_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧૠ")].insert(0, bstack11ll11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭ૡ").format(item.bstack1l1l1111ll_opy_))
  if bstack111lll1l1_opy_:
    item.options[bstack11ll11_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩૢ")].insert(0, bstack11ll11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓ࠻ࡽࢀࠫૣ").format(bstack111lll1l1_opy_))
  return bstack1l1ll11l1l_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1l1111ll1_opy_(command, item_index):
  if bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ૤")):
    os.environ[bstack11ll11_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫ૥")] = json.dumps(CONFIG[bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૦")][item_index % bstack1l11lll111_opy_])
  global bstack111lll1l1_opy_
  if bstack111lll1l1_opy_:
    command[0] = command[0].replace(bstack11ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ૧"), bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪ૨") + str(
      item_index) + bstack11ll11_opy_ (u"ࠧࠡࠩ૩") + bstack111lll1l1_opy_, 1)
  else:
    command[0] = command[0].replace(bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ૪"),
                                    bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭૫") + str(item_index), 1)
def bstack1l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l11l1l11_opy_
  bstack1l1111ll1_opy_(command, item_index)
  return bstack1l11l1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1l1ll1l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l11l1l11_opy_
  bstack1l1111ll1_opy_(command, item_index)
  return bstack1l11l1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1lll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l11l1l11_opy_
  bstack1l1111ll1_opy_(command, item_index)
  return bstack1l11l1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1l1l1111_opy_(self, runner, quiet=False, capture=True):
  global bstack11lllll11_opy_
  bstack1l111ll11_opy_ = bstack11lllll11_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11ll11_opy_ (u"ࠪࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡥࡡࡳࡴࠪ૬")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11ll11_opy_ (u"ࠫࡪࡾࡣࡠࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࡣࡦࡸࡲࠨ૭")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l111ll11_opy_
def bstack1lll1l11ll_opy_(self, name, context, *args):
  os.environ[bstack11ll11_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭૮")] = json.dumps(CONFIG[bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૯")][int(threading.current_thread()._name) % bstack1l11lll111_opy_])
  global bstack1llll11ll1_opy_
  if name == bstack11ll11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ૰"):
    bstack1llll11ll1_opy_(self, name, context, *args)
    try:
      if not bstack1111l1lll_opy_:
        bstack1111lll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1lll_opy_(bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ૱")) else context.browser
        bstack1ll111l1_opy_ = str(self.feature.name)
        bstack1l1l11l111_opy_(context, bstack1ll111l1_opy_)
        bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ૲") + json.dumps(bstack1ll111l1_opy_) + bstack11ll11_opy_ (u"ࠪࢁࢂ࠭૳"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ૴").format(str(e)))
  elif name == bstack11ll11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ૵"):
    bstack1llll11ll1_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack11ll11_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ૶")):
        self.driver_before_scenario = True
      if (not bstack1111l1lll_opy_):
        scenario_name = args[0].name
        feature_name = bstack1ll111l1_opy_ = str(self.feature.name)
        bstack1ll111l1_opy_ = feature_name + bstack11ll11_opy_ (u"ࠧࠡ࠯ࠣࠫ૷") + scenario_name
        bstack1111lll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1lll_opy_(bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ૸")) else context.browser
        if self.driver_before_scenario:
          bstack1l1l11l111_opy_(context, bstack1ll111l1_opy_)
          bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧૹ") + json.dumps(bstack1ll111l1_opy_) + bstack11ll11_opy_ (u"ࠪࢁࢂ࠭ૺ"))
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬૻ").format(str(e)))
  elif name == bstack11ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ૼ"):
    try:
      bstack1ll11111l_opy_ = args[0].status.name
      bstack1111lll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ૽") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1ll11111l_opy_).lower() == bstack11ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ૾"):
        bstack1l1ll1l11_opy_ = bstack11ll11_opy_ (u"ࠨࠩ૿")
        bstack11ll1ll1l_opy_ = bstack11ll11_opy_ (u"ࠩࠪ଀")
        bstack1lll11ll1_opy_ = bstack11ll11_opy_ (u"ࠪࠫଁ")
        try:
          import traceback
          bstack1l1ll1l11_opy_ = self.exception.__class__.__name__
          bstack1ll111l11l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack11ll1ll1l_opy_ = bstack11ll11_opy_ (u"ࠫࠥ࠭ଂ").join(bstack1ll111l11l_opy_)
          bstack1lll11ll1_opy_ = bstack1ll111l11l_opy_[-1]
        except Exception as e:
          logger.debug(bstack1llllll1ll_opy_.format(str(e)))
        bstack1l1ll1l11_opy_ += bstack1lll11ll1_opy_
        bstack1lll11lll1_opy_(context, json.dumps(str(args[0].name) + bstack11ll11_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦଃ") + str(bstack11ll1ll1l_opy_)),
                            bstack11ll11_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ଄"))
        if self.driver_before_scenario:
          bstack111111l1_opy_(getattr(context, bstack11ll11_opy_ (u"ࠧࡱࡣࡪࡩࠬଅ"), None), bstack11ll11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣଆ"), bstack1l1ll1l11_opy_)
          bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧଇ") + json.dumps(str(args[0].name) + bstack11ll11_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤଈ") + str(bstack11ll1ll1l_opy_)) + bstack11ll11_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫଉ"))
        if self.driver_before_scenario:
          bstack11l11ll11_opy_(bstack1111lll11_opy_, bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬଊ"), bstack11ll11_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥଋ") + str(bstack1l1ll1l11_opy_))
      else:
        bstack1lll11lll1_opy_(context, bstack11ll11_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣଌ"), bstack11ll11_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ଍"))
        if self.driver_before_scenario:
          bstack111111l1_opy_(getattr(context, bstack11ll11_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ଎"), None), bstack11ll11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥଏ"))
        bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩଐ") + json.dumps(str(args[0].name) + bstack11ll11_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ଑")) + bstack11ll11_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ଒"))
        if self.driver_before_scenario:
          bstack11l11ll11_opy_(bstack1111lll11_opy_, bstack11ll11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢଓ"))
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪଔ").format(str(e)))
  elif name == bstack11ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩକ"):
    try:
      bstack1111lll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1lll_opy_(bstack11ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଖ")) else context.browser
      if context.failed is True:
        bstack1lll1l111_opy_ = []
        bstack1l1111l1l_opy_ = []
        bstack11111111l_opy_ = []
        bstack1ll11l111l_opy_ = bstack11ll11_opy_ (u"ࠫࠬଗ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1lll1l111_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1ll111l11l_opy_ = traceback.format_tb(exc_tb)
            bstack1l1ll1ll1l_opy_ = bstack11ll11_opy_ (u"ࠬࠦࠧଘ").join(bstack1ll111l11l_opy_)
            bstack1l1111l1l_opy_.append(bstack1l1ll1ll1l_opy_)
            bstack11111111l_opy_.append(bstack1ll111l11l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1llllll1ll_opy_.format(str(e)))
        bstack1l1ll1l11_opy_ = bstack11ll11_opy_ (u"࠭ࠧଙ")
        for i in range(len(bstack1lll1l111_opy_)):
          bstack1l1ll1l11_opy_ += bstack1lll1l111_opy_[i] + bstack11111111l_opy_[i] + bstack11ll11_opy_ (u"ࠧ࡝ࡰࠪଚ")
        bstack1ll11l111l_opy_ = bstack11ll11_opy_ (u"ࠨࠢࠪଛ").join(bstack1l1111l1l_opy_)
        if not self.driver_before_scenario:
          bstack1lll11lll1_opy_(context, bstack1ll11l111l_opy_, bstack11ll11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣଜ"))
          bstack111111l1_opy_(getattr(context, bstack11ll11_opy_ (u"ࠪࡴࡦ࡭ࡥࠨଝ"), None), bstack11ll11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦଞ"), bstack1l1ll1l11_opy_)
          bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪଟ") + json.dumps(bstack1ll11l111l_opy_) + bstack11ll11_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ଠ"))
          bstack11l11ll11_opy_(bstack1111lll11_opy_, bstack11ll11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢଡ"), bstack11ll11_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨଢ") + str(bstack1l1ll1l11_opy_))
          bstack1lll111111_opy_ = bstack1ll1l1l1ll_opy_(bstack1ll11l111l_opy_, self.feature.name, logger)
          if (bstack1lll111111_opy_ != None):
            bstack1llll11111_opy_.append(bstack1lll111111_opy_)
      else:
        if not self.driver_before_scenario:
          bstack1lll11lll1_opy_(context, bstack11ll11_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧଣ") + str(self.feature.name) + bstack11ll11_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧତ"), bstack11ll11_opy_ (u"ࠦ࡮ࡴࡦࡰࠤଥ"))
          bstack111111l1_opy_(getattr(context, bstack11ll11_opy_ (u"ࠬࡶࡡࡨࡧࠪଦ"), None), bstack11ll11_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨଧ"))
          bstack1111lll11_opy_.execute_script(bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬନ") + json.dumps(bstack11ll11_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦ଩") + str(self.feature.name) + bstack11ll11_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦପ")) + bstack11ll11_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩଫ"))
          bstack11l11ll11_opy_(bstack1111lll11_opy_, bstack11ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫବ"))
          bstack1lll111111_opy_ = bstack1ll1l1l1ll_opy_(bstack1ll11l111l_opy_, self.feature.name, logger)
          if (bstack1lll111111_opy_ != None):
            bstack1llll11111_opy_.append(bstack1lll111111_opy_)
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧଭ").format(str(e)))
  else:
    bstack1llll11ll1_opy_(self, name, context, *args)
  if name in [bstack11ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ମ"), bstack11ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨଯ")]:
    bstack1llll11ll1_opy_(self, name, context, *args)
    if (name == bstack11ll11_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩର") and self.driver_before_scenario) or (
            name == bstack11ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩ଱") and not self.driver_before_scenario):
      try:
        bstack1111lll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1lll_opy_(bstack11ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଲ")) else context.browser
        bstack1111lll11_opy_.quit()
      except Exception:
        pass
def bstack11llll11_opy_(config, startdir):
  return bstack11ll11_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤଳ").format(bstack11ll11_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ଴"))
notset = Notset()
def bstack1l1l1l11l1_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1llllll_opy_
  if str(name).lower() == bstack11ll11_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭ଵ"):
    return bstack11ll11_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨଶ")
  else:
    return bstack1l1llllll_opy_(self, name, default, skip)
def bstack1lll1l1l_opy_(item, when):
  global bstack111l1ll1l_opy_
  try:
    bstack111l1ll1l_opy_(item, when)
  except Exception as e:
    pass
def bstack1lll1l11l_opy_():
  return
def bstack11llll1l1_opy_(type, name, status, reason, bstack11ll1lll1_opy_, bstack11ll1l11l_opy_):
  bstack1ll11l1111_opy_ = {
    bstack11ll11_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨଷ"): type,
    bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬସ"): {}
  }
  if type == bstack11ll11_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬହ"):
    bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ଺")][bstack11ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ଻")] = bstack11ll1lll1_opy_
    bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴ଼ࠩ")][bstack11ll11_opy_ (u"ࠧࡥࡣࡷࡥࠬଽ")] = json.dumps(str(bstack11ll1l11l_opy_))
  if type == bstack11ll11_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩା"):
    bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬି")][bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨୀ")] = name
  if type == bstack11ll11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧୁ"):
    bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨୂ")][bstack11ll11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ୃ")] = status
    if status == bstack11ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧୄ"):
      bstack1ll11l1111_opy_[bstack11ll11_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ୅")][bstack11ll11_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ୆")] = json.dumps(str(reason))
  bstack1ll1l11l1_opy_ = bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨେ").format(json.dumps(bstack1ll11l1111_opy_))
  return bstack1ll1l11l1_opy_
def bstack1l11l1111_opy_(driver_command, response):
    if driver_command == bstack11ll11_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨୈ"):
        bstack1l1l111lll_opy_.bstack1l1ll1ll11_opy_({
            bstack11ll11_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ୉"): response[bstack11ll11_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ୊")],
            bstack11ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧୋ"): bstack1l1l111lll_opy_.current_test_uuid()
        })
def bstack1lll1l1111_opy_(item, call, rep):
  global bstack11l11l1ll_opy_
  global bstack1l111l11l_opy_
  global bstack1111l1lll_opy_
  name = bstack11ll11_opy_ (u"ࠨࠩୌ")
  try:
    if rep.when == bstack11ll11_opy_ (u"ࠩࡦࡥࡱࡲ୍ࠧ"):
      bstack1l11llll11_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1111l1lll_opy_:
          name = str(rep.nodeid)
          bstack1ll11ll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ୎"), name, bstack11ll11_opy_ (u"ࠫࠬ୏"), bstack11ll11_opy_ (u"ࠬ࠭୐"), bstack11ll11_opy_ (u"࠭ࠧ୑"), bstack11ll11_opy_ (u"ࠧࠨ୒"))
          threading.current_thread().bstack1l11l1lll_opy_ = name
          for driver in bstack1l111l11l_opy_:
            if bstack1l11llll11_opy_ == driver.session_id:
              driver.execute_script(bstack1ll11ll11_opy_)
      except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ୓").format(str(e)))
      try:
        bstack11lll111l_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ୔"):
          status = bstack11ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ୕") if rep.outcome.lower() == bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫୖ") else bstack11ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬୗ")
          reason = bstack11ll11_opy_ (u"࠭ࠧ୘")
          if status == bstack11ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ୙"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11ll11_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭୚") if status == bstack11ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ୛") else bstack11ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩଡ଼")
          data = name + bstack11ll11_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ଢ଼") if status == bstack11ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ୞") else name + bstack11ll11_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩୟ") + reason
          bstack1lllllll11_opy_ = bstack11llll1l1_opy_(bstack11ll11_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩୠ"), bstack11ll11_opy_ (u"ࠨࠩୡ"), bstack11ll11_opy_ (u"ࠩࠪୢ"), bstack11ll11_opy_ (u"ࠪࠫୣ"), level, data)
          for driver in bstack1l111l11l_opy_:
            if bstack1l11llll11_opy_ == driver.session_id:
              driver.execute_script(bstack1lllllll11_opy_)
      except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ୤").format(str(e)))
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩ୥").format(str(e)))
  bstack11l11l1ll_opy_(item, call, rep)
def bstack1l1lll1111_opy_(driver, bstack1ll1ll11ll_opy_):
  PercySDK.screenshot(driver, bstack1ll1ll11ll_opy_)
def bstack11111l1l1_opy_(driver):
  if bstack1l1l11111l_opy_.bstack1llll11l1_opy_() is True or bstack1l1l11111l_opy_.capturing() is True:
    return
  bstack1l1l11111l_opy_.bstack1ll1l11ll_opy_()
  while not bstack1l1l11111l_opy_.bstack1llll11l1_opy_():
    bstack11l11llll_opy_ = bstack1l1l11111l_opy_.bstack1lll1ll1l1_opy_()
    bstack1l1lll1111_opy_(driver, bstack11l11llll_opy_)
  bstack1l1l11111l_opy_.bstack1ll1l1ll11_opy_()
def bstack1l1l111ll_opy_(sequence, driver_command, response = None, bstack11l1ll11_opy_ = None, args = None):
    try:
      if sequence != bstack11ll11_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭୦"):
        return
      if not CONFIG.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭୧"), False):
        return
      bstack11l11llll_opy_ = bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ୨"), None)
      for command in bstack1ll1ll11l_opy_:
        if command == driver_command:
          for driver in bstack1l111l11l_opy_:
            bstack11111l1l1_opy_(driver)
      bstack1ll1ll111_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬ୩"), bstack11ll11_opy_ (u"ࠥࡥࡺࡺ࡯ࠣ୪"))
      if driver_command in bstack1l1lll11l_opy_[bstack1ll1ll111_opy_]:
        bstack1l1l11111l_opy_.bstack1ll1lll11l_opy_(bstack11l11llll_opy_, driver_command)
    except Exception as e:
      pass
def bstack1lll1llll1_opy_(framework_name):
  global bstack1l11llll1_opy_
  global bstack1llll111l_opy_
  global bstack1l1ll1111_opy_
  bstack1l11llll1_opy_ = framework_name
  logger.info(bstack1l1l111l1_opy_.format(bstack1l11llll1_opy_.split(bstack11ll11_opy_ (u"ࠫ࠲࠭୫"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l111ll1_opy_:
      Service.start = bstack1ll11l11l_opy_
      Service.stop = bstack1llllllll_opy_
      webdriver.Remote.get = bstack1llll1111_opy_
      WebDriver.close = bstack1ll1lll11_opy_
      WebDriver.quit = bstack1lll11l1ll_opy_
      webdriver.Remote.__init__ = bstack1l1l11l1l1_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1l111ll1_opy_ and bstack1l1l111lll_opy_.on():
      webdriver.Remote.__init__ = bstack1lll1lll_opy_
    WebDriver.execute = bstack1ll1l1l1l_opy_
    bstack1llll111l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l111ll1_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1l11ll1_opy_
  except Exception as e:
    pass
  bstack1lll1l1l1_opy_()
  if not bstack1llll111l_opy_:
    bstack11l1llll_opy_(bstack11ll11_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ୬"), bstack11111l1ll_opy_)
  if bstack1llll1l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1ll1llll_opy_
    except Exception as e:
      logger.error(bstack1111l1l1_opy_.format(str(e)))
  if bstack1ll11lll1_opy_():
    bstack1ll11l11ll_opy_(CONFIG, logger)
  if (bstack11ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ୭") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭୮"), False):
          bstack1l11lll11l_opy_(bstack1l1l111ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111lll11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1l1lll1l_opy_
      except Exception as e:
        logger.warn(bstack11111lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import bstack1l1l11ll1l_opy_
        bstack1l1l11ll1l_opy_.close = bstack1ll111ll_opy_
      except Exception as e:
        logger.debug(bstack1l11ll111l_opy_ + str(e))
    except Exception as e:
      bstack11l1llll_opy_(e, bstack11111lll_opy_)
    Output.start_test = bstack1llll1lll1_opy_
    Output.end_test = bstack1lll1lllll_opy_
    TestStatus.__init__ = bstack1ll1lll1_opy_
    QueueItem.__init__ = bstack111ll111_opy_
    pabot._create_items = bstack111l1111_opy_
    try:
      from pabot import __version__ as bstack11l1llll1_opy_
      if version.parse(bstack11l1llll1_opy_) >= version.parse(bstack11ll11_opy_ (u"ࠨ࠴࠱࠵࠺࠴࠰ࠨ୯")):
        pabot._run = bstack1lll1l1lll_opy_
      elif version.parse(bstack11l1llll1_opy_) >= version.parse(bstack11ll11_opy_ (u"ࠩ࠵࠲࠶࠹࠮࠱ࠩ୰")):
        pabot._run = bstack1l1ll1l11l_opy_
      else:
        pabot._run = bstack1l1ll111l_opy_
    except Exception as e:
      pabot._run = bstack1l1ll111l_opy_
    pabot._create_command_for_execution = bstack1ll11111l1_opy_
    pabot._report_results = bstack1l1lll1l11_opy_
  if bstack11ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪୱ") in str(framework_name).lower():
    if not bstack1l111ll1_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11l1llll_opy_(e, bstack1l1ll1l1l1_opy_)
    Runner.run_hook = bstack1lll1l11ll_opy_
    Step.run = bstack1l1l1111_opy_
  if bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ୲") in str(framework_name).lower():
    if not bstack1l111ll1_opy_:
      return
    try:
      if CONFIG.get(bstack11ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ୳"), False):
          bstack1l11lll11l_opy_(bstack1l1l111ll_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11llll11_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1lll1l11l_opy_
      Config.getoption = bstack1l1l1l11l1_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1lll1l1111_opy_
    except Exception as e:
      pass
def bstack1l11l11lll_opy_():
  global CONFIG
  if bstack11ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭୴") in CONFIG and int(CONFIG[bstack11ll11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ୵")]) > 1:
    logger.warn(bstack1111ll1ll_opy_)
def bstack111ll1ll_opy_(arg, bstack1l1l11ll_opy_, bstack1ll11l1ll1_opy_=None):
  global CONFIG
  global bstack1l11l1l1l1_opy_
  global bstack11llll1l_opy_
  global bstack1l111ll1_opy_
  global bstack1l1l1l1l1_opy_
  bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ୶")
  if bstack1l1l11ll_opy_ and isinstance(bstack1l1l11ll_opy_, str):
    bstack1l1l11ll_opy_ = eval(bstack1l1l11ll_opy_)
  CONFIG = bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ୷")]
  bstack1l11l1l1l1_opy_ = bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ୸")]
  bstack11llll1l_opy_ = bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭୹")]
  bstack1l111ll1_opy_ = bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ୺")]
  bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ୻"), bstack1l111ll1_opy_)
  os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ୼")] = bstack11ll111ll_opy_
  os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧ୽")] = json.dumps(CONFIG)
  os.environ[bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩ୾")] = bstack1l11l1l1l1_opy_
  os.environ[bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ୿")] = str(bstack11llll1l_opy_)
  os.environ[bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪ஀")] = str(True)
  if bstack1111l11l1_opy_(arg, [bstack11ll11_opy_ (u"ࠬ࠳࡮ࠨ஁"), bstack11ll11_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧஂ")]) != -1:
    os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨஃ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1lll11l1_opy_)
    return
  bstack1l1l11111_opy_()
  global bstack1111llll1_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack111111ll_opy_
  global bstack111lll1l1_opy_
  global bstack111111111_opy_
  global bstack1l1ll1111_opy_
  global bstack1l11lll1_opy_
  arg.append(bstack11ll11_opy_ (u"ࠣ࠯࡚ࠦ஄"))
  arg.append(bstack11ll11_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧஅ"))
  arg.append(bstack11ll11_opy_ (u"ࠥ࠱࡜ࠨஆ"))
  arg.append(bstack11ll11_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥஇ"))
  global bstack1lll1ll11l_opy_
  global bstack1l1l11lll_opy_
  global bstack1l111l111_opy_
  global bstack11l11l1l1_opy_
  global bstack1llll111l1_opy_
  global bstack11lll1l11_opy_
  global bstack1l1ll11l1l_opy_
  global bstack11ll1ll11_opy_
  global bstack1lllll1lll_opy_
  global bstack1lll111l1l_opy_
  global bstack1l1llllll_opy_
  global bstack111l1ll1l_opy_
  global bstack11l11l1ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lll1ll11l_opy_ = webdriver.Remote.__init__
    bstack1l1l11lll_opy_ = WebDriver.quit
    bstack11ll1ll11_opy_ = WebDriver.close
    bstack1lllll1lll_opy_ = WebDriver.get
    bstack1l111l111_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1ll1llll_opy_(CONFIG) and bstack11111llll_opy_():
    if bstack111ll1l11_opy_() < version.parse(bstack1ll11l11l1_opy_):
      logger.error(bstack1l1ll1lll1_opy_.format(bstack111ll1l11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lll111l1l_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1111l1l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1llllll_opy_ = Config.getoption
    from _pytest import runner
    bstack111l1ll1l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1lllll11ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack11l11l1ll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11ll11_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ஈ"))
  bstack111111ll_opy_ = CONFIG.get(bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪஉ"), {}).get(bstack11ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩஊ"))
  bstack1l11lll1_opy_ = True
  bstack1lll1llll1_opy_(bstack1l1l11lll1_opy_)
  os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ஋")] = CONFIG[bstack11ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ஌")]
  os.environ[bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭஍")] = CONFIG[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧஎ")]
  os.environ[bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨஏ")] = bstack1l111ll1_opy_.__str__()
  from _pytest.config import main as bstack1l11ll1ll1_opy_
  bstack1ll11ll1ll_opy_ = []
  try:
    bstack1llll1ll_opy_ = bstack1l11ll1ll1_opy_(arg)
    if bstack11ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪஐ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll11ll1ll_opy_.append(bstack1l11111l_opy_)
    try:
      bstack1l1ll1l1l_opy_ = (bstack1ll11ll1ll_opy_, int(bstack1llll1ll_opy_))
      bstack1ll11l1ll1_opy_.append(bstack1l1ll1l1l_opy_)
    except:
      bstack1ll11l1ll1_opy_.append((bstack1ll11ll1ll_opy_, bstack1llll1ll_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1ll11ll1ll_opy_.append({bstack11ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ஑"): bstack11ll11_opy_ (u"ࠨࡒࡵࡳࡨ࡫ࡳࡴࠢࠪஒ") + os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩஓ")), bstack11ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩஔ"): traceback.format_exc(), bstack11ll11_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪக"): int(os.environ.get(bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ஖")))})
    bstack1ll11l1ll1_opy_.append((bstack1ll11ll1ll_opy_, 1))
def bstack1l1l1ll11_opy_(arg):
  global bstack11l1l11l1_opy_
  bstack1lll1llll1_opy_(bstack11llll11l_opy_)
  os.environ[bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ஗")] = str(bstack11llll1l_opy_)
  from behave.__main__ import main as bstack111ll111l_opy_
  status_code = bstack111ll111l_opy_(arg)
  if status_code != 0:
    bstack11l1l11l1_opy_ = status_code
def bstack111l1ll1_opy_():
  logger.info(bstack1ll1ll1111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭஘"), help=bstack11ll11_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩங"))
  parser.add_argument(bstack11ll11_opy_ (u"ࠩ࠰ࡹࠬச"), bstack11ll11_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ஛"), help=bstack11ll11_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪஜ"))
  parser.add_argument(bstack11ll11_opy_ (u"ࠬ࠳࡫ࠨ஝"), bstack11ll11_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬஞ"), help=bstack11ll11_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨட"))
  parser.add_argument(bstack11ll11_opy_ (u"ࠨ࠯ࡩࠫ஠"), bstack11ll11_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ஡"), help=bstack11ll11_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ஢"))
  bstack11l1l1ll_opy_ = parser.parse_args()
  try:
    bstack1ll11ll111_opy_ = bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨண")
    if bstack11l1l1ll_opy_.framework and bstack11l1l1ll_opy_.framework not in (bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬத"), bstack11ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ஥")):
      bstack1ll11ll111_opy_ = bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭஦")
    bstack111ll1lll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll11ll111_opy_)
    bstack111l1l1ll_opy_ = open(bstack111ll1lll_opy_, bstack11ll11_opy_ (u"ࠨࡴࠪ஧"))
    bstack1llll1l111_opy_ = bstack111l1l1ll_opy_.read()
    bstack111l1l1ll_opy_.close()
    if bstack11l1l1ll_opy_.username:
      bstack1llll1l111_opy_ = bstack1llll1l111_opy_.replace(bstack11ll11_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩந"), bstack11l1l1ll_opy_.username)
    if bstack11l1l1ll_opy_.key:
      bstack1llll1l111_opy_ = bstack1llll1l111_opy_.replace(bstack11ll11_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬன"), bstack11l1l1ll_opy_.key)
    if bstack11l1l1ll_opy_.framework:
      bstack1llll1l111_opy_ = bstack1llll1l111_opy_.replace(bstack11ll11_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬப"), bstack11l1l1ll_opy_.framework)
    file_name = bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ஫")
    file_path = os.path.abspath(file_name)
    bstack1ll1l11l_opy_ = open(file_path, bstack11ll11_opy_ (u"࠭ࡷࠨ஬"))
    bstack1ll1l11l_opy_.write(bstack1llll1l111_opy_)
    bstack1ll1l11l_opy_.close()
    logger.info(bstack1llll1lll_opy_)
    try:
      os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ஭")] = bstack11l1l1ll_opy_.framework if bstack11l1l1ll_opy_.framework != None else bstack11ll11_opy_ (u"ࠣࠤம")
      config = yaml.safe_load(bstack1llll1l111_opy_)
      config[bstack11ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩய")] = bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩர")
      bstack111l11l11_opy_(bstack11l1l1111_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1ll1lll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l11l111_opy_.format(str(e)))
def bstack111l11l11_opy_(bstack1l1l1l1l_opy_, config, bstack1l11l11l1l_opy_={}):
  global bstack1l111ll1_opy_
  global bstack1lll11lll_opy_
  global bstack1l1l1l1l1_opy_
  if not config:
    return
  bstack1ll11lll_opy_ = bstack11111lll1_opy_ if not bstack1l111ll1_opy_ else (
    bstack111lllll1_opy_ if bstack11ll11_opy_ (u"ࠫࡦࡶࡰࠨற") in config else bstack1l11l1llll_opy_)
  bstack111l11l1_opy_ = False
  bstack1ll111lll1_opy_ = False
  if bstack1l111ll1_opy_ is True:
      if bstack11ll11_opy_ (u"ࠬࡧࡰࡱࠩல") in config:
          bstack111l11l1_opy_ = True
      else:
          bstack1ll111lll1_opy_ = True
  bstack111llll1_opy_ = {
      bstack11ll11_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ள"): bstack1l1l111lll_opy_.bstack111l111l_opy_(bstack1lll11lll_opy_),
      bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧழ"): bstack1l111111l_opy_.bstack11ll11ll1_opy_(config),
      bstack11ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧவ"): config.get(bstack11ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨஶ"), False),
      bstack11ll11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬஷ"): bstack1ll111lll1_opy_,
      bstack11ll11_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪஸ"): bstack111l11l1_opy_
  }
  data = {
    bstack11ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧஹ"): config[bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ஺")],
    bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ஻"): config[bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ஼")],
    bstack11ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭஽"): bstack1l1l1l1l_opy_,
    bstack11ll11_opy_ (u"ࠪࡨࡪࡺࡥࡤࡶࡨࡨࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧா"): os.environ.get(bstack11ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ி"), bstack1lll11lll_opy_),
    bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧீ"): bstack1ll1l1l111_opy_,
    bstack11ll11_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬ࠨு"): bstack11111l111_opy_(),
    bstack11ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪூ"): {
      bstack11ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௃"): str(config[bstack11ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ௄")]) if bstack11ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ௅") in config else bstack11ll11_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧெ"),
      bstack11ll11_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࡖࡦࡴࡶ࡭ࡴࡴࠧே"): sys.version,
      bstack11ll11_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨை"): bstack1ll11ll1l_opy_(os.getenv(bstack11ll11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤ௉"), bstack11ll11_opy_ (u"ࠣࠤொ"))),
      bstack11ll11_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫோ"): bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪௌ"),
      bstack11ll11_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸ்ࠬ"): bstack1ll11lll_opy_,
      bstack11ll11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ௎"): bstack111llll1_opy_,
      bstack11ll11_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬ௏"): os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬௐ")],
      bstack11ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ௑"): bstack11l111l1_opy_(os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ௒"), bstack1lll11lll_opy_)),
      bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௓"): config[bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௔")] if config[bstack11ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௕")] else bstack11ll11_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ௖"),
      bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩௗ"): str(config[bstack11ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௘")]) if bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௙") in config else bstack11ll11_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ௚"),
      bstack11ll11_opy_ (u"ࠫࡴࡹࠧ௛"): sys.platform,
      bstack11ll11_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ௜"): socket.gethostname(),
      bstack11ll11_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ௝"): bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ௞"))
    }
  }
  if not bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ௟")) is None:
    data[bstack11ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ௠")][bstack11ll11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭௡")] = {
      bstack11ll11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ௢"): bstack11ll11_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ௣"),
      bstack11ll11_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭௤"): bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ௥")),
      bstack11ll11_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ௦"): bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ௧"))
    }
  update(data[bstack11ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭௨")], bstack1l11l11l1l_opy_)
  try:
    response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠫࡕࡕࡓࡕࠩ௩"), bstack11l1ll1ll_opy_(bstack11ll11l11_opy_), data, {
      bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪ௪"): (config[bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ௫")], config[bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ௬")])
    })
    if response:
      logger.debug(bstack1l11l11l_opy_.format(bstack1l1l1l1l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11ll11l1_opy_.format(str(e)))
def bstack1ll11ll1l_opy_(framework):
  return bstack11ll11_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ௭").format(str(framework), __version__) if framework else bstack11ll11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥ௮").format(
    __version__)
def bstack1l1l11111_opy_():
  global CONFIG
  global bstack1l1l11l11l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l11lll1ll_opy_()
    logger.debug(bstack1llllll11l_opy_.format(str(CONFIG)))
    bstack1l1l11l11l_opy_ = bstack1l1l1l1l11_opy_.bstack1l11l1lll1_opy_(CONFIG, bstack1l1l11l11l_opy_)
    bstack11lll1111_opy_()
  except Exception as e:
    logger.error(bstack11ll11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢ௯") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1llll11l_opy_
  atexit.register(bstack1ll11111ll_opy_)
  signal.signal(signal.SIGINT, bstack1ll1l111ll_opy_)
  signal.signal(signal.SIGTERM, bstack1ll1l111ll_opy_)
def bstack1llll11l_opy_(exctype, value, traceback):
  global bstack1l111l11l_opy_
  try:
    for driver in bstack1l111l11l_opy_:
      bstack11l11ll11_opy_(driver, bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ௰"), bstack11ll11_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ௱") + str(value))
  except Exception:
    pass
  bstack1l1lllllll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1lllllll_opy_(message=bstack11ll11_opy_ (u"࠭ࠧ௲"), bstack1ll1l1l1_opy_ = False):
  global CONFIG
  bstack1111111ll_opy_ = bstack11ll11_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠩ௳") if bstack1ll1l1l1_opy_ else bstack11ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ௴")
  try:
    if message:
      bstack1l11l11l1l_opy_ = {
        bstack1111111ll_opy_ : str(message)
      }
      bstack111l11l11_opy_(bstack1l111lll_opy_, CONFIG, bstack1l11l11l1l_opy_)
    else:
      bstack111l11l11_opy_(bstack1l111lll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll11lll1l_opy_.format(str(e)))
def bstack1ll1l1111_opy_(bstack111l11111_opy_, size):
  bstack1lll1111l_opy_ = []
  while len(bstack111l11111_opy_) > size:
    bstack11l11111_opy_ = bstack111l11111_opy_[:size]
    bstack1lll1111l_opy_.append(bstack11l11111_opy_)
    bstack111l11111_opy_ = bstack111l11111_opy_[size:]
  bstack1lll1111l_opy_.append(bstack111l11111_opy_)
  return bstack1lll1111l_opy_
def bstack11l111l11_opy_(args):
  if bstack11ll11_opy_ (u"ࠩ࠰ࡱࠬ௵") in args and bstack11ll11_opy_ (u"ࠪࡴࡩࡨࠧ௶") in args:
    return True
  return False
def run_on_browserstack(bstack1lll1l11l1_opy_=None, bstack1ll11l1ll1_opy_=None, bstack1l11ll1ll_opy_=False):
  global CONFIG
  global bstack1l11l1l1l1_opy_
  global bstack11llll1l_opy_
  global bstack1lll11lll_opy_
  global bstack1l1l1l1l1_opy_
  bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠫࠬ௷")
  bstack1llll1llll_opy_(bstack1l1ll11l11_opy_, logger)
  if bstack1lll1l11l1_opy_ and isinstance(bstack1lll1l11l1_opy_, str):
    bstack1lll1l11l1_opy_ = eval(bstack1lll1l11l1_opy_)
  if bstack1lll1l11l1_opy_:
    CONFIG = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ௸")]
    bstack1l11l1l1l1_opy_ = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ௹")]
    bstack11llll1l_opy_ = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ௺")]
    bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ௻"), bstack11llll1l_opy_)
    bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ௼")
  bstack1l1l1l1l1_opy_.bstack1l11lllll1_opy_(bstack11ll11_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ௽"), uuid4().__str__())
  logger.debug(bstack11ll11_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩࡃࠧ௾") + bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ௿")))
  if not bstack1l11ll1ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1lll11l1_opy_)
      return
    if sys.argv[1] == bstack11ll11_opy_ (u"࠭࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩఀ") or sys.argv[1] == bstack11ll11_opy_ (u"ࠧ࠮ࡸࠪఁ"):
      logger.info(bstack11ll11_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡑࡻࡷ࡬ࡴࡴࠠࡔࡆࡎࠤࡻࢁࡽࠨం").format(__version__))
      return
    if sys.argv[1] == bstack11ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨః"):
      bstack111l1ll1_opy_()
      return
  args = sys.argv
  bstack1l1l11111_opy_()
  global bstack1111llll1_opy_
  global bstack1l11lll111_opy_
  global bstack1l11lll1_opy_
  global bstack1l11ll11l1_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack111111ll_opy_
  global bstack111lll1l1_opy_
  global bstack1ll11lllll_opy_
  global bstack111111111_opy_
  global bstack1l1ll1111_opy_
  global bstack1ll1ll1ll_opy_
  bstack1l11lll111_opy_ = len(CONFIG.get(bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఄ"), []))
  if not bstack11ll111ll_opy_:
    if args[1] == bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫఅ") or args[1] == bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭ఆ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ఇ")
      args = args[2:]
    elif args[1] == bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఈ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧఉ")
      args = args[2:]
    elif args[1] == bstack11ll11_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨఊ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩఋ")
      args = args[2:]
    elif args[1] == bstack11ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬఌ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭఍")
      args = args[2:]
    elif args[1] == bstack11ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ఎ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧఏ")
      args = args[2:]
    elif args[1] == bstack11ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨఐ"):
      bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ఑")
      args = args[2:]
    else:
      if not bstack11ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ఒ") in CONFIG or str(CONFIG[bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧఓ")]).lower() in [bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬఔ"), bstack11ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧక")]:
        bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧఖ")
        args = args[1:]
      elif str(CONFIG[bstack11ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫగ")]).lower() == bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨఘ"):
        bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩఙ")
        args = args[1:]
      elif str(CONFIG[bstack11ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧచ")]).lower() == bstack11ll11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫఛ"):
        bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬజ")
        args = args[1:]
      elif str(CONFIG[bstack11ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪఝ")]).lower() == bstack11ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨఞ"):
        bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩట")
        args = args[1:]
      elif str(CONFIG[bstack11ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ఠ")]).lower() == bstack11ll11_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫడ"):
        bstack11ll111ll_opy_ = bstack11ll11_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬఢ")
        args = args[1:]
      else:
        os.environ[bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨణ")] = bstack11ll111ll_opy_
        bstack1111ll1l1_opy_(bstack11l1l11l_opy_)
  os.environ[bstack11ll11_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨత")] = bstack11ll111ll_opy_
  bstack1lll11lll_opy_ = bstack11ll111ll_opy_
  global bstack1llllll111_opy_
  if bstack1lll1l11l1_opy_:
    try:
      os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪథ")] = bstack11ll111ll_opy_
      bstack111l11l11_opy_(bstack1llllll1l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack11ll1llll_opy_.format(str(e)))
  global bstack1lll1ll11l_opy_
  global bstack1l1l11lll_opy_
  global bstack11lll1ll1_opy_
  global bstack1llll1l1l1_opy_
  global bstack1l1l111ll1_opy_
  global bstack1ll1111ll_opy_
  global bstack11l11l1l1_opy_
  global bstack1llll111l1_opy_
  global bstack1l11l1l11_opy_
  global bstack11lll1l11_opy_
  global bstack1l1ll11l1l_opy_
  global bstack11ll1ll11_opy_
  global bstack1llll11ll1_opy_
  global bstack11lllll11_opy_
  global bstack1lllll1lll_opy_
  global bstack1lll111l1l_opy_
  global bstack1l1llllll_opy_
  global bstack111l1ll1l_opy_
  global bstack1llll1111l_opy_
  global bstack11l11l1ll_opy_
  global bstack1l111l111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lll1ll11l_opy_ = webdriver.Remote.__init__
    bstack1l1l11lll_opy_ = WebDriver.quit
    bstack11ll1ll11_opy_ = WebDriver.close
    bstack1lllll1lll_opy_ = WebDriver.get
    bstack1l111l111_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1llllll111_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    global bstack1lll11ll11_opy_
    from QWeb.keywords import browser
    bstack1lll11ll11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1ll1llll_opy_(CONFIG) and bstack11111llll_opy_():
    if bstack111ll1l11_opy_() < version.parse(bstack1ll11l11l1_opy_):
      logger.error(bstack1l1ll1lll1_opy_.format(bstack111ll1l11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lll111l1l_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1111l1l1_opy_.format(str(e)))
  if not CONFIG.get(bstack11ll11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫద"), False) and not bstack1lll1l11l1_opy_:
    logger.info(bstack1l1l1l1111_opy_)
  if bstack11ll111ll_opy_ != bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪధ") or (bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫన") and not bstack1lll1l11l1_opy_):
    bstack1lll11ll1l_opy_()
  if (bstack11ll111ll_opy_ in [bstack11ll11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ఩"), bstack11ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬప"), bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨఫ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111lll11_opy_
        bstack1ll1111ll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11111lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import bstack1l1l11ll1l_opy_
        bstack1l1l111ll1_opy_ = bstack1l1l11ll1l_opy_.close
      except Exception as e:
        logger.debug(bstack1l11ll111l_opy_ + str(e))
    except Exception as e:
      bstack11l1llll_opy_(e, bstack11111lll_opy_)
    if bstack11ll111ll_opy_ != bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩబ"):
      bstack1111ll11_opy_()
    bstack11lll1ll1_opy_ = Output.start_test
    bstack1llll1l1l1_opy_ = Output.end_test
    bstack11l11l1l1_opy_ = TestStatus.__init__
    bstack1l11l1l11_opy_ = pabot._run
    bstack11lll1l11_opy_ = QueueItem.__init__
    bstack1l1ll11l1l_opy_ = pabot._create_command_for_execution
    bstack1llll1111l_opy_ = pabot._report_results
  if bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩభ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11l1llll_opy_(e, bstack1l1ll1l1l1_opy_)
    bstack1llll11ll1_opy_ = Runner.run_hook
    bstack11lllll11_opy_ = Step.run
  if bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪమ"):
    try:
      from _pytest.config import Config
      bstack1l1llllll_opy_ = Config.getoption
      from _pytest import runner
      bstack111l1ll1l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1lllll11ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack11l11l1ll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬయ"))
  try:
    framework_name = bstack11ll11_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫర") if bstack11ll111ll_opy_ in [bstack11ll11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬఱ"), bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ల"), bstack11ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩళ")] else bstack11ll1l1l1_opy_(bstack11ll111ll_opy_)
    bstack1l1l111lll_opy_.launch(CONFIG, {
      bstack11ll11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪఴ"): bstack11ll11_opy_ (u"ࠪࡿ࠵ࢃ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩవ").format(framework_name) if bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫశ") and bstack1l1ll11l1_opy_() else framework_name,
      bstack11ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩష"): bstack11l111l1_opy_(framework_name),
      bstack11ll11_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫస"): __version__,
      bstack11ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨహ"): bstack11ll111ll_opy_
    })
  except Exception as e:
    logger.debug(bstack1l11lllll_opy_.format(bstack11ll11_opy_ (u"ࠨࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ఺"), str(e)))
  if bstack11ll111ll_opy_ in bstack1l11ll1l11_opy_:
    try:
      framework_name = bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ఻") if bstack11ll111ll_opy_ in [bstack11ll11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵ఼ࠩ"), bstack11ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪఽ")] else bstack11ll111ll_opy_
      if bstack1l111ll1_opy_ and bstack11ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬా") in CONFIG and CONFIG[bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ి")] == True:
        if bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧీ") in CONFIG:
          os.environ[bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩు")] = os.getenv(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪూ"), json.dumps(CONFIG[bstack11ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪృ")]))
          CONFIG[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫౄ")].pop(bstack11ll11_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ౅"), None)
          CONFIG[bstack11ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ె")].pop(bstack11ll11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬే"), None)
        bstack11lll1ll_opy_, bstack111111l11_opy_ = bstack1l111111l_opy_.bstack1ll1l111_opy_(CONFIG, bstack11ll111ll_opy_, bstack11l111l1_opy_(framework_name), str(bstack111ll1l11_opy_()))
        if not bstack11lll1ll_opy_ is None:
          os.environ[bstack11ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ై")] = bstack11lll1ll_opy_
          os.environ[bstack11ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡘࡊ࡙ࡔࡠࡔࡘࡒࡤࡏࡄࠨ౉")] = str(bstack111111l11_opy_)
    except Exception as e:
      logger.debug(bstack1l11lllll_opy_.format(bstack11ll11_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪొ"), str(e)))
  if bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫో"):
    bstack1l11lll1_opy_ = True
    if bstack1lll1l11l1_opy_ and bstack1l11ll1ll_opy_:
      bstack111111ll_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩౌ"), {}).get(bstack11ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ్"))
      bstack1lll1llll1_opy_(bstack1ll1lllll_opy_)
    elif bstack1lll1l11l1_opy_:
      bstack111111ll_opy_ = CONFIG.get(bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ౎"), {}).get(bstack11ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ౏"))
      global bstack1l111l11l_opy_
      try:
        if bstack11l111l11_opy_(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౐")]) and multiprocessing.current_process().name == bstack11ll11_opy_ (u"ࠪ࠴ࠬ౑"):
          bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౒")].remove(bstack11ll11_opy_ (u"ࠬ࠳࡭ࠨ౓"))
          bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౔")].remove(bstack11ll11_opy_ (u"ࠧࡱࡦࡥౕࠫ"))
          bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨౖࠫ")] = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౗")][0]
          with open(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ౘ")], bstack11ll11_opy_ (u"ࠫࡷ࠭ౙ")) as f:
            bstack1ll1l1llll_opy_ = f.read()
          bstack1ll11ll1l1_opy_ = bstack11ll11_opy_ (u"ࠧࠨࠢࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡪ࡫ࠡ࡫ࡰࡴࡴࡸࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨ࠿ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࠩࡽࢀ࠭ࡀࠦࡦࡳࡱࡰࠤࡵࡪࡢࠡ࡫ࡰࡴࡴࡸࡴࠡࡒࡧࡦࡀࠦ࡯ࡨࡡࡧࡦࠥࡃࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࡴࡨࡥࡰࡁࠊࡥࡧࡩࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠨࡴࡧ࡯ࡪ࠱ࠦࡡࡳࡩ࠯ࠤࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠠ࠾ࠢ࠳࠭࠿ࠐࠠࠡࡶࡵࡽ࠿ࠐࠠࠡࠢࠣࡥࡷ࡭ࠠ࠾ࠢࡶࡸࡷ࠮ࡩ࡯ࡶࠫࡥࡷ࡭ࠩࠬ࠳࠳࠭ࠏࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࡰࡢࡵࡶࠎࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࡕࡪࡢ࠯ࡦࡲࡣࡧࠦ࠽ࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠎࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭ࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࡒࡧࡦ࠭࠯࠮ࡴࡧࡷࡣࡹࡸࡡࡤࡧࠫ࠭ࡡࡴࠢࠣࠤౚ").format(str(bstack1lll1l11l1_opy_))
          bstack1l1l1l111_opy_ = bstack1ll11ll1l1_opy_ + bstack1ll1l1llll_opy_
          bstack1llll1l1l_opy_ = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౛")] + bstack11ll11_opy_ (u"ࠧࡠࡤࡶࡸࡦࡩ࡫ࡠࡶࡨࡱࡵ࠴ࡰࡺࠩ౜")
          with open(bstack1llll1l1l_opy_, bstack11ll11_opy_ (u"ࠨࡹࠪౝ")):
            pass
          with open(bstack1llll1l1l_opy_, bstack11ll11_opy_ (u"ࠤࡺ࠯ࠧ౞")) as f:
            f.write(bstack1l1l1l111_opy_)
          import subprocess
          bstack11ll111l_opy_ = subprocess.run([bstack11ll11_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥ౟"), bstack1llll1l1l_opy_])
          if os.path.exists(bstack1llll1l1l_opy_):
            os.unlink(bstack1llll1l1l_opy_)
          os._exit(bstack11ll111l_opy_.returncode)
        else:
          if bstack11l111l11_opy_(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧౠ")]):
            bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨౡ")].remove(bstack11ll11_opy_ (u"࠭࠭࡮ࠩౢ"))
            bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪౣ")].remove(bstack11ll11_opy_ (u"ࠨࡲࡧࡦࠬ౤"))
            bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౥")] = bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౦")][0]
          bstack1lll1llll1_opy_(bstack1ll1lllll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౧")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11ll11_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧ౨")] = bstack11ll11_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨ౩")
          mod_globals[bstack11ll11_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩ౪")] = os.path.abspath(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ౫")])
          exec(open(bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౬")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11ll11_opy_ (u"ࠪࡇࡦࡻࡧࡩࡶࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠪ౭").format(str(e)))
          for driver in bstack1l111l11l_opy_:
            bstack1ll11l1ll1_opy_.append({
              bstack11ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ౮"): bstack1lll1l11l1_opy_[bstack11ll11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ౯")],
              bstack11ll11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ౰"): str(e),
              bstack11ll11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭౱"): multiprocessing.current_process().name
            })
            bstack11l11ll11_opy_(driver, bstack11ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ౲"), bstack11ll11_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ౳") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l111l11l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11llll1l_opy_, CONFIG, logger)
      bstack1lll1111l1_opy_()
      bstack1l11l11lll_opy_()
      bstack1l1l11ll_opy_ = {
        bstack11ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౴"): args[0],
        bstack11ll11_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ౵"): CONFIG,
        bstack11ll11_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭౶"): bstack1l11l1l1l1_opy_,
        bstack11ll11_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ౷"): bstack11llll1l_opy_
      }
      percy.bstack1ll111ll11_opy_()
      if bstack11ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ౸") in CONFIG:
        bstack11l11l11_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l1l1l1ll_opy_ = manager.list()
        if bstack11l111l11_opy_(args):
          for index, platform in enumerate(CONFIG[bstack11ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ౹")]):
            if index == 0:
              bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౺")] = args
            bstack11l11l11_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l1l11ll_opy_, bstack1l1l1l1ll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭౻")]):
            bstack11l11l11_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l1l11ll_opy_, bstack1l1l1l1ll_opy_)))
        for t in bstack11l11l11_opy_:
          t.start()
        for t in bstack11l11l11_opy_:
          t.join()
        bstack1ll11lllll_opy_ = list(bstack1l1l1l1ll_opy_)
      else:
        if bstack11l111l11_opy_(args):
          bstack1l1l11ll_opy_[bstack11ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౼")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1l1l11ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1lll1llll1_opy_(bstack1ll1lllll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11ll11_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧ౽")] = bstack11ll11_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨ౾")
          mod_globals[bstack11ll11_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩ౿")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧಀ") or bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ"):
    percy.init(bstack11llll1l_opy_, CONFIG, logger)
    percy.bstack1ll111ll11_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11l1llll_opy_(e, bstack11111lll_opy_)
    bstack1lll1111l1_opy_()
    bstack1lll1llll1_opy_(bstack1ll1l11l11_opy_)
    if bstack1l111ll1_opy_ and bstack11ll11_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨಂ") in args:
      i = args.index(bstack11ll11_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩಃ"))
      args.pop(i)
      args.pop(i)
    if bstack1l111ll1_opy_:
      args.insert(0, str(bstack1111llll1_opy_))
      args.insert(0, str(bstack11ll11_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ಄")))
    if bstack1l1l111lll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11lll1lll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1llll1l11_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11ll11_opy_ (u"ࠨࡒࡐࡄࡒࡘࡤࡕࡐࡕࡋࡒࡒࡘࠨಅ"),
        ).parse_args(bstack11lll1lll_opy_)
        bstack1ll1l11lll_opy_ = args.index(bstack11lll1lll_opy_[0]) if len(bstack11lll1lll_opy_) > 0 else len(args)
        args.insert(bstack1ll1l11lll_opy_, str(bstack11ll11_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫಆ")))
        args.insert(bstack1ll1l11lll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡴࡲࡦࡴࡺ࡟࡭࡫ࡶࡸࡪࡴࡥࡳ࠰ࡳࡽࠬಇ"))))
        if bstack111l1l1l_opy_(os.environ.get(bstack11ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧಈ"))) and str(os.environ.get(bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧಉ"), bstack11ll11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩಊ"))) != bstack11ll11_opy_ (u"ࠬࡴࡵ࡭࡮ࠪಋ"):
          for bstack1l111l1l_opy_ in bstack1llll1l11_opy_:
            args.remove(bstack1l111l1l_opy_)
          bstack11l1111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪಌ")).split(bstack11ll11_opy_ (u"ࠧ࠭ࠩ಍"))
          for bstack111lll111_opy_ in bstack11l1111ll_opy_:
            args.append(bstack111lll111_opy_)
      except Exception as e:
        logger.error(bstack11ll11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡵࡶࡤࡧ࡭࡯࡮ࡨࠢ࡯࡭ࡸࡺࡥ࡯ࡧࡵࠤ࡫ࡵࡲࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࠦಎ").format(e))
    pabot.main(args)
  elif bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪಏ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11l1llll_opy_(e, bstack11111lll_opy_)
    for a in args:
      if bstack11ll11_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩಐ") in a:
        bstack1ll1l1l1l1_opy_ = int(a.split(bstack11ll11_opy_ (u"ࠫ࠿࠭಑"))[1])
      if bstack11ll11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩಒ") in a:
        bstack111111ll_opy_ = str(a.split(bstack11ll11_opy_ (u"࠭࠺ࠨಓ"))[1])
      if bstack11ll11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧಔ") in a:
        bstack111lll1l1_opy_ = str(a.split(bstack11ll11_opy_ (u"ࠨ࠼ࠪಕ"))[1])
    bstack1l1llll11_opy_ = None
    if bstack11ll11_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨಖ") in args:
      i = args.index(bstack11ll11_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩಗ"))
      args.pop(i)
      bstack1l1llll11_opy_ = args.pop(i)
    if bstack1l1llll11_opy_ is not None:
      global bstack11ll1111_opy_
      bstack11ll1111_opy_ = bstack1l1llll11_opy_
    bstack1lll1llll1_opy_(bstack1ll1l11l11_opy_)
    run_cli(args)
    if bstack11ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨಘ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll11l1ll1_opy_.append(bstack1l11111l_opy_)
  elif bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬಙ"):
    percy.init(bstack11llll1l_opy_, CONFIG, logger)
    percy.bstack1ll111ll11_opy_()
    bstack1ll111ll1_opy_ = bstack11lll1l1_opy_(args, logger, CONFIG, bstack1l111ll1_opy_)
    bstack1ll111ll1_opy_.bstack1ll1111l11_opy_()
    bstack1lll1111l1_opy_()
    bstack1l11ll11l1_opy_ = True
    bstack1l1ll1111_opy_ = bstack1ll111ll1_opy_.bstack111lll11l_opy_()
    bstack1ll111ll1_opy_.bstack1l1l11ll_opy_(bstack1111l1lll_opy_)
    bstack11111l11_opy_ = bstack1ll111ll1_opy_.bstack1lll11l11_opy_(bstack111ll1ll_opy_, {
      bstack11ll11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧಚ"): bstack1l11l1l1l1_opy_,
      bstack11ll11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩಛ"): bstack11llll1l_opy_,
      bstack11ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫಜ"): bstack1l111ll1_opy_
    })
    try:
      bstack1ll11ll1ll_opy_, bstack1l1ll1l111_opy_ = map(list, zip(*bstack11111l11_opy_))
      bstack111111111_opy_ = bstack1ll11ll1ll_opy_[0]
      for status_code in bstack1l1ll1l111_opy_:
        if status_code != 0:
          bstack1ll1ll1ll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡩࡷࡸ࡯ࡳࡵࠣࡥࡳࡪࠠࡴࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠳ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠽ࠤࢀࢃࠢಝ").format(str(e)))
  elif bstack11ll111ll_opy_ == bstack11ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಞ"):
    try:
      from behave.__main__ import main as bstack111ll111l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11l1llll_opy_(e, bstack1l1ll1l1l1_opy_)
    bstack1lll1111l1_opy_()
    bstack1l11ll11l1_opy_ = True
    bstack1111l1111_opy_ = 1
    if bstack11ll11_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫಟ") in CONFIG:
      bstack1111l1111_opy_ = CONFIG[bstack11ll11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬಠ")]
    bstack11l1lllll_opy_ = int(bstack1111l1111_opy_) * int(len(CONFIG[bstack11ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಡ")]))
    config = Configuration(args)
    bstack1lll1lll1_opy_ = config.paths
    if len(bstack1lll1lll1_opy_) == 0:
      import glob
      pattern = bstack11ll11_opy_ (u"ࠧࠫࠬ࠲࠮࠳࡬ࡥࡢࡶࡸࡶࡪ࠭ಢ")
      bstack11llll111_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11llll111_opy_)
      config = Configuration(args)
      bstack1lll1lll1_opy_ = config.paths
    bstack1l1l1111l_opy_ = [os.path.normpath(item) for item in bstack1lll1lll1_opy_]
    bstack1llll11l1l_opy_ = [os.path.normpath(item) for item in args]
    bstack1l1l11ll11_opy_ = [item for item in bstack1llll11l1l_opy_ if item not in bstack1l1l1111l_opy_]
    import platform as pf
    if pf.system().lower() == bstack11ll11_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩಣ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l1l1111l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l1l1ll1_opy_)))
                    for bstack11l1l1ll1_opy_ in bstack1l1l1111l_opy_]
    bstack111l1111l_opy_ = []
    for spec in bstack1l1l1111l_opy_:
      bstack1l1111l11_opy_ = []
      bstack1l1111l11_opy_ += bstack1l1l11ll11_opy_
      bstack1l1111l11_opy_.append(spec)
      bstack111l1111l_opy_.append(bstack1l1111l11_opy_)
    execution_items = []
    for bstack1l1111l11_opy_ in bstack111l1111l_opy_:
      for index, _ in enumerate(CONFIG[bstack11ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬತ")]):
        item = {}
        item[bstack11ll11_opy_ (u"ࠪࡥࡷ࡭ࠧಥ")] = bstack11ll11_opy_ (u"ࠫࠥ࠭ದ").join(bstack1l1111l11_opy_)
        item[bstack11ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫಧ")] = index
        execution_items.append(item)
    bstack1lll1l1ll_opy_ = bstack1ll1l1111_opy_(execution_items, bstack11l1lllll_opy_)
    for execution_item in bstack1lll1l1ll_opy_:
      bstack11l11l11_opy_ = []
      for item in execution_item:
        bstack11l11l11_opy_.append(bstack1l11ll1l_opy_(name=str(item[bstack11ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬನ")]),
                                             target=bstack1l1l1ll11_opy_,
                                             args=(item[bstack11ll11_opy_ (u"ࠧࡢࡴࡪࠫ಩")],)))
      for t in bstack11l11l11_opy_:
        t.start()
      for t in bstack11l11l11_opy_:
        t.join()
  else:
    bstack1111ll1l1_opy_(bstack11l1l11l_opy_)
  if not bstack1lll1l11l1_opy_:
    bstack1ll111ll1l_opy_()
  bstack1l1l1l1l11_opy_.bstack1llll11lll_opy_()
def browserstack_initialize(bstack11ll1l11_opy_=None):
  run_on_browserstack(bstack11ll1l11_opy_, None, True)
def bstack1ll111ll1l_opy_():
  global CONFIG
  global bstack1lll11lll_opy_
  global bstack1ll1ll1ll_opy_
  global bstack11l1l11l1_opy_
  global bstack1l1l1l1l1_opy_
  bstack1l1l111lll_opy_.stop(bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨಪ")))
  bstack1l1l111lll_opy_.bstack1l11ll11l_opy_()
  if bstack1l111111l_opy_.bstack11ll11ll1_opy_(CONFIG):
    bstack1l111111l_opy_.bstack1lll1llll_opy_()
  [bstack1l11l1ll11_opy_, bstack1l1lllll_opy_] = get_build_link()
  if bstack1l11l1ll11_opy_ is not None and bstack11l11111l_opy_() != -1:
    sessions = bstack1l1llll1l1_opy_(bstack1l11l1ll11_opy_)
    bstack1l1ll11111_opy_(sessions, bstack1l1lllll_opy_)
  if bstack1lll11lll_opy_ == bstack11ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩಫ") and bstack1ll1ll1ll_opy_ != 0:
    sys.exit(bstack1ll1ll1ll_opy_)
  if bstack1lll11lll_opy_ == bstack11ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಬ") and bstack11l1l11l1_opy_ != 0:
    sys.exit(bstack11l1l11l1_opy_)
def bstack11ll1l1l1_opy_(bstack11lll11l_opy_):
  if bstack11lll11l_opy_:
    return bstack11lll11l_opy_.capitalize()
  else:
    return bstack11ll11_opy_ (u"ࠫࠬಭ")
def bstack1ll111l1ll_opy_(bstack111ll11l1_opy_):
  if bstack11ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪಮ") in bstack111ll11l1_opy_ and bstack111ll11l1_opy_[bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫಯ")] != bstack11ll11_opy_ (u"ࠧࠨರ"):
    return bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ಱ")]
  else:
    bstack1l1lllll1l_opy_ = bstack11ll11_opy_ (u"ࠤࠥಲ")
    if bstack11ll11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪಳ") in bstack111ll11l1_opy_ and bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ಴")] != None:
      bstack1l1lllll1l_opy_ += bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬವ")] + bstack11ll11_opy_ (u"ࠨࠬࠡࠤಶ")
      if bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠧࡰࡵࠪಷ")] == bstack11ll11_opy_ (u"ࠣ࡫ࡲࡷࠧಸ"):
        bstack1l1lllll1l_opy_ += bstack11ll11_opy_ (u"ࠤ࡬ࡓࡘࠦࠢಹ")
      bstack1l1lllll1l_opy_ += (bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ಺")] or bstack11ll11_opy_ (u"ࠫࠬ಻"))
      return bstack1l1lllll1l_opy_
    else:
      bstack1l1lllll1l_opy_ += bstack11ll1l1l1_opy_(bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ಼࠭")]) + bstack11ll11_opy_ (u"ࠨࠠࠣಽ") + (
              bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩಾ")] or bstack11ll11_opy_ (u"ࠨࠩಿ")) + bstack11ll11_opy_ (u"ࠤ࠯ࠤࠧೀ")
      if bstack111ll11l1_opy_[bstack11ll11_opy_ (u"ࠪࡳࡸ࠭ು")] == bstack11ll11_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧೂ"):
        bstack1l1lllll1l_opy_ += bstack11ll11_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥೃ")
      bstack1l1lllll1l_opy_ += bstack111ll11l1_opy_[bstack11ll11_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪೄ")] or bstack11ll11_opy_ (u"ࠧࠨ೅")
      return bstack1l1lllll1l_opy_
def bstack1ll111lll_opy_(bstack1111lll1_opy_):
  if bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠣࡦࡲࡲࡪࠨೆ"):
    return bstack11ll11_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬೇ")
  elif bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥೈ"):
    return bstack11ll11_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ೉")
  elif bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧೊ"):
    return bstack11ll11_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ೋ")
  elif bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨೌ"):
    return bstack11ll11_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀ್ࠪ")
  elif bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥ೎"):
    return bstack11ll11_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ೏")
  elif bstack1111lll1_opy_ == bstack11ll11_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧ೐"):
    return bstack11ll11_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭೑")
  else:
    return bstack11ll11_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪ೒") + bstack11ll1l1l1_opy_(
      bstack1111lll1_opy_) + bstack11ll11_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭೓")
def bstack1l1lll111_opy_(session):
  return bstack11ll11_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨ೔").format(
    session[bstack11ll11_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ೕ")], bstack1ll111l1ll_opy_(session), bstack1ll111lll_opy_(session[bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩೖ")]),
    bstack1ll111lll_opy_(session[bstack11ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ೗")]),
    bstack11ll1l1l1_opy_(session[bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭೘")] or session[bstack11ll11_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭೙")] or bstack11ll11_opy_ (u"ࠧࠨ೚")) + bstack11ll11_opy_ (u"ࠣࠢࠥ೛") + (session[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ೜")] or bstack11ll11_opy_ (u"ࠪࠫೝ")),
    session[bstack11ll11_opy_ (u"ࠫࡴࡹࠧೞ")] + bstack11ll11_opy_ (u"ࠧࠦࠢ೟") + session[bstack11ll11_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪೠ")], session[bstack11ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩೡ")] or bstack11ll11_opy_ (u"ࠨࠩೢ"),
    session[bstack11ll11_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ೣ")] if session[bstack11ll11_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧ೤")] else bstack11ll11_opy_ (u"ࠫࠬ೥"))
def bstack1l1ll11111_opy_(sessions, bstack1l1lllll_opy_):
  try:
    bstack11ll111l1_opy_ = bstack11ll11_opy_ (u"ࠧࠨ೦")
    if not os.path.exists(bstack1lll111l_opy_):
      os.mkdir(bstack1lll111l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll11_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫ೧")), bstack11ll11_opy_ (u"ࠧࡳࠩ೨")) as f:
      bstack11ll111l1_opy_ = f.read()
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack11ll11_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬ೩"), str(len(sessions)))
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack11ll11_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩ೪"), bstack1l1lllll_opy_)
    bstack11ll111l1_opy_ = bstack11ll111l1_opy_.replace(bstack11ll11_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫ೫"),
                                              sessions[0].get(bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨ೬")) if sessions[0] else bstack11ll11_opy_ (u"ࠬ࠭೭"))
    with open(os.path.join(bstack1lll111l_opy_, bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪ೮")), bstack11ll11_opy_ (u"ࠧࡸࠩ೯")) as stream:
      stream.write(bstack11ll111l1_opy_.split(bstack11ll11_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬ೰"))[0])
      for session in sessions:
        stream.write(bstack1l1lll111_opy_(session))
      stream.write(bstack11ll111l1_opy_.split(bstack11ll11_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ೱ"))[1])
    logger.info(bstack11ll11_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭ೲ").format(bstack1lll111l_opy_));
  except Exception as e:
    logger.debug(bstack111l111ll_opy_.format(str(e)))
def bstack1l1llll1l1_opy_(bstack1l11l1ll11_opy_):
  global CONFIG
  try:
    host = bstack11ll11_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧೳ") if bstack11ll11_opy_ (u"ࠬࡧࡰࡱࠩ೴") in CONFIG else bstack11ll11_opy_ (u"࠭ࡡࡱ࡫ࠪ೵")
    user = CONFIG[bstack11ll11_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ೶")]
    key = CONFIG[bstack11ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ೷")]
    bstack1l1l1ll1l_opy_ = bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ೸") if bstack11ll11_opy_ (u"ࠪࡥࡵࡶࠧ೹") in CONFIG else bstack11ll11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭೺")
    url = bstack11ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪ೻").format(user, key, host, bstack1l1l1ll1l_opy_,
                                                                                bstack1l11l1ll11_opy_)
    headers = {
      bstack11ll11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ೼"): bstack11ll11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ೽"),
    }
    proxies = bstack111ll11l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭೾")], response.json()))
  except Exception as e:
    logger.debug(bstack1l11lll1l_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack1ll1l1l111_opy_
  try:
    if bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ೿") in CONFIG:
      host = bstack11ll11_opy_ (u"ࠪࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠭ഀ") if bstack11ll11_opy_ (u"ࠫࡦࡶࡰࠨഁ") in CONFIG else bstack11ll11_opy_ (u"ࠬࡧࡰࡪࠩം")
      user = CONFIG[bstack11ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨഃ")]
      key = CONFIG[bstack11ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪഄ")]
      bstack1l1l1ll1l_opy_ = bstack11ll11_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧഅ") if bstack11ll11_opy_ (u"ࠩࡤࡴࡵ࠭ആ") in CONFIG else bstack11ll11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬഇ")
      url = bstack11ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠫഈ").format(user, key, host, bstack1l1l1ll1l_opy_)
      headers = {
        bstack11ll11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫഉ"): bstack11ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩഊ"),
      }
      if bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩഋ") in CONFIG:
        params = {bstack11ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഌ"): CONFIG[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ഍")], bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭എ"): CONFIG[bstack11ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ഏ")]}
      else:
        params = {bstack11ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪഐ"): CONFIG[bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ഑")]}
      proxies = bstack111ll11l_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack11l111ll_opy_ = response.json()[0][bstack11ll11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡧࡻࡩ࡭ࡦࠪഒ")]
        if bstack11l111ll_opy_:
          bstack1l1lllll_opy_ = bstack11l111ll_opy_[bstack11ll11_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬഓ")].split(bstack11ll11_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤ࠯ࡥࡹ࡮ࡲࡤࠨഔ"))[0] + bstack11ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵ࠲ࠫക") + bstack11l111ll_opy_[
            bstack11ll11_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧഖ")]
          logger.info(bstack1ll11l1l1_opy_.format(bstack1l1lllll_opy_))
          bstack1ll1l1l111_opy_ = bstack11l111ll_opy_[bstack11ll11_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨഗ")]
          bstack1l1111lll_opy_ = CONFIG[bstack11ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩഘ")]
          if bstack11ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩങ") in CONFIG:
            bstack1l1111lll_opy_ += bstack11ll11_opy_ (u"ࠨࠢࠪച") + CONFIG[bstack11ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫഛ")]
          if bstack1l1111lll_opy_ != bstack11l111ll_opy_[bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨജ")]:
            logger.debug(bstack1l1lll1ll_opy_.format(bstack11l111ll_opy_[bstack11ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩഝ")], bstack1l1111lll_opy_))
          return [bstack11l111ll_opy_[bstack11ll11_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨഞ")], bstack1l1lllll_opy_]
    else:
      logger.warn(bstack111llll11_opy_)
  except Exception as e:
    logger.debug(bstack1l1l1ll11l_opy_.format(str(e)))
  return [None, None]
def bstack1l1111ll_opy_(url, bstack111111lll_opy_=False):
  global CONFIG
  global bstack1lllll1l11_opy_
  if not bstack1lllll1l11_opy_:
    hostname = bstack1l111l11_opy_(url)
    is_private = bstack1l11ll11ll_opy_(hostname)
    if (bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪട") in CONFIG and not bstack111l1l1l_opy_(CONFIG[bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫഠ")])) and (is_private or bstack111111lll_opy_):
      bstack1lllll1l11_opy_ = hostname
def bstack1l111l11_opy_(url):
  return urlparse(url).hostname
def bstack1l11ll11ll_opy_(hostname):
  for bstack1l1ll1ll_opy_ in bstack1ll1ll1l1_opy_:
    regex = re.compile(bstack1l1ll1ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11l1l1lll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll1l1l1l1_opy_
  bstack11lll1l1l_opy_ = not (bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഡ"), None) and bstack1l1lll1ll1_opy_(
          threading.current_thread(), bstack11ll11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഢ"), None))
  bstack1lll1ll1_opy_ = getattr(driver, bstack11ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪണ"), None) != True
  if not bstack1l111111l_opy_.bstack111l1ll11_opy_(CONFIG, bstack1ll1l1l1l1_opy_) or (bstack1lll1ll1_opy_ and bstack11lll1l1l_opy_):
    logger.warning(bstack11ll11_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢത"))
    return {}
  try:
    logger.debug(bstack11ll11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩഥ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1ll1lll1ll_opy_.bstack1ll11l1lll_opy_)
    return results
  except Exception:
    logger.error(bstack11ll11_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡻࡪࡸࡥࠡࡨࡲࡹࡳࡪ࠮ࠣദ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll1l1l1l1_opy_
  bstack11lll1l1l_opy_ = not (bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫധ"), None) and bstack1l1lll1ll1_opy_(
          threading.current_thread(), bstack11ll11_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧന"), None))
  bstack1lll1ll1_opy_ = getattr(driver, bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩഩ"), None) != True
  if not bstack1l111111l_opy_.bstack111l1ll11_opy_(CONFIG, bstack1ll1l1l1l1_opy_) or (bstack1lll1ll1_opy_ and bstack11lll1l1l_opy_):
    logger.warning(bstack11ll11_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢപ"))
    return {}
  try:
    logger.debug(bstack11ll11_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩഫ"))
    logger.debug(perform_scan(driver))
    bstack1l1lll11ll_opy_ = driver.execute_async_script(bstack1ll1lll1ll_opy_.bstack111l11lll_opy_)
    return bstack1l1lll11ll_opy_
  except Exception:
    logger.error(bstack11ll11_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨബ"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1ll1l1l1l1_opy_
  bstack11lll1l1l_opy_ = not (bstack1l1lll1ll1_opy_(threading.current_thread(), bstack11ll11_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪഭ"), None) and bstack1l1lll1ll1_opy_(
          threading.current_thread(), bstack11ll11_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭മ"), None))
  bstack1lll1ll1_opy_ = getattr(driver, bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨയ"), None) != True
  if not bstack1l111111l_opy_.bstack111l1ll11_opy_(CONFIG, bstack1ll1l1l1l1_opy_) or (bstack1lll1ll1_opy_ and bstack11lll1l1l_opy_):
    logger.warning(bstack11ll11_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡸࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦര"))
    return {}
  try:
    bstack1llll1l11l_opy_ = driver.execute_async_script(bstack1ll1lll1ll_opy_.perform_scan, {bstack11ll11_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪറ"): kwargs.get(bstack11ll11_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬല"), None) or bstack11ll11_opy_ (u"ࠬ࠭ള")})
    return bstack1llll1l11l_opy_
  except Exception:
    logger.error(bstack11ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠧഴ"))
    return {}