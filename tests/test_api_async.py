import pytest
import aiohttp
import asyncio

@pytest.mark.asyncio
async def test_github_api():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/users/sylvana-tzzs") as resp:
            data = await resp.json()
            assert data["login"] == "sylvana-tzzs"
            assert resp.status == 200