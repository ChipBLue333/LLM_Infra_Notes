# 第0阶段知识点总表（LLM推理框架/优化入门前）

| 模块 | 知识点 | 需要掌握到什么程度 | 为什么要学 | 学完后的自测标准 |
|---|---|---|---|---|
| 全景认知 | 训练 / 推理 / 部署 / Serving 的区别 | 能清楚区分四者的目标、流程和关注指标 | 避免把“会跑模型”误认为“理解推理系统” | 能解释：训练关注什么，推理关注什么，Serving又额外解决什么问题 |
| 全景认知 | 一次LLM请求的完整生命周期 | 能按顺序说出：输入、分词、prefill、decode、停止 | 后续所有框架本质上都在优化这条链路 | 能自己画出请求执行流程图 |
| 模型基础 | Token / Embedding / Hidden State | 知道文本如何变成模型输入，以及中间表示如何流动 | 不理解这些，后面就看不懂推理流程 | 能解释“模型为什么不能直接吃自然语言字符串” |
| 模型基础 | 自回归生成（Autoregressive Generation） | 理解模型为何是逐 token 生成，而不是一次生成整句 | 这是理解 decode 的前提 | 能解释“为什么大模型输出是一 token 一 token 产生的” |
| 模型基础 | Self-Attention 基本过程 | 知道 Q/K/V 的作用，以及 attention 依赖上下文 | 推理优化很多都围绕 attention 和 KV cache | 能解释“为什么上下文变长会让推理更难” |
| 模型基础 | Transformer推理最小流程 | 知道一层 Transformer 在推理时大致做什么 | 帮助你把 runtime 行为和模型结构对应起来 | 能口述“token经过一层大致经历了什么” |
| 推理核心 | Prefill 的定义 | 知道 prefill 是对整段 prompt 做首次前向计算 | 后续 TTFT、prefix cache、chunked prefill 都和它相关 | 能解释“prefill阶段到底在算什么” |
| 推理核心 | Decode 的定义 | 知道 decode 是每次生成一个新 token 的迭代过程 | 后续 TPOT、KV cache、调度优化都围绕它展开 | 能解释“decode为什么和prefill不是一回事” |
| 推理核心 | Prefill 和 Decode 的差异 | 能从输入规模、计算特点、访存特点、性能指标上比较两者 | 这是学习推理优化最重要的地基 | 能自己列一个 prefill vs decode 对比表 |
| 推理核心 | KV Cache 的作用 | 理解为什么缓存历史 K/V，缓存后节省了什么 | 这是大模型推理系统最核心概念之一 | 能解释“没有KV cache会怎样” |
| 推理核心 | KV Cache 的代价 | 理解 KV cache 会占显存、带来管理问题 | 后面看 paged KV、prefix cache 才不会停留在口号层面 | 能解释“为什么KV cache既重要又麻烦” |
| 推理核心 | 上下文长度对推理的影响 | 知道长上下文为什么会带来更高显存和访存压力 | 这决定很多优化的必要性 | 能解释“为什么长上下文比短上下文更难服务” |
| 指标体系 | TTFT（首token时延） | 理解它表示用户多久看到第一个输出 | 是用户体验最敏感的指标之一 | 能解释“TTFT高一般说明哪里可能有问题” |
| 指标体系 | TPOT（每输出token时间） | 理解它主要反映 decode 性能 | 是判断生成阶段快不快的关键指标 | 能解释“TPOT高更可能是哪个阶段的问题” |
| 指标体系 | Throughput（吞吐） | 知道 tokens/s、requests/s 的意义 | 后面比较框架时一定会看到 | 能解释“吞吐高为什么不一定代表用户体验最好” |
| 指标体系 | Latency（总时延） | 理解总时延由哪些部分组成 | 避免只盯一个指标看系统性能 | 能分解一次请求的总延迟构成 |
| 指标体系 | Memory Footprint（显存占用） | 知道显存主要花在权重和KV cache上 | 推理系统很多限制首先来自显存 | 能解释“为什么显存常常比算力更先成为瓶颈” |
| 性能分析 | Compute-bound | 知道什么时候是算力瓶颈 | 后续分析优化收益时的基础分类 | 能举例说明什么情况更像算力受限 |
| 性能分析 | Memory-bandwidth-bound | 知道什么时候是带宽瓶颈 | decode 常常和这个强相关 | 能解释“为什么decode常被说成更偏memory-bound” |
| 性能分析 | Memory-capacity-bound | 知道什么时候是显存容量瓶颈 | 长上下文、大batch时非常常见 | 能解释“OOM往往和哪些因素有关” |
| 性能分析 | Scheduling-bound | 知道调度不佳也会让系统慢 | 推理框架优化不只是 kernel 问题 | 能解释“GPU没吃满不一定是算子太慢，也可能是调度问题” |
| 性能分析 | Communication-bound | 知道多卡场景下通信也会成为瓶颈 | 为后续学习并行推理打基础 | 能理解“多卡不一定线性加速”的原因 |
| 方法论 | 瓶颈—机制—代价 分析法 | 对每个优化都能按这个模板分析 | 这是后续读框架/论文最有用的方法 | 能用该模板分析 KV cache / batching / quantization |
| 术语预热 | Batch / Batching | 知道什么是批处理以及为什么要做批处理 | 后续 continuous batching 会高频出现 | 能解释“batching解决了什么问题” |
| 术语预热 | Static Batching | 知道固定批处理的基本特点 | 作为 continuous batching 的对照组 | 能解释“为什么静态batch不适合在线场景” |
| 术语预热 | Continuous Batching | 先知道它是动态批处理思想 | 是现代推理框架的核心概念之一 | 能用一句话解释它和 static batching 的区别 |
| 术语预热 | Scheduler | 知道它负责请求组织与执行安排 | 后续看 runtime 时会反复碰到 | 能理解“推理框架里为什么需要调度器” |
| 术语预热 | Prefix Cache | 知道它和重复前缀复用有关 | 后续学习高复用 workload 优化时很重要 | 能解释“它和KV cache的关系是什么” |
| 术语预热 | Paged KV Cache | 先知道它是对KV cache的分页式管理思路 | 为后面学习vLLM打基础 | 能理解“为什么要对KV cache做分页管理” |
| 术语预热 | Quantization | 知道量化和精度-性能-显存之间的关系 | 后续量化优化离不开这层认知 | 能解释“量化通常想换来什么收益” |
| 术语预热 | Tensor Parallel / Pipeline Parallel | 先知道它们是多卡并行的两类基本思路 | 为后续多GPU推理学习铺路 | 能大致说出两者区别 |
| 术语预热 | Speculative Decoding | 先知道它是为了减少生成延迟的思路 | 后面会经常出现在推理优化资料里 | 至少能说出“它在优化哪类问题” |
| 术语预热 | Flash Attention | 先知道它是 attention 高效实现相关技术 | 后续理解 kernel 优化时会碰到 | 能知道它和“更高效attention计算”有关 |
| 学习产出 | 流程图 | 能画出完整推理请求流程 | 帮助形成系统视角 | 画出：prompt→tokenize→prefill→KV cache→decode→output |
| 学习产出 | 术语表 | 用自己的话写出核心术语解释 | 防止只是“眼熟”而不是“会说” | 至少能写出10~15个核心术语 |
| 学习产出 | 对比表 | 能整理训练vs推理、prefillvsdecode等对比 | 帮助建立结构化认知 | 能独立写出至少两张对比表 |
| 学习产出 | 自测问答 | 能口头讲清关键概念 | 检验是否真正理解 | 能不查资料回答5个核心问题 |


--------
| 资料 | 重点看什么 | 对应知识点 |
|---|---|---|
| HF Cache explanation | autoregressive generation、KV cache 为什么存在、为什么只用于 inference | 自回归生成、Self-Attention基本过程、KV Cache作用、训练vs推理 |
| HF Cache strategies | Dynamic/Static/Quantized cache、memory usage、offloading | KV Cache代价、Memory Footprint、Memory-capacity-bound、Quantization、瓶颈—机制—代价 |
| vLLM Overview / Design | PagedAttention、continuous batching、prefix caching、chunked prefill、speculative decoding | 请求生命周期、Prefill/Decode、Prefill vs Decode、Continuous Batching、Prefix Cache、Paged KV Cache、Scheduler术语预热 |
| vLLM Offline Inference | continuous batching、GPU utilization、tensor/pipeline parallelism | Throughput、Scheduler、Tensor Parallel、Pipeline Parallel |
| SGLang Overview | RadixAttention、prefix caching、multi-GPU parallelism | Prefix Cache、Scheduler、多GPU术语预热 |
| SGLang HiCache design | GPU/host/distributed storage三级缓存、prefix reuse | KV Cache系统理解、Memory Footprint、Memory-capacity-bound、缓存层次化思想 |
| TensorRT-LLM Overview | quantization、parallelism、KV cache transmission | Quantization、Communication-bound、Tensor/Pipeline Parallel、KV Cache系统视角 |