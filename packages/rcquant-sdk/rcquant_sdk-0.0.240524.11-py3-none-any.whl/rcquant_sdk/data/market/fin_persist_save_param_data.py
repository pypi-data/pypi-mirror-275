from typing import List
from ...interface import IData
from ...packer.market.fin_persist_save_param_data_packer import FinPersistSaveParamDataPacker
from .fin_persist_filed_data import FinPersistFiledData


class FinPersistSaveParamData(IData):
    def __init__(self, instrument_id: str = '', period: str = '',
                 append: bool = False, vacuum: bool = False):
        super().__init__(FinPersistSaveParamDataPacker(self))
        self._InstrumentID: str = instrument_id
        self._Period: str = period
        self._Fileds: List[FinPersistFiledData] = []
        self._Append: bool = append
        self._Vacuum: bool = vacuum

    @property
    def InstrumentID(self):
        return self._InstrumentID

    @InstrumentID.setter
    def InstrumentID(self, value: str):
        self._InstrumentID = value

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, value: str):
        self._Period = value

    @property
    def Fileds(self):
        return self._Fileds

    @Fileds.setter
    def Fileds(self, value: List[FinPersistFiledData]):
        self._Fileds = value

    @property
    def Append(self):
        return self._Append

    @Append.setter
    def Append(self, value: bool):
        self._Append = value

    @property
    def Vacuum(self):
        return self._Vacuum

    @Vacuum.setter
    def Vacuum(self, value: bool):
        self._Vacuum = value
