# 大数据专业学生 GitHub 开源项目清单

> 整理人：大三 · 大数据专业（数据库 / Python / C++ / AIGC 方向）
> 数据核实时间：2026-08-27，来源：GitHub REST API（star 数为查询时点真实值）

## 一、数据库方向

| 项目 | Star | 语言 | 简介 | 为什么值得学生用 |
|------|------|------|------|------------------|
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | 40,690 | C++ | 进程内分析型 SQL 数据库 | 免安装服务器，直接对 CSV/Parquet 跑 SQL，数据分析课设/实验神器；源码也是学 C++ 数据库内核的好材料 |
| [sqlite/sqlite](https://github.com/sqlite/sqlite) | 10,351 | C | 全球部署最广的嵌入式数据库 | 数据库课程必学，零配置，Python 内置 sqlite3 直接练手 |
| [apache/spark](https://github.com/apache/spark) | 43,881 | Scala | 大规模数据处理统一分析引擎 | 大数据专业课核心框架，PySpark 是求职高频技能点 |
| [redis/redis](https://github.com/redis/redis) | 76,116 | C | 内存键值数据库 | NoSQL 代表，缓存/排行榜/消息队列场景必备，源码注释质量极高 |
| [metabase/metabase](https://github.com/metabase/metabase) | 48,949 | Clojure | 开源 BI 与嵌入式分析工具 | 不写前端也能把 SQL 结果做成仪表盘，适合做数据分析课程展示 |

## 二、Python / 数据工程方向

| 项目 | Star | 语言 | 简介 | 为什么值得学生用 |
|------|------|------|------|------------------|
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | 49,564 | Python | Python 数据分析标准库 | 数据分析、机器学习预处理绕不开的基础 |
| [pola-rs/polars](https://github.com/pola-rs/polars) | 39,505 | Rust | Rust 编写的高性能 DataFrame 引擎 | 大数据量下比 pandas 快数倍，近年大厂面试常问的性能优化话题 |
| [apache/airflow](https://github.com/apache/airflow) | 46,615 | Python | 工作流编排调度平台 | 数据仓库/ETL 岗位核心工具，搭一个 DAG 项目写进简历很加分 |
| [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) | 13,698 | Rust | 用 SQL 做数据转换的工程化工具 | 数仓分层建模（ODS/DWD/DWS）的现代标准做法 |

## 三、C++ 方向

| 项目 | Star | 语言 | 简介 | 为什么值得学生用 |
|------|------|------|------|------------------|
| [cmu-db/bustub](https://github.com/cmu-db/bustub) | 5,066 | C++ | CMU 15-445 数据库系统课程教学项目 | 手写缓冲池/B+树/查询执行器，数据库内核方向最经典的练手项目 |
| [google/leveldb](https://github.com/google/leveldb) | 39,365 | C++ | Google 开源的高性能 KV 存储库 | LSM-Tree 存储引擎入门必读，代码量小（约 2 万行）适合通读 |
| [nlohmann/json](https://github.com/nlohmann/json) | 50,472 | C++ | 现代 C++ JSON 库 | 单头文件即插即用，C++ 项目处理数据交换格式的标配 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 125,832 | C++ | 纯 C/C++ 大模型推理引擎 | C++ 与 AIGC 的交叉点，能学量化/KV Cache/推理优化等硬核知识 |

## 四、AIGC 方向

| 项目 | Star | 语言 | 简介 | 为什么值得学生用 |
|------|------|------|------|------------------|
| [ollama/ollama](https://github.com/ollama/ollama) | 179,527 | Go | 一条命令在本地跑开源大模型 | 零门槛部署 DeepSeek/Qwen 等模型，做自己的 AI 应用底座 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 145,092 | Python | 智能体（Agent）工程化平台 | 做 RAG、Agent 课程项目的主流框架 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 164,482 | Python | 主流机器学习模型定义框架 | 调用 BERT/Qwen 等模型微调、推理的标准入口 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 130,182 | Python | 节点式扩散模型 GUI 与后端（原 comfyanonymous/ComfyUI） | AI 绘画工作流事实标准，适合做多模态方向的探索 |

## 五、已接入 Kimi 的项目

本清单中的 **DuckDB** 已被包装为 Kimi 本地插件（见 `kimi-plugin-duckdb-analytics/`），
可以在 Kimi 对话中直接用自然语言对本地 CSV 文件跑 SQL 分析，无需安装数据库。

## 使用建议（按学期节奏）

1. **本学期**：DuckDB + pandas 做数据分析课设；用 SQLite 过一遍 SQL 语法
2. **寒假**：BusTub 或 LevelDB 二选一精读源码，补 C++ 和存储内核
3. **大三下**：Airflow + dbt + Spark 搭一套迷你数仓项目（简历主项目）
4. **穿插**：Ollama + LangChain 做一个"用自然语言查自己课表/成绩库"的 RAG 小应用
