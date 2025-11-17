# Stanford AI Town (Generative Agents) 项目详细说明文档

## 项目概述

这是斯坦福大学Generative Agents项目的中文深度汉化版本，基于"wounderland"重构版本开发。该项目模拟了25个AI智能体在虚拟小镇中的生活，完全由大语言模型驱动，支持Ollama、OpenAI兼容API等多种LLM提供商。

## 项目文件结构及作用

### 根目录文件

- **start.py**: 仿真主入口，负责创建和运行虚拟小镇
- **compress.py**: 处理仿真结果，生成回放数据（movement.json和simulation.md）
- **replay.py**: Flask服务器，提供仿真回放的可视化界面

### 核心模块 (`modules/`)

#### 1. **agent.py** - 智能体核心逻辑
实现智能体的核心行为，包含：
- 记忆系统（空间记忆、日程记忆、关联记忆）
- 感知和行动逻辑
- 思考和反思机制
- 聊天和社交互动

#### 2. **game.py** - 仿真管理器
管理整体游戏状态：
- 创建和协调所有智能体
- 管理仿真时间
- 处理智能体思考周期

#### 3. **maze.py** - 环境和地图
定义空间世界：
- **Tile**: 单个地图单元格，包含地址层次结构（世界:区域:场所:对象）
- **Maze**: 完整地图，包含路径查找和空间查询功能

#### 4. **memory/** - 记忆系统（论文核心实现）

##### **event.py** - 事件表示
记忆的基本单位：`Event(subject, predicate, object, address, describe, emoji)`
示例："伊莎贝拉正在准备早餐 @ 小镇:约翰逊公园:咖啡馆"

##### **associate.py** - 关联记忆（记忆流）
**这是论文中"记忆流"的核心实现：**
- **Concept**: 将事件包装元数据（重要性、创建时间、访问时间、过期时间）
- **Associate**: 使用向量嵌入管理记忆流
  - 存储三种类型：事件、思考、对话
  - 检索使用**三因子评分系统**：
    - **时间性**: 近期记忆得分更高（指数衰减：0.995^n）
    - **重要性**: 基于重要性评分（1-10）
    - **相关性**: 向量相似度
  - 公式：`最终得分 = 时间权重 * 时间性 + 重要性权重 * 重要性 + 相关性权重 * 相关性`

##### **schedule.py** - 日程安排
管理智能体的日常计划：
- 创建小时级日程
- 将活动分解为子任务
- 处理日程修订

##### **spatial.py** - 空间记忆
智能体已知位置的层次树：
- 世界 → 区域 → 场所 → 对象
- 用于确定活动地点

##### **action.py** - 当前行动
表示智能体当前正在做的事情，包含持续时间和时间安排。

#### 5. **prompt/scratch.py** - LLM提示模板
包含约30个提示生成方法，所有模板存储在`data/prompts/`中：
- 日程生成（wake_up, schedule_init, schedule_daily, schedule_decompose）
- 决策制定（determine_sector, determine_arena, determine_object）
- 社交互动（decide_chat, generate_chat, decide_wait）
- 反思（reflect_focus, reflect_insights）
- 记忆检索（retrieve_plan, retrieve_thought, retrieve_currently）

#### 6. **model/llm_model.py** - LLM接口
不同LLM提供商的抽象：
- **OpenAILLMModel**: OpenAI兼容API
- **OllamaLLMModel**: 本地Ollama部署
- 处理重试、故障恢复和响应解析

#### 7. **storage/index.py** - 向量存储
**LlamaIndex**包装器，用于基于嵌入的记忆检索：
- 支持HuggingFace、Ollama、OpenAI嵌入
- 持久化存储和过期记忆清理

## 核心设计原理（来自论文）

### 1. 记忆流设计

**架构：**
```
记忆流 = [概念₁, 概念₂, ..., 概念ₙ]
每个概念 = {
    describe: "自然语言观察",
    type: "event" | "thought" | "chat",
    poignancy: 1-10 (重要性评分),
    create: 时间戳,
    access: 最后访问时间戳,
    expire: 过期时间戳,
    embedding: 向量表示
}
```

**实现位置：**
- `modules/memory/associate.py`: Associate类
- 使用LlamaIndex进行向量存储（`modules/storage/index.py`）

**关键特性：**
1. **自动清理**: 移除过期记忆（默认30天）
2. **容量限制**: 可通过`max_memory`参数限制记忆数量
3. **访问跟踪**: 每次检索时更新访问时间

### 2. 检索机制

**三因子评分系统**（在`AssociateRetriever._retrieve()`中实现）：

```python
# 时间性：指数衰减
recency_scores = [0.995^i for i in 1..n]

# 重要性：来自重要性元数据
importance_scores = [concept.poignancy for concept in concepts]

# 相关性：向量搜索的余弦相似度
relevance_scores = [similarity(query, concept) for concept in concepts]

# 最终排名
final_score = 0.5*recency + 2*importance + 3*relevance
```

**检索类型：**
- `retrieve_events()`: 近期事件观察
- `retrieve_thoughts()`: 反思结果
- `retrieve_chats()`: 对话历史
- `retrieve_focus()`: 自定义查询的聚焦检索

### 3. 反思（思考）设计

**实现位置：** `agent.py` - `reflect()`方法

**触发条件：**
当累积重要性达到阈值（默认150）时，触发反思。

**过程：**
1. **收集证据**: 检索近期高重要性事件和思考
2. **生成问题**: LLM生成3个高级问题（`reflect_focus`）
   - 示例："伊莎贝拉与他人的关系如何？"，"伊莎贝拉今天计划做什么？"
3. **综合洞察**: 对每个问题，检索相关记忆并生成洞察（`reflect_insights`）
   - 格式："洞察文本（证据索引：2,3,5）"
4. **存储为思考**: 将洞察作为新的思考节点保存回记忆流

**代码流程：**
```python
def reflect(self):
    if poignancy < threshold:
        return
    
    # 获取近期重要记忆
    nodes = retrieve_events() + retrieve_thoughts()
    
    # 生成反思问题
    focus = completion("reflect_focus", nodes, 3)
    # 返回：["问题1", "问题2", "问题3"]
    
    # 对每个问题，检索并综合
    retrieved = retrieve_focus(focus)
    for r_nodes in retrieved:
        thoughts = completion("reflect_insights", r_nodes, 5)
        # 返回：[("洞察", 证据_ids), ...]
        for thought, evidence in thoughts:
            add_concept("thought", event=thought, filling=evidence)
    
    # 重置重要性
    poignancy = 0
```

### 4. 规划（决策制定）设计

**实现位置：** `agent.py` - `make_schedule()`和`make_plan()`方法

**层次化规划系统：**

#### 第一层：日常日程
```python
def make_schedule(self):
    # 1. 从记忆检索更新"当前状态"
    focus = ["智能体今天的计划", "重要的近期事件"]
    retrieved = retrieve_focus(focus)
    plan = completion("retrieve_plan", retrieved)
    thought = completion("retrieve_thought", retrieved)
    currently = completion("retrieve_currently", plan, thought)
    
    # 2. 确定起床时间
    wake_up = completion("wake_up")  # 返回：6
    
    # 3. 生成粗略日常计划
    init_schedule = completion("schedule_init", wake_up)
    # 返回：["6点起床", "7点早餐", "8点阅读", ...]
    
    # 4. 填充小时级日程
    schedule = completion("schedule_daily", wake_up, init_schedule)
    # 返回：{6:00: "起床", 7:00: "早餐", ...}
```

#### 第二层：活动分解
```python
def schedule_decompose(plan):
    # 对于非睡眠活动，分解为子任务
    if duration > threshold:
        decompose = completion("schedule_decompose", plan)
        # 返回：[("刷牙", 10分钟), ("洗澡", 20分钟), ...]
```

#### 第三层：行动执行
```python
def _determine_action(self):
    plan = get_current_plan()  # "准备早餐"
    
    # 层次化位置选择：
    # 1. 区域选择
    sector = completion("determine_sector", plan, spatial_memory)
    
    # 2. 场所选择
    arena = completion("determine_arena", plan, spatial_memory)
    
    # 3. 对象选择
    object = completion("determine_object", plan, spatial_memory)
    
    address = [world, sector, arena, object]
    event = make_event(agent, plan, address)
    return Action(event, duration, start_time)
```

### 5. 感知系统

**实现位置：** `agent.py` - `percept()`方法

**过程：**
1. **空间扫描**: 获取视野半径内的瓦片（默认8个瓦片，盒子模式）
2. **事件过滤**: 
   - 仅限同一场所
   - 按距离排序
   - 取前N个（att_bandwidth = 8）
3. **新颖性检查**: 如果已在近期记忆中则跳过
4. **重要性评分**: LLM为每个事件评分重要性（1-10）
5. **记忆存储**: 添加到关联记忆流

```python
def percept(self):
    scope = maze.get_scope(coord, vision_r=8)
    events = gather_events(scope, same_arena=True)
    
    for event in events[:att_bandwidth]:
        if event not in recent_memory:
            poignancy = completion("poignancy_event", event)
            concept = associate.add_node("event", event, poignancy)
            concepts.append(concept)
```

### 6. 社交互动（反应）

**实现位置：** `agent.py` - `_reaction()`, `_chat_with()`, `_wait_other()`

#### 聊天决策过程：
```python
def _chat_with(self, other, focus):
    # 1. 检查约束条件
    if both_agents_sleeping or recent_chat_within_60min:
        return False
    
    # 2. LLM决定是否聊天
    chats_history = retrieve_chats(other.name)
    should_chat = completion("decide_chat", self, other, focus, chats_history)
    
    if should_chat:
        # 3. 生成对话
        relations = [
            summarize_relation(self, other),
            summarize_relation(other, self)
        ]
        
        for i in range(chat_iter):  # 默认4轮
            # 自己说话
            text = completion("generate_chat", self, other, relations[0], chats)
            
            # 检查终止
            if i > 0:
                should_end = completion("decide_chat_terminate", self, other, chats)
                if should_end:
                    break
            
            chats.append((self.name, text))
            
            # 对方回应
            text = completion("generate_chat", other, self, relations[1], chats)
            chats.append((other.name, text))
        
        # 4. 总结并保存
        summary = completion("summarize_chats", chats)
        schedule_chat(chats, summary, start, duration)
```

#### 等待决策过程：
```python
def _wait_other(self, other, focus):
    # 决定是否等待对方完成使用共享资源
    should_wait = completion("decide_wait", self, other, focus)
    
    if should_wait:
        # 创建等待行动
        event = Event(self, "等待开始", other.action)
        revise_schedule(event, start=now, duration=other.remaining_time)
```

## 关键设计模式

### 1. 故障恢复机制
每个LLM调用都有故障恢复返回值：
```python
completion(prompt, callback, failsafe="默认值", retry=10)
```

### 2. 层次化地址系统
所有位置使用4级寻址：
```
世界 : 区域 : 场所 : 对象
"小镇" : "约翰逊公园" : "咖啡馆" : "咖啡机"
```

### 3. 事件驱动更新
智能体移动时更新瓦片事件，为其他智能体创建可观察环境。

### 4. 基于模板的提示
所有提示使用基于文件的模板和变量替换：
```python
self.build_prompt("模板名称", {"var1": value1, "var2": value2})
```

## 仿真流程

```
1. start.py创建SimulateServer
2. 对于每个时间步：
   a. 对于每个智能体：
   - make_schedule() [如果是新的一天]
   - move() [更新位置]
   - percept() [观察环境]
   - make_plan() [决定行动]
   - reflect() [如果重要性阈值达到]
   - think()返回带路径的计划
   b. 用新事件更新迷宫
   c. 保存检查点
3. compress.py生成回放数据
4. replay.py提供可视化服务
```

## 修改指南

### 添加新记忆类型：
1. 在`Associate.memory`字典中添加类型
2. 在`Associate`类中创建检索方法
3. 在`Agent.reflect()`中添加相应的反思逻辑

### 自定义智能体行为：
1. 修改`data/prompts/`中的提示模板
2. 调整`AssociateRetriever._retrieve()`中的权重
3. 更改智能体配置中的阈值（poignancy_max, vision_r等）

### 添加新行动：
1. 创建新的提示模板
2. 在`Scratch`类中添加提示方法
3. 集成到`Agent.make_plan()`或`Agent._reaction()`中

### 修改社交动态：
1. 调整`_chat_with()`中的聊天决策逻辑
2. 修改记忆中的关系跟踪
3. 自定义`decide_chat`和`decide_wait`提示

## 论文核心组件实现

这个架构忠实地实现了论文的三个核心组件：

- **记忆流**: 具有重要性和相关性的时间加权关联记忆
- **反思**: 将经验定期综合为高级洞察
- **规划**: 从日常日程到具体行动的层次化目标分解

## 技术特点

### 中文优化
- 所有提示语完全中文化
- 针对中文LLM（如Qwen、GLM-4）优化
- 支持中文对话和思考模式

### 本地部署支持
- 支持Ollama本地模型部署
- 降低实验成本
- 完全离线运行能力

### 断点恢复
- 支持仿真中断后继续运行
- 自动保存检查点
- 状态持久化

### 可视化回放
- 基于Web的回放界面
- 时间线展示
- 对话记录导出为Markdown

这个项目为基于Generative Agents进行修改和实验提供了坚实的基础，所有核心组件都经过精心设计，便于理解和扩展。
