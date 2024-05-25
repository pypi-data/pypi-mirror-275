from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRateCls:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, min_py: float, max_py: float, def_py: float) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:SRATe \n
		Snippet: driver.diagnostic.gprf.measurement.rfProperty.symbolRate.set(min_py = 1.0, max_py = 1.0, def_py = 1.0) \n
		No command help available \n
			:param min_py: No help available
			:param max_py: No help available
			:param def_py: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('min_py', min_py, DataType.Float), ArgSingle('max_py', max_py, DataType.Float), ArgSingle('def_py', def_py, DataType.Float))
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:SRATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class SymbolRateStruct(StructBase):
		"""Response structure. Fields: \n
			- Min_Py: float: No parameter help available
			- Max_Py: float: No parameter help available
			- Def_Py: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Min_Py'),
			ArgStruct.scalar_float('Max_Py'),
			ArgStruct.scalar_float('Def_Py')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Py: float = None
			self.Max_Py: float = None
			self.Def_Py: float = None

	def get(self) -> SymbolRateStruct:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:SRATe \n
		Snippet: value: SymbolRateStruct = driver.diagnostic.gprf.measurement.rfProperty.symbolRate.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SymbolRateStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:SRATe?', self.__class__.SymbolRateStruct())
