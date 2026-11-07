FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install --no-cache-dir poetry

ENV PATH=/opt/venv/bin:$PATH

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root --no-interaction

FROM python:3.13-slim AS runtime

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH=/opt/venv/bin:$PATH

COPY --from=builder /opt/venv /opt/venv
COPY app ./app

RUN useradd --system --uid 10001 --create-home appuser
USER appuser
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
