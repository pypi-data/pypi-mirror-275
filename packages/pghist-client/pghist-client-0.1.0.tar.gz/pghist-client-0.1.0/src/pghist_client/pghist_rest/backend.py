from pghist_client.pghist_rest.dataclasses import (
    HistoryData,
)
from pghist_client.pghist_rest.server import (
    server,
)
from pghist_client.pghist_rest.utils import (
    WrongFilterException,
)


class Backend:
    """Бэкенд для работы с API получения данных из PGHist."""

    main_object_loader = HistoryData

    def __init__(self):
        self.__data_url = '/data'
        self.__server = server

    def get_history_data(self, params=None, as_json=False):
        """Возвращает результат запроса данных из PGHist.

        Args:
            params: Параметры запроса
            as_json: Возвращать данные в формате JSON
        """
        if params is None:
            params = dict()

        data = self.__server.get(self.__data_url, params=params).json()
        if not as_json:
            data = self.__prepare_data(data)

        return data

    def __prepare_data(self, data):
        """Подготавливает сырые данные из PGHist."""
        data['raw_data'] = data.pop('results', {})

        try:
            result = self.main_object_loader(**data)
        except TypeError as e:
            if '__all__' in data:
                raise WrongFilterException(message=data['__all__'])
            else:
                raise e
        else:
            return result


