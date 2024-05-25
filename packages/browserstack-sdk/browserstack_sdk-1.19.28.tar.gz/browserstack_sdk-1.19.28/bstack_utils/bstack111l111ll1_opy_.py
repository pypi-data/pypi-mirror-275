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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack111l1l1l11_opy_
from browserstack_sdk.bstack1lll111l11_opy_ import bstack11lll1l1_opy_
def _111l11lll1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111l111l1l_opy_:
    def __init__(self, handler):
        self._111l111l11_opy_ = {}
        self._111l111111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11lll1l1_opy_.version()
        if bstack111l1l1l11_opy_(pytest_version, bstack11ll11_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣፂ")) >= 0:
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ፃ")] = Module._register_setup_function_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬፄ")] = Module._register_setup_module_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬፅ")] = Class._register_setup_class_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧፆ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪፇ"))
            Module._register_setup_module_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩፈ"))
            Class._register_setup_class_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩፉ"))
            Class._register_setup_method_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫፊ"))
        else:
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧፋ")] = Module._inject_setup_function_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ፌ")] = Module._inject_setup_module_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ፍ")] = Class._inject_setup_class_fixture
            self._111l111l11_opy_[bstack11ll11_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨፎ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫፏ"))
            Module._inject_setup_module_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪፐ"))
            Class._inject_setup_class_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪፑ"))
            Class._inject_setup_method_fixture = self.bstack111l11l11l_opy_(bstack11ll11_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬፒ"))
    def bstack111l11111l_opy_(self, bstack111l11ll1l_opy_, hook_type):
        meth = getattr(bstack111l11ll1l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111l111111_opy_[hook_type] = meth
            setattr(bstack111l11ll1l_opy_, hook_type, self.bstack111l11l1ll_opy_(hook_type))
    def bstack111l111lll_opy_(self, instance, bstack111l11ll11_opy_):
        if bstack111l11ll11_opy_ == bstack11ll11_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣፓ"):
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢፔ"))
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦፕ"))
        if bstack111l11ll11_opy_ == bstack11ll11_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤፖ"):
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣፗ"))
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧፘ"))
        if bstack111l11ll11_opy_ == bstack11ll11_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦፙ"):
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥፚ"))
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢ፛"))
        if bstack111l11ll11_opy_ == bstack11ll11_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣ፜"):
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢ፝"))
            self.bstack111l11111l_opy_(instance.obj, bstack11ll11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦ፞"))
    @staticmethod
    def bstack111l11l111_opy_(hook_type, func, args):
        if hook_type in [bstack11ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩ፟"), bstack11ll11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭፠")]:
            _111l11lll1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111l11l1ll_opy_(self, hook_type):
        def bstack111l1111l1_opy_(arg=None):
            self.handler(hook_type, bstack11ll11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ፡"))
            result = None
            exception = None
            try:
                self.bstack111l11l111_opy_(hook_type, self._111l111111_opy_[hook_type], (arg,))
                result = Result(result=bstack11ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭።"))
            except Exception as e:
                result = Result(result=bstack11ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ፣"), exception=e)
                self.handler(hook_type, bstack11ll11_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧ፤"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨ፥"), result)
        def bstack111l11l1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack11ll11_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ፦"))
            result = None
            exception = None
            try:
                self.bstack111l11l111_opy_(hook_type, self._111l111111_opy_[hook_type], (this, arg))
                result = Result(result=bstack11ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ፧"))
            except Exception as e:
                result = Result(result=bstack11ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ፨"), exception=e)
                self.handler(hook_type, bstack11ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ፩"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭፪"), result)
        if hook_type in [bstack11ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ፫"), bstack11ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ፬")]:
            return bstack111l11l1l1_opy_
        return bstack111l1111l1_opy_
    def bstack111l11l11l_opy_(self, bstack111l11ll11_opy_):
        def bstack111l1111ll_opy_(this, *args, **kwargs):
            self.bstack111l111lll_opy_(this, bstack111l11ll11_opy_)
            self._111l111l11_opy_[bstack111l11ll11_opy_](this, *args, **kwargs)
        return bstack111l1111ll_opy_