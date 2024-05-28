from ert.gui.ertnotifier import ErtNotifier
from ert.gui.ertwidgets.models.valuemodel import ValueModel


class IterValueModel(ValueModel):
    def __init__(self, notifier: ErtNotifier, default_value: int = 0) -> None:
        self._default_value = str(default_value)
        ValueModel.__init__(self, self.getDefaultValue())
        notifier.current_ensemble_changed.connect(self._ensembleChanged)

    def setValue(self, value: int) -> None:
        ValueModel.setValue(self, value)

    def getDefaultValue(self):
        return self._default_value

    def _ensembleChanged(self) -> None:
        ValueModel.setValue(self, self.getDefaultValue())
