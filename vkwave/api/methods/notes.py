from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Notes(Category):
    async def add(
        self,
        title: str = None,
        text: str = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        raw: bool = False,
    ) -> typing.Union[dict, NotesAddResponse]:
        """
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if raw:
            return raw_result

        result = NotesAddResponse(**raw_result)
        return result

    async def create_comment(
        self,
        note_id: int = None,
        owner_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        message: str = None,
        guid: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, NotesCreateCommentResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param reply_to: - ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param message: - Comment text.
        :param guid:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if raw:
            return raw_result

        result = NotesCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self, note_id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param note_id: - Note ID.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_comment(
        self,
        comment_id: int = None,
        owner_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteComment", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        note_id: int = None,
        title: str = None,
        text: str = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param note_id: - Note ID.
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        comment_id: int = None,
        owner_id: typing.Optional[int] = None,
        message: str = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param message: - New comment text.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editComment", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        note_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, NotesGetResponse]:
        """
        :param note_ids: - Note IDs.
        :param user_id: - Note owner ID.
        :param offset:
        :param count: - Number of notes to return.
        :param sort:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = NotesGetResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        note_id: int = None,
        owner_id: typing.Optional[int] = None,
        need_wiki: typing.Optional[bool] = None,
        raw: bool = False,
    ) -> typing.Union[dict, NotesGetByIdResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param need_wiki:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if raw:
            return raw_result

        result = NotesGetByIdResponse(**raw_result)
        return result

    async def get_comments(
        self,
        note_id: int = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, NotesGetCommentsResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param sort:
        :param offset:
        :param count: - Number of comments to return.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if raw:
            return raw_result

        result = NotesGetCommentsResponse(**raw_result)
        return result

    async def restore_comment(
        self,
        comment_id: int = None,
        owner_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result
