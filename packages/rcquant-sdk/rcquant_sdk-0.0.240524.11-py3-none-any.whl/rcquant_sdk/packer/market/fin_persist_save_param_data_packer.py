from ...interface import IPacker
from ...data.market.fin_persist_filed_data import FinPersistFiledData


class FinPersistSaveParamDataPacker(IPacker):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def obj_to_tuple(self):
        tempfileds = []
        for filed in self._obj.Fileds:
            tempfileds.append(filed.obj_to_tuple())

        return [str(self._obj.InstrumentID), str(self._obj.Period), tempfileds, bool(self._obj.Append), bool(self._obj.Vacuum)]

    def tuple_to_obj(self, t):
        if len(t) >= 5:
            self._obj.InstrumentID = t[0]
            self._obj.Period = t[1]
            for temp in t[2]:
                fd = FinPersistFiledData()
                fd.tuple_to_obj(temp)
                self._obj.Fileds.append(fd)
            self._obj.Append = t[3]
            self._obj.Vacuum = t[4]

            return True
        return False
