---
name: duckdb-analytics
description: 用 DuckDB 对本地 CSV/TSV/Parquet/JSON 数据文件执行 SQL 查询与分析。当用户想查看数据文件结构、对本地表格数据做筛选/聚合/关联/统计，或练习 SQL 时使用。无需安装数据库服务器。
---

# DuckDB 数据分析

基于开源项目 [DuckDB](https://github.com/duckdb/duckdb)（进程内分析型 SQL 数据库），让用户在对话中直接对**本地数据文件**跑 SQL，无需安装任何数据库服务器。

## 何时使用

- 用户给出一个本地 CSV / TSV / Parquet / JSON / JSONL 文件，想做查询、筛选、聚合、统计
- 用户想练习 SQL（可以没有数据文件，直接用 SQL 造数）
- 用户问"这个数据文件有哪些列/多少行/分布如何"

## 怎么用

脚本位置：插件根目录下 `scripts/run_sql.py`，用 `python3`（受管 Python 运行时，已内置 duckdb）调用：

```bash
# 1. 看表结构 + 行数（拿到新数据文件的第一步）
python3 scripts/run_sql.py --data <文件路径> --describe

# 2. 跑 SQL：数据文件自动映射为视图 t（可用 --table 改名）
python3 scripts/run_sql.py --data <文件路径> --sql "SELECT * FROM t LIMIT 10"

# 3. 聚合分析示例
python3 scripts/run_sql.py --data sales.csv --sql "SELECT region, SUM(amount) AS total FROM t GROUP BY region ORDER BY total DESC"

# 4. 无数据文件也能练 SQL（DuckDB 内置函数造数）
python3 scripts/run_sql.py --sql "SELECT * FROM range(5)"

# 输出 CSV 而不是 Markdown 表格：加 --csv；调大行数：--limit 500
```

## 工作流程建议

1. **先 `--describe`**：确认列名和类型，再写 SQL，避免列名猜错。
2. SQL 里用视图名 `t` 引用数据文件；路径含空格时用引号包路径参数。
3. 结果默认 Markdown 表格、最多 100 行；需要完整导出时用 `--csv` 并重定向到文件。
4. SQL 报错时把错误信息如实展示给用户，并给出修正后的 SQL。

## 注意

- 只读操作：脚本不修改数据文件本身。
- 多文件关联：可多次执行或让用户把文件放同一目录，用 `read_csv_auto('dir/*.csv')` 之类 DuckDB 原生语法（写在 --sql 里即可，不走视图映射）。
- 数据口径：回答用户时说明结果基于哪个文件、哪条 SQL 得出。
