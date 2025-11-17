# Generative Agents 场景和角色定制指导文档

## 概述

本文档详细说明如何在 Generative Agents 项目中更换仿真场景和代理角色。项目支持完全自定义的虚拟世界和智能体配置，包括地图、角色属性、行为模式等。

## 目录结构

```
GenerativeAgentsCN/
├── generative_agents/
│   ├── data/
│   │   ├── config.json          # 全局配置
│   │   └── prompts/             # LLM提示模板
│   ├── frontend/static/assets/village/
│   │   ├── maze.json            # 主地图配置
│   │   ├── sjtu.json            # 备用地图配置
│   │   ├── agents/              # 智能体配置目录
│   │   │   ├── 阿伊莎/
│   │   │   │   ├── agent.json   # 角色配置文件
│   │   │   │   └── portrait.png # 角色头像
│   │   │   └── ...
│   │   └── tilemap/             # 地图瓦片资源
│   └── start.py                 # 仿真启动脚本
```

## 第一部分：更换仿真场景

### 1.1 地图文件结构

地图文件（如 `maze.json`）定义了虚拟世界的空间结构：

```json
{
    "world": "the Ville",           // 世界名称
    "tile_size": 32,               // 瓦片大小（像素）
    "size": [100, 140],            // 地图尺寸（宽x高）
    "map": {
        "asset": "map",
        "tileset_groups": {...},   // 瓦片组配置
        "layers": [...],           // 地图图层
        "tiles": [...]             // 具体瓦片数据
    }
}
```

### 1.2 创建新地图的步骤

#### 步骤1：准备地图资源
1. **瓦片集准备**：
   - 将地图瓦片图片放入 `frontend/static/assets/village/tilemap/` 目录
   - 支持的瓦片集格式：PNG图片文件
   - 瓦片大小必须为32x32像素

2. **地图设计**：
   - 使用地图编辑器（如Tiled Map Editor）创建地图
   - 设计层次结构：地面层、装饰层、墙体层等
   - 确保路径连通性，智能体需要能够在地图间移动

#### 步骤2：配置地图JSON文件

创建新的地图配置文件，例如 `university.json`：

```json
{
    "world": "大学城",
    "tile_size": 32,
    "size": [120, 100],
    "map": {
        "asset": "university_map",
        "tileset_groups": {
            "group_1": [
                "university_buildings",
                "university_ground",
                "university_decorations"
            ]
        },
        "layers": [
            {
                "name": "Ground",
                "tileset_group": "group_1"
            },
            {
                "name": "Buildings", 
                "tileset_group": "group_1"
            },
            {
                "name": "Decorations",
                "tileset_group": "group_1"
            }
        ],
        "tiles": [
            // 具体的瓦片数据数组
            // 每个元素代表一个地图位置的值
        ]
    }
}
```

#### 步骤3：更新启动配置

修改 `start.py` 中的地图路径：

```python
# 在 get_config() 函数中修改
config = {
    "stride": stride,
    "time": {"start": start_time},
    "maze": {"path": os.path.join(assets_root, "university.json")},  # 修改这里
    "agent_base": agent_config,
    "agents": {},
}
```

### 1.3 地图层次结构设计

地图需要支持四层地址系统：`世界:区域:场所:对象`

#### 示例：大学城地图结构
```json
{
    "spatial": {
        "tree": {
            "大学城": {
                "计算机学院": {
                    "教学楼": ["教室A101", "教室A102", "实验室"],
                    "办公室": ["教授办公室", "学生办公室"]
                },
                "图书馆": {
                    "阅览室": ["阅览桌1", "阅览桌2", "书架区"],
                    "自习室": ["自习桌", "讨论区"]
                },
                "学生宿舍": {
                    "男生宿舍": ["房间101", "房间102", "公共区域"],
                    "女生宿舍": ["房间201", "房间202", "公共区域"]
                },
                "食堂": {
                    "一楼": ["窗口1", "窗口2", "座位区"],
                    "二楼": ["窗口3", "窗口4", "座位区"]
                }
            }
        }
    }
}
```

## 第二部分：更换代理角色

### 2.1 角色配置文件结构

每个智能体都有独立的配置文件，位于 `agents/[角色名]/agent.json`：

```json
{
    "name": "角色名称",
    "portrait": "assets/village/agents/角色名/portrait.png",
    "coord": [x, y],                    // 初始坐标
    "currently": "当前状态描述",
    "scratch": {
        "age": 20,                      // 年龄
        "innate": "性格特征",           // 内在性格
        "learned": "背景描述",          // 学习到的特征
        "lifestyle": "生活习惯",        // 日常作息
        "daily_plan": "日常计划"        // 基本日程安排
    },
    "spatial": {
        "address": {
            "living_area": ["世界", "区域", "场所"]
        },
        "tree": {
            // 空间记忆树结构
        }
    }
}
```

### 2.2 创建新角色的步骤

#### 步骤1：创建角色目录和文件

```bash
# 创建角色目录
mkdir -p frontend/static/assets/village/agents/新角色名

# 创建配置文件
touch frontend/static/assets/village/agents/新角色名/agent.json

# 添加角色头像（可选）
cp 头像文件.png frontend/static/assets/village/agents/新角色名/portrait.png
```

#### 步骤2：编写角色配置文件

创建 `agent.json` 文件：

```json
{
    "name": "李明",
    "portrait": "assets/village/agents/李明/portrait.png",
    "coord": [50, 30],
    "currently": "李明正在计算机实验室调试程序，准备明天的项目答辩。",
    "scratch": {
        "age": 22,
        "innate": "勤奋、专注、技术导向",
        "learned": "李明是一名计算机科学专业的研究生，专攻人工智能方向。他喜欢编程，对新技术充满热情。",
        "lifestyle": "李明通常晚上11点睡觉，早上7点起床，中午12点吃午饭，晚上6点吃晚饭。",
        "daily_plan": "李明从上午9点到下午5点在实验室工作，晚上在宿舍学习或休息。"
    },
    "spatial": {
        "address": {
            "living_area": ["大学城", "学生宿舍", "李明房间"]
        },
        "tree": {
            "大学城": {
                "计算机学院": {
                    "实验室": ["工作站1", "工作站2", "服务器"],
                    "教室": ["教室A101", "教室A102", "黑板"]
                },
                "图书馆": {
                    "阅览室": ["阅览桌", "书架区", "讨论区"]
                },
                "学生宿舍": {
                    "李明房间": ["书桌", "床", "衣柜", "电脑"]
                },
                "食堂": {
                    "一楼": ["窗口1", "窗口2", "座位区"]
                }
            }
        }
    }
}
```

#### 步骤3：更新角色列表

在 `start.py` 中更新 `personas` 列表：

```python
personas = [
    "阿伊莎", "克劳斯", "玛丽亚", "沃尔夫冈",  # 原有角色
    "梅", "约翰", "埃迪",  # 原有角色
    "李明", "张华", "王芳",  # 新增角色
    # ... 其他角色
]
```

### 2.3 角色属性详解

#### 核心属性说明

1. **name**: 角色名称，用于识别和对话
2. **coord**: 初始坐标 `[x, y]`，在地图中的起始位置
3. **currently**: 当前状态描述，影响角色的初始行为
4. **scratch.age**: 年龄，影响角色的行为模式
5. **scratch.innate**: 内在性格，影响决策和对话风格
6. **scratch.learned**: 背景知识，影响角色的专业领域
7. **scratch.lifestyle**: 作息习惯，影响日程安排
8. **scratch.daily_plan**: 基本日程，作为日程生成的参考

#### 空间记忆配置

`spatial.tree` 定义了角色对世界的认知结构：

```json
{
    "spatial": {
        "tree": {
            "世界名": {
                "区域名": {
                    "场所名": ["对象1", "对象2", "对象3"]
                }
            }
        }
    }
}
```

**重要原则**：
- 层次结构必须与地图实际布局一致
- 每个角色可以有不同的空间认知
- 对象列表影响角色的行为选择

### 2.4 角色行为定制

#### 通过提示模板定制行为

修改 `data/prompts/` 目录下的模板文件：

1. **日程生成** (`schedule_init.txt`, `schedule_daily.txt`)
2. **决策制定** (`determine_sector.txt`, `determine_arena.txt`)
3. **社交互动** (`decide_chat.txt`, `generate_chat.txt`)
4. **反思机制** (`reflect_focus.txt`, `reflect_insights.txt`)

#### 示例：定制角色对话风格

修改 `generate_chat.txt`：

```
${base_desc}

${agent} 正在与 ${other} 对话。
${agent} 的性格特点：${innate}
${agent} 的背景：${learned}

对话历史：
${chats}

请生成 ${agent} 的下一句话，要体现其性格特点。
```

## 第三部分：高级定制

### 3.1 全局配置修改

修改 `data/config.json` 来调整全局行为：

```json
{
    "agent": {
        "percept": {
            "mode": "box",           // 感知模式
            "vision_r": 8,          // 视野半径
            "att_bandwidth": 8       // 注意力带宽
        },
        "schedule": {
            "max_try": 5,           // 日程生成最大尝试次数
            "diversity": 5         // 日程多样性
        },
        "think": {
            "llm": {
                "provider": "openai",
                "model": "deepseek-ai/DeepSeek-V3.2-Exp",
                "base_url": "https://api.siliconflow.cn/v1",
                "api_key": "your-api-key"
            },
            "interval": 1000,       // 思考间隔
            "poignancy_max": 150    // 反思阈值
        },
        "chat_iter": 4,            // 对话轮数
        "associate": {
            "embedding": {
                "provider": "openai",
                "model": "BAAI/bge-m3",
                "base_url": "https://api.siliconflow.cn/v1", 
                "api_key": "your-api-key"
            },
            "retention": 8         // 记忆保留天数
        }
    }
}
```

### 3.2 创建主题场景

#### 示例：创建校园场景

1. **地图设计**：
   - 教学楼、图书馆、宿舍、食堂、操场
   - 确保各区域间有连通路径
   - 设置合适的瓦片和装饰

2. **角色设计**：
   - 学生角色：不同专业、年级
   - 教师角色：不同学科、性格
   - 工作人员：食堂、图书馆、宿舍管理员

3. **行为模式**：
   - 上课时间：学生去教室，教师授课
   - 用餐时间：集中在食堂
   - 学习时间：图书馆、自习室
   - 休息时间：宿舍、操场

#### 示例：创建公司场景

1. **地图设计**：
   - 办公区、会议室、休息区、食堂
   - 不同部门的工作区域
   - 管理层办公室

2. **角色设计**：
   - 员工：不同部门、职位
   - 管理者：不同层级、管理风格
   - 客户：外部访客

3. **行为模式**：
   - 工作时间：办公、会议
   - 休息时间：休息区、食堂
   - 社交时间：同事交流、客户接待

### 3.3 多场景切换

#### 场景切换配置

创建场景配置文件 `scenarios.json`：

```json
{
    "scenarios": {
        "campus": {
            "map": "university.json",
            "agents": ["李明", "张华", "王芳", "教授A", "教授B"],
            "description": "大学校园场景"
        },
        "office": {
            "map": "company.json", 
            "agents": ["员工A", "员工B", "经理A", "客户A"],
            "description": "公司办公场景"
        },
        "village": {
            "map": "maze.json",
            "agents": ["阿伊莎", "克劳斯", "玛丽亚", "沃尔夫冈"],
            "description": "原始村庄场景"
        }
    }
}
```

#### 动态场景加载

修改 `start.py` 支持场景选择：

```python
def load_scenario(scenario_name):
    with open("scenarios.json", "r", encoding="utf-8") as f:
        scenarios = json.load(f)
    
    if scenario_name not in scenarios:
        raise ValueError(f"Scenario {scenario_name} not found")
    
    scenario = scenarios[scenario_name]
    return get_config(
        start_time="20240213-09:30",
        stride=15,
        agents=scenario["agents"],
        map_path=scenario["map"]
    )
```

## 第四部分：测试和调试

### 4.1 测试新场景

1. **启动仿真**：
```bash
cd /home/scy/ai_agent/GenerativeAgentsCN/generative_agents
python start.py --name test-new-scenario --step 5
```

2. **检查日志**：
   - 查看控制台输出
   - 检查 `results/checkpoints/test-new-scenario/` 目录
   - 查看 `simulate-*.json` 文件

3. **验证行为**：
   - 角色是否正确移动
   - 对话是否合理
   - 日程安排是否符合预期

### 4.2 常见问题解决

#### 问题1：角色无法移动
- **原因**：地图路径不连通
- **解决**：检查地图瓦片配置，确保有可通行路径

#### 问题2：角色行为异常
- **原因**：空间记忆配置错误
- **解决**：检查 `spatial.tree` 配置是否与地图一致

#### 问题3：对话内容不合理
- **原因**：提示模板不适合新场景
- **解决**：修改 `data/prompts/` 中的相关模板

#### 问题4：LLM调用失败
- **原因**：API配置错误或网络问题
- **解决**：检查 `config.json` 中的API配置

### 4.3 性能优化

1. **减少角色数量**：测试时使用较少的角色
2. **调整思考间隔**：增加 `think.interval` 值
3. **优化记忆设置**：减少 `associate.retention` 天数
4. **使用本地模型**：配置Ollama本地部署

## 第五部分：最佳实践

### 5.1 场景设计原则

1. **层次清晰**：确保世界-区域-场所-对象的层次结构清晰
2. **路径连通**：所有重要区域都应该有可达路径
3. **功能完整**：包含生活、工作、娱乐等基本功能区域
4. **规模适中**：避免过大的地图影响性能

### 5.2 角色设计原则

1. **性格鲜明**：每个角色都有独特的性格特征
2. **背景合理**：角色的背景要与场景匹配
3. **行为一致**：角色的行为要符合其性格和背景
4. **关系网络**：角色间要有合理的社会关系

### 5.3 配置管理

1. **版本控制**：使用Git管理配置文件
2. **备份重要**：定期备份自定义配置
3. **文档记录**：记录修改内容和原因
4. **测试充分**：在正式使用前充分测试

## 总结

通过本指导文档，您可以：

1. **完全自定义地图**：创建任何主题的虚拟世界
2. **灵活配置角色**：设计符合场景需求的智能体
3. **调整行为模式**：通过提示模板定制角色行为
4. **多场景支持**：实现不同场景间的切换
5. **性能优化**：根据需求调整系统参数

Generative Agents 项目提供了强大的定制能力，支持创建各种主题的仿真场景。通过合理的设计和配置，可以创造出丰富多样的虚拟世界和智能体交互体验。

## 附录：配置文件模板

### 地图配置模板
```json
{
    "world": "场景名称",
    "tile_size": 32,
    "size": [宽度, 高度],
    "map": {
        "asset": "地图资源名",
        "tileset_groups": {
            "group_1": ["瓦片集1", "瓦片集2"]
        },
        "layers": [
            {"name": "图层名", "tileset_group": "group_1"}
        ],
        "tiles": []
    }
}
```

### 角色配置模板
```json
{
    "name": "角色名称",
    "portrait": "头像路径",
    "coord": [x, y],
    "currently": "当前状态描述",
    "scratch": {
        "age": 年龄,
        "innate": "内在性格",
        "learned": "背景描述", 
        "lifestyle": "生活习惯",
        "daily_plan": "日常计划"
    },
    "spatial": {
        "address": {
            "living_area": ["世界", "区域", "场所"]
        },
        "tree": {
            "世界名": {
                "区域名": {
                    "场所名": ["对象1", "对象2"]
                }
            }
        }
    }
}
```

通过遵循这些模板和指导原则，您可以成功创建和定制自己的Generative Agents仿真场景。

