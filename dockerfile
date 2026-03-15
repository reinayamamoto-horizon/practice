FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev build-essential pkg-config curl \
    && rm -rf /var/lib/apt/lists/*

# Node.js 20 LTS をインストール
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 先に package.json だけコピーしてコンテナ内で npm install（Linux 用バイナリが入る）
COPY package.json package-lock.json* ./
RUN npm ci 2>/dev/null || npm install

# エントリポイントは /code 外に置く（.:/code マウントで上書きされないようにする）
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .
ENTRYPOINT ["/entrypoint.sh"]