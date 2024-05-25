from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 176 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 9 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def scenario(self):
		"""scenario commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import CorrectionCls
			self._correction = CorrectionCls(self._core, self._cmd_group)
		return self._correction

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .IqVsSlot import IqVsSlotCls
			self._iqVsSlot = IqVsSlotCls(self._core, self._cmd_group)
		return self._iqVsSlot

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensorCls
			self._extPwrSensor = ExtPwrSensorCls(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrpm(self):
		"""nrpm commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_nrpm'):
			from .Nrpm import NrpmCls
			self._nrpm = NrpmCls(self._core, self._cmd_group)
		return self._nrpm

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 5 Sub-classes, 11 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorderCls
			self._iqRecorder = IqRecorderCls(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAnCls
			self._fftSpecAn = FftSpecAnCls(self._core, self._cmd_group)
		return self._fftSpecAn

	@property
	def canalyzer(self):
		"""canalyzer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_canalyzer'):
			from .Canalyzer import CanalyzerCls
			self._canalyzer = CanalyzerCls(self._core, self._cmd_group)
		return self._canalyzer

	@property
	def ploss(self):
		"""ploss commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_ploss'):
			from .Ploss import PlossCls
			self._ploss = PlossCls(self._core, self._cmd_group)
		return self._ploss

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
