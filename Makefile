.PHONY: install run gui lint clean list process download

# 默认 Python 解释器
PYTHON = python3

# 虚拟环境路径
VENV = venv

# 激活虚拟环境的命令
ACTIVATE = . $(VENV)/bin/activate

install: $(VENV)/bin/activate
	$(ACTIVATE) && pip install -r requirements.txt

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

## 启动图形界面
gui:
	$(ACTIVATE) && $(PYTHON) UVR.py

## 列出所有模型
list:
	$(ACTIVATE) && $(PYTHON) uvr_cli.py list

## 搜索模型信息 (用法: make info QUERY="vocals")
info:
	$(ACTIVATE) && $(PYTHON) uvr_cli.py info $(QUERY)

## 分离音频 (用法: make process INPUT="歌曲.mp3" [STEM="vocals"])
process:
	$(ACTIVATE) && $(PYTHON) uvr_cli.py process $(INPUT) --two-stem $(STEM)

## 预下载 Demucs 模型（curl 加速）
download:
	$(ACTIVATE) && $(PYTHON) uvr_cli.py download-models

## 运行代码检查
lint:
	$(ACTIVATE) && pip install ruff -q && ruff check --select=E,F,W,I --ignore=E501 uvr_cli.py playsound.py demucs/pretrained.py demucs/repo.py

## 自动修复 lint 问题
fix:
	$(ACTIVATE) && ruff check --select=E,F,W,I --ignore=E501 --fix uvr_cli.py playsound.py demucs/pretrained.py demucs/repo.py

## 清理缓存文件
clean:
	rm -rf $(VENV)
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf .ruff_cache
	rm -rf tmp

## 显示帮助
help:
	@echo "用法: make <target>"
	@echo ""
	@echo "可用命令:"
	@echo "  install         安装依赖"
	@echo "  gui             启动图形界面"
	@echo "  list            列出所有模型"
	@echo "  info QUERY=x    搜索模型信息"
	@echo "  process INPUT=x 分离音频 (STEM=vocals)"
	@echo "  download        预下载模型"
	@echo "  lint            代码检查"
	@echo "  fix             自动修复 lint"
	@echo "  clean           清理缓存"
