# 大数据从业者级 GitHub 开源项目清单

> 定位：从「学习用」升级到「生产用」——以下是互联网/数据团队真实部署在生产环境的项目。
> 适用人群：数据开发 / 数仓工程师 / 后端 C++ / AIGC 工程方向从业者。
> 数据核实时间：2026-08-27，来源：GitHub REST API（star 数为查询时点真实值）。

## 一、OLAP / 实时数仓（数据库方向的生产主力）

| 项目 | Star | 语言 | 生产场景 |
|------|------|------|----------|
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | 49,478 | C++ | 实时分析数据库，用户画像/报表/日志分析的事实标准，字节/腾讯/快手大规模在用 |
| [apache/doris](https://github.com/apache/doris) | 15,820 | C++ | 实时分析 + 混合检索，国产 OLAP 主力，湖仓一体与联邦查询场景 |
| [StarRocks/starrocks](https://github.com/StarRocks/starrocks) | 12,045 | Java | 亚秒级查询引擎，主键模型支持实时更新，替 Druid/Presto 的常见选择 |

**从业者要点**：三者的取舍（写入模型、Join 能力、物化视图）是数仓面试高频题；ClickHouse 源码是 C++ 数据库工程的标杆。

## 二、湖仓与流批（数据工程主链路）

| 项目 | Star | 语言 | 生产场景 |
|------|------|------|----------|
| [apache/iceberg](https://github.com/apache/iceberg) | 9,178 | Java | 湖仓表格式事实标准，Netflix/苹果在用，隐藏分区/时间旅行 |
| [delta-io/delta](https://github.com/delta-io/delta) | 8,960 | Scala | Databricks 主导的 Lakehouse 存储框架，Spark 生态首选 |
| [apache/hudi](https://github.com/apache/hudi) | 6,222 | Java | Upsert/删除/增量处理，CDC 入湖场景常用 |
| [apache/flink](https://github.com/apache/flink) | 26,294 | Java | 流处理事实标准，实时数仓/实时计算核心 |
| [apache/kafka](https://github.com/apache/kafka) | 33,633 | Java | 分布式事件流平台，数据管道的中枢神经 |
| [apache/pulsar](https://github.com/apache/pulsar) | 15,315 | Java | 存算分离的消息系统，多租户场景替 Kafka 的选项 |
| [apache/dolphinscheduler](https://github.com/apache/dolphinscheduler) | 14,447 | Java | 可视化 DAG 调度平台，国内数仓团队主流，比 Airflow 更贴国内实践 |
| [fivetran/great_expectations](https://github.com/fivetran/great_expectations) | 11,741 | Python | 数据质量校验框架（已迁移至 fivetran 名下），入仓前质量门禁 |
| [datahub-project/datahub](https://github.com/datahub-project/datahub) | 12,590 | Python | 数据与 AI 资产的元数据/血缘平台，数据治理标配 |

**从业者要点**：Kafka→Flink→Iceberg/Doris 是当前实时湖仓的经典链路；调度选型国内看 DolphinScheduler、海外看 Airflow。

## 三、Python 分布式计算

| 项目 | Star | 语言 | 生产场景 |
|------|------|------|----------|
| [ray-project/ray](https://github.com/ray-project/ray) | 43,616 | Python | AI 分布式计算引擎，大模型训练/推理编排底座（OpenAI 在用） |
| [dask/dask](https://github.com/dask/dask) | 13,897 | Python | 并行计算 + 任务调度，单机 pandas 代码平滑扩展到集群 |

## 四、C++ 基础设施（存储与性能工程）

| 项目 | Star | 语言 | 生产场景 |
|------|------|------|----------|
| [facebook/rocksdb](https://github.com/facebook/rocksdb) | 32,012 | C++ | 可嵌入持久 KV 存储（LevelDB 的生产级进化版），Flink/Kafka Streams 状态后端 |
| [apache/arrow](https://github.com/apache/arrow) | 17,064 | C++ | 列式内存格式与多语言工具箱，大数据组件间的"通用语"，DuckDB/Spark/Parquet 都依赖 |
| [simdjson/simdjson](https://github.com/simdjson/simdjson) | 24,199 | C++ | 每秒解析 GB 级 JSON（SIMD），Meta Velox 等引擎在用 |

**从业者要点**：C++ 方向的护城河在存储引擎与计算引擎——RocksDB（LSM 调优）和 Arrow（向量化/零拷贝）是两大必懂件。

## 五、AIGC 工程（推理、检索、应用框架）

| 项目 | Star | 语言 | 生产场景 |
|------|------|------|----------|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 90,188 | Python | 高吞吐 LLM 推理引擎（PagedAttention），生产部署大模型首选 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 45,817 | Go | 云原生向量数据库，大规模 RAG/推荐召回 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 34,215 | Rust | 高性能向量数据库，中小规模 RAG 的快速选择 |
| [langgenius/dify](https://github.com/langgenius/dify) | 153,635 | TypeScript | 可视化搭建 Agent 工作流与 RAG 管线，企业 LLM 应用落地平台 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 89,899 | TypeScript | MCP 官方服务器集合，给 AI 助手接数据库/文件系统/Git 的标准协议实现 |

**从业者要点**：AIGC 工程岗的三板斧 = vLLM（推理服务化）+ 向量库（RAG）+ MCP/Dify（应用编排）；MCP 协议正在成为 AI 工具接入的行业标准。

## 从业者 vs 学生版的关键差异

| 维度 | 学生版 | 从业者版（本清单） |
|------|--------|--------------------|
| 数据库 | SQLite/DuckDB 单机练手 | ClickHouse/Doris/StarRocks 分布式生产 |
| 存储 | 读源码理解原理 | RocksDB/Iceberg 调优与线上运维 |
| 计算 | pandas 单机 | Flink/Ray 分布式 |
| AIGC | Ollama 本地玩模型 | vLLM 高并发推理 + RAG 管线工程化 |

## 与上一版的关系

学生版清单（`github-开源项目清单.md`）仍然有效——学生版适合课设与入门，本清单面向实习/求职/工作场景。
本地已接入的 Kimi 插件 **DuckDB 数据分析** 在从业者场景同样适用：生产排查时经常需要对导出的 CSV/日志切片做临时 SQL 分析。
