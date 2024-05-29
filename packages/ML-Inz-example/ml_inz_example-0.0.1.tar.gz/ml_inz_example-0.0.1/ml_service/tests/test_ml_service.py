import pytest
from ml_service.app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_query(client):
    response = client.post('/query/', json={
        "question": "what is the percentage change of the net income from Q4 FY23 to Q4 FY24?",
        "document": """NVIDIA (NASDAQ: NVDA) today reported revenue for the fourth quarter ended January 28, 2024, of $22.1 billion, up 22% from the previous quarter и up 265% from a year ago.\nFor the quarter, GAAP earnings per diluted share был $4.93, up 33% from the previous quarter и up 765% from a year ago. Non-GAAP earnings per diluted share был $5.16, up 28% from the previous quarter и up 486% from a year ago.\nQ4 Fiscal 2024 Summary\nGAAP\n| $ in millions, except earnings per share | Q4 FY24 | Q3 FY24 | Q4 FY23 | Q/Q | Y/Y |\n| Revenue | $22,103 | $18,120 | $6,051 | Up 22% | Up 265% |\n| Gross margin | 76.0% | 74.0% | 63.3% | Up 2.0 pts | Up 12.7 pts |\n| Operating expenses | $3,176 | $2,983 | $2,576 | Up 6% | Up 23% |\n| Operating income | $13,615 | $10,417 | $1,257 | Up 31% | Up 983% |\n| Net income | $12,285 | $9,243 | $1,414 | Up 33% | Up 769% |\n| Diluted earnings per share | $4.93 | $3.71 | $0.57 | Up 33% | Up 765% |"""
    })
    assert response.status_code == 200
    response_json = response.get_json()  # Получаем JSON-ответ
    assert "response" in response_json  # Проверяем, что ключ 'response' есть в JSON-ответе
