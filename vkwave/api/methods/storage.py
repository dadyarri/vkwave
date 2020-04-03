from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Storage(Category):
    async def get(
        self,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param key:
        :param keys:
        :param user_id:
        :param global_:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = dict(**raw_result)
        return result

    async def get_keys(
        self,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, StorageGetKeysResponse]:
        """
        :param user_id: - user id, whose variables names are returned if they were requested with a server method.
        :param global_:
        :param offset:
        :param count: - amount of variable names the info needs to be collected from.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getKeys", params)
        if raw:
            return raw_result

        result = StorageGetKeysResponse(**raw_result)
        return result

    async def set(
        self,
        key: str = None,
        value: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param key:
        :param value:
        :param user_id:
        :param global_:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("set", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result
