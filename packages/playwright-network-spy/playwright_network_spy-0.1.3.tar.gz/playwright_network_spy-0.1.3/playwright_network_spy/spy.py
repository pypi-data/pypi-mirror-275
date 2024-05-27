import asyncio
from collections.abc import Awaitable, Callable
from typing import Any

from playwright.async_api import Page, Response

TargetResponseCheckerType = Callable[[Response], Awaitable[bool]]


class NetworkSpy:
    """
    A class to intercept and store network responses on a Playwright page.
    """

    def __init__(
        self,
        page: Page,
        target_response_checker: TargetResponseCheckerType,
    ) -> None:
        """
        Initializes the NetworkSpy with a Playwright Page object and a target response checker.

        Args:
            page (Page): The Playwright Page object representing the web page.
            target_response_checker (TargetResponseCheckerType): \
                A callable that checks if a response is a target response.
        """
        self.page = page
        self._responses: list[Response] = []
        self._attach_response_interceptor(target_response_checker)

    def _attach_response_interceptor(self, target_response_checker: TargetResponseCheckerType) -> None:
        """
        Attaches an interceptor to the page to capture responses that match the target response checker.

        Args:
            target_response_checker (TargetResponseCheckerType): \
                A callable that checks if a response is a target response.
        """

        async def _capture_response(response: Response) -> None:
            if await target_response_checker(response):
                self._responses.append(response)

        self.page.on("response", _capture_response)

    def get_new_responses(self) -> list[Response]:
        """
        Retrieves and clears the list of new responses.

        Returns:
            list[Response]: A list of new responses.
        """
        new_responses = self._responses.copy()
        self._responses.clear()
        return new_responses


class JSONSpy(NetworkSpy):
    """
    A class to intercept and store JSON network responses on a Playwright page.

    Inherits from NetworkSpy and adds functionality to filter and retrieve JSON responses.
    """

    def __init__(self, page: Page, target_response_checker: TargetResponseCheckerType) -> None:
        """
        Initializes the JSONSpy with a Playwright Page object and a target response checker.

        Args:
            page (Page): The Playwright Page object representing the web page.
            target_response_checker (TargetResponseCheckerType): \
                A callable that checks if a response is a target response.
        """

        async def _target_json_response_checker(response: Response) -> bool:
            return await target_response_checker(response) and "application/json" in response.headers.get(
                "content-type", ""
            )

        super().__init__(page, _target_json_response_checker)

    async def get_new_json_responses(self) -> list[dict[str, Any]]:
        """
        Retrieves and clears the list of new JSON responses.

        Returns:
            list[dict[str, Any]]: A list of new JSON responses.
        """
        new_responses: list[Response] = self.get_new_responses()
        response_bodies_with_exceptions: list[dict[str, Any] | Exception] = await asyncio.gather(
            *(response.json() for response in new_responses),
            return_exceptions=True,
        )
        response_bodies: list[dict[str, Any]] = [
            response_body
            for response_body in response_bodies_with_exceptions
            if not isinstance(response_body, Exception)
        ]
        return response_bodies


class VideoSpy(NetworkSpy):
    """
    A class to intercept and store video network responses on a Playwright page.

    Inherits from NetworkSpy and adds functionality to filter and retrieve video responses.
    """

    def __init__(self, page: Page, target_response_checker: TargetResponseCheckerType) -> None:
        """
        Initializes the VideoSpy with a Playwright Page object and a target response checker.

        Args:
            page (Page): The Playwright Page object representing the web page.
            target_response_checker (TargetResponseCheckerType): \
                A callable that checks if a response is a target response.
        """

        async def _target_video_response_checker(response: Response) -> bool:
            return await target_response_checker(response) and "video/mp4" in response.headers.get("content-type", "")

        super().__init__(page, _target_video_response_checker)

    async def get_new_video_responses(self) -> list[bytes]:
        """
        Retrieves and clears the list of new video responses.

        Returns:
            list[bytes]: A list of new video responses.
        """
        new_responses: list[Response] = self.get_new_responses()
        response_bodies_with_exceptions: list[bytes | Exception] = await asyncio.gather(
            *(response.body() for response in new_responses),
            return_exceptions=True,
        )
        response_bodies: list[bytes] = [
            response_body
            for response_body in response_bodies_with_exceptions
            if not isinstance(response_body, Exception)
        ]
        return response_bodies
