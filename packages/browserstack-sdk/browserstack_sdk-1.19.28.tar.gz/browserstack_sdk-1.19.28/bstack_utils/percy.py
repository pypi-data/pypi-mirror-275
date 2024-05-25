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
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11l1ll1ll_opy_, bstack1l1ll11ll_opy_
class bstack1lllll1ll1_opy_:
  working_dir = os.getcwd()
  bstack11l1l11ll_opy_ = False
  config = {}
  binary_path = bstack11ll11_opy_ (u"ࠫࠬᏥ")
  bstack1111111lll_opy_ = bstack11ll11_opy_ (u"ࠬ࠭Ꮶ")
  bstack1l1l11111l_opy_ = False
  bstack1111l11111_opy_ = None
  bstack11111l1111_opy_ = {}
  bstack111111llll_opy_ = 300
  bstack1llllllll1l_opy_ = False
  logger = None
  bstack111111111l_opy_ = False
  bstack11111llll1_opy_ = bstack11ll11_opy_ (u"࠭ࠧᏧ")
  bstack11111ll111_opy_ = {
    bstack11ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᏨ") : 1,
    bstack11ll11_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩᏩ") : 2,
    bstack11ll11_opy_ (u"ࠩࡨࡨ࡬࡫ࠧᏪ") : 3,
    bstack11ll11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪᏫ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11111l1lll_opy_(self):
    bstack11111l1l1l_opy_ = bstack11ll11_opy_ (u"ࠫࠬᏬ")
    bstack11111111l1_opy_ = sys.platform
    bstack11111l1l11_opy_ = bstack11ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᏭ")
    if re.match(bstack11ll11_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨᏮ"), bstack11111111l1_opy_) != None:
      bstack11111l1l1l_opy_ = bstack11l1l1111l_opy_ + bstack11ll11_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣᏯ")
      self.bstack11111llll1_opy_ = bstack11ll11_opy_ (u"ࠨ࡯ࡤࡧࠬᏰ")
    elif re.match(bstack11ll11_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢᏱ"), bstack11111111l1_opy_) != None:
      bstack11111l1l1l_opy_ = bstack11l1l1111l_opy_ + bstack11ll11_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦᏲ")
      bstack11111l1l11_opy_ = bstack11ll11_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢᏳ")
      self.bstack11111llll1_opy_ = bstack11ll11_opy_ (u"ࠬࡽࡩ࡯ࠩᏴ")
    else:
      bstack11111l1l1l_opy_ = bstack11l1l1111l_opy_ + bstack11ll11_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤᏵ")
      self.bstack11111llll1_opy_ = bstack11ll11_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭᏶")
    return bstack11111l1l1l_opy_, bstack11111l1l11_opy_
  def bstack1111l1l11l_opy_(self):
    try:
      bstack11111111ll_opy_ = [os.path.join(expanduser(bstack11ll11_opy_ (u"ࠣࢀࠥ᏷")), bstack11ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᏸ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11111111ll_opy_:
        if(self.bstack11111ll1l1_opy_(path)):
          return path
      raise bstack11ll11_opy_ (u"࡙ࠥࡳࡧ࡬ࡣࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᏹ")
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨᏺ").format(e))
  def bstack11111ll1l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11111lll11_opy_(self, bstack11111l1l1l_opy_, bstack11111l1l11_opy_):
    try:
      bstack11111l111l_opy_ = self.bstack1111l1l11l_opy_()
      bstack111111l1l1_opy_ = os.path.join(bstack11111l111l_opy_, bstack11ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡿ࡯ࡰࠨᏻ"))
      bstack1111111ll1_opy_ = os.path.join(bstack11111l111l_opy_, bstack11111l1l11_opy_)
      if os.path.exists(bstack1111111ll1_opy_):
        self.logger.info(bstack11ll11_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡸࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣᏼ").format(bstack1111111ll1_opy_))
        return bstack1111111ll1_opy_
      if os.path.exists(bstack111111l1l1_opy_):
        self.logger.info(bstack11ll11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡺࡪࡲࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡸࡲࡿ࡯ࡰࡱ࡫ࡱ࡫ࠧᏽ").format(bstack111111l1l1_opy_))
        return self.bstack1111111l11_opy_(bstack111111l1l1_opy_, bstack11111l1l11_opy_)
      self.logger.info(bstack11ll11_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯ࠣࡿࢂࠨ᏾").format(bstack11111l1l1l_opy_))
      response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠩࡊࡉ࡙࠭᏿"), bstack11111l1l1l_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack111111l1l1_opy_, bstack11ll11_opy_ (u"ࠪࡻࡧ࠭᐀")) as file:
          file.write(response.content)
        self.logger.info(bstack11ll11_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤᐁ").format(bstack111111l1l1_opy_))
        return self.bstack1111111l11_opy_(bstack111111l1l1_opy_, bstack11111l1l11_opy_)
      else:
        raise(bstack11ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣᐂ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢᐃ").format(e))
  def bstack11111ll1ll_opy_(self, bstack11111l1l1l_opy_, bstack11111l1l11_opy_):
    try:
      retry = 2
      bstack1111111ll1_opy_ = None
      bstack1llllllll11_opy_ = False
      while retry > 0:
        bstack1111111ll1_opy_ = self.bstack11111lll11_opy_(bstack11111l1l1l_opy_, bstack11111l1l11_opy_)
        bstack1llllllll11_opy_ = self.bstack11111lllll_opy_(bstack11111l1l1l_opy_, bstack11111l1l11_opy_, bstack1111111ll1_opy_)
        if bstack1llllllll11_opy_:
          break
        retry -= 1
      return bstack1111111ll1_opy_, bstack1llllllll11_opy_
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦᐄ").format(e))
    return bstack1111111ll1_opy_, False
  def bstack11111lllll_opy_(self, bstack11111l1l1l_opy_, bstack11111l1l11_opy_, bstack1111111ll1_opy_, bstack1111l11ll1_opy_ = 0):
    if bstack1111l11ll1_opy_ > 1:
      return False
    if bstack1111111ll1_opy_ == None or os.path.exists(bstack1111111ll1_opy_) == False:
      self.logger.warn(bstack11ll11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᐅ"))
      return False
    bstack1lllllllll1_opy_ = bstack11ll11_opy_ (u"ࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽࡡ࠵ࡣ࡭࡫ࠣࡠࡩ࠴࡜ࡥ࠭࠱ࡠࡩ࠱ࠢᐆ")
    command = bstack11ll11_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩᐇ").format(bstack1111111ll1_opy_)
    bstack1111111l1l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllllllll1_opy_, bstack1111111l1l_opy_) != None:
      return True
    else:
      self.logger.error(bstack11ll11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥᐈ"))
      return False
  def bstack1111111l11_opy_(self, bstack111111l1l1_opy_, bstack11111l1l11_opy_):
    try:
      working_dir = os.path.dirname(bstack111111l1l1_opy_)
      shutil.unpack_archive(bstack111111l1l1_opy_, working_dir)
      bstack1111111ll1_opy_ = os.path.join(working_dir, bstack11111l1l11_opy_)
      os.chmod(bstack1111111ll1_opy_, 0o755)
      return bstack1111111ll1_opy_
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨᐉ"))
  def bstack1111111111_opy_(self):
    try:
      percy = str(self.config.get(bstack11ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᐊ"), bstack11ll11_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᐋ"))).lower()
      if percy != bstack11ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨᐌ"):
        return False
      self.bstack1l1l11111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᐍ").format(e))
  def bstack111111l11l_opy_(self):
    try:
      bstack111111l11l_opy_ = str(self.config.get(bstack11ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᐎ"), bstack11ll11_opy_ (u"ࠦࡦࡻࡴࡰࠤᐏ"))).lower()
      return bstack111111l11l_opy_
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠠࡤࡣࡳࡸࡺࡸࡥࠡ࡯ࡲࡨࡪ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᐐ").format(e))
  def init(self, bstack11l1l11ll_opy_, config, logger):
    self.bstack11l1l11ll_opy_ = bstack11l1l11ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111111111_opy_():
      return
    self.bstack11111l1111_opy_ = config.get(bstack11ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬᐑ"), {})
    self.bstack11111lll1l_opy_ = config.get(bstack11ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᐒ"), bstack11ll11_opy_ (u"ࠣࡣࡸࡸࡴࠨᐓ"))
    try:
      bstack11111l1l1l_opy_, bstack11111l1l11_opy_ = self.bstack11111l1lll_opy_()
      bstack1111111ll1_opy_, bstack1llllllll11_opy_ = self.bstack11111ll1ll_opy_(bstack11111l1l1l_opy_, bstack11111l1l11_opy_)
      if bstack1llllllll11_opy_:
        self.binary_path = bstack1111111ll1_opy_
        thread = Thread(target=self.bstack1lllllll1l1_opy_)
        thread.start()
      else:
        self.bstack111111111l_opy_ = True
        self.logger.error(bstack11ll11_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡴࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࠦ࠭ࠡࡽࢀ࠰࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡑࡧࡵࡧࡾࠨᐔ").format(bstack1111111ll1_opy_))
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᐕ").format(e))
  def bstack1llllllllll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11ll11_opy_ (u"ࠫࡱࡵࡧࠨᐖ"), bstack11ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡱࡵࡧࠨᐗ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11ll11_opy_ (u"ࠨࡐࡶࡵ࡫࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࡶࠤࡦࡺࠠࡼࡿࠥᐘ").format(logfile))
      self.bstack1111111lll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࠣࡴࡦࡺࡨ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᐙ").format(e))
  def bstack1lllllll1l1_opy_(self):
    bstack1111l1l111_opy_ = self.bstack11111l11ll_opy_()
    if bstack1111l1l111_opy_ == None:
      self.bstack111111111l_opy_ = True
      self.logger.error(bstack11ll11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠦᐚ"))
      return False
    command_args = [bstack11ll11_opy_ (u"ࠤࡤࡴࡵࡀࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠥᐛ") if self.bstack11l1l11ll_opy_ else bstack11ll11_opy_ (u"ࠪࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠧᐜ")]
    bstack1111l11l1l_opy_ = self.bstack11111ll11l_opy_()
    if bstack1111l11l1l_opy_ != None:
      command_args.append(bstack11ll11_opy_ (u"ࠦ࠲ࡩࠠࡼࡿࠥᐝ").format(bstack1111l11l1l_opy_))
    env = os.environ.copy()
    env[bstack11ll11_opy_ (u"ࠧࡖࡅࡓࡅ࡜ࡣ࡙ࡕࡋࡆࡐࠥᐞ")] = bstack1111l1l111_opy_
    bstack111111l1ll_opy_ = [self.binary_path]
    self.bstack1llllllllll_opy_()
    self.bstack1111l11111_opy_ = self.bstack1111l11lll_opy_(bstack111111l1ll_opy_ + command_args, env)
    self.logger.debug(bstack11ll11_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᐟ"))
    bstack1111l11ll1_opy_ = 0
    while self.bstack1111l11111_opy_.poll() == None:
      bstack111111l111_opy_ = self.bstack1lllllll11l_opy_()
      if bstack111111l111_opy_:
        self.logger.debug(bstack11ll11_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᐠ"))
        self.bstack1llllllll1l_opy_ = True
        return True
      bstack1111l11ll1_opy_ += 1
      self.logger.debug(bstack11ll11_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᐡ").format(bstack1111l11ll1_opy_))
      time.sleep(2)
    self.logger.error(bstack11ll11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᐢ").format(bstack1111l11ll1_opy_))
    self.bstack111111111l_opy_ = True
    return False
  def bstack1lllllll11l_opy_(self, bstack1111l11ll1_opy_ = 0):
    try:
      if bstack1111l11ll1_opy_ > 10:
        return False
      bstack1111l1ll11_opy_ = os.environ.get(bstack11ll11_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᐣ"), bstack11ll11_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᐤ"))
      bstack1111l111l1_opy_ = bstack1111l1ll11_opy_ + bstack11l1l11111_opy_
      response = requests.get(bstack1111l111l1_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11111l11ll_opy_(self):
    bstack1lllllll1ll_opy_ = bstack11ll11_opy_ (u"ࠬࡧࡰࡱࠩᐥ") if self.bstack11l1l11ll_opy_ else bstack11ll11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᐦ")
    bstack111l1lll1l_opy_ = bstack11ll11_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠨᐧ").format(self.config[bstack11ll11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᐨ")], bstack1lllllll1ll_opy_)
    uri = bstack11l1ll1ll_opy_(bstack111l1lll1l_opy_)
    try:
      response = bstack1l1ll11ll_opy_(bstack11ll11_opy_ (u"ࠩࡊࡉ࡙࠭ᐩ"), uri, {}, {bstack11ll11_opy_ (u"ࠪࡥࡺࡺࡨࠨᐪ"): (self.config[bstack11ll11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᐫ")], self.config[bstack11ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᐬ")])})
      if response.status_code == 200:
        bstack111111lll1_opy_ = response.json()
        if bstack11ll11_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᐭ") in bstack111111lll1_opy_:
          return bstack111111lll1_opy_[bstack11ll11_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᐮ")]
        else:
          raise bstack11ll11_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨᐯ").format(bstack111111lll1_opy_)
      else:
        raise bstack11ll11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤᐰ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦᐱ").format(e))
  def bstack11111ll11l_opy_(self):
    bstack1111l11l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢᐲ"))
    try:
      if bstack11ll11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᐳ") not in self.bstack11111l1111_opy_:
        self.bstack11111l1111_opy_[bstack11ll11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᐴ")] = 2
      with open(bstack1111l11l11_opy_, bstack11ll11_opy_ (u"ࠧࡸࠩᐵ")) as fp:
        json.dump(self.bstack11111l1111_opy_, fp)
      return bstack1111l11l11_opy_
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᐶ").format(e))
  def bstack1111l11lll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11111llll1_opy_ == bstack11ll11_opy_ (u"ࠩࡺ࡭ࡳ࠭ᐷ"):
        bstack1111l1l1ll_opy_ = [bstack11ll11_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫᐸ"), bstack11ll11_opy_ (u"ࠫ࠴ࡩࠧᐹ")]
        cmd = bstack1111l1l1ll_opy_ + cmd
      cmd = bstack11ll11_opy_ (u"ࠬࠦࠧᐺ").join(cmd)
      self.logger.debug(bstack11ll11_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥᐻ").format(cmd))
      with open(self.bstack1111111lll_opy_, bstack11ll11_opy_ (u"ࠢࡢࠤᐼ")) as bstack1111l1l1l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111l1l1l1_opy_, text=True, stderr=bstack1111l1l1l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack111111111l_opy_ = True
      self.logger.error(bstack11ll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᐽ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllll1l_opy_:
        self.logger.info(bstack11ll11_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥᐾ"))
        cmd = [self.binary_path, bstack11ll11_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨᐿ")]
        self.bstack1111l11lll_opy_(cmd)
        self.bstack1llllllll1l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᑀ").format(cmd, e))
  def bstack1ll111ll11_opy_(self):
    if not self.bstack1l1l11111l_opy_:
      return
    try:
      bstack111111ll11_opy_ = 0
      while not self.bstack1llllllll1l_opy_ and bstack111111ll11_opy_ < self.bstack111111llll_opy_:
        if self.bstack111111111l_opy_:
          self.logger.info(bstack11ll11_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥᑁ"))
          return
        time.sleep(1)
        bstack111111ll11_opy_ += 1
      os.environ[bstack11ll11_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᑂ")] = str(self.bstack11111l1ll1_opy_())
      self.logger.info(bstack11ll11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣᑃ"))
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᑄ").format(e))
  def bstack11111l1ll1_opy_(self):
    if self.bstack11l1l11ll_opy_:
      return
    try:
      bstack1111l1111l_opy_ = [platform[bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᑅ")].lower() for platform in self.config.get(bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᑆ"), [])]
      bstack11111l11l1_opy_ = sys.maxsize
      bstack111111ll1l_opy_ = bstack11ll11_opy_ (u"ࠫࠬᑇ")
      for browser in bstack1111l1111l_opy_:
        if browser in self.bstack11111ll111_opy_:
          bstack1111l111ll_opy_ = self.bstack11111ll111_opy_[browser]
        if bstack1111l111ll_opy_ < bstack11111l11l1_opy_:
          bstack11111l11l1_opy_ = bstack1111l111ll_opy_
          bstack111111ll1l_opy_ = browser
      return bstack111111ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᑈ").format(e))