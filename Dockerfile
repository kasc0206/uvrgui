FROM python:3.10-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖清单并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 创建非 root 用户
RUN useradd -m -u 1000 uvr && chown -R uvr:uvr /app
USER uvr

# 预下载模型（构建时可选，取消注释以预下载）
# RUN python uvr_cli.py download-models

ENTRYPOINT ["python", "uvr_cli.py"]
CMD ["--help"]
