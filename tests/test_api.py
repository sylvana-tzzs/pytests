import pytest
import aiohttp
import os
from utils.api_utils import get_json

# Получаем токен из переменной окружения
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@pytest.mark.asyncio
async def test_github_api():
    if not GITHUB_TOKEN:
        pytest.skip("GITHUB_TOKEN не установлен, тест пропускается")

    url = "https://api.github.com"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            assert response.status == 200  # сервер ответил успешно
            data = await response.json()
            # Проверяем ключ, который точно есть для авторизованных запросов
            assert "current_user_url" in data