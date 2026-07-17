# Pt(100) + CO — 怎么开干

工作笔记本：`Pt_CO_surface_study.ipynb`  
空白教学脚手架（对照用）：`Assignment_template.ipynb`

本环境**没有 CASTEP**。把笔记本拷到集群自己的主目录研究文件夹里跑。

## 上机前

1. 从 `classfiles` **复制**笔记本到 `~/…/pt_co_study/`（单独目录）
2. 打开 `Pt_CO_surface_study.ipynb`，在 Cell 1 填写 `NAME`、`USERNAME`
3. 确认 Part 0 三行 OK

## 推荐运行顺序

| 顺序 | 内容 | 产出文件 |
|---:|---|---|
| 1 | 1.1 截断能扫描 → 看图改 `CUTOFF` | `results_cutoff.txt` |
| 2 | 1.2 k 点扫描 → 改 `K_BULK` / slab 网格 | `results_kpoints.txt` |
| 3 | 1.3 优化 a₀ | `a0.txt`, `E_bulk_per_atom.txt` |
| 4 | 2.1 层数 → γ 图 → 改 `NL` | `results_layers.txt` |
| 5 | 2.3 真空 → 改 `VACUUM` | `results_vacuum.txt` |
| 6 | 3.1–3.2 CO 参考 + cutoff → **生产 cutoff=max(金属,CO)** | `results_reference.txt`, `results_ref_cutoff.txt` |
| 7 | **Part 4 重做**：clean → on-top → bridge → hollow（**每次只交 1 个**，16 核） | `results_clean_slab.txt`, `result_ads_*.txt`, `results_Eads.txt` |
| 8 | 量几何、填汇总表与讨论四题 | Part 5 |
| 9 | 扩展：6.1 势垒 → 6.2 ZPE → 6.3 B₀ → 6.5 覆盖度 → 6.4 Pt(111) | `results_diffusion.txt` 等 |

每个 `%%sbatch` 任务：墙时 4 h，分区 `aqmtcm`，Part 4 用 `-n 16`。几秒就结束 = 出错，看日志。

Part 4 使用新目录 `part4_clean` / `part4_ontop` / `part4_bridge` / `part4_hollow`，避开旧的 `*_final_850eV` / `.bak` 残留。

## 满分纪律

- 全程 **PBE** + 同一套生产 cutoff / k **线密度**
- ASE `fcc100`：**tag 1 = 顶面**，冻底部
- CO：**单重态**，`E_ref = E(CO)`
- 边算边写「做了什么 / 为什么」
- 扩展计分上限 +10，但尽量都做；先 6.1+6.2

## 提交

`~/submission/surface_study/`：

- 笔记本（含已保存输出）
- 全部 `results_*.txt` 与 `system.txt` / `settings.txt` / `a0.txt`
- 汇总表 + 讨论
