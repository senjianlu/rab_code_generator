# rab_code_generator
## 依赖
1. 依赖于 `rab_common` 模块的数据库连接。

## 配置片段
```toml
# 外部模块
[external]
  [external.rab_code_generator]
    [external.rab_code_generator.output]
      # 代码生成器的输出路径
      dir_path = "../generated_code"
```