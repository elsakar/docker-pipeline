FROM python:3.9.10-slim-bullseye

WORKDIR /app

COPY ./src .

EXPOSE 5000

CMD [ "python", "microwebserver.py" ]

USER Xmaeltht

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl --fail http://localhost || exit 1" ]