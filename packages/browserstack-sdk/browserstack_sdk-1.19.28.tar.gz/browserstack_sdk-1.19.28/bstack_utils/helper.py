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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11l1l11l1l_opy_, bstack1ll1ll1l1_opy_, bstack1l1ll111l1_opy_, bstack11l11ll1l_opy_,
                                    bstack11l11llll1_opy_, bstack11l11ll1ll_opy_)
from bstack_utils.messages import bstack1l11llllll_opy_, bstack1111l1l1_opy_
from bstack_utils.proxy import bstack111ll11l_opy_, bstack1l11l1ll1l_opy_
bstack1l1l1l1l1_opy_ = Config.bstack1ll111111_opy_()
logger = logging.getLogger(__name__)
def bstack11ll11l11l_opy_(config):
    return config[bstack11ll11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᆟ")]
def bstack11l1lllll1_opy_(config):
    return config[bstack11ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᆠ")]
def bstack1ll1ll11_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111ll1l1l1_opy_(obj):
    values = []
    bstack111llll1l1_opy_ = re.compile(bstack11ll11_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᆡ"), re.I)
    for key in obj.keys():
        if bstack111llll1l1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111lll1l1l_opy_(config):
    tags = []
    tags.extend(bstack111ll1l1l1_opy_(os.environ))
    tags.extend(bstack111ll1l1l1_opy_(config))
    return tags
def bstack111ll11ll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111lllll1l_opy_(bstack111ll1lll1_opy_):
    if not bstack111ll1lll1_opy_:
        return bstack11ll11_opy_ (u"࠭ࠧᆢ")
    return bstack11ll11_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᆣ").format(bstack111ll1lll1_opy_.name, bstack111ll1lll1_opy_.email)
def bstack11l1lll11l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1ll111_opy_ = repo.common_dir
        info = {
            bstack11ll11_opy_ (u"ࠣࡵ࡫ࡥࠧᆤ"): repo.head.commit.hexsha,
            bstack11ll11_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᆥ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll11_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᆦ"): repo.active_branch.name,
            bstack11ll11_opy_ (u"ࠦࡹࡧࡧࠣᆧ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᆨ"): bstack111lllll1l_opy_(repo.head.commit.committer),
            bstack11ll11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᆩ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll11_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢᆪ"): bstack111lllll1l_opy_(repo.head.commit.author),
            bstack11ll11_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨᆫ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll11_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᆬ"): repo.head.commit.message,
            bstack11ll11_opy_ (u"ࠥࡶࡴࡵࡴࠣᆭ"): repo.git.rev_parse(bstack11ll11_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨᆮ")),
            bstack11ll11_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᆯ"): bstack111l1ll111_opy_,
            bstack11ll11_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᆰ"): subprocess.check_output([bstack11ll11_opy_ (u"ࠢࡨ࡫ࡷࠦᆱ"), bstack11ll11_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦᆲ"), bstack11ll11_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧᆳ")]).strip().decode(
                bstack11ll11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᆴ")),
            bstack11ll11_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᆵ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᆶ"): repo.git.rev_list(
                bstack11ll11_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᆷ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111ll1ll11_opy_ = []
        for remote in remotes:
            bstack111ll1l1ll_opy_ = {
                bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᆸ"): remote.name,
                bstack11ll11_opy_ (u"ࠣࡷࡵࡰࠧᆹ"): remote.url,
            }
            bstack111ll1ll11_opy_.append(bstack111ll1l1ll_opy_)
        bstack111ll1ll1l_opy_ = {
            bstack11ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆺ"): bstack11ll11_opy_ (u"ࠥ࡫࡮ࡺࠢᆻ"),
            **info,
            bstack11ll11_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᆼ"): bstack111ll1ll11_opy_
        }
        bstack111ll1ll1l_opy_ = bstack111ll1l11l_opy_(bstack111ll1ll1l_opy_)
        return bstack111ll1ll1l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᆽ").format(err))
        return {}
def bstack111ll1l11l_opy_(bstack111ll1ll1l_opy_):
    bstack11l11l1111_opy_ = bstack11l11l1ll1_opy_(bstack111ll1ll1l_opy_)
    if bstack11l11l1111_opy_ and bstack11l11l1111_opy_ > bstack11l11llll1_opy_:
        bstack111l1l111l_opy_ = bstack11l11l1111_opy_ - bstack11l11llll1_opy_
        bstack11l1111ll1_opy_ = bstack11l111l111_opy_(bstack111ll1ll1l_opy_[bstack11ll11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᆾ")], bstack111l1l111l_opy_)
        bstack111ll1ll1l_opy_[bstack11ll11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᆿ")] = bstack11l1111ll1_opy_
        logger.info(bstack11ll11_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᇀ")
                    .format(bstack11l11l1ll1_opy_(bstack111ll1ll1l_opy_) / 1024))
    return bstack111ll1ll1l_opy_
def bstack11l11l1ll1_opy_(bstack1lll11llll_opy_):
    try:
        if bstack1lll11llll_opy_:
            bstack111l1l1lll_opy_ = json.dumps(bstack1lll11llll_opy_)
            bstack111ll11lll_opy_ = sys.getsizeof(bstack111l1l1lll_opy_)
            return bstack111ll11lll_opy_
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᇁ").format(e))
    return -1
def bstack11l111l111_opy_(field, bstack111l1ll1l1_opy_):
    try:
        bstack111l1l1l1l_opy_ = len(bytes(bstack11l11ll1ll_opy_, bstack11ll11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᇂ")))
        bstack11l11l111l_opy_ = bytes(field, bstack11ll11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᇃ"))
        bstack11l111lll1_opy_ = len(bstack11l11l111l_opy_)
        bstack111l1l1ll1_opy_ = ceil(bstack11l111lll1_opy_ - bstack111l1ll1l1_opy_ - bstack111l1l1l1l_opy_)
        if bstack111l1l1ll1_opy_ > 0:
            bstack111lll111l_opy_ = bstack11l11l111l_opy_[:bstack111l1l1ll1_opy_].decode(bstack11ll11_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᇄ"), errors=bstack11ll11_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ᇅ")) + bstack11l11ll1ll_opy_
            return bstack111lll111l_opy_
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᇆ").format(e))
    return field
def bstack11lllll1_opy_():
    env = os.environ
    if (bstack11ll11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᇇ") in env and len(env[bstack11ll11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᇈ")]) > 0) or (
            bstack11ll11_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᇉ") in env and len(env[bstack11ll11_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᇊ")]) > 0):
        return {
            bstack11ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᇋ"): bstack11ll11_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢᇌ"),
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᇍ"): env.get(bstack11ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᇎ")),
            bstack11ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᇏ"): env.get(bstack11ll11_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᇐ")),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᇑ"): env.get(bstack11ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᇒ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠨࡃࡊࠤᇓ")) == bstack11ll11_opy_ (u"ࠢࡵࡴࡸࡩࠧᇔ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᇕ"))):
        return {
            bstack11ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᇖ"): bstack11ll11_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᇗ"),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᇘ"): env.get(bstack11ll11_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᇙ")),
            bstack11ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᇚ"): env.get(bstack11ll11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᇛ")),
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇜ"): env.get(bstack11ll11_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᇝ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠥࡇࡎࠨᇞ")) == bstack11ll11_opy_ (u"ࠦࡹࡸࡵࡦࠤᇟ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᇠ"))):
        return {
            bstack11ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᇡ"): bstack11ll11_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᇢ"),
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᇣ"): env.get(bstack11ll11_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᇤ")),
            bstack11ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᇥ"): env.get(bstack11ll11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᇦ")),
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᇧ"): env.get(bstack11ll11_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᇨ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠢࡄࡋࠥᇩ")) == bstack11ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨᇪ") and env.get(bstack11ll11_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᇫ")) == bstack11ll11_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᇬ"):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇭ"): bstack11ll11_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᇮ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇯ"): None,
            bstack11ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇰ"): None,
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇱ"): None
        }
    if env.get(bstack11ll11_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᇲ")) and env.get(bstack11ll11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᇳ")):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇴ"): bstack11ll11_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᇵ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇶ"): env.get(bstack11ll11_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᇷ")),
            bstack11ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇸ"): None,
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇹ"): env.get(bstack11ll11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᇺ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠦࡈࡏࠢᇻ")) == bstack11ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥᇼ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᇽ"))):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇾ"): bstack11ll11_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᇿ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሀ"): env.get(bstack11ll11_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨሁ")),
            bstack11ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨሂ"): None,
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሃ"): env.get(bstack11ll11_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦሄ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠢࡄࡋࠥህ")) == bstack11ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨሆ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧሇ"))):
        return {
            bstack11ll11_opy_ (u"ࠥࡲࡦࡳࡥࠣለ"): bstack11ll11_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢሉ"),
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣሊ"): env.get(bstack11ll11_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧላ")),
            bstack11ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤሌ"): env.get(bstack11ll11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨል")),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣሎ"): env.get(bstack11ll11_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨሏ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠦࡈࡏࠢሐ")) == bstack11ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥሑ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤሒ"))):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧሓ"): bstack11ll11_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣሔ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሕ"): env.get(bstack11ll11_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢሖ")),
            bstack11ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨሗ"): env.get(bstack11ll11_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥመ")),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧሙ"): env.get(bstack11ll11_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥሚ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠣࡅࡌࠦማ")) == bstack11ll11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢሜ") and bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨም"))):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሞ"): bstack11ll11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣሟ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሠ"): env.get(bstack11ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨሡ")),
            bstack11ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥሢ"): env.get(bstack11ll11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦሣ")) or env.get(bstack11ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨሤ")),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሥ"): env.get(bstack11ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢሦ"))
        }
    if bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣሧ"))):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧረ"): bstack11ll11_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣሩ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሪ"): bstack11ll11_opy_ (u"ࠥࡿࢂࢁࡽࠣራ").format(env.get(bstack11ll11_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧሬ")), env.get(bstack11ll11_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬር"))),
            bstack11ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሮ"): env.get(bstack11ll11_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨሯ")),
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢሰ"): env.get(bstack11ll11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤሱ"))
        }
    if bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧሲ"))):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሳ"): bstack11ll11_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢሴ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤስ"): bstack11ll11_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨሶ").format(env.get(bstack11ll11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧሷ")), env.get(bstack11ll11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪሸ")), env.get(bstack11ll11_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫሹ")), env.get(bstack11ll11_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨሺ"))),
            bstack11ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢሻ"): env.get(bstack11ll11_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥሼ")),
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨሽ"): env.get(bstack11ll11_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤሾ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥሿ")) and env.get(bstack11ll11_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧቀ")):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤቁ"): bstack11ll11_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢቂ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤቃ"): bstack11ll11_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥቄ").format(env.get(bstack11ll11_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫቅ")), env.get(bstack11ll11_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧቆ")), env.get(bstack11ll11_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪቇ"))),
            bstack11ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨቈ"): env.get(bstack11ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ቉")),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧቊ"): env.get(bstack11ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢቋ"))
        }
    if any([env.get(bstack11ll11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨቌ")), env.get(bstack11ll11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣቍ")), env.get(bstack11ll11_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ቎"))]):
        return {
            bstack11ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ቏"): bstack11ll11_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧቐ"),
            bstack11ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤቑ"): env.get(bstack11ll11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨቒ")),
            bstack11ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥቓ"): env.get(bstack11ll11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢቔ")),
            bstack11ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤቕ"): env.get(bstack11ll11_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤቖ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥ቗")):
        return {
            bstack11ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦቘ"): bstack11ll11_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢ቙"),
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦቚ"): env.get(bstack11ll11_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦቛ")),
            bstack11ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቜ"): env.get(bstack11ll11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥቝ")),
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ቞"): env.get(bstack11ll11_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ቟"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣበ")) or env.get(bstack11ll11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥቡ")):
        return {
            bstack11ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቢ"): bstack11ll11_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦባ"),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቤ"): env.get(bstack11ll11_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤብ")),
            bstack11ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቦ"): bstack11ll11_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢቧ") if env.get(bstack11ll11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥቨ")) else None,
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቩ"): env.get(bstack11ll11_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣቪ"))
        }
    if any([env.get(bstack11ll11_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤቫ")), env.get(bstack11ll11_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨቬ")), env.get(bstack11ll11_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨቭ"))]):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧቮ"): bstack11ll11_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢቯ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧተ"): None,
            bstack11ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቱ"): env.get(bstack11ll11_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣቲ")),
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦታ"): env.get(bstack11ll11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣቴ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥት")):
        return {
            bstack11ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨቶ"): bstack11ll11_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧቷ"),
            bstack11ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨቸ"): env.get(bstack11ll11_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥቹ")),
            bstack11ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢቺ"): bstack11ll11_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢቻ").format(env.get(bstack11ll11_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪቼ"))) if env.get(bstack11ll11_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦች")) else None,
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቾ"): env.get(bstack11ll11_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧቿ"))
        }
    if bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧኀ"))):
        return {
            bstack11ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥኁ"): bstack11ll11_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢኂ"),
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥኃ"): env.get(bstack11ll11_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧኄ")),
            bstack11ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦኅ"): env.get(bstack11ll11_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨኆ")),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥኇ"): env.get(bstack11ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢኈ"))
        }
    if bstack111l1l1l_opy_(env.get(bstack11ll11_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢ኉"))):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኊ"): bstack11ll11_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤኋ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧኌ"): bstack11ll11_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦኍ").format(env.get(bstack11ll11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨ኎")), env.get(bstack11ll11_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩ኏")), env.get(bstack11ll11_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ነ"))),
            bstack11ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤኑ"): env.get(bstack11ll11_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥኒ")),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣና"): env.get(bstack11ll11_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥኔ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠦࡈࡏࠢን")) == bstack11ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥኖ") and env.get(bstack11ll11_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨኗ")) == bstack11ll11_opy_ (u"ࠢ࠲ࠤኘ"):
        return {
            bstack11ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨኙ"): bstack11ll11_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤኚ"),
            bstack11ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨኛ"): bstack11ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢኜ").format(env.get(bstack11ll11_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩኝ"))),
            bstack11ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣኞ"): None,
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኟ"): None,
        }
    if env.get(bstack11ll11_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦአ")):
        return {
            bstack11ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢኡ"): bstack11ll11_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧኢ"),
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢኣ"): None,
            bstack11ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኤ"): env.get(bstack11ll11_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢእ")),
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኦ"): env.get(bstack11ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢኧ"))
        }
    if any([env.get(bstack11ll11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧከ")), env.get(bstack11ll11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥኩ")), env.get(bstack11ll11_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤኪ")), env.get(bstack11ll11_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨካ"))]):
        return {
            bstack11ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦኬ"): bstack11ll11_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥክ"),
            bstack11ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኮ"): None,
            bstack11ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦኯ"): env.get(bstack11ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦኰ")) or None,
            bstack11ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ኱"): env.get(bstack11ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢኲ"), 0)
        }
    if env.get(bstack11ll11_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦኳ")):
        return {
            bstack11ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኴ"): bstack11ll11_opy_ (u"ࠣࡉࡲࡇࡉࠨኵ"),
            bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ኶"): None,
            bstack11ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ኷"): env.get(bstack11ll11_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤኸ")),
            bstack11ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦኹ"): env.get(bstack11ll11_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧኺ"))
        }
    if env.get(bstack11ll11_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧኻ")):
        return {
            bstack11ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨኼ"): bstack11ll11_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧኽ"),
            bstack11ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨኾ"): env.get(bstack11ll11_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ኿")),
            bstack11ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢዀ"): env.get(bstack11ll11_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤ዁")),
            bstack11ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨዂ"): env.get(bstack11ll11_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨዃ"))
        }
    return {bstack11ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣዄ"): None}
def get_host_info():
    return {
        bstack11ll11_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧዅ"): platform.node(),
        bstack11ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ዆"): platform.system(),
        bstack11ll11_opy_ (u"ࠧࡺࡹࡱࡧࠥ዇"): platform.machine(),
        bstack11ll11_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢወ"): platform.version(),
        bstack11ll11_opy_ (u"ࠢࡢࡴࡦ࡬ࠧዉ"): platform.architecture()[0]
    }
def bstack11111llll_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111ll1llll_opy_():
    if bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩዊ")):
        return bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨዋ")
    return bstack11ll11_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩዌ")
def bstack111lll11l1_opy_(driver):
    info = {
        bstack11ll11_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪው"): driver.capabilities,
        bstack11ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩዎ"): driver.session_id,
        bstack11ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧዏ"): driver.capabilities.get(bstack11ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬዐ"), None),
        bstack11ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪዑ"): driver.capabilities.get(bstack11ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪዒ"), None),
        bstack11ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬዓ"): driver.capabilities.get(bstack11ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪዔ"), None),
    }
    if bstack111ll1llll_opy_() == bstack11ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫዕ"):
        info[bstack11ll11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧዖ")] = bstack11ll11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭዗") if bstack11l1l11ll_opy_() else bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪዘ")
    return info
def bstack11l1l11ll_opy_():
    if bstack1l1l1l1l1_opy_.get_property(bstack11ll11_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨዙ")):
        return True
    if bstack111l1l1l_opy_(os.environ.get(bstack11ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫዚ"), None)):
        return True
    return False
def bstack1l1ll11ll_opy_(bstack111ll1111l_opy_, url, data, config):
    headers = config.get(bstack11ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬዛ"), None)
    proxies = bstack111ll11l_opy_(config, url)
    auth = config.get(bstack11ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪዜ"), None)
    response = requests.request(
            bstack111ll1111l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1ll1l1111_opy_(bstack111l11111_opy_, size):
    bstack1lll1111l_opy_ = []
    while len(bstack111l11111_opy_) > size:
        bstack11l11111_opy_ = bstack111l11111_opy_[:size]
        bstack1lll1111l_opy_.append(bstack11l11111_opy_)
        bstack111l11111_opy_ = bstack111l11111_opy_[size:]
    bstack1lll1111l_opy_.append(bstack111l11111_opy_)
    return bstack1lll1111l_opy_
def bstack111lll11ll_opy_(message, bstack111llll111_opy_=False):
    os.write(1, bytes(message, bstack11ll11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬዝ")))
    os.write(1, bytes(bstack11ll11_opy_ (u"ࠧ࡝ࡰࠪዞ"), bstack11ll11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧዟ")))
    if bstack111llll111_opy_:
        with open(bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨዠ") + os.environ[bstack11ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩዡ")] + bstack11ll11_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩዢ"), bstack11ll11_opy_ (u"ࠬࡧࠧዣ")) as f:
            f.write(message + bstack11ll11_opy_ (u"࠭࡜࡯ࠩዤ"))
def bstack111lll1l11_opy_():
    return os.environ[bstack11ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪዥ")].lower() == bstack11ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ዦ")
def bstack11l1ll1ll_opy_(bstack111l1lll1l_opy_):
    return bstack11ll11_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨዧ").format(bstack11l1l11l1l_opy_, bstack111l1lll1l_opy_)
def bstack11l11l11l_opy_():
    return bstack1l11l1111l_opy_().replace(tzinfo=None).isoformat() + bstack11ll11_opy_ (u"ࠪ࡞ࠬየ")
def bstack111lllll11_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll11_opy_ (u"ࠫ࡟࠭ዩ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll11_opy_ (u"ࠬࡠࠧዪ")))).total_seconds() * 1000
def bstack111ll1l111_opy_(timestamp):
    return bstack111ll11l11_opy_(timestamp).isoformat() + bstack11ll11_opy_ (u"࡚࠭ࠨያ")
def bstack111ll11111_opy_(bstack11l1111l11_opy_):
    date_format = bstack11ll11_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬዬ")
    bstack111ll111l1_opy_ = datetime.datetime.strptime(bstack11l1111l11_opy_, date_format)
    return bstack111ll111l1_opy_.isoformat() + bstack11ll11_opy_ (u"ࠨ࡜ࠪይ")
def bstack11l1111lll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዮ")
    else:
        return bstack11ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዯ")
def bstack111l1l1l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll11_opy_ (u"ࠫࡹࡸࡵࡦࠩደ")
def bstack11l11l11l1_opy_(val):
    return val.__str__().lower() == bstack11ll11_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫዱ")
def bstack1l1111l11l_opy_(bstack111l11llll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l11llll_opy_ as e:
                print(bstack11ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨዲ").format(func.__name__, bstack111l11llll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111lll1111_opy_(bstack111l1l11l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1l11l1_opy_(cls, *args, **kwargs)
            except bstack111l11llll_opy_ as e:
                print(bstack11ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢዳ").format(bstack111l1l11l1_opy_.__name__, bstack111l11llll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111lll1111_opy_
    else:
        return decorator
def bstack11l1lll1l_opy_(bstack11ll1l1ll1_opy_):
    if bstack11ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዴ") in bstack11ll1l1ll1_opy_ and bstack11l11l11l1_opy_(bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ድ")]):
        return False
    if bstack11ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዶ") in bstack11ll1l1ll1_opy_ and bstack11l11l11l1_opy_(bstack11ll1l1ll1_opy_[bstack11ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ዷ")]):
        return False
    return True
def bstack1l1ll11l1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1llllll11_opy_(hub_url):
    if bstack111ll1l11_opy_() <= version.parse(bstack11ll11_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬዸ")):
        if hub_url != bstack11ll11_opy_ (u"࠭ࠧዹ"):
            return bstack11ll11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣዺ") + hub_url + bstack11ll11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧዻ")
        return bstack1l1ll111l1_opy_
    if hub_url != bstack11ll11_opy_ (u"ࠩࠪዼ"):
        return bstack11ll11_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧዽ") + hub_url + bstack11ll11_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧዾ")
    return bstack11l11ll1l_opy_
def bstack11l111ll1l_opy_():
    return isinstance(os.getenv(bstack11ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫዿ")), str)
def bstack1l111l11_opy_(url):
    return urlparse(url).hostname
def bstack1l11ll11ll_opy_(hostname):
    for bstack1l1ll1ll_opy_ in bstack1ll1ll1l1_opy_:
        regex = re.compile(bstack1l1ll1ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111llll11l_opy_(bstack111l1lll11_opy_, file_name, logger):
    bstack1ll11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"࠭ࡾࠨጀ")), bstack111l1lll11_opy_)
    try:
        if not os.path.exists(bstack1ll11llll1_opy_):
            os.makedirs(bstack1ll11llll1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll11_opy_ (u"ࠧࡿࠩጁ")), bstack111l1lll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll11_opy_ (u"ࠨࡹࠪጂ")):
                pass
            with open(file_path, bstack11ll11_opy_ (u"ࠤࡺ࠯ࠧጃ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l11llllll_opy_.format(str(e)))
def bstack11l111l1ll_opy_(file_name, key, value, logger):
    file_path = bstack111llll11l_opy_(bstack11ll11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪጄ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1ll1l1ll1_opy_ = json.load(open(file_path, bstack11ll11_opy_ (u"ࠫࡷࡨࠧጅ")))
        else:
            bstack1ll1l1ll1_opy_ = {}
        bstack1ll1l1ll1_opy_[key] = value
        with open(file_path, bstack11ll11_opy_ (u"ࠧࡽࠫࠣጆ")) as outfile:
            json.dump(bstack1ll1l1ll1_opy_, outfile)
def bstack11l11l111_opy_(file_name, logger):
    file_path = bstack111llll11l_opy_(bstack11ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ጇ"), file_name, logger)
    bstack1ll1l1ll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll11_opy_ (u"ࠧࡳࠩገ")) as bstack1l1l1ll1_opy_:
            bstack1ll1l1ll1_opy_ = json.load(bstack1l1l1ll1_opy_)
    return bstack1ll1l1ll1_opy_
def bstack1llll1llll_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬጉ") + file_path + bstack11ll11_opy_ (u"ࠩࠣࠫጊ") + str(e))
def bstack111ll1l11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll11_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧጋ")
def bstack111111ll1_opy_(config):
    if bstack11ll11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪጌ") in config:
        del (config[bstack11ll11_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫግ")])
        return False
    if bstack111ll1l11_opy_() < version.parse(bstack11ll11_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬጎ")):
        return False
    if bstack111ll1l11_opy_() >= version.parse(bstack11ll11_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ጏ")):
        return True
    if bstack11ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨጐ") in config and config[bstack11ll11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ጑")] is False:
        return False
    else:
        return True
def bstack1111l11l1_opy_(args_list, bstack11l111l11l_opy_):
    index = -1
    for value in bstack11l111l11l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l111llll1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l111llll1_opy_ = bstack1l111llll1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪጒ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫጓ"), exception=exception)
    def bstack11ll1l111l_opy_(self):
        if self.result != bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬጔ"):
            return None
        if bstack11ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤጕ") in self.exception_type:
            return bstack11ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ጖")
        return bstack11ll11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ጗")
    def bstack111ll11l1l_opy_(self):
        if self.result != bstack11ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩጘ"):
            return None
        if self.bstack1l111llll1_opy_:
            return self.bstack1l111llll1_opy_
        return bstack11l111l1l1_opy_(self.exception)
def bstack11l111l1l1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111llllll1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1lll1ll1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll11l11ll_opy_(config, logger):
    try:
        import playwright
        bstack11l111ll11_opy_ = playwright.__file__
        bstack111l1llll1_opy_ = os.path.split(bstack11l111ll11_opy_)
        bstack111l1ll1ll_opy_ = bstack111l1llll1_opy_[0] + bstack11ll11_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ጙ")
        os.environ[bstack11ll11_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧጚ")] = bstack1l11l1ll1l_opy_(config)
        with open(bstack111l1ll1ll_opy_, bstack11ll11_opy_ (u"ࠬࡸࠧጛ")) as f:
            bstack1ll1l1llll_opy_ = f.read()
            bstack111ll111ll_opy_ = bstack11ll11_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬጜ")
            bstack111l1lllll_opy_ = bstack1ll1l1llll_opy_.find(bstack111ll111ll_opy_)
            if bstack111l1lllll_opy_ == -1:
              process = subprocess.Popen(bstack11ll11_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦጝ"), shell=True, cwd=bstack111l1llll1_opy_[0])
              process.wait()
              bstack11l11l1lll_opy_ = bstack11ll11_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨጞ")
              bstack111l1ll11l_opy_ = bstack11ll11_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨጟ")
              bstack111l1l11ll_opy_ = bstack1ll1l1llll_opy_.replace(bstack11l11l1lll_opy_, bstack111l1ll11l_opy_)
              with open(bstack111l1ll1ll_opy_, bstack11ll11_opy_ (u"ࠪࡻࠬጠ")) as f:
                f.write(bstack111l1l11ll_opy_)
    except Exception as e:
        logger.error(bstack1111l1l1_opy_.format(str(e)))
def bstack11111l111_opy_():
  try:
    bstack111l1l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫጡ"))
    bstack11l111llll_opy_ = []
    if os.path.exists(bstack111l1l1111_opy_):
      with open(bstack111l1l1111_opy_) as f:
        bstack11l111llll_opy_ = json.load(f)
      os.remove(bstack111l1l1111_opy_)
    return bstack11l111llll_opy_
  except:
    pass
  return []
def bstack11llll1ll_opy_(bstack1l11lll11_opy_):
  try:
    bstack11l111llll_opy_ = []
    bstack111l1l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬጢ"))
    if os.path.exists(bstack111l1l1111_opy_):
      with open(bstack111l1l1111_opy_) as f:
        bstack11l111llll_opy_ = json.load(f)
    bstack11l111llll_opy_.append(bstack1l11lll11_opy_)
    with open(bstack111l1l1111_opy_, bstack11ll11_opy_ (u"࠭ࡷࠨጣ")) as f:
        json.dump(bstack11l111llll_opy_, f)
  except:
    pass
def bstack1ll1llll1l_opy_(logger, bstack11l11111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll11_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪጤ"), bstack11ll11_opy_ (u"ࠨࠩጥ"))
    if test_name == bstack11ll11_opy_ (u"ࠩࠪጦ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩጧ"), bstack11ll11_opy_ (u"ࠫࠬጨ"))
    bstack11l1111111_opy_ = bstack11ll11_opy_ (u"ࠬ࠲ࠠࠨጩ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11l11111ll_opy_:
        bstack1llll111ll_opy_ = os.environ.get(bstack11ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ጪ"), bstack11ll11_opy_ (u"ࠧ࠱ࠩጫ"))
        bstack1lll111111_opy_ = {bstack11ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ጬ"): test_name, bstack11ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨጭ"): bstack11l1111111_opy_, bstack11ll11_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩጮ"): bstack1llll111ll_opy_}
        bstack11l1111l1l_opy_ = []
        bstack11l11l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪጯ"))
        if os.path.exists(bstack11l11l11ll_opy_):
            with open(bstack11l11l11ll_opy_) as f:
                bstack11l1111l1l_opy_ = json.load(f)
        bstack11l1111l1l_opy_.append(bstack1lll111111_opy_)
        with open(bstack11l11l11ll_opy_, bstack11ll11_opy_ (u"ࠬࡽࠧጰ")) as f:
            json.dump(bstack11l1111l1l_opy_, f)
    else:
        bstack1lll111111_opy_ = {bstack11ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫጱ"): test_name, bstack11ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ጲ"): bstack11l1111111_opy_, bstack11ll11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧጳ"): str(multiprocessing.current_process().name)}
        if bstack11ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ጴ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lll111111_opy_)
  except Exception as e:
      logger.warn(bstack11ll11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢጵ").format(e))
def bstack11lllllll_opy_(error_message, test_name, index, logger):
  try:
    bstack11l11111l1_opy_ = []
    bstack1lll111111_opy_ = {bstack11ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩጶ"): test_name, bstack11ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫጷ"): error_message, bstack11ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬጸ"): index}
    bstack111llll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨጹ"))
    if os.path.exists(bstack111llll1ll_opy_):
        with open(bstack111llll1ll_opy_) as f:
            bstack11l11111l1_opy_ = json.load(f)
    bstack11l11111l1_opy_.append(bstack1lll111111_opy_)
    with open(bstack111llll1ll_opy_, bstack11ll11_opy_ (u"ࠨࡹࠪጺ")) as f:
        json.dump(bstack11l11111l1_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧጻ").format(e))
def bstack1ll1l1l1ll_opy_(bstack1ll11l111l_opy_, name, logger):
  try:
    bstack1lll111111_opy_ = {bstack11ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨጼ"): name, bstack11ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪጽ"): bstack1ll11l111l_opy_, bstack11ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫጾ"): str(threading.current_thread()._name)}
    return bstack1lll111111_opy_
  except Exception as e:
    logger.warn(bstack11ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥጿ").format(e))
  return
def bstack11l11ll111_opy_():
    return platform.system() == bstack11ll11_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨፀ")
def bstack1l1l1lll11_opy_(bstack111lllllll_opy_, config, logger):
    bstack111lll1ll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111lllllll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢፁ").format(e))
    return bstack111lll1ll1_opy_
def bstack111l1l1l11_opy_(bstack11l11l1l1l_opy_, bstack111lll1lll_opy_):
    bstack11l11l1l11_opy_ = version.parse(bstack11l11l1l1l_opy_)
    bstack11l111111l_opy_ = version.parse(bstack111lll1lll_opy_)
    if bstack11l11l1l11_opy_ > bstack11l111111l_opy_:
        return 1
    elif bstack11l11l1l11_opy_ < bstack11l111111l_opy_:
        return -1
    else:
        return 0
def bstack1l11l1111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111ll11l11_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)