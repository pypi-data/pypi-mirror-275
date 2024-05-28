"""Tests for firing requests at the Fumis WiRCU API."""

import asyncio

import aiohttp
import pytest

from fumis_wircu import Fumis
from fumis_wircu.__version__ import __version__
from fumis_wircu.exceptions import FumisConnectionError, FumisError


@pytest.mark.asyncio
async def test_json_request(aresponses):
    """Test JSON response is handled correctly."""
    event_loop = asyncio.get_event_loop()
    aresponses.add(
        "api.fumis.si",
        "/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"test": "ok"}',
        ),
    )
    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
        )
        response = await fumis._request("/")
        assert response["test"] == "ok"


@pytest.mark.asyncio
async def test_internal_session(aresponses):
    """Test internal client session is handled correctly."""
    event_loop = asyncio.get_event_loop()
    aresponses.add(
        "api.fumis.si",
        "/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"test": "ok"}',
        ),
    )

    async with Fumis(
        mac="AABBCCDDEEFF",
        password="1234",
        loop=event_loop,
    ) as fumis:
        response = await fumis._request("/")
        assert response["test"] == "ok"


@pytest.mark.asyncio
async def test_request_user_agent(aresponses):
    """Test client sending correct user agent headers."""
    event_loop = asyncio.get_event_loop()

    # Handle to run asserts on request in
    async def response_handler(request):
        assert request.headers["User-Agent"] == f"PythonFumis/{__version__}"
        return aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        )

    aresponses.add("api.fumis.si", "/", "GET", response_handler)

    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
        )
        await fumis._request("/")


@pytest.mark.asyncio
async def test_request_custom_user_agent(aresponses):
    """Test client sending correct user agent headers."""
    event_loop = asyncio.get_event_loop()

    # Handle to run asserts on request in
    async def response_handler(request):
        assert request.headers["User-Agent"] == "LoremIpsum/1.0"
        return aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        )

    aresponses.add("api.fumis.si", "/", "GET", response_handler)

    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
            user_agent="LoremIpsum/1.0",
        )
        await fumis._request("/")


@pytest.mark.asyncio
async def test_timeout(aresponses):
    """Test request timeout from Fumis WiRCU API."""
    event_loop = asyncio.get_event_loop()

    # Faking a timeout by sleeping
    async def response_handler(_):
        await asyncio.sleep(2)
        return aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        )

    aresponses.add("api.fumis.si", "/", "GET", response_handler)

    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
            request_timeout=1,
        )
        with pytest.raises(FumisConnectionError):
            assert await fumis._request("/")


@pytest.mark.asyncio
async def test_invalid_content_type(aresponses):
    """Test invalid content type from Fumis WiRCU API."""
    event_loop = asyncio.get_event_loop()
    aresponses.add(
        "api.fumis.si",
        "/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "other/content"},
            text="{}",
        ),
    )

    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
            request_timeout=1,
        )
        with pytest.raises(FumisError):
            await fumis._request("/")


@pytest.mark.asyncio
async def test_http_error(aresponses):
    """Test HTTP error response handling."""
    event_loop = asyncio.get_event_loop()
    aresponses.add(
        "api.fumis.si",
        "/",
        "GET",
        aresponses.Response(text="OMG PUPPIES!", status=404),
    )
    aresponses.add(
        "api.fumis.si",
        "/",
        "GET",
        aresponses.Response(text="OMG PUPPIES!", status=500),
    )

    async with aiohttp.ClientSession(loop=event_loop) as session:
        fumis = Fumis(
            mac="AABBCCDDEEFF",
            password="1234",
            session=session,
            loop=event_loop,
            request_timeout=1,
        )
        with pytest.raises(FumisError):
            assert await fumis._request("/")

        with pytest.raises(FumisError):
            assert await fumis._request("/")
