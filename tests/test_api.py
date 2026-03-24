import pytest
from utils.api_utils import get_json

@pytest.mark.asyncio
async def test_github_api():
    url = "https://api.github.com"
    data = await get_json(url)
    assert "current_user_url" in data