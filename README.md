# DIY生成式智能体（Generative Agents）

本项目基于[GenerativeAgentsCN](https://github.com/x-glacier/GenerativeAgentsCN)项目进行二次开发，主要工作是修改了场景地图和角色定义，并编写了较为详细的教程文档：详见`docs/`文件夹中的[tutorial.md](docs/tutorial.md)

## 1. 准备工作

### 1.1 获取代码：

```
git clone https://github.com/x-glacier/GenerativeAgentsCN.git
cd GenerativeAgentsCN
```

### 1.2 配置大语言模型（LLM）

修改配置文件 `generative_agents/data/config.json`:

1. 默认使用[Ollama](https://ollama.com/)加载本地量化模型，并提供OpenAI兼容API。需要先拉取量化模型（参考[ollama.md](docs/ollama.md)），并确保 `base_url`和 `model`与Ollama中的配置一致。
2. 如果希望调用其他OpenAI兼容API，需要将 `provider`改为 `openai`，并根据API文档修改 `model`、`api_key`和 `base_url`。

### 1.3 安装python依赖

建议先使用anaconda3创建并激活虚拟环境：

```
conda create -n generative_agents_cn python=3.12
conda activate generative_agents_cn
```

安装依赖：

```
pip install -r requirements.txt
```

## 2. 运行虚拟小镇

```
cd generative_agents
python start.py --name sim-test --start "20250213-09:30" --step 10 --stride 10
```

参数说明:

- `name` - 每次启动虚拟小镇，需要设定唯一的名称，用于事后回放。
- `start` - 虚拟小镇的起始时间。
- `resume` - 在运行结束或意外中断后，从上次的“断点”处，继续运行虚拟小镇。
- `step` - 在迭代多少步之后停止运行。
- `stride` - 每一步迭代在虚拟小镇中对应的时间（分钟）。假如设定 `--stride 10`，虚拟小镇在迭代过程中的时间变化将会是 9:00，9:10，9:20 ...

## 3. 回放

### 3.1 生成回放数据

```
python compress.py --name <simulation-name>
```

运行结束后将在 `results/compressed/<simulation-name>`目录下生成回放数据文件 `movement.json`。同时还将生成 `simulation.md`，以时间线方式呈现每个智能体的状态及对话内容。

### 3.2 启动回放服务

```
python replay.py
```

通过浏览器打开回放页面（地址：`http://127.0.0.1:5000/?name=<simulation-name>`），可以看到虚拟小镇中的居民在各个时间段的活动。

*可通过方向键移动画面*

参数说明

- `name` - 启动虚拟小镇时设定的名称。
- `step` - 回放的起始步数，0代表从第一帧开始回放，预设值为0。
- `speed` - 回放速度（0-5），0最慢，5最快，预设值为2。
- `zoom` - 画面缩放比例，预设值为0.8。

发布版本中内置了名为 `example`的回放数据（由qwen2.5:32b-instruct-q4_K_M生成）。若希望以较快速度从头开始回放，画面缩放比例为0.6，则对应的url是：
http://127.0.0.1:5000/?name=example&step=0&speed=2&zoom=0.6

也可直接打开[simulation.md](generative_agents/results/compressed/example/simulation.md)，查看 `example`中所有人物活动和对话信息。