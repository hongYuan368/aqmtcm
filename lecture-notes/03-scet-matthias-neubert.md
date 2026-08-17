# 软共线有效理论（SCET）课前预习讲义 — 面向 Matthias Neubert 教授课程 《SCET / Soft-Collinear Effective Theory》

*课前自学材料（简体中文，英文术语另列）*

> 本文由 LaTeX 课前讲义转换为 Markdown，可在 GitHub 直接阅读。公式已按 GitHub 渲染要求处理（独立公式块、常用宏已展开）。若仍有个别公式异常，请对照同目录 `.tex`。

> **摘要**
>
> 本讲义是为选修 Matthias Neubert 教授《软共线有效理论》（(Soft-Collinear Effective Theory)， 简称 SCET）课程的同学准备的**课前预习**材料。预设读者已经学过量子场论（正则量子化、 Feynman 规则、单圈重整化）与基本粒子物理，但**没有系统学习过 SCET**，也可能对 有效场论（(effective field theory), EFT）只有零散印象。
>
> 讲义的写法遵循三条原则：（一）从相对论运动学与 EFT 的一般思想出发，不假定读者已经熟悉 光锥坐标或标度计数；（二）**完整给出推导**，尤其是光锥坐标、模式（mode）标度赋值、 以及至少一个匹配／标度计数的算例，每一步都可以自己用纸笔复核；（三）强调**物理图像**， 即“为什么大对数会出现”“软与共线到底差在哪里”，而不是堆砌高级技巧。
>
> 所有英文专业术语在正文中首次出现时用括号标注，并在第 9 节汇总为英汉术语表。

# 导读：如何使用这份讲义

## 这份讲义想解决的问题

SCET 是一套用来处理**同时存在多个能量标度**、并且低能自由度**沿着光锥方向高度 不对称**的强相互作用过程的有效场论。它的技术门槛主要来自三件事：

1.  记号：光锥坐标、$n$ 与 $\bar n$ 参考向量、$p^+$／$p^-$／$p_\perp$、标签动量 （label momentum）与残余动量（residual momentum）。

2.  标度计数（power counting）：为什么共线夸克场是 $\mathcal O(\lambda)$、 共线胶子场的三个分量各自是 $\mathcal O(\lambda^2,1,\lambda)$。

3.  概念：$\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 的区别、软与共线的重叠（zero-bin）、 快度发散（rapidity divergence）。

如果第一节课就要同时消化这三样，多数人会卡在记号上而错过物理。因此本讲义把它们**拆开**： 第 1–4 节只用普通的四动量与 QCD Feynman 规则，把“为什么需要 SCET”讲清楚；第 5 节才引入光锥坐标；第 6 节做标度 计数；第 7 节才写下有效拉氏量。

## 建议的阅读路径

- **时间紧（约 2 小时）**：读第 2 节（多标度问题）、 第 5 节（光锥坐标，务必自己推一遍）、 第 6 节的表 2（模式标度表）、 第 9 节术语表、第 11 节听课重点。

- **时间充裕（约 6–8 小时）**：按顺序全读，并动手完成正文中标注的 **练习**。特别是第 3 节的 Fermi 理论匹配、 第 4 节的软胶子发射（eikonal）计算、 第 6 节的“按区域展开”（expansion by regions）算例。

- **只想补记号**：第 5 节 $+$ 附录 13 （Dirac 代数与光锥恒等式速查）。

## 符号约定

全篇采用自然单位 $\hbar=c=1$，度规 

$$
g^{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1),
  \qquad
  a\cdot b = a^0b^0-\boldsymbol{a}\cdot\boldsymbol{b} .
$$

 QCD 规范群为 $SU(N_c)$，$N_c=3$，$C_F=(N_c^2-1)/(2N_c)=4/3$，$C_A=N_c=3$， $T_F=1/2$，$n_f$ 为活跃味数。维数正规化取 $d=4-2\epsilon$，减除方案为 $\overline{\mathrm{MS}}$。 小参数一律记作 $\lambda\ll1$。字母 $n,\bar n$ 保留给光锥参考向量， $Q$ 表示过程的硬标度（hard scale）。

**注。**

本讲义中若某个系数只需要“量级”而不需要精确值，会明确写成 $\mathcal O(\cdot)$ 或 “$\sim$”；凡是给出确定数值系数的公式，都可以（并且建议）自己验算。 少数用于定向的文献编号见第 12 节，建议听课时以老师给出的版本为准。

# 预备知识：运动学、Feynman 规则、跑动耦合

本节把后面反复使用的基础工具集中复习一遍。已经很熟的同学可以只看 第 1.3 小节末尾的“大对数”讨论。

## 相对论运动学：不变量、快度、相空间

#### Mandelstam 变量。

对 $2\to2$ 过程 $p_1+p_2\to p_3+p_4$，定义 

$$
s=(p_1+p_2)^2,\qquad t=(p_1-p_3)^2,\qquad u=(p_1-p_4)^2,
  \qquad s+t+u=\sum_{i=1}^{4}m_i^2 .
$$

 在质心系（center-of-mass frame）中 $\sqrt s$ 就是总能量。对无质量粒子， $s=2p_1\cdot p_2$。整个 SCET 的出发点是：**一个过程往往同时含有大不变量 （如 $s\sim Q^2$）和小不变量（如某个喷注的不变质量平方 $m_J^2\ll Q^2$）**。

#### 快度与横动量。

取 $z$ 轴为束流／喷注轴，定义横动量 $\boldsymbol{p}_\perp=(p^1,p^2)$、$p_T=|\boldsymbol{p}_\perp|$，以及快度（rapidity） 

$$
y=\frac12\ln\frac{p^0+p^3}{p^0-p^3} .
$$

 沿 $z$ 轴的 Lorentz 推动（boost）参数 $\eta$ 作用为 

$$
y \;\longrightarrow\; y+\eta ,
  \qquad
  \boldsymbol{p}_\perp\;\longrightarrow\; \boldsymbol{p}_\perp.
$$

 即：**快度在纵向推动下只是平移，横动量不变**。这条性质是后面 “不同模式按快度分类”的根源；对无质量粒子，快度退化为伪快度 $\eta=-\ln\tan(\theta/2)$，其中 $\theta$ 是与 $z$ 轴的夹角。

小角度极限下（$\theta\ll1$） 

$$
\eta \simeq \ln\frac{2}{\theta}\;\longrightarrow\;+\infty ,
$$

 所以**共线极限就是快度发散的极限**。请记住这句话，它在第 4 与第 10 节还会回来。

#### 无质量两体相空间。

单粒子相空间元 

$$
\int\!\frac{d^3k}{(2\pi)^3 2E_k}
  =\int\!\frac{d^4k}{(2\pi)^4}\,2\pi\,\delta_+(k^2)
  =\frac{1}{(2\pi)^3}\int_0^\infty \frac{E_k\,dE_k}{2}
    \int_{-1}^{1}d\cos\theta\int_0^{2\pi}\!d\varphi ,
$$

 其中 $\delta_+$ 表示只取正能解。式 [eq:1ps] 在第 4.1 小节推导软胶子发射时会直接用到。

## QCD Feynman 规则回顾（分层次）

QCD 拉氏量（含规范固定项，Feynman 规范 $\xi=1$） 

$$
\mathcal L_{\rm QCD}
  =\bar\psi\,(i\not{D}-m)\,\psi
   -\frac14 G^a_{\mu\nu}G^{a\,\mu\nu}
   -\frac{1}{2\xi}\big(\partial^\mu A^a_\mu\big)^2
   +\mathcal L_{\rm ghost},
$$

 

$$
D_\mu=\partial_\mu-ig_s A^a_\mu t^a ,
  \qquad
  G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu
                +g_s f^{abc}A^b_\mu A^c_\nu .
$$

 本讲义使用 $D_\mu=\partial_\mu-ig_sA_\mu$ 的约定（$A_\mu\equiv A_\mu^a t^a$）。

按“听课时最常用”的顺序，把规则分成三层：

夸克传播子 $\dfrac{i(\not{p}+m)}{p^2-m^2+i0}$； 胶子传播子 $\dfrac{-i g^{\mu\nu}\delta^{ab}}{p^2+i0}$（Feynman 规范）； 夸克–胶子顶点 $ig_s\gamma^\mu t^a$。

三胶子、四胶子顶点；ghost 顶点；颜色因子恒等式 

$$
t^at^a=C_F\mathbf 1,\qquad
    \mathrm{Tr}[t^at^b]=T_F\delta^{ab},\qquad
    f^{acd}f^{bcd}=C_A\delta^{ab} .
$$

外线极化求和、$\gamma$ 矩阵迹技术、维数正规化中的 $\gamma^\mu\gamma_\mu=d$。SCET 会把这些量在光锥基底中重新组织， 见附录 13。

**要点。**

SCET 并不引入新的 Feynman 规则“魔法”：它的传播子与顶点都是 QCD 规则在 特定动量区域中的**展开结果**。所以只要熟练掌握第一层规则，加上 一次仔细的展开，就能自己推出 SCET 的 Feynman 规则（第 7.3 小节）。

## 重整化与跑动：大对数从哪里来

#### 跑动耦合。

维数正规化 $\overline{\mathrm{MS}}$ 方案中，强耦合 $\alpha_s(\mu)$ 满足 

$$
\frac{d\alpha_s(\mu)}{d\ln\mu}
  =-\frac{\beta_0}{2\pi}\alpha_s^2+\mathcal O(\alpha_s^3),
  \qquad
  \beta_0=11-\frac23 n_f .
$$

 积分一次（单圈） 

$$
\alpha_s(\mu)=\frac{\alpha_s(\mu_0)}
  {1+\dfrac{\beta_0\alpha_s(\mu_0)}{2\pi}\ln\dfrac{\mu}{\mu_0}} .
$$

 [eq:alphasrun] 的分母里出现了 $\alpha_s\ln(\mu/\mu_0)$：这就是最简单的 “**重整化群把一串对数重求和**”的例子——展开分母得到 $\alpha_s\sum_n\big(-\tfrac{\beta_0\alpha_s}{2\pi}L\big)^n$， 即把所有 $\alpha_s^{n+1}L^n$ 一次性收拢。

#### 反常量纲的作用。

更一般地，若某个（重整化后的）系数 $C(\mu)$ 满足 

$$
\frac{dC(\mu)}{d\ln\mu}=\gamma(\alpha_s)\,C(\mu),
$$

 则 

$$
C(\mu)=C(\mu_0)\,\exp\!\left[\int_{\ln\mu_0}^{\ln\mu}\!
  \gamma\big(\alpha_s(\mu')\big)\,d\ln\mu'\right].
$$

 把 $C(\mu_0)$ 在 $\mu_0\sim$（该系数的“自然标度”）处用固定阶 微扰论计算，再用 [eq:rgesol] 演化到我们真正需要的标度 $\mu$， 就得到**重求和**（resummation）的结果。这正是 SCET 的最终用途。

#### 两种对数：单对数与双对数。

上面 $\alpha_s^n L^n$ 的结构叫**单对数**（single logarithm）， 来自紫外／共线的一重发散。而在含有软与共线两类发散的过程中， 每阶 $\alpha_s$ 最多带来**两个**对数： 

$$
\text{幅度或截面} \;\sim\; \sum_n \alpha_s^n
  \big(c_{n,2n}L^{2n}+c_{n,2n-1}L^{2n-1}+\dots\big),
  \qquad L=\ln\frac{Q}{\mu_{\rm soft}} .
$$

 这类 $\alpha_s^nL^{2n}$ 称为**Sudakov 双对数**（Sudakov double logarithm）。 当 $\alpha_sL^2\sim1$ 时固定阶微扰论彻底失效，即使 $\alpha_s\ll1$。

**要点。**

一句话总结整门课的动机：**当过程中出现层级化的标度 $Q\gg\mu_1\gg\mu_2\gg\dots$ 时，固定阶微扰论里会出现 $\alpha_s^nL^{2n}$； SCET 的作用是把每个标度装进一个独立的因子（硬函数、喷注函数、软函数）， 让每个因子在自己的自然标度上无大对数，再用重整化群把它们连接起来。**

**练习。**

用 [eq:beta] 验证 [eq:alphasrun]；再证明用 $\mu^2$ 作变量时 $d\alpha_s/d\ln\mu^2=-\beta_0\alpha_s^2/(4\pi)$。注意区分 $\ln\mu$ 与 $\ln\mu^2$ 的约定，SCET 文献中两者都常见，差一个因子 2 是最常见的低级错误。

# 散射运动学与多标度问题：为什么需要有效理论

## 一个具体的“坏”例子：$e^+e^-\to$ 喷注的 thrust 分布

考虑 $e^+e^-$ 在质心能量 $Q$ 上湮灭产生强子。定义 thrust（thrust） 

$$
T=\max_{\boldsymbol{n}}\frac{\sum_i|\boldsymbol{p}_i\cdot\boldsymbol{n}|}{\sum_i|\boldsymbol{p}_i|},
  \qquad \tau\equiv 1-T .
$$

 $\tau\to0$ 对应两个极窄的背对背喷注（back-to-back jets）， $\tau$ 越大事件越“胖”。在双喷注极限下有一个很有用的等价表述 

$$
\tau\;\simeq\;\frac{m_L^2+m_R^2}{Q^2},
$$

 其中 $m_{L,R}$ 是把事件按 thrust 轴分成两个半球后各半球的总不变质量。

用固定阶 QCD 计算 $\mathcal O(\alpha_s)$ 的 thrust 分布，在 $\tau\to0$ 的 奇异部分（singular part）为 

$$
\frac{1}{\sigma_0}\frac{d\sigma}{d\tau}
  \;\xrightarrow[\ \tau\to0\ ]{}\;
  \frac{\alpha_sC_F}{2\pi}\,\frac{1}{\tau}
  \Big(-4\ln\tau-3\Big)+\dots
$$

 （$\sigma_0$ 为 Born 截面，$\dots$ 表示 $\tau\to0$ 时不奇异的项与 $\delta(\tau)$ 项）。 把它累积起来： 

$$
\frac{\sigma(\tau)}{\sigma_0}
  =\int_0^\tau\! d\tau'\,\frac{1}{\sigma_0}\frac{d\sigma}{d\tau'}
  =1+\frac{\alpha_sC_F}{2\pi}\Big(-2\ln^2\tau-3\ln\tau\Big)+\mathcal O(\alpha_s^2).
$$

[eq:thrustcumul] 就是 [eq:doublelogs] 的具体实现： 系数是 $\alpha_s\ln^2\tau$。取 $Q=m_Z\simeq91\,$GeV、$\alpha_s\simeq0.12$， 当 $\tau\sim10^{-3}$ 时 $\alpha_s\ln^2\tau\sim0.12\times(6.9)^2/(2\pi)\times\tfrac43\times2\approx 2$， 微扰级数已经不收敛。而实验上恰恰是小 $\tau$ 区域统计量最大、最适合精确测 $\alpha_s$。这就是必须重求和的现实压力。

## 标度层级：一个过程里到底有几个标度

回到 [eq:thrusthemisphere]。在双喷注构型下：

- 两个喷注的**总能量**是 $\mathcal O(Q)$——这是**硬标度** （hard scale）。

- 每个喷注的不变质量满足 $m_J^2\sim \tau Q^2$，即 $m_J\sim Q\sqrt\tau$——这是**喷注标度**（jet scale）。

- 喷注之间大角度交换的软辐射，其能量 $\sim Q\tau$——这是 **软标度**（soft scale）。因为半球质量 $m^2 \supset 2E_{\rm jet}\,k^0(1-\cos\theta)\sim Q\,k^0$， 要贡献 $m^2\sim\tau Q^2$ 就需要 $k^0\sim\tau Q$。

于是 

$$
\boxed{\;Q\;\gg\;Q\sqrt\tau\;\gg\;Q\tau\;}
  \qquad(\tau\ll1),
$$

 三个标度呈等比层级。表 1 列出若干常见过程的标度层级。

| 过程 / 可观测量                          | 硬标度 | 中间（共线）标度                   | 软标度                   |
|:-----------------------------------------|:-------|:-----------------------------------|:-------------------------|
| $e^+e^-\to$ 2 jets, thrust $\tau$        | $Q$    | $Q\sqrt\tau$                       | $Q\tau$                  |
| DIS，$x\to1$                             | $Q$    | $Q\sqrt{1-x}$                      | $Q(1-x)$                 |
| $B\to X_s\gamma$ 端点区                  | $m_b$  | $\sqrt{m_b\Lambda_{\mathrm{QCD}}}$ | $\Lambda_{\mathrm{QCD}}$ |
| Drell–Yan，小 $q_T$                      | $Q$    | $\sqrt{Q q_T}$ 或 $q_T$            | $q_T$                    |
| $B\to\pi\ell\nu$（$\mathrm{SCET}_{II}$） | $m_b$  | $\Lambda_{\mathrm{QCD}}$           | $\Lambda_{\mathrm{QCD}}$ |

几个典型过程中的标度层级。$\lambda$ 为 SCET 展开小参数； $\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 的区别见第 6.3 小节。

## 为什么“直接算”不行

有人会问：既然固定阶 QCD 原则上给出正确答案，为什么不多算几阶？三个理由：

1.  **收敛性**：如上所述，$\alpha_sL^2\sim1$ 时每一阶都同等重要， 加阶数不解决问题，必须**对全部阶重求和**。

2.  **结构性**：重求和需要知道对数系数的**全阶结构**。 EFT 提供的因子化定理（factorization theorem）恰恰把这个结构 变成“每个因子满足一个重整化群方程”，从而可以指数化。

3.  **非微扰输入**：当软标度降到 $\Lambda_{\mathrm{QCD}}$ 附近时，软函数 不再是微扰量。EFT 给出**清晰的算符定义**，让非微扰部分 被隔离成一个普适的、可以从实验或格点提取的对象 （如形状函数 (shape function)、光锥分布振幅 (light-cone distribution amplitude)）。

**要点。**

EFT 的价值不只是“算得更准”，更重要的是**把不同标度的物理分离成独立、 可分别定义、可分别计算或测量的对象**。这一点在第 3 节展开。

**练习。**

由 [eq:thrustfixed] 出发验证 [eq:thrustcumul] （提示：$\int_0^\tau d\tau'\,(-4\ln\tau'-3)/\tau'$ 在 $\tau'\to0$ 端点发散， 需要与 $\delta(\tau)$ 处的虚修正相加才有限；这正是“加号分布” (plus distribution) 的用途，见第 10 节第 [item:plusdist] 条）。

# 有效场论总览：积分掉重模、匹配、Wilson 系数

## EFT 的三步法

任何一个有效场论的构造都可以概括为三步：

1.  **识别自由度与展开参数**。写下在所关心的能量区域里**仍然 动力学活跃**的场，以及被“积分掉”（integrated out）的重自由度， 确定小参数（$\lambda=$ 轻标度／重标度）。

2.  **写下最一般的有效拉氏量**。按 $\lambda$ 的幂次组织算符， 只受对称性约束： 

$$
\mathcal L_{\rm eff}=\sum_{k}\sum_{i} C_i^{(k)}(\mu)\,
              \frac{O_i^{(k)}}{M^{k}} .
$$

 算符 $O_i$ 只含轻自由度；重物理全部藏进系数 $C_i$。

3.  **匹配（matching）与跑动**。在某个标度 $\mu\sim M$ 处要求 全理论与有效理论的（在轻标度上展开后的）$S$ 矩阵元 **逐阶相等**，解出 Wilson 系数（Wilson coefficient）$C_i(\mu\sim M)$； 再用重整化群把 $C_i$ 演化到 $\mu\sim$ 轻标度。

**要点。**

匹配的本质：**全理论与有效理论的紫外行为不同，但红外行为必须相同**。 两者之差只含短距离信息，因此是 $\Lambda_{\mathrm{QCD}}$ 或轻标度的解析函数，可以吸收进 局域算符的系数。这句话在 SCET 中依然成立，只不过“局域”要放宽为 “沿光锥方向非局域”（见第 7 节）。

## 范例一：Fermi 理论的完整匹配（含推导）

这是最干净的匹配算例，请务必自己推一遍。考虑 $b\to c\bar u d$ 的树图， 由 $W$ 玻色子交换给出。全理论振幅： 

$$
i\mathcal M_{\rm full}
  =\left(\frac{-ig}{2\sqrt2}\right)^2 V_{cb}V_{ud}^*
  \Big[\bar u_c\gamma^\mu(1-\gamma_5)u_b\Big]
  \Big[\bar u_d\gamma^\nu(1-\gamma_5)u_u\Big]
  \frac{-i\left(g_{\mu\nu}-\dfrac{q_\mu q_\nu}{M_W^2}\right)}{q^2-M_W^2} ,
$$

 其中 $q$ 是 $W$ 传递的动量，$q^2\sim m_b^2\ll M_W^2$。

#### 展开传播子。

这是“积分掉重模”的字面含义： 

$$
\frac{1}{q^2-M_W^2}
  =-\frac{1}{M_W^2}\cdot\frac{1}{1-q^2/M_W^2}
  =-\frac{1}{M_W^2}\left(1+\frac{q^2}{M_W^2}+\frac{q^4}{M_W^4}+\dots\right).
$$

 注意 $q_\mu q_\nu/M_W^2$ 项在与流收缩后给出正比于夸克质量的贡献 （用运动方程 $\not{q}\to m$），也被 $1/M_W^2$ 压低。保留领头项： 

$$
i\mathcal M_{\rm full}
  = -i\,\frac{g^2}{8M_W^2}\,V_{cb}V_{ud}^*
    \Big[\bar u_c\gamma^\mu(1-\gamma_5)u_b\Big]
    \Big[\bar u_d\gamma_\mu(1-\gamma_5)u_u\Big]
    +\mathcal O\!\left(\frac{q^2}{M_W^4}\right).
$$

#### 有效理论一侧。

低能理论中不再有 $W$ 场，只有四费米子局域算符 

$$
\mathcal L_{\rm eff}
  =-\frac{4G_F}{\sqrt2}V_{cb}V_{ud}^*\,
   \Big[C_1(\mu)\,O_1+C_2(\mu)\,O_2\Big]+\text{h.c.}+\mathcal O(1/M_W^4),
$$

 

$$
O_1=\big[\bar c\,\gamma^\mu P_L\, b\big]\big[\bar d\,\gamma_\mu P_L\, u\big],
  \qquad
  O_2=\big[\bar c\,\gamma^\mu P_L\, u\big]\big[\bar d\,\gamma_\mu P_L\, b\big],
  \qquad P_L=\frac{1-\gamma_5}{2}.
$$

 （$O_2$ 是 $O_1$ 的“颜色重排”版本，树图上不产生，单圈胶子交换后必须引入。）

#### 匹配条件。

比较 [eq:fullexpanded] 与 [eq:lefffermi] 的树级矩阵元，得到 

$$
\boxed{\;\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}\;},
  \qquad
  C_1(\mu\!\sim\! M_W)=1+\mathcal O(\alpha_s),
  \qquad
  C_2(\mu\!\sim\! M_W)=0+\mathcal O(\alpha_s).
$$

#### 跑动。

到 $\mathcal O(\alpha_s)$，$O_{1,2}$ 会**混合**， 其 Wilson 系数满足矩阵形式的重整化群方程 

$$
\frac{d}{d\ln\mu}\begin{pmatrix}C_1\\C_2\end{pmatrix}
  =\hat\gamma^{T}(\alpha_s)\begin{pmatrix}C_1\\C_2\end{pmatrix},
  \qquad
  \hat\gamma=\frac{\alpha_s}{4\pi}
  \begin{pmatrix}-6/N_c & 6\\ 6 & -6/N_c\end{pmatrix}+\mathcal O(\alpha_s^2).
$$

 （转置位置与 $\ln\mu$ 对 $\ln\mu^2$ 的归一化各家约定不同， 使用时请核对来源。）把 $C_i$ 从 $\mu=M_W$ 演化到 $\mu=m_b$， 就把所有 $\alpha_s^n\ln^n(M_W/m_b)$ 重求和了。

**要点。**

Fermi 理论示范了 EFT 的全部要素，但它只有**单对数** $\alpha_s^n\ln^n(M_W/m_b)$：这是因为被积掉的重模与保留的轻模在**虚度** （virtuality）上一刀两断，红外结构简单。SCET 的困难在于低能理论里 **同时存在几种虚度／快度都不同的轻模**，从而出现双对数。

## 范例二：HQET —— 场的重新定义与标度赋值的预演

重夸克有效理论（(Heavy Quark Effective Theory), HQET）是 SCET 的直接前身， Neubert 本人是该领域的奠基者之一，课上极可能作为类比反复引用。

重夸克动量分解为“大部分 $+$ 残余”： 

$$
p^\mu = m_Q\, v^\mu + k^\mu ,
  \qquad v^2=1,\qquad k^\mu\sim\Lambda_{\mathrm{QCD}}\ll m_Q .
$$

 定义把快速振荡相位剥离后的场 

$$
h_v(x)=e^{\,i m_Q v\cdot x}\,\frac{1+\not{v}}{2}\,Q(x),
  \qquad \not{v}\equiv v_\mu\gamma^\mu ,
$$

 则领头阶拉氏量为 

$$
\mathcal L_{\rm HQET}
  =\bar h_v\,(i v\cdot D)\,h_v
   +\frac{1}{2m_Q}\Big[\bar h_v (iD_\perp)^2 h_v
   +\frac{c_{\rm mag}(\mu)}{2}\,\bar h_v\, g_s\sigma_{\mu\nu}G^{\mu\nu} h_v\Big]
   +\mathcal O\!\left(\frac{1}{m_Q^2}\right).
$$

请注意其中三个将在 SCET 里原封不动复用的思想：

1.  **相位剥离**：$e^{imv\cdot x}$ 把“大动量”变成场的**标签**， 剩下的场只携带小动量 $k$。SCET 的标签动量（label momentum） 就是这个想法的推广。

2.  **投影算符**：$(1+\not{v})/2$ 只保留粒子解，把反粒子（大分量）积掉。 SCET 中对应的是光锥投影 $\not{n}\not{\bar{n}}/4$。

3.  **按 $1/m$ 展开的算符阶梯**：领头阶极简，高阶项系数需要匹配。 SCET 中的展开参数是 $\lambda$，结构完全类似。

**练习。**

从 QCD 的 $\bar Q(i\not{D}-m_Q)Q$ 出发，代入 $Q(x)=e^{-im_Qv\cdot x}\big[h_v(x)+H_v(x)\big]$， 其中 $H_v=e^{im_Qv\cdot x}\tfrac{1-\not{v}}{2}Q$， 用 $H_v$ 的运动方程消去 $H_v$，验证 [eq:lhqet] 的前两项。 这个练习与第 7.2 小节把 SCET 拉氏量推出来的步骤**一模一样**， 先做它会让后面轻松很多。

# 软极限与共线极限：物理图像与奇异性来源

本节回答一个关键问题：**QCD 振幅在什么情况下发散，发散来自哪个传播子？** 答案有两个（也只有两个，这是 QCD 的红外结构定理内容）： **软**（soft）与**共线**（collinear）。

## 软极限与 eikonal 近似（完整推导）

设有一个硬过程，其中有一条出射的无质量夸克线，动量 $p$（$p^2=0$）。 现在从这条腿上发射一个软胶子，动量 $k$、颜色 $a$、极化 $\varepsilon$， 且 $k^\mu\to0$。修改后的振幅为 

$$
\mathcal M^{\mu}
  =\bar u(p)\,\big(ig_s\gamma^\mu t^a\big)\,
   \frac{i\big(\not{p}+\not{k}\big)}{(p+k)^2+i0}\,\Gamma\,\big|\dots\big\rangle ,
$$

 其中 $\Gamma$ 代表硬过程其余部分。分母： 

$$
(p+k)^2=p^2+2p\cdot k+k^2=2p\cdot k+k^2\;\xrightarrow[\ k\to0\ ]{}\;2p\cdot k .
$$

 分子用 Dirac 代数处理。利用 $\gamma^\mu\not{p}=2p^\mu-\not{p}\gamma^\mu$ 与外线运动方程 $\bar u(p)\not{p}=0$： 

$$
\begin{aligned}
  \bar u(p)\,\gamma^\mu(\not{p}+\not{k})
  &=\bar u(p)\big(2p^\mu-\not{p}\gamma^\mu\big)+\bar u(p)\gamma^\mu\not{k}
   \notag\\
  &=2p^\mu\,\bar u(p)+\underbrace{\bar u(p)\gamma^\mu\not{k}}_{\mathcal O(k)} .
  
\end{aligned}
$$

 在 $k\to0$ 下第二项相对第一项被压低一个 $k$ 的幂次，可以丢掉。于是 

$$
\boxed{\;
  \mathcal M^\mu \;\simeq\;
  g_s\,t^a\,\frac{p^\mu}{p\cdot k}\;\mathcal M_0\;}
$$

 （$\mathcal M_0$ 为不发射软胶子的振幅）。这就是**eikonal 近似** （(eikonal approximation)，也叫 soft approximation）。

**注。**

[eq:eikonal] 的物理含义极其重要：软胶子**完全看不见**发射它的粒子的 自旋，也看不见硬过程的内部结构，只“看到”粒子的**方向与颜色荷**。 这就是为什么软辐射可以用 Wilson 线（Wilson line）——即经典色荷沿直线运动 产生的规范场——来完整描述。$p^\mu/(p\cdot k)$ 正是 Wilson 线的 Feynman 规则。

## 软发射给出双对数：显式计算

现在把 [eq:eikonal] 用于 $e^+e^-\to q\bar q$ 加一个软胶子。 取质心系 

$$
p_1=E(1,0,0,1),\qquad p_2=E(1,0,0,-1),\qquad Q=2E ,
$$

 

$$
k=E_k\big(1,\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta\big).
$$

 两条腿都可以发射，总 eikonal 电流为 $J^\mu=g_st^a\big(\frac{p_1^\mu}{p_1\cdot k}-\frac{p_2^\mu}{p_2\cdot k}\big)$ （相对符号来自出射夸克与出射反夸克的色荷相反）。对极化与颜色求和： 

$$
\begin{aligned}
  \sum_{\rm pol,col}|J|^2
  &= g_s^2\,C_F\left[-\left(\frac{p_1}{p_1\cdot k}-\frac{p_2}{p_2\cdot k}\right)^2\right]
   = g_s^2\,C_F\,\frac{2\,p_1\cdot p_2}{(p_1\cdot k)(p_2\cdot k)} ,
  
\end{aligned}
$$

 这里用了 $p_{1,2}^2=0$。代入运动学： 

$$
p_1\cdot k=E E_k(1-\cos\theta),\qquad
  p_2\cdot k=E E_k(1+\cos\theta),\qquad
  2p_1\cdot p_2=4E^2 ,
$$

 

$$
\Rightarrow\quad
  \frac{2p_1\cdot p_2}{(p_1\cdot k)(p_2\cdot k)}
  =\frac{4E^2}{E^2E_k^2(1-\cos^2\theta)}
  =\frac{4}{E_k^2\sin^2\theta} .
$$

 配上相空间 [eq:1ps]： 

$$
\begin{aligned}
  \frac{d\sigma}{\sigma_0}
  &= g_s^2C_F\,\frac{1}{(2\pi)^3}\,\frac{E_k\,dE_k}{2}\,
     d\cos\theta\, d\varphi\;\frac{4}{E_k^2\sin^2\theta}
   \notag\\
  &= \frac{4\pi\alpha_s\,C_F\cdot 4}{2(2\pi)^3}\,
     \frac{dE_k}{E_k}\,\frac{d\cos\theta}{\sin^2\theta}\,d\varphi
   \notag\\
  &= \frac{2\alpha_sC_F}{\pi}\,\frac{dE_k}{E_k}\,
     \frac{d\cos\theta}{\sin^2\theta} ,
  
\end{aligned}
$$

 最后一步用了 $g_s^2=4\pi\alpha_s$ 与 $\int_0^{2\pi}d\varphi=2\pi$。

现在读出奇异性。在 $\theta\to0$ 附近 $|d\cos\theta|=\sin\theta\,d\theta$、$\sin^2\theta\simeq\theta^2$，所以 

$$
\boxed{\;
  \frac{d\sigma}{\sigma_0}\;\simeq\;
  \frac{2\alpha_sC_F}{\pi}\,\frac{dE_k}{E_k}\,\frac{d\theta}{\theta}\;}
  \qquad(\theta\to0\ \text{或}\ \theta\to\pi).
$$

两个独立的对数发散清清楚楚：

- $dE_k/E_k$：**软发散**（soft divergence），来自 $E_k\to0$，即 [eq:eikonal] 分母中的 $p\cdot k\to0$ 因为 $k\to0$。

- $d\theta/\theta$：**共线发散**（collinear divergence），来自 $\theta\to0$，即 $p\cdot k\to0$ 因为 $k$ 与 $p$ 平行 （即便 $E_k$ 不小！）。

若把积分限设为 $\mu_{\rm IR}<E_k<Q$、$\theta_0<\theta<1$，则 

$$
\frac{\Delta\sigma}{\sigma_0}\sim
  \frac{2\alpha_sC_F}{\pi}\ln\frac{Q}{\mu_{\rm IR}}\ln\frac{1}{\theta_0}
  \;\sim\;\alpha_sL^2 .
$$

 这就是 [eq:doublelogs] 与 [eq:thrustcumul] 中双对数的来源： **一个来自能量，一个来自角度（等价地：快度）**。

**要点。**

**双对数 $=$ 软（能量）对数 $\times$ 共线（角度／快度）对数。** SCET 的全部结构，本质上都是为了把这两类对数分别装进 “软函数”与“喷注函数”，从而各自只含单一标度。

## 共线极限与分裂函数

共线发散也可以在**不取软极限**的情况下单独看到。设 $p$ 分裂为 两个近共线的动量 $p_1=z p+\dots$、$p_2=(1-z)p+\dots$， 则中间传播子的虚度为 

$$
(p_1+p_2)^2 \simeq \frac{\boldsymbol{k}_\perp^2}{z(1-z)} ,
$$

 其中 $\boldsymbol{k}_\perp$ 是相对横动量。$\boldsymbol{k}_\perp\to0$ 时传播子发散，且 $z$ 保持有限。 积掉这个区域给出著名的 Altarelli–Parisi 分裂函数（splitting function）： 

$$
d\sigma_{n+1}\simeq d\sigma_n\,\frac{\alpha_s}{2\pi}\,
  \frac{d\boldsymbol{k}_\perp^2}{\boldsymbol{k}_\perp^2}\,dz\;P_{ji}(z),
$$

 

$$
P_{qq}(z)=C_F\,\frac{1+z^2}{1-z},\qquad
  P_{gq}(z)=C_F\,\frac{1+(1-z)^2}{z},\qquad
  P_{gg}(z)=2C_A\!\left[\frac{z}{1-z}+\frac{1-z}{z}+z(1-z)\right].
$$

 注意 $P_{qq}(z)$ 在 $z\to1$ 时还有一个 $1/(1-z)$ 的极点——那正是 **软**极限，它同时是共线的：这就是软与共线区域的**重叠** （overlap），在 SCET 里必须小心处理（(zero-bin subtraction)， 见第 10 节）。

## 奇异性的来源：一句话总结

回顾一下 [eq:softamp1]–[eq:splitvirt]，所有红外奇异性都来自 **某个内线传播子的分母趋于零**： 

$$
\frac{1}{(p+k)^2}=\frac{1}{2p\cdot k}
  =\frac{1}{2E_pE_k(1-\cos\theta_{pk})} \;\to\;\infty
  \quad\Longleftrightarrow\quad
  \underbrace{E_k\to0}_{\text{软}}
  \ \ \text{或}\ \
  \underbrace{\theta_{pk}\to0}_{\text{共线}} .
$$

**注（KLN 与 IR 安全）。**

对足够“包含性”（inclusive）的可观测量，实发射与虚修正的红外发散 互相抵消（Kinoshita–Lee–Nauenberg 定理），末态截面有限。但**留下的 不是零，而是大对数**——因为可观测量本身（如 $\tau$）给出了一个截断。 换句话说：**测量行为把红外发散转化为对数增强**， 而这些对数的比值标度正是表 1 中列出的那些。

**练习。**

用 [eq:eikonal] 证明式 [eq:eiksq] 中的等式 $-\big(\frac{p_1}{p_1\cdot k}-\frac{p_2}{p_2\cdot k}\big)^2
=\frac{2p_1\cdot p_2}{(p_1\cdot k)(p_2\cdot k)}$， 并说明为什么必须用 $\sum_{\rm pol}\varepsilon^\mu\varepsilon^{*\nu}\to-g^{\mu\nu}$ 才是合法的（提示：eikonal 电流守恒 $k\cdot J=0$）。

# 光锥坐标：完整引入与四动量分解

第 4 节告诉我们，红外奇异性有两个来源：能量与角度。 普通的 Cartesian 分量 $(p^0,p^1,p^2,p^3)$ 把这两者混在一起。 **光锥坐标**（light-cone coordinates）的全部意义就是： 用一组坐标把“沿喷注方向的大分量”“逆喷注方向的小分量”“横向分量”**彼此分开**， 使标度层级一眼可见。本节从零开始建立这套记号，请一定动手验算每一步。

## 两个光锥参考向量

**定义（光锥基底）。**

选取两个类光（light-like）向量 $n^\mu$ 与 $\bar n^\mu$，满足 

$$
n^2=\bar n^2=0,
  \qquad
  n\cdot\bar n=2 .
$$

最常用的具体选择是沿 $z$ 轴： 

$$
n^\mu=(1,0,0,1),
  \qquad
  \bar n^\mu=(1,0,0,-1).
$$

 验证：$n^2=1-1=0$；$\bar n^2=1-1=0$； $n\cdot\bar n=1\cdot1-(1)(-1)=1+1=2$。$\checkmark$

**注。**

归一化 $n\cdot\bar n=2$ 是 SCET 文献（含 Becher–Neubert 一系）的通用约定。 有些文献用 $n\cdot\bar n=1$ 并在 $n^\mu=\frac{1}{\sqrt2}(1,0,0,1)$， 这会让所有分解式里的 $1/2$ 变成 $1/\sqrt2$ 之类。 **上课第一件事就是确认老师用的归一化**，否则后面每个式子都差因子 2。

## 四动量的光锥分解（推导）

**命题（光锥分解）。**

对任意四动量 $p^\mu$， 

$$
\boxed{\;
  p^\mu=(n\cdot p)\,\frac{\bar n^\mu}{2}
        +(\bar n\cdot p)\,\frac{n^\mu}{2}
        +p_\perp^\mu \;}
$$

 其中 $p_\perp^\mu$ 满足 $n\cdot p_\perp=\bar n\cdot p_\perp=0$。

**证明。**

先证 [eq:lcdecomp] 是恒等式。定义 $r^\mu\equiv p^\mu-(n\cdot p)\frac{\bar n^\mu}{2}-(\bar n\cdot p)\frac{n^\mu}{2}$， 只需证明 $r$ 与 $n,\bar n$ 都正交。用 $n_\mu$ 收缩： 

$$
n\cdot r
  = n\cdot p-(n\cdot p)\frac{n\cdot\bar n}{2}-(\bar n\cdot p)\frac{n^2}{2}
  = n\cdot p-(n\cdot p)\cdot\frac{2}{2}-0
  = 0 .
$$

 同理用 $\bar n_\mu$ 收缩： 

$$
\bar n\cdot r
  = \bar n\cdot p-(n\cdot p)\frac{\bar n^2}{2}-(\bar n\cdot p)\frac{n\cdot\bar n}{2}
  = \bar n\cdot p-0-\bar n\cdot p=0 .
$$

 所以 $r^\mu\equiv p_\perp^\mu$ 确实横向。

**定义（光锥分量与记号）。**

定义 

$$
p^+\equiv n\cdot p,
  \qquad
  p^-\equiv \bar n\cdot p,
  \qquad
  p_\perp^\mu ,
$$

 并把一个四动量简写为三元组 

$$
p \;=\; \big(p^+,\,p^-,\,p_\perp\big)
  \;=\;\big(n\cdot p,\ \bar n\cdot p,\ p_\perp\big).
$$

**注（约定警告）。**

文献中至少有三套互相冲突的习惯： (i) $p^\pm=n\cdot p,\ \bar n\cdot p$（本讲义与 Becher–Neubert）； (ii) $p^\pm=(p^0\pm p^3)/\sqrt2$（弦论／老式光锥量子化）； (iii) 三元组按 $(p^-,p^+,p_\perp)$ 排序。 本讲义固定用 [eq:triple]，即**第一个分量是小的、第二个是大的** （对 $n$-共线动量而言）。

用 [eq:nexplicit] 时具体地 

$$
p^+=p^0-p^3,
  \qquad
  p^-=p^0+p^3,
  \qquad
  p_\perp=(0,p^1,p^2,0).
$$

 反解 

$$
p^0=\frac{p^++p^-}{2},\qquad p^3=\frac{p^--p^+}{2}.
$$

## 不变量、快度、体积元

#### （1）不变质量。

把 [eq:lcdecomp] 平方： 

$$
\begin{aligned}
  p^2
  &=\left[(n\cdot p)\frac{\bar n}{2}+(\bar n\cdot p)\frac{n}{2}+p_\perp\right]^2
   \notag\\
  &=\underbrace{(n\cdot p)^2\frac{\bar n^2}{4}}_{=0}
   +\underbrace{(\bar n\cdot p)^2\frac{n^2}{4}}_{=0}
   +2\,(n\cdot p)(\bar n\cdot p)\frac{n\cdot\bar n}{4}
   +p_\perp^2
   \notag\\
  &=(n\cdot p)(\bar n\cdot p)+p_\perp^2 ,
\end{aligned}
$$

 即 

$$
\boxed{\;p^2=p^+p^-+p_\perp^2=p^+p^--\boldsymbol{p}_\perp^2\;}
$$

 （$p_\perp$ 是类空的，$p_\perp^2=-\boldsymbol{p}_\perp^2\le0$，$\boldsymbol{p}_\perp$ 为二维欧氏矢量）。

[eq:psq] 是全课程最重要的公式之一。它说：**虚度 $p^2$ 是 一个“大分量 $\times$ 小分量”减去“横动量平方”**。所以一个粒子可以有巨大的 能量却几乎在质量壳上，只要 $p^+$ 足够小。

无质量在壳条件 $p^2=0$ 给出 

$$
p^+=\frac{\boldsymbol{p}_\perp^2}{p^-} .
$$

#### （2）两个动量的点积。

对 $p,k$ 用 [eq:lcdecomp]： 

$$
\boxed{\;
  p\cdot k=\frac12\big(p^+k^-+p^-k^+\big)+p_\perp\!\cdot\! k_\perp
  =\frac12\big(p^+k^-+p^-k^+\big)-\boldsymbol{p}_\perp\!\cdot\!\boldsymbol{k}_\perp\;}
$$

**证明。**

交叉项： $2\times\big[(n\cdot p)\frac{\bar n}{2}\big]\cdot\big[(\bar n\cdot k)\frac{n}{2}\big]
=\frac{2}{4}(n\cdot p)(\bar n\cdot k)(n\cdot\bar n)=(n\cdot p)(\bar n\cdot k)$； 但要注意组合系数：完整展开为 $\frac{1}{4}\big[(n\!\cdot\!p)(\bar n\!\cdot\!k)+(\bar n\!\cdot\!p)(n\!\cdot\!k)\big](n\!\cdot\!\bar n)
=\frac12\big[p^+k^-+p^-k^+\big]$，再加 $p_\perp\cdot k_\perp$。

#### （3）快度。

由 [eq:rapidity] 与 [eq:pmexplicit]， 

$$
y=\frac12\ln\frac{p^0+p^3}{p^0-p^3}=\frac12\ln\frac{p^-}{p^+}
  \qquad\Longleftrightarrow\qquad
  \frac{p^-}{p^+}=e^{2y} .
$$

 沿 $z$ 轴以快度 $\eta$ 推动时（$y\to y+\eta$，$\boldsymbol{p}_\perp$ 不变）， 由 [eq:yratio] 与 $p^+p^-=p^2+\boldsymbol{p}_\perp^2$ 不变，得到 

$$
\boxed{\;p^-\to e^{\eta}p^-,\qquad p^+\to e^{-\eta}p^+,\qquad p_\perp\to p_\perp\;}
$$

 即：**纵向推动在光锥坐标下是对角的——只是把 $p^\pm$ 各自乘一个因子。** 这是光锥坐标最深刻的优点，也是“不同模式按快度分类”这句话的技术基础。

#### （4）四维体积元。

由 [eq:inverse] 计算 Jacobi 行列式： 

$$
\frac{\partial(p^0,p^3)}{\partial(p^+,p^-)}
  =\det\begin{pmatrix}
    \partial p^0/\partial p^+ & \partial p^0/\partial p^-\
$$

2pt]
    \partial p^3/\partial p^+ & \partial p^3/\partial p^-
  \end{pmatrix}
  =\det\begin{pmatrix} 1/2 & 1/2\\ -1/2 & 1/2\end{pmatrix}
  =\frac14+\frac14=\frac12 ,

$$
所以
$$

\boxed{\;d^4p=\frac12\,dp^+\,dp^-\,d^2p_\perp\;}
  

$$
#### （5）横向度规。

定义
$$

g_\perp^{\mu\nu}\equiv g^{\mu\nu}-\frac{n^\mu\bar n^\nu+\bar n^\mu n^\nu}{2} .
  

$$
它满足（自己验算）
$$

n_\mu g_\perp^{\mu\nu}=\bar n_\mu g_\perp^{\mu\nu}=0,
  \qquad
  g_\perp^{\mu\nu}g_{\perp\,\nu\rho}=g^{\mu}_{\perp\,\rho},
  \qquad
  g_{\perp\,\mu}^{\ \ \mu}=d-2 .
  

$$
第一式的验算： $n_\mu g^{\mu\nu}-\frac{n^2\bar n^\nu+(n\cdot\bar n)n^\nu}{2}
=n^\nu-\frac{0+2n^\nu}{2}=0$。$\checkmark$ 迹：$d-\frac{2(n\cdot\bar n)}{2}=d-2$，在 $d=4$ 时为 2， 正是两个横向维度。$\checkmark$

## 小角度与横动量：$\lambda$ 的几何意义

设一个无质量粒子与 $n$ 方向（$+z$）夹角 $\theta\ll1$，能量 $E$。则
$$

p^-=p^0+p^3=E(1+\cos\theta)\simeq 2E,
  \qquad
  p^+=E(1-\cos\theta)\simeq \frac{E\theta^2}{2},
  \qquad
  |\boldsymbol{p}_\perp|=E\sin\theta\simeq E\theta .

$$
于是
$$

\big(p^+,p^-,p_\perp\big)
  \;\sim\; E\left(\frac{\theta^2}{2},\,2,\,\theta\right)
  \;\sim\; Q\left(\lambda^2,\,1,\,\lambda\right),
  \qquad
  \boxed{\;\lambda\sim\theta\;}
  

$$
（取 $Q\sim E$）。

**要点。**

**$\lambda$ 就是喷注的张角（opening angle）。** 一个夹角 $\theta\sim\lambda$ 的共线粒子，其三个光锥分量自然地按 $(\lambda^2,1,\lambda)$ 层级排列，虚度 $p^2\sim Q^2\lambda^2$。 式 [eq:lambdatheta] 是整个 SCET 标度计数的**几何起点**， 不是人为假设。

## Dirac 代数的光锥投影（推导）

定义
$$

P_n\equiv\frac{\not{n}\not{\bar{n}}}{4},
  \qquad
  P_{\bar n}\equiv\frac{\not{\bar{n}}\not{n}}{4} .
  

$$
**命题。**

$P_n,P_{\bar n}$ 是一对完备的正交幂等投影算符：
$$

P_n+P_{\bar n}=\mathbf 1,
  \qquad
  P_n^2=P_n,
  \qquad
  P_{\bar n}^2=P_{\bar n},
  \qquad
  P_nP_{\bar n}=P_{\bar n}P_n=0 .

$$
**证明。**

基本关系（由 $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ 与 [eq:nnbar]）：
$$

\not{n}\not{n}=n^2=0,
  \qquad
  \not{\bar{n}}\not{\bar{n}}=\bar n^2=0,
  \qquad
  \not{n}\not{\bar{n}}+\not{\bar{n}}\not{n}=2\,n\cdot\bar n=4 .
  

$$
完备性：$P_n+P_{\bar n}=\frac{\not{n}\not{\bar{n}}+\not{\bar{n}}\not{n}}{4}=\frac44=\mathbf1$。$\checkmark$

幂等性：由 [eq:nalg] 有 $\not{\bar{n}}\not{n}=4-\not{n}\not{\bar{n}}$，故
$$

\begin{aligned}
  16\,P_n^2=\not{n}\not{\bar{n}}\,\not{n}\not{\bar{n}}
  =\not{n}\big(4-\not{n}\not{\bar{n}}\big)\not{\bar{n}}
  =4\,\not{n}\not{\bar{n}}-\underbrace{\not{n}\not{n}}_{=0}\not{\bar{n}}\not{\bar{n}}
  =4\,\not{n}\not{\bar{n}},
\end{aligned}

$$
即 $P_n^2=\frac{\not{n}\not{\bar{n}}}{4}=P_n$。$\checkmark$（$P_{\bar n}$ 同理。） 正交性由完备与幂等自动成立： $P_nP_{\bar n}=P_n(\mathbf1-P_n)=P_n-P_n^2=0$。

另外两条在推导拉氏量时必用的关系：
$$

\gamma_\perp^\mu\,\not{n}=-\not{n}\,\gamma_\perp^\mu,
  \qquad
  \gamma_\perp^\mu\,\not{\bar{n}}=-\not{\bar{n}}\,\gamma_\perp^\mu ,
  

$$
因为 $\{\gamma_\perp^\mu,\not{n}\}=2n^\mu_\perp=0$（$n$ 没有横向分量）。 由此立即得到
$$

P_n\,\gamma_\perp^\mu=\gamma_\perp^\mu\,P_{\bar n},
  \qquad
  P_{\bar n}\,\gamma_\perp^\mu=\gamma_\perp^\mu\,P_{n} ,
  

$$
即**横向 $\gamma$ 矩阵把“大分量”翻转成“小分量”**。

最后，任意 $\gamma^\mu$ 的光锥分解为
$$

\not{D}=\not{n}\,\frac{\bar n\cdot D}{2}+\not{\bar{n}}\,\frac{n\cdot D}{2}+\not{D}_\perp ,
  

$$
这直接由 [eq:lcdecomp] 收缩 $\gamma_\mu$ 得到（注意 $\bar n$ 与 $n$ 的**互换**： $n\cdot D$ 配的是 $\not{\bar{n}}$）。

**练习。**

 (a) 验证 $\mathrm{Tr}[\not{n}\not{\bar{n}}]=8$。 (b) 证明 $\not{n}\gamma^\mu\not{n}=2n^\mu\not{n}$。 (c) 对 $n$-共线动量 $p\sim Q(\lambda^2,1,\lambda)$，用 [eq:slashdecomp] 说明 $\not{p}$ 的三项分别是 $\mathcal O(1),\mathcal O(\lambda^2),\mathcal O(\lambda)$ ——注意 $\not{n}\frac{\bar n\cdot p}{2}$ 才是领头项。 (d) 写出 $p_\perp^\mu=g_\perp^{\mu\nu}p_\nu$ 并验证 $p_\perp\cdot n=0$。

# Power counting：给动量模式赋标度

现在我们有了记号，可以做 SCET 真正的技术核心：**标度计数**。

## 什么是“模式”

**定义（动量模式）。**

在一个含小参数 $\lambda$ 的过程中，一个**模式**（mode）指的是 Feynman 积分中一个（在 $\lambda\to0$ 下）自洽的动量区域，其光锥分量 $(p^+,p^-,p_\perp)$ 相对于硬标度 $Q$ 有确定的 $\lambda$ 幂次。 每个模式在 EFT 中对应一个独立的场。

哪些模式出现，**不是先验给定的**，而是由（i）外态运动学与 （ii）**所测量的可观测量**共同决定。找出它们的系统方法叫 **按区域展开**（(expansion by regions)，又称 (strategy of regions)，Beneke–Smirnov）。

## 标准模式表

以 $n$ 方向为“喷注方向”，$\bar n$ 为反方向，最常见的模式如表 2。

| 模式（英文）                                                 | 标度 $(p^+,p^-,p_\perp)$           | 虚度 $p^2$                 | 出现于                                 |
|:-------------------------------------------------------------|:-----------------------------------|:---------------------------|:---------------------------------------|
| 硬 (hard)                       | $Q(1,1,1)$                         | $Q^2$                      | 被积掉 $\to$ Wilson 系数               |
| $n$-共线 (collinear)            | $Q(\lambda^2,1,\lambda)$           | $Q^2\lambda^2$             | $\mathrm{SCET}_{I},\mathrm{SCET}_{II}$ |
| $\bar n$-共线 (anti-collinear)  | $Q(1,\lambda^2,\lambda)$           | $Q^2\lambda^2$             | $\mathrm{SCET}_{I},\mathrm{SCET}_{II}$ |
| 超软 (ultrasoft)                | $Q(\lambda^2,\lambda^2,\lambda^2)$ | $Q^2\lambda^4$             | $\mathrm{SCET}_{I}$                    |
| 软 (soft)                       | $Q(\lambda,\lambda,\lambda)$       | $Q^2\lambda^2$             | $\mathrm{SCET}_{II}$                   |
| （附加）硬共线 (hard-collinear) | $Q(\lambda^2,1,\lambda)$           | $Q^2\lambda^2$             | $\mathrm{SCET}_{I}$ 中共线模的别名     |
| （附加）Glauber                                              | $Q(\lambda^2,\lambda^2,\lambda)$   | $Q^2\lambda^2$（横向主导） | 前向散射／强子对撞                     |

SCET 的标准动量模式。第 2 列为 $(p^+,p^-,p_\perp)=(n\cdot p,\bar n\cdot p,p_\perp)$ 以 $Q$ 为单位的标度。

**注。**

表中“硬共线”只是 $\mathrm{SCET}_{I}$ 语境下对共线模的称呼（因为它的虚度 $Q^2\lambda^2$ 比超软的 $Q^2\lambda^4$ 大得多，属于“较硬”的一类）。 Glauber 模式是高阶／前向物理的话题，第一堂课一般不涉及， 但值得知道它的存在——它是“朴素因子化”会失效的地方之一。

## 关键观察：虚度 vs. 快度

把表 2 画到 $(\ln p^+,\ln p^-)$ 平面上（这是听 SCET 课时 最有用的一张图，建议自己画）：

- **虚度**对应 $\ln p^++\ln p^-$（因为 $p^2\simeq p^+p^-$）， 即图上的“反对角线”。

- **快度**对应 $\ln p^--\ln p^+$（由 [eq:yratio]）， 即图上的“对角线”。

于是：

- 在 $\mathrm{SCET}_{I}$ 中，共线（$Q^2\lambda^2$）与超软（$Q^2\lambda^4$） **虚度不同**，可以用普通的 $\overline{\mathrm{MS}}$ 维数正规化 $+$ $\mu$ 依赖 彼此分开。$\Longrightarrow$ 只需要一个正规化子。

- 在 $\mathrm{SCET}_{II}$ 中，共线与软**虚度相同**（都是 $Q^2\lambda^2$）， 只有**快度不同**。维数正规化对快度积分无能为力，于是出现 **快度发散**（rapidity divergence），需要额外的正规化子 与相应的“快度重整化群”／**共线异常**（collinear anomaly）。

**要点。**

**$\mathrm{SCET}_{I}$ vs. $\mathrm{SCET}_{II}$ 的唯一本质区别就在这里**： 低能模式是靠虚度分开的（$\mathrm{SCET}_{I}$），还是虚度相同、只靠快度分开的（$\mathrm{SCET}_{II}$）。 这是全课程最重要的概念分水岭。Becher–Neubert 的“共线异常”正是处理后者的框架。

## 完整算例：按区域展开与 $1/\epsilon$ 极点的抵消

下面这个算例**可以完全解析求解**，因此是检验“按区域展开”思想最好的 练兵场。它体现了 SCET 里几乎所有技术特征：区域分解、无标度积分为零、 不同区域的 $1/\epsilon$ 极点互相抵消、大对数从标度比值中出现。

考虑（带解析正规化子 $\epsilon$ 的）单参数积分
$$

I(\epsilon)=\int_0^\infty\! dx\;
  \frac{x^{-\epsilon}}{(x+m^2)(x+Q^2)},
  \qquad m^2\ll Q^2 .
  

$$
把 $x$ 想成一个圈动量的虚度，$m^2$ 想成红外标度，$Q^2$ 想成硬标度。

#### 精确结果（$\epsilon\to0$）。
$$

I(0)=\int_0^\infty\!\frac{dx}{(x+m^2)(x+Q^2)}
  =\frac{1}{Q^2-m^2}\ln\frac{Q^2}{m^2}
  \;\xrightarrow[\ m^2\ll Q^2\ ]{}\;
  \frac{1}{Q^2}\ln\frac{Q^2}{m^2}
  \Big[1+\mathcal O\!\big(m^2/Q^2\big)\Big].
  

$$
（用部分分式 $\frac{1}{(x+m^2)(x+Q^2)}
=\frac{1}{Q^2-m^2}\big[\frac{1}{x+m^2}-\frac{1}{x+Q^2}\big]$ 即得。） 注意结果里有一个 $\ln(Q^2/m^2)$：**这就是“大对数”**。 我们的目标是理解它来自哪些区域。

#### 硬区域（$x\sim Q^2$）。

此时 $m^2\ll x$，展开
$$

\frac{1}{x+m^2}=\frac1x\left(1-\frac{m^2}{x}+\dots\right).

$$
领头项：
$$

I_h=\int_0^\infty\! dx\,\frac{x^{-1-\epsilon}}{x+Q^2} .

$$
用标准公式 $\int_0^\infty dx\,\frac{x^{a-1}}{(x+A)^b}=A^{a-b}\,\frac{\Gamma(a)\Gamma(b-a)}{\Gamma(b)}$， 取 $a=-\epsilon$、$b=1$、$A=Q^2$：
$$

I_h=(Q^2)^{-1-\epsilon}\,\Gamma(-\epsilon)\Gamma(1+\epsilon)
     =-\frac{1}{\epsilon}\,(Q^2)^{-1-\epsilon}\,
      \underbrace{\Gamma(1-\epsilon)\Gamma(1+\epsilon)}_{\displaystyle \equiv G(\epsilon)} ,
  

$$
最后一步用了 $\Gamma(-\epsilon)=-\Gamma(1-\epsilon)/\epsilon$。

#### 软（低能）区域（$x\sim m^2$）。

此时 $x\ll Q^2$，展开
$$

\frac{1}{x+Q^2}=\frac{1}{Q^2}\left(1-\frac{x}{Q^2}+\dots\right).

$$
领头项：
$$

I_s=\frac{1}{Q^2}\int_0^\infty\! dx\,\frac{x^{-\epsilon}}{x+m^2}
     =\frac{(m^2)^{-\epsilon}}{Q^2}\,\Gamma(1-\epsilon)\Gamma(\epsilon)
     =+\frac{1}{\epsilon}\,\frac{(m^2)^{-\epsilon}}{Q^2}\,G(\epsilon) ,
  

$$
这里 $a=1-\epsilon$、$b=1$、$A=m^2$，且 $\Gamma(\epsilon)=\Gamma(1+\epsilon)/\epsilon$。

#### 相加。
$$

\begin{aligned}
  I_h+I_s
  &=\frac{G(\epsilon)}{\epsilon\,Q^2}
    \Big[(m^2)^{-\epsilon}-(Q^2)^{-\epsilon}\Big]
   \notag\\
  &=\frac{G(\epsilon)}{\epsilon\,Q^2}
    \Big[\big(1-\epsilon\ln m^2+\mathcal O(\epsilon^2)\big)
        -\big(1-\epsilon\ln Q^2+\mathcal O(\epsilon^2)\big)\Big]
   \notag\\
  &=\frac{G(\epsilon)}{\epsilon\,Q^2}\,
    \epsilon\ln\frac{Q^2}{m^2}+\mathcal O(\epsilon)
   \notag\\
  &=\frac{1}{Q^2}\ln\frac{Q^2}{m^2}+\mathcal O(\epsilon).
  
\end{aligned}

$$
与精确结果 [eq:exact] 的领头幂次**完全一致**。$\checkmark$

从这个五行的计算里，请提取以下四条教训，它们**逐条对应** SCET 中的真实现象：

1.  **单个区域是发散的，总和是有限的。** $I_h\sim-1/\epsilon$、$I_s\sim+1/\epsilon$，极点互相抵消。 在 SCET 中，这正是“硬函数的 IR 极点 $=$ 低能矩阵元的 UV 极点（反号）”， 也就是**匹配是 IR 有限的**这一断言的技术内容。

2.  **每个区域只依赖一个标度。** $I_h$ 只含 $Q^2$，$I_s$ 只含 $m^2$， 所以每个区域里**没有大对数**。 大对数只在两者相加时，从 $(m^2)^{-\epsilon}-(Q^2)^{-\epsilon}$ 的 $\epsilon$ 展开中产生。**这就是因子化能实现重求和的机制。**

3.  **正规化子是必需的。**若一开始取 $\epsilon=0$ 再分区域， $I_h=\int dx\,x^{-1}/(x+Q^2)$ 在 $x\to0$ 处对数发散——但那个区域 本来不属于硬区域。正规化子把这种“越界”变成 $1/\epsilon$ 极点， 使其能与另一个区域的相应极点抵消。 在 $\mathrm{SCET}_{II}$ 中，维数正规化对某些越界（快度方向）无效， 于是必须引入额外的快度正规化子。

4.  **无标度积分为零。**在维数正规化中， $\int_0^\infty dx\,x^{-1-\epsilon}=0$（无任何标度可依赖）。 这条规则在 SCET 里天天用到，也是**零区间减除** （zero-bin subtraction）为什么常常“看起来什么都没做”却很重要的原因。

**练习。**

把 [eq:regint] 的下一阶幂次修正算出来： 在硬区域取 $-m^2\!\int_0^\infty dx\,x^{-2-\epsilon}/(x+Q^2)$， 在软区域取 $-\frac{1}{Q^4}\!\int_0^\infty dx\,x^{1-\epsilon}/(x+m^2)$， 证明两者之和给出 [eq:exact] 展开的 $\mathcal O(m^2/Q^4)$ 项。 这一练习示范了 SCET 的**幂次修正**（power correction）如何系统化。

## 场的标度：从作用量出发（完整推导）

现在推导 SCET 中**场**的标度。原则只有一条：
$$

\boxed{\;\text{每个模式的领头阶动能项作用量必须是 }\mathcal O(\lambda^0)\;}
  

$$
理由是动能项定义传播子，其归一化不能带 $\lambda$ 的幂次。

#### 第一步：坐标的标度。

由 [eq:dotprod]，相位 $p\cdot x$ 中 $p^-x^+$、$p^+x^-$、$\boldsymbol{p}_\perp\!\cdot\!\boldsymbol{x}_\perp$ 各自必须是 $\mathcal O(1)$ 才不会被快速振荡抹掉。对 $n$-共线动量 $p_c\sim Q(\lambda^2,1,\lambda)$：
$$

x^+\sim\frac{1}{p^-}\sim\frac1Q,
  \qquad
  x^-\sim\frac{1}{p^+}\sim\frac{1}{Q\lambda^2},
  \qquad
  x_\perp\sim\frac{1}{|\boldsymbol{p}_\perp|}\sim\frac{1}{Q\lambda} .

$$
即 $x_c\sim\frac1Q(1,\lambda^{-2},\lambda^{-1})$，注意与动量**反向**排序。 由 [eq:volume]
$$

d^4x_c=\frac12dx^+dx^-d^2x_\perp
  \sim\frac1Q\cdot\frac{1}{Q\lambda^2}\cdot\frac{1}{Q^2\lambda^2}
  =\frac{1}{Q^4\lambda^4}
  \qquad\Longrightarrow\qquad
  d^4x_c\sim\lambda^{-4} .
  

$$
#### 第二步：共线夸克场。

第 7.2 小节将证明领头阶共线拉氏量为
$$

\mathcal L_c=\bar\xi_n\left[i\,n\cdot D
  +i\not{D}_\perp\frac{1}{i\,\bar n\cdot D}\,i\not{D}_\perp\right]
  \frac{\not{\bar{n}}}{2}\,\xi_n .
  

$$
其中每个导数按对应动量分量标度：
$$

i\,n\cdot D\sim n\cdot p_c\sim Q\lambda^2,
  \qquad
  i\,\bar n\cdot D\sim Q\lambda^0,
  \qquad
  iD_\perp\sim Q\lambda .

$$
所以方括号中**两项同阶**：
$$

i\,n\cdot D\sim\lambda^2,
  \qquad
  i\not{D}_\perp\frac{1}{i\bar n\cdot D}i\not{D}_\perp
  \sim\frac{\lambda\cdot\lambda}{1}=\lambda^2 .
  

$$
（这个“恰好同阶”不是巧合，而是 [eq:onshell] 的在壳条件 $p^+=\boldsymbol{p}_\perp^2/p^-$ 的算符版本。）故 $\mathcal L_c\sim\lambda^2\,\bar\xi_n\xi_n$， 代入 [eq:actionrule] 与 [eq:d4xc]：
$$

S_c=\int\! d^4x_c\,\mathcal L_c
  \sim\lambda^{-4}\cdot\lambda^2\cdot\bar\xi_n\xi_n
  \stackrel{!}{=}\lambda^0
  \qquad\Longrightarrow\qquad
  \bar\xi_n\xi_n\sim\lambda^2
  \qquad\Longrightarrow\qquad
  \boxed{\;\xi_n\sim\lambda\;}
  

$$
#### 第三步：共线胶子场。

规范不变性要求 $D_\mu=\partial_\mu-ig_sA_\mu$ 中的两项同阶， 即 $A_c^\mu$ 必须与 $\partial^\mu$（也就是 $p_c^\mu$）同标度**逐分量**相同：
$$

\boxed{\;
  \big(n\cdot A_c,\ \bar n\cdot A_c,\ A_{c\perp}\big)
  \sim Q\big(\lambda^2,\ 1,\ \lambda\big)\;}
  

$$
以 $Q$ 为单位即 $(\lambda^2,1,\lambda)$。请**独立地**用胶子动能项交叉检验： 场强张量的横向–横向分量
$$

F_c^{\perp\perp}\sim\partial_\perp A_\perp\sim\lambda\cdot\lambda=\lambda^2,

$$
而 $+-$ 分量
$$

F_c^{+-}\sim \bar n\cdot\partial\;(n\cdot A_c)\sim 1\cdot\lambda^2=\lambda^2 ,

$$
两者一致，都给 $F_c\sim\lambda^2$。于是
$$

S_c^{\rm gluon}\sim\int d^4x_c\,(F_c)^2\sim\lambda^{-4}\cdot\lambda^4=\lambda^0 .
  \checkmark

$$
**标度赋值自洽**——这是检查自己有没有算错的最好办法： 同一个场的标度必须能从多个不同的项推出相同答案。

#### 第四步：超软场（$\mathrm{SCET}_{I}$）。

$p_{us}\sim Q(\lambda^2,\lambda^2,\lambda^2)$，故 $x_{us}\sim\frac{1}{Q\lambda^2}(1,1,1)$，
$$

d^4x_{us}\sim\lambda^{-8} .

$$
胶子：$A_{us}^\mu\sim\partial_{us}^\mu\sim\lambda^2$， $F_{us}\sim\lambda^2\cdot\lambda^2=\lambda^4$， $S\sim\lambda^{-8}\lambda^8=\lambda^0$。$\checkmark$ 夸克：$\mathcal L=\bar q_{us}\,i\not{D}_{us}\,q_{us}\sim\lambda^2\,\bar q_{us}q_{us}$，
$$

\lambda^{-8}\cdot\lambda^2\cdot\bar q_{us}q_{us}\stackrel{!}{=}\lambda^0
  \quad\Longrightarrow\quad
  \bar q_{us}q_{us}\sim\lambda^6
  \quad\Longrightarrow\quad
  \boxed{\;q_{us}\sim\lambda^3\;}

$$
#### 第五步：软场（$\mathrm{SCET}_{II}$）。

$p_{s}\sim Q(\lambda,\lambda,\lambda)$，故 $d^4x_s\sim\lambda^{-4}$， $A_s^\mu\sim\lambda$，$F_s\sim\lambda^2$， $S\sim\lambda^{-4}\lambda^4=\lambda^0$ $\checkmark$；夸克：
$$

\lambda^{-4}\cdot\lambda\cdot\bar q_sq_s\stackrel{!}{=}\lambda^0
  \quad\Longrightarrow\quad
  \bar q_sq_s\sim\lambda^3
  \quad\Longrightarrow\quad
  \boxed{\;q_{s}\sim\lambda^{3/2}\;}

$$
结果汇总于表 3。

| 对象                                                     | 标度                    | 来源                                                                                                    |
|:---------------------------------------------------------|:------------------------|:--------------------------------------------------------------------------------------------------------|
| $d^4x$（共线）                                           | $\lambda^{-4}$          | 式 [eq:d4xc]                |
| $d^4x$（超软）                                           | $\lambda^{-8}$          | 同法                                                                                                    |
| $d^4x$（软）                                             | $\lambda^{-4}$          | 同法                                                                                                    |
| 共线夸克 $\xi_n$                                         | $\lambda$               | 式 [eq:xiscaling] |
| 共线胶子 $(n\!\cdot\!A_c,\bar n\!\cdot\!A_c,A_{c\perp})$ | $(\lambda^2,1,\lambda)$ | 式 [eq:Acscaling] |
| 超软夸克 $q_{us}$                                        | $\lambda^3$             | 第四步                                                                                                  |
| 超软胶子 $A_{us}^\mu$                                    | $\lambda^2$             | 第四步                                                                                                  |
| 软夸克 $q_{s}$                                           | $\lambda^{3/2}$         | 第五步                                                                                                  |
| 软胶子 $A_{s}^\mu$                                       | $\lambda$               | 第五步                                                                                                  |
| $\mathcal L^{(0)}$（共线）                               | $\lambda^{4}$           | $\lambda^{-4}$ 的倒数                                                                                   |

SCET 中场与算符的 $\lambda$ 标度（领头阶）。

**要点。**

表 3 是 SCET 的“乘法表”。有了它，任何算符的 $\lambda$ 阶数都可以**数出来**，从而回答“哪些算符属于领头幂次 （leading power）”这个问题——这才是 EFT 的真正威力： **它告诉你哪些项可以忽略，以及忽略造成的误差有多大。**

## 推论：超软胶子为什么只通过 $n\cdot A_{us}$ 耦合

表 3 立刻给出 $\mathrm{SCET}_{I}$ 的一条核心结论。把共线拉氏量 [eq:Lcprev] 中的协变导数写成共线场与超软场之和，
$$

D_\mu = \partial_\mu - i g_s\big(A_{c\,\mu}+A_{us\,\mu}\big),

$$
然后**逐分量比较**两者的标度：

| 分量            | 共线场      | 超软场      | 超软／共线                        |
|:----------------|:------------|:------------|:----------------------------------|
| $n\cdot A$      | $\lambda^2$ | $\lambda^2$ | $\lambda^0$（**同阶，必须保留**） |
| $A_\perp$       | $\lambda$   | $\lambda^2$ | $\lambda^1$（压低）               |
| $\bar n\cdot A$ | $1$         | $\lambda^2$ | $\lambda^2$（压低）               |

**要点。**

 在领头幂次，超软胶子**只能**通过 $n\cdot A_{us}$ 进入共线扇区：
$$

\mathcal L_c^{(0)}
  =\bar\xi_n\left[i\,n\cdot D_c+g_s\,n\cdot A_{us}
   +i\not{D}_{c\perp}\frac{1}{i\,\bar n\cdot D_c}\,i\not{D}_{c\perp}\right]
   \frac{\not{\bar{n}}}{2}\,\xi_n .
  

$$
而 $n\cdot A_{us}$ 恰好是**沿 $n$ 方向的 Wilson 线** $Y_n=\mathbf{P}\exp\big[ig_s\!\int ds\,n\cdot A_{us}\big]$ 的构件。 这就是“软辐射可以用 Wilson 线完整描述”（第 4.1 小节 eikonal 近似的结论）在拉氏量层面的实现， 也是**软–共线解耦**（soft-collinear decoupling）与因子化定理的技术基础。

**练习。**

\(a\) 用表 3 数出 $\bar\xi_n\,(n\cdot A_{us})\,\not{\bar{n}}\,\xi_n$ 的阶数，验证它确实与 $\mathcal L^{(0)}\sim\lambda^4$ 同阶。  
(b) 证明 $\bar\xi_n\,\gamma_\perp^\mu\,\xi_n=0$（提示：用 [eq:projflip] 与 $\not{n}\xi_n=0$）。这说明有些算符不是被幂次压低，而是被 **Dirac 代数直接消灭**——两种“消失机制”要分清。  
(c) 在 $\mathrm{SCET}_{II}$ 中，软动量 $p_s\sim Q(\lambda,\lambda,\lambda)$。 证明把它加到共线动量 $p_c\sim Q(\lambda^2,1,\lambda)$ 上会给出
$$

(p_c+p_s)^2\;\simeq\;(n\cdot p_s)(\bar n\cdot p_c)\;\sim\;Q^2\lambda
  \;\gg\; Q^2\lambda^2 ,
  

$$
即**一次软发射就把共线线推离质量壳，且离壳程度远超典型共线虚度**。 由此论证：$\mathrm{SCET}_{II}$ 中软–共线相互作用**不能**用低能理论里的局域顶点描述， 必须被积掉——这就是 $\mathrm{SCET}_{II}$ 需要从 $\mathrm{SCET}_{I}$ 再做一次匹配、 且领头幂次上软与共线扇区**解耦**（只通过算符定义中的 Wilson 线相连） 的根本原因。

# SCET 的基本结构

本节把前面所有材料拼起来，得到有效理论本身。目标是**教学级完整**： 每一步都能复核，但不追求最一般的情形（不做高阶算符、不做多方向推广）。

## 夸克场的模式分解

在双喷注运动学中，QCD 的夸克场包含几种完全不同的成分。按第 6.2 小节的模式分类写
$$

\psi(x)=\underbrace{\psi_{n}(x)}_{n\text{-共线}}
         +\underbrace{\psi_{\bar n}(x)}_{\bar n\text{-共线}}
         +\underbrace{q_{us}(x)}_{\text{超软}}
         +\underbrace{\psi_{\rm hard}}_{\text{被积掉}} .
  

$$
硬成分虚度 $\sim Q^2$，在低能理论中不作为动力学场出现，而是被积掉 成为 Wilson 系数。

对共线成分再做一次**自旋**分解。用 [eq:projdef] 的投影算符：
$$

\xi_n(x)\equiv P_n\,\psi_n(x)=\frac{\not{n}\not{\bar{n}}}{4}\psi_n(x),
  \qquad
  \eta_n(x)\equiv P_{\bar n}\,\psi_n(x)=\frac{\not{\bar{n}}\not{n}}{4}\psi_n(x),
  

$$
所以 $\psi_n=\xi_n+\eta_n$。由投影算符性质立刻得到**四条恒等式** （后面反复使用，请自己验证）：
$$

\not{n}\,\xi_n=0,
  \qquad
  \bar\xi_n\,\not{n}=0,
  \qquad
  \not{\bar{n}}\,\eta_n=0,
  \qquad
  \bar\eta_n\,\not{\bar{n}}=0 .
  

$$
**证明（验证第一、二式）。**

$\not{n}\,\xi_n=\not{n}\frac{\not{n}\not{\bar{n}}}{4}\psi_n
=\frac{(\not{n}\not{n})\not{\bar{n}}}{4}\psi_n=0$（因 $\not{n}\not{n}=n^2=0$）。 对第二式，注意 $\bar\xi_n=\xi_n^\dagger\gamma^0=\psi_n^\dagger P_n^\dagger\gamma^0
=\bar\psi_n\big(\gamma^0P_n^\dagger\gamma^0\big)$， 而 $\gamma^0(\not{n}\not{\bar{n}})^\dagger\gamma^0
=(\gamma^0\not{\bar{n}}^\dagger\gamma^0)(\gamma^0\not{n}^\dagger\gamma^0)=\not{\bar{n}}\,\not{n}$ （用 $\gamma^0\gamma^{\mu\dagger}\gamma^0=\gamma^\mu$），故
$$

\bar\xi_n=\bar\psi_n\,\frac{\not{\bar{n}}\not{n}}{4}=\bar\psi_n\,P_{\bar n}
  \qquad\Longrightarrow\qquad
  \bar\xi_n\,\not{n}=\bar\psi_n\frac{\not{\bar{n}}\,\not{n}\,\not{n}}{4}=0 .

$$
**注（物理含义）。**

$\xi_n$ 是“大分量”，$\eta_n$ 是“小分量”。用标度计数： $\xi_n\sim\lambda$ 而 $\eta_n\sim\lambda^2$（见下面 [eq:etasol]）， 所以 $\eta_n$ 相对被压低一个 $\lambda$。 这与 HQET 中 $h_v$（大）与 $H_v$（小）的关系完全平行 （第 3.3 小节）。

## 领头阶共线拉氏量的完整推导

**命题（SCET 领头阶共线拉氏量）。**

从无质量 QCD 出发，消去小分量 $\eta_n$ 后
$$

\boxed{\;
  \mathcal L_c^{(0)}
  =\bar\xi_n\left[\,i\,n\cdot D
  +i\not{D}_\perp\,\frac{1}{i\,\bar n\cdot D}\,i\not{D}_\perp\,\right]
  \frac{\not{\bar{n}}}{2}\;\xi_n \;}
  

$$
**证明。**

**第 1 步：分解 $\not{D}$ 与场。** 从 $\mathcal L=\bar\psi_n\,i\not{D}\,\psi_n$ 出发，代入 $\psi_n=\xi_n+\eta_n$ 与 [eq:slashdecomp]：
$$

\mathcal L=\big(\bar\xi_n+\bar\eta_n\big)
  \left[\not{n}\,\frac{i\bar n\cdot D}{2}
       +\not{\bar{n}}\,\frac{i n\cdot D}{2}
       +i\not{D}_\perp\right]
  \big(\xi_n+\eta_n\big).
  

$$
**第 2 步：用 [eq:fouriden] 与 [eq:projflip] 杀掉大部分交叉项。** 逐项检查 [eq:step1] 展开后的 $3\times4=12$ 项：

*（i）$\bar\xi_n\dots\xi_n$ 型：*
$$

\begin{aligned}
  \bar\xi_n\,\not{n}\,\frac{i\bar n\cdot D}{2}\,\xi_n&=0
    &&\text{（}\bar\xi_n\not{n}=0\text{）},\\
  \bar\xi_n\,\not{\bar{n}}\,\frac{in\cdot D}{2}\,\xi_n&\ne0
    &&\text{保留},\\
  \bar\xi_n\,i\not{D}_\perp\,\xi_n&=0
    &&\text{（}\gamma_\perp\text{ 翻转投影，见下）} .
\end{aligned}

$$
第三式的理由：在 $\bar\xi_n\gamma_\perp^\mu\xi_n$ 中把 $\xi_n=\frac{\not{n}\not{\bar{n}}}{4}\psi_n$ 代入，再用 $\gamma_\perp^\mu\not{n}=-\not{n}\gamma_\perp^\mu$ 把 $\not{n}$ 移到最左边， 最后用 $\bar\xi_n\not{n}=0$：
$$

\bar\xi_n\,\gamma_\perp^\mu\,\xi_n
  =\bar\xi_n\,\gamma_\perp^\mu\,\frac{\not{n}\not{\bar{n}}}{4}\psi_n
  =-\bar\xi_n\,\frac{\not{n}\,\gamma_\perp^\mu\,\not{\bar{n}}}{4}\psi_n=0 ,

$$
其中第二步用了 $\gamma_\perp^\mu\not{n}=-\not{n}\gamma_\perp^\mu$， 第三步用了 $\bar\xi_n\not{n}=0$。$\checkmark$

*（ii）$\bar\eta_n\dots\eta_n$ 型：*同理只剩 $\bar\eta_n\,\not{n}\,\frac{i\bar n\cdot D}{2}\,\eta_n$。

*（iii）交叉项：* $\bar\xi_n\,\not{n}(\cdots)\eta_n=0$（$\bar\xi_n\not{n}=0$）； $\bar\xi_n\,\not{\bar{n}}(\cdots)\eta_n=0$（$\not{\bar{n}}\eta_n=0$）； 所以 $\xi$–$\eta$ 之间**只通过横向导数耦合**。

汇总：
$$

\mathcal L
  =\bar\xi_n\,\frac{\not{\bar{n}}}{2}\,(i n\cdot D)\,\xi_n
  +\bar\eta_n\,\frac{\not{n}}{2}\,(i\bar n\cdot D)\,\eta_n
  +\bar\xi_n\,i\not{D}_\perp\,\eta_n
  +\bar\eta_n\,i\not{D}_\perp\,\xi_n .
  

$$
（$\not{\bar{n}}$ 与 $n\cdot D$ 可交换，因为后者不含 $\gamma$ 矩阵。）

**第 3 步：解 $\eta_n$ 的运动方程。** $\eta_n$ 在 [eq:Lsplit] 中**没有 $\bar n\cdot\partial$ 之外的动力学**， 且质量维度上它是被压低的分量，因此可以精确地消去（在经典层面即用运动方程； 在量子层面即做 Gauss 积分，两者对这个二次型拉氏量结果相同）。 对 $\bar\eta_n$ 变分：
$$

\frac{\delta\mathcal L}{\delta\bar\eta_n}
  =\frac{\not{n}}{2}\,(i\bar n\cdot D)\,\eta_n+i\not{D}_\perp\,\xi_n=0 .
  

$$
左乘 $\not{\bar{n}}/2$ 并使用 $\frac{\not{\bar{n}}\not{n}}{4}\eta_n=P_{\bar n}\eta_n=\eta_n$：
$$

(i\bar n\cdot D)\,\eta_n
  =-\frac{\not{\bar{n}}}{2}\,i\not{D}_\perp\,\xi_n
  \qquad\Longrightarrow\qquad
  \boxed{\;\eta_n=-\frac{1}{i\,\bar n\cdot D}\,\frac{\not{\bar{n}}}{2}\,i\not{D}_\perp\,\xi_n\;}
  

$$
标度检查：$\eta_n\sim\frac{1}{\lambda^0}\cdot\lambda\cdot\lambda=\lambda^2$， 确实比 $\xi_n\sim\lambda$ 压低一阶。$\checkmark$

**第 4 步：代回。** 注意 [eq:Lsplit] 中最后两项之和可以写成 $\bar\eta_n\big[\frac{\not{n}}{2}(i\bar n\cdot D)\eta_n+i\not{D}_\perp\xi_n\big]
+\bar\xi_n\,i\not{D}_\perp\,\eta_n$， 而方括号按 [eq:etaeom] 恰为零。于是
$$

\mathcal L_c^{(0)}
  =\bar\xi_n\,\frac{\not{\bar{n}}}{2}(i n\cdot D)\xi_n
   +\bar\xi_n\,i\not{D}_\perp\,\eta_n
  =\bar\xi_n\,\frac{\not{\bar{n}}}{2}(i n\cdot D)\xi_n
   -\bar\xi_n\,i\not{D}_\perp\,\frac{1}{i\bar n\cdot D}\,\frac{\not{\bar{n}}}{2}\,i\not{D}_\perp\,\xi_n .
  

$$
**第 5 步：整理 $\gamma$ 矩阵顺序。** 把第二项里的 $\not{\bar{n}}$ 移到最右边。用 [eq:anticomm] （$\not{\bar{n}}\gamma_\perp^\mu=-\gamma_\perp^\mu\not{\bar{n}}$）：
$$

-\,i\not{D}_\perp\frac{1}{i\bar n\cdot D}\,\frac{\not{\bar{n}}}{2}\,i\not{D}_\perp
  =-\,i\not{D}_\perp\frac{1}{i\bar n\cdot D}\Big(-i\not{D}_\perp\Big)\frac{\not{\bar{n}}}{2}
  =+\,i\not{D}_\perp\,\frac{1}{i\bar n\cdot D}\,i\not{D}_\perp\,\frac{\not{\bar{n}}}{2} .

$$
代入 [eq:almost]，并把公共因子 $\frac{\not{\bar{n}}}{2}$ 提到右侧 （第一项中 $\frac{\not{\bar{n}}}{2}$ 与 $in\cdot D$ 可交换），即得 [eq:LSCET]。

**要点。**

请注意 [eq:LSCET] 的两个特征，它们是 SCET 与普通 EFT 最大的差别：

1.  **非局域性**：出现 $\dfrac{1}{i\bar n\cdot D}$，即沿 $\bar n$ 方向的 **反导数**。它不是病态，而是“积掉的 $\eta_n$ 沿光锥方向传播”的痕迹。 在动量空间它就是 $1/(\bar n\cdot p)$，是一个良好定义的**有理函数**； 在坐标空间它对应沿光锥的线积分——正是 Wilson 线的来源。

2.  **两项同阶**（式 [eq:sameorder]）：这保证领头阶传播子 正确复现在壳条件 [eq:onshell]，见下一小节。

## 共线夸克传播子与 Feynman 规则

关掉相互作用（$D\to\partial$），[eq:LSCET] 在动量空间给出 二次型算符
$$

\bar\xi_n\left[n\cdot p+\frac{p_\perp^2}{\bar n\cdot p}\right]
  \frac{\not{\bar{n}}}{2}\,\xi_n
  =\bar\xi_n\,\frac{n\cdot p\,\,\bar n\cdot p+p_\perp^2}{\bar n\cdot p}\,
  \frac{\not{\bar{n}}}{2}\,\xi_n
  =\bar\xi_n\,\frac{p^2}{\bar n\cdot p}\,\frac{\not{\bar{n}}}{2}\,\xi_n ,

$$
其中用了 $\not{D}_\perp\not{D}_\perp\to \not{p}_\perp\not{p}_\perp=p_\perp^2$ 与 [eq:psq]。求逆得到**共线夸克传播子**
$$

\boxed{\;
  \frac{i\,\bar n\cdot p}{p^2+i0}\,\frac{\not{n}}{2}\;}
  

$$
（$\not{\bar{n}}/2$ 的“逆”是 $\not{n}/2$，因为 $\frac{\not{n}}{2}\frac{\not{\bar{n}}}{2}=P_n$ 在 $\xi_n$ 的子空间上是单位算符）。

**注。**

[eq:collprop] 可以直接从 QCD 传播子取共线极限验证：
$$

\frac{i\,\not{p}}{p^2+i0}
  =\frac{i}{p^2+i0}\left[\not{n}\frac{\bar n\cdot p}{2}
   +\underbrace{\not{\bar{n}}\frac{n\cdot p}{2}}_{\mathcal O(\lambda^2)}
   +\underbrace{\not{p}_\perp}_{\mathcal O(\lambda)}\right]
  \;\simeq\;\frac{i\,\bar n\cdot p}{p^2+i0}\,\frac{\not{n}}{2} .

$$
**完全吻合**。这再次说明：SCET 的 Feynman 规则就是 QCD 规则的展开， 没有任何新输入。同样可以验证 $\xi$–胶子顶点在领头阶为 $ig_s t^a\big(n^\mu+\frac{\gamma_\perp^\mu\not{p}_\perp'
+\not{p}_\perp\gamma_\perp^\mu}{\bar n\cdot p'}\dots\big)\frac{\not{\bar{n}}}{2}$ 之类的结构，其中 $n^\mu$ 一项即 eikonal 顶点 [eq:eikonal]。

## 标签动量与多极展开

共线动量 $p_c\sim Q(\lambda^2,1,\lambda)$ 里同时含有**大分量** （$\bar n\cdot p\sim Q$、$p_\perp\sim Q\lambda$）与**小分量** （$n\cdot p\sim Q\lambda^2$）。为了让有效理论的导数只产生小动量， 仿照 HQET 的相位剥离（第 3.3 小节 (a)），把动量拆成
$$

p_c^\mu=\underbrace{\tilde p^\mu}_{\text{标签}}+\underbrace{k^\mu}_{\text{残余}},
  \qquad
  \tilde p^\mu=(\bar n\cdot\tilde p)\frac{n^\mu}{2}+\tilde p_\perp^\mu,
  \qquad
  k^\mu\sim Q\lambda^2 .
  

$$
即：$\bar n\cdot p$ 与 $p_\perp$ 的**大部分**被冻结成离散标签 $\tilde p$，只有 $\mathcal O(Q\lambda^2)$ 的残余动量 $k$ 由场的坐标依赖携带。 相应地
$$

\xi_n(x)=\sum_{\tilde p}e^{-i\tilde p\cdot x}\,\xi_{n,\tilde p}(x),
  \qquad
  \partial^\mu\xi_{n,\tilde p}\sim Q\lambda^2\,\xi_{n,\tilde p} .
  

$$
于是所有大动量都变成**标签算符**（label operator） $\bar{\mathcal P}\equiv\bar n\cdot\tilde{\mathcal P}$、$\mathcal P_\perp$ 的本征值，而 $\frac{1}{i\bar n\cdot D}$ 中的 $\bar n\cdot\partial$ 就变成 $\bar{\mathcal P}$ 这个**数**——非局域性因此变得非常好操作。

**注（两种等价表述）。**

文献中有两套做法：

- **标签动量表述**（Bauer–Fleming–Pirjol–Stewart 一系）： 显式引入 $\tilde p$ 求和与标签算符 $\bar{\mathcal P}$， 与之配套的是“零区间减除”（zero-bin）处理软／共线重叠。

- **位置空间／多极展开表述**（Beneke–Chapovsky–Diehl–Feldmann， 以及 Becher–Neubert 的讲法）：不引入标签，直接对场做 **多极展开**（multipole expansion）。

两者物理等价。Neubert 的课通常采用后者，因为它更接近标准 QFT 语言。

多极展开的核心公式：超软场在共线顶点上只“看到”坐标的 $n\cdot x$ 分量，
$$

A_{us}^\mu(x)
  = A_{us}^\mu(x_-)
   + x_\perp\!\cdot\!\partial_\perp A_{us}^\mu(x_-)
   + \dots ,
  \qquad
  x_-^\mu\equiv (n\cdot x)\,\frac{\bar n^\mu}{2} .
  

$$
理由（用第 6.5 小节第一步的坐标标度）： 在共线顶点上 $x^+\sim1/Q$、$x_\perp\sim1/(Q\lambda)$、$x^-\sim1/(Q\lambda^2)$， 而超软动量各分量 $\sim Q\lambda^2$，故
$$

p_{us}\cdot x \sim
  \underbrace{\tfrac12 p_{us}^-x^+}_{\sim\lambda^2}
  +\underbrace{\tfrac12 p_{us}^+x^-}_{\sim\lambda^0}
  -\underbrace{\boldsymbol{p}_{us\perp}\!\cdot\!\boldsymbol{x}_\perp}_{\sim\lambda} .

$$
只有 $p_{us}^+x^-=\mathcal O(1)$ 必须保留在指数上，其余可以展开。 这就是 [eq:multipole]：**超软场只依赖 $x_-$。** 它是软–共线解耦（要点 [kp:usoft]）的位置空间版本。

## 规范不变性与 Wilson 线

SCET 有两类规范变换：共线规范变换（变换参数是共线场）与超软规范变换。 在共线规范变换下 $\xi_n$ 与 $\bar n\cdot A_n$ 各自变换， 单独的 $\xi_n$ 不是好的构件。定义**共线 Wilson 线**
$$

W_n(x)=\mathbf{P}\exp\left[i g_s\!\int_{-\infty}^{0}\!ds\;
  \bar n\cdot A_n\big(x+s\,\bar n\big)\right],
  

$$
它满足 $\big(i\,\bar n\cdot D\big)W_n=0$，并在共线规范变换 $U_n$ 下变换为 $W_n\to U_nW_n$。于是
$$

\boxed{\;\chi_n\equiv W_n^\dagger\,\xi_n,
  \qquad
  \mathcal A_{n\perp}^\mu\equiv\frac{1}{g_s}\,
  W_n^\dagger\big[\,i D_{\perp}^\mu\,W_n\big]\;}
  

$$
是**共线规范不变的构件**（gauge-invariant building blocks）。 所有领头幂次算符都可以只用 $\chi_n,\chi_{\bar n},\mathcal A_{n\perp}$ 与超软 Wilson 线搭出来。

类似地，超软 Wilson 线
$$

Y_n(x)=\mathbf{P}\exp\left[i g_s\!\int_{-\infty}^{0}\!ds\;
  n\cdot A_{us}\big(x+s\,n\big)\right]
  

$$
实现**软–共线解耦**：作场重定义
$$

\xi_n\to Y_n\,\xi_n^{(0)},
  \qquad
  A_n^\mu\to Y_n\,A_n^{(0)\mu}\,Y_n^\dagger ,
  

$$
则 [eq:Lcusoft] 中的 $g_s\,n\cdot A_{us}$ 项被完全吸收， 新的拉氏量里**共线扇区与超软扇区不再相互作用**：
$$

\mathcal L_c^{(0)}\big[\xi_n,A_n,A_{us}\big]
  \;=\;\mathcal L_c^{(0)}\big[\xi_n^{(0)},A_n^{(0)},A_{us}=0\big].
  

$$
这个变换称为 **BPS 场重定义**（(BPS field redefinition)， Bauer–Pirjol–Stewart）。

**要点。**

[eq:decoupling] 是**因子化定理的证明机器**： 一旦软与共线在拉氏量层面解耦，任何算符的矩阵元就自动分解成 “共线矩阵元 $\times$ 软矩阵元”的乘积（或卷积）， 因为真空与态也按扇区分解。软相互作用的全部残余 以 $Y_n,Y_{\bar n}$ 的形式留在算符里，其真空期望值就是**软函数**。

## 有效拉氏量的整体组织结构

把上面所有部分拼起来，SCET（以 $\mathrm{SCET}_{I}$ 为例）的完整结构是：
$$

\mathcal L_{\rm SCET}
  =\underbrace{\mathcal L_{c}^{(0)}[\xi_n,A_n]
   +\mathcal L_{\bar c}^{(0)}[\xi_{\bar n},A_{\bar n}]
   +\mathcal L_{us}^{(0)}[q_{us},A_{us}]}_{\text{领头幂次，扇区解耦（BPS 后）}}
   \;+\;\sum_{k\ge1}\lambda^k\,\mathcal L^{(k)} ,
  

$$
而**外部硬相互作用**（如电磁流 $\bar\psi\gamma^\mu\psi$）在 SCET 中 被展开成算符 $+$ Wilson 系数：
$$

\boxed{\;
  \bar\psi\gamma^\mu\psi
  \;\longrightarrow\;
  \int\! d s\,d\bar s\;
  \tilde C\big(s,\bar s;\mu\big)\;
  \bar\chi_{\bar n}(\bar s\,n)\,\gamma^\mu_\perp\,\chi_n(s\,\bar n)
  \;+\;\mathcal O(\lambda)\;}
  

$$
在动量空间（对光锥位置做 Fourier 变换）即
$$

J^\mu_{\rm SCET}
  =C_V\big(Q^2,\mu\big)\;\bar\chi_{\bar n}\,\gamma^\mu_\perp\,\chi_n ,
  \qquad Q^2=(\bar n\cdot p_n)(n\cdot p_{\bar n}) .
  

$$
**注（SCET 里的“局域”是什么意思）。**

[eq:current] 中的算符在**横向与时间方向都是局域的**， 但沿光锥方向（$s\bar n$ 与 $\bar s n$）是**非局域的**， 系数 $\tilde C(s,\bar s)$ 是一个函数而不是一个数。 这是 SCET 与 Fermi 理论（第 3.2 小节）最重要的结构差异： **被积掉的是“横向／虚度”方向的硬涨落，而不是所有方向。** 这就是为什么 SCET 的 Wilson 系数会依赖光锥动量分数， 以及为什么因子化定理常常是**卷积**而不是简单乘积。

## 一次真正的匹配：矢量流的 Wilson 系数

匹配条件：在同一套外态上计算 QCD 的形状因子与 SCET 的矩阵元， 两边的红外结构相同，其差即 $C_V$。单圈结果（$\overline{\mathrm{MS}}$ 方案， $L\equiv\ln\dfrac{Q^2}{\mu^2}$）
$$

\boxed{\;
  C_V\big(Q^2,\mu\big)
  =1+\frac{\alpha_sC_F}{4\pi}
   \left[-L^2+3L-8+\frac{\pi^2}{6}\right]+\mathcal O(\alpha_s^2)\;}
  

$$
**注（关于 [eq:CV] 的约定）。**

式 [eq:CV] 写的是**类空**情形（$Q^2=-q^2>0$）、$\overline{\mathrm{MS}}$ 方案、 $L=\ln(Q^2/\mu^2)$。三点提醒：

- $-L^2$ 项与约定无关（$L^2$ 不变号）；但 $+3L$ 的**符号**随 $L\leftrightarrow-L$ 的约定翻转。判断办法见下面 [eq:CVrge]： 自洽的约定必须给出标准值 $\gamma_0^V=-6C_F$。

- **常数项依赖方案与运动学**。对**类时**情形 （如 $e^+e^-$ 湮灭，$q^2=Q^2>0$）需要解析延拓 $L\to L-i\pi$，于是常数中会多出 $\pi^2$ 项， 且 $C_V$ 变成复数（$H=|C_V|^2$ 仍为实）。

- 因此**不要背常数项**。要记住的是结构 $-L^2+3L+\text{常数}$，以及它由 [eq:cusp] 的 $\Gamma_0=4C_F$、$\gamma_0^V=-6C_F$ 唯一确定对数部分这件事。

请注意三件事：

1.  $C_V$ 是**红外有限**的——所有 $1/\epsilon^2,1/\epsilon$ 极点 都在 QCD 与 SCET 矩阵元之差中抵消（这正是第 6.4 小节教训 (1) 的实例）。

2.  里面有 $L^2$：说明**取 $\mu\ne Q$ 时 $C_V$ 含双对数**。 因此 $C_V$ 的“自然标度”是 $\mu\sim Q$，在那里 $L=0$， 微扰展开最可靠。

3.  $C_V$ 依赖 $\mu$，其 $\mu$ 依赖由重整化群方程控制。

#### 从 [eq:CV] 直接读出重整化群方程。

对 $\ln\mu$ 求导，注意 $\dfrac{dL}{d\ln\mu}=-2$：
$$

\frac{d C_V}{d\ln\mu}
  =\frac{\alpha_sC_F}{4\pi}\big(-2L+3\big)\cdot(-2)
  =\frac{\alpha_sC_F}{4\pi}\big(4L-6\big)
  =\left[\Gamma_{\mathrm{cusp}}(\alpha_s)\,\ln\frac{Q^2}{\mu^2}+\gamma_V(\alpha_s)\right]C_V ,
  

$$
其中
$$

\Gamma_{\mathrm{cusp}}(\alpha_s)=\frac{\alpha_s}{4\pi}\,\Gamma_0+\dots,\quad \Gamma_0=4C_F,
  \qquad
  \gamma_V(\alpha_s)=\frac{\alpha_s}{4\pi}\,\gamma_0+\dots,\quad \gamma_0=-6C_F.
  

$$
$\Gamma_{\mathrm{cusp}}$ 称为**尖点反常量纲**（cusp anomalous dimension）， 它是整个 SCET 中最重要的单个函数——所有领头双对数都由它控制。

#### 解方程：Sudakov 指数化。

为了看清物理，先取固定耦合。由 [eq:CVrge]，
$$

\begin{aligned}
  \ln\frac{C_V(\mu)}{C_V(Q)}
  &=\int_{\ln Q}^{\ln\mu}\! d\ln\mu'\;\Gamma_{\mathrm{cusp}}\ln\frac{Q^2}{\mu'^2}
   =\Gamma_{\mathrm{cusp}}\int_{\ln Q}^{\ln\mu}\!(-2)\big(\ln\mu'-\ln Q\big)\,d\ln\mu'
   \notag\\
  &=-\Gamma_{\mathrm{cusp}}\,\ln^2\frac{\mu}{Q} ,
  
\end{aligned}

$$
即
$$

\boxed{\;
  C_V(\mu)\;\simeq\;C_V(Q)\;
  \exp\!\left[-\Gamma_{\mathrm{cusp}}\,\ln^2\frac{\mu}{Q}\right]\;}
  

$$
$\Gamma_{\mathrm{cusp}}>0$，所以 $\mu\ne Q$ 时形状因子被**指数压低**—— 这就是 **Sudakov 压低**（Sudakov suppression）。

#### 自洽性检查。

把 [eq:sudakovexp] 展开到 $\mathcal O(\alpha_s)$：
$$

-\Gamma_{\mathrm{cusp}}\ln^2\frac{\mu}{Q}
  =-\frac{4C_F\alpha_s}{4\pi}\cdot\frac{L^2}{4}
  =-\frac{\alpha_sC_F}{4\pi}L^2 ,

$$
（用了 $L=\ln(Q^2/\mu^2)=2\ln(Q/\mu)$，故 $\ln^2(\mu/Q)=L^2/4$）， 与 [eq:CV] 中的 $-L^2$ 项**精确一致**。$\checkmark$

**要点。**

[eq:CV]–[eq:sudakovexp] 是本讲义最值得反复看的一段： 它展示了 SCET 的完整工作流程—— **（i）在硬标度匹配得到无大对数的 $C_V(Q)$； （ii）用重整化群（其核心是 $\Gamma_{\mathrm{cusp}}$）演化； （iii）演化的解自动把 $\alpha_s^nL^{2n}$ 全部重求和成一个指数。** 把这三步理解透，整门课的骨架就有了。

**练习。**

\(a\) 若约定 $L'=\ln(\mu^2/Q^2)=-L$，重新写出 [eq:CV] 与 [eq:CVrge]，并检查 $\Gamma_{\mathrm{cusp}}$ 与 $\gamma_V$ 的符号如何变化。 （这是听课时最容易出错的地方，务必自己走一遍。）  
(b) 用 [eq:alphasrun] 的跑动耦合代替固定耦合重做 [eq:sudakov]，说明为什么真实的 Sudakov 指数是 $\alpha_s$ 与 $L$ 的双重展开，需要引入“对数计数” （LL、NLL、NNLL 等，(logarithmic accuracy)）。

# 典型例子：尺度分离的两个实例

本节把前面的机器用到两个具体过程上。第 8.1 小节 （$e^+e^-$ 喷注／thrust）是 $\mathrm{SCET}_{I}$ 的标准范例，讲透； 第 8.2 小节（$B$ 介子衰变）用来对照 $\mathrm{SCET}_{II}$ 与 非微扰输入，讲结构。

## 例一：$e^+e^-\to$ 双喷注与 thrust 的因子化（$\mathrm{SCET}_{I}$）

#### 运动学与模式确定。

回到第 2.1 小节。取 $\lambda=\sqrt\tau$。 末态由两个近背对背的喷注加软辐射组成：

- 沿 $n$ 方向的喷注：$p_n\sim Q(\tau,1,\sqrt\tau)=Q(\lambda^2,1,\lambda)$， 虚度 $p_n^2\sim Q^2\tau$。

- 沿 $\bar n$ 方向的喷注：$p_{\bar n}\sim Q(1,\lambda^2,\lambda)$。

- 软辐射：所有分量 $\sim Q\tau=Q\lambda^2$， 虚度 $\sim Q^2\tau^2=Q^2\lambda^4$。

共线（$Q^2\lambda^2$）与软（$Q^2\lambda^4$）**虚度不同** $\Longrightarrow$ 这是 $\mathrm{SCET}_{I}$。软模在此语境下叫超软， 且它对 thrust 的贡献不可忽略：$\tau\supset k^+/Q$， $k^+\sim Q\tau$ 恰好贡献 $\mathcal O(\tau)$。

#### 因子化定理。

把电磁流用 [eq:currentmom] 替换， 做 BPS 场重定义 [eq:BPS] 使扇区解耦，再把 thrust 的测量函数 按 [eq:thrusthemisphere] 分解到各扇区，得到
$$

\boxed{\;
  \frac{1}{\sigma_0}\frac{d\sigma}{d\tau}
  = H\big(Q^2,\mu\big)\!\int\! ds_n\,ds_{\bar n}\,dk\;
    J\big(s_n,\mu\big)\,J\big(s_{\bar n},\mu\big)\,S\big(k,\mu\big)\,
    \delta\!\left(\tau-\frac{s_n+s_{\bar n}}{Q^2}-\frac{k}{Q}\right)\;}
  

$$
其中

- **硬函数**（hard function）$H=\big|C_V(Q^2,\mu)\big|^2$， 由 [eq:CV] 给出，自然标度 $\mu_H\sim Q$；

- **喷注函数**（jet function）$J(s,\mu)$， 定义为共线场的两点关联（$\chi_n$ 的不连续部分）， 自然标度 $\mu_J\sim\sqrt{s}\sim Q\sqrt\tau$；

- **软函数**（soft function） $S(k,\mu)=\frac{1}{N_c}\big\langle 0\big|
          \mathrm{Tr}\big[\bar T\{Y_{\bar n}^\dagger Y_n\}\,\delta(k-\hat k^+)\,
          T\{Y_n^\dagger Y_{\bar n}\}\big]\big|0\big\rangle$， 即两条超软 Wilson 线的真空期望值，自然标度 $\mu_S\sim Q\tau$。

[eq:thrustfact] 恰好把表 1 第一行的三个标度 分别装进三个函数。每个函数在自己的自然标度上**没有大对数**。

#### 对数如何被重求和。

三个函数各满足一个重整化群方程， 核心都是同一个 $\Gamma_{\mathrm{cusp}}$（这不是巧合，而是 QCD 红外结构的普适性）。 把 $H$ 从 $\mu_H\sim Q$ 演化、$J$ 从 $\mu_J\sim Q\sqrt\tau$ 演化、 $S$ 从 $\mu_S\sim Q\tau$ 演化到共同的 $\mu$， 所有 $\alpha_s^n\ln^{2n}\tau$ 被自动重求和。

#### 一致性条件（很好的自查工具）。

由于 [eq:thrustfact] 左边**与 $\mu$ 无关**， 各因子的反常量纲必须满足
$$

\gamma_H\big(Q,\mu\big)
  +2\,\gamma_J\big(Q\sqrt\tau,\mu\big)
  +\gamma_S\big(Q\tau,\mu\big)=0 .
  

$$
把每个 $\gamma$ 写成 $\Gamma_{\mathrm{cusp}}\ln(\text{标度}^2/\mu^2)+\text{常数}$ 的形式，[eq:consistency] 就固定了各系数间的关系。 **这是检查自己是否记对反常量纲的最快办法**， 课上如果某个符号记混了，用这条式子当场就能验出来。

**练习。**

用 [eq:consistency] 与 [eq:cusp] 验证： 若 $\gamma_H=2\Gamma_{\mathrm{cusp}}\ln\frac{Q^2}{\mu^2}+\dots$、 $\gamma_J=-\Gamma_{\mathrm{cusp}}\ln\frac{\mu^2}{s}+\dots$， 则 $\gamma_S$ 中 $\Gamma_{\mathrm{cusp}}$ 的系数被完全确定。 （提示：把 $s\sim Q^2\tau$、$k\sim Q\tau$ 代入， 比较 $\ln Q$ 与 $\ln\tau$ 的系数；不同文献对 $J$ 与 $S$ 的变量约定不同，重点是掌握*方法*。）

#### 数值感受。

取 $Q=m_Z$、$\tau=0.05$： $\mu_H\simeq91$ GeV、$\mu_J\simeq91\sqrt{0.05}\simeq20$ GeV、 $\mu_S\simeq91\times0.05\simeq4.6$ GeV。 三个标度确实相差一个量级以上，$\alpha_s$ 分别约为 $0.118$、$0.14$、$0.21$——层级清晰，但软标度已经开始接近非微扰区， 这就是为什么 thrust 拟合 $\alpha_s$ 时必须仔细处理幂次修正 （$\Lambda_{\mathrm{QCD}}/(Q\tau)$ 效应）。

## 例二：$B$ 介子衰变中的尺度分离（$\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 对照）

$B$ 物理是 SCET 的另一个主战场，也是 Neubert 的主要研究领域， 课上几乎一定会出现。这里对照两个过程。

#### （a）$B\to X_s\gamma$ 端点区：$\mathrm{SCET}_{I}$。

在 $B$ 静止系中光子能量 $E_\gamma\to m_b/2$（端点）时， 强子末态 $X_s$ 是一个高能、低不变质量的喷注：
$$

E_X\sim m_b,
  \qquad
  m_X^2=p_X^2\sim m_b\Lambda_{\mathrm{QCD}}
  \qquad\Longrightarrow\qquad
  \lambda=\sqrt{\frac{\Lambda_{\mathrm{QCD}}}{m_b}}\sim0.3 .

$$
三个标度
$$

\underbrace{m_b}_{\text{硬}}
  \;\gg\;
  \underbrace{\sqrt{m_b\Lambda_{\mathrm{QCD}}}}_{\text{硬共线}}
  \;\gg\;
  \underbrace{\Lambda_{\mathrm{QCD}}}_{\text{超软}} ,

$$
虚度分别是 $m_b^2$、$m_b\Lambda_{\mathrm{QCD}}$、$\Lambda_{\mathrm{QCD}}^2$——**三层不同虚度， 标准 $\mathrm{SCET}_{I}$**。因子化定理形式上与 [eq:thrustfact] 同构：
$$

\frac{d\Gamma}{dE_\gamma}
  \;\propto\;
  H\big(m_b,\mu\big)\!\int\! d\omega\;
  J\big(p_X^2+m_b\,\omega,\mu\big)\;
  S\big(\omega,\mu\big) ,
  

$$
其中 $S(\omega,\mu)$ 是 **$B$ 介子形状函数** （shape function），即 $b$ 夸克在 $B$ 介子中光锥动量分布， 是**非微扰**对象。

**要点。**

注意 [eq:bsgamma] 与 [eq:thrustfact] 的**结构完全一样**： 硬函数 $\times$ 喷注函数 $\otimes$ 软函数。 这正是 EFT 的力量——两个物理上毫不相干的过程 （$e^+e^-$ 湮灭与 $B$ 衰变）共享同一个因子化骨架， 因为它们的**模式结构相同**。喷注函数甚至是*同一个函数*。

#### （b）$B\to\pi\ell\nu$ 大反冲区 / $B\to\gamma\ell\nu$：$\mathrm{SCET}_{II}$。

现在末态是一个**单个轻强子**（而不是一个有质量的喷注）。 $\pi$ 的组分夸克是真正共线的：
$$

p_\pi\sim m_b\left(\frac{\Lambda_{\mathrm{QCD}}^2}{m_b^2},\,1,\,\frac{\Lambda_{\mathrm{QCD}}}{m_b}\right),
  \qquad
  p_\pi^2\sim\Lambda_{\mathrm{QCD}}^2 ,

$$
而 $B$ 中的软夸克 $p_s\sim\Lambda_{\mathrm{QCD}}(1,1,1)$，$p_s^2\sim\Lambda_{\mathrm{QCD}}^2$。 **两者虚度相同**（都是 $\Lambda_{\mathrm{QCD}}^2$），只有快度不同 $\Longrightarrow$ 这是 $\mathrm{SCET}_{II}$（取 $\lambda=\Lambda_{\mathrm{QCD}}/m_b$）。

处理方式是**两步匹配**：
$$

\text{QCD}
  \;\xrightarrow[\ \mu\sim m_b\ ]{}\;
  \mathrm{SCET}_{I}
  \;\xrightarrow[\ \mu\sim\sqrt{m_b\Lambda_{\mathrm{QCD}}}\ ]{}\;
  \mathrm{SCET}_{II}.
  

$$
第二步把硬共线模（虚度 $m_b\Lambda_{\mathrm{QCD}}$）也积掉——正是练习中 式 [eq:scet2offshell] 所预示的那些离壳涨落。

以 $B\to\gamma\ell\nu$（理论上最干净）为例，领头幂次因子化给出
$$

F_{B\to\gamma}\big(E_\gamma\big)
  \;\propto\;
  \frac{f_B\,m_B}{2E_\gamma}\;\times\;\frac{1}{\lambda_B(\mu)}
  \;\times\;\Big[1+\mathcal O(\alpha_s)+\mathcal O\big(\Lambda_{\mathrm{QCD}}/E_\gamma\big)\Big],
  

$$
其中出现了 $B$ 介子**光锥分布振幅** （(light-cone distribution amplitude), LCDA）$\phi_+^B(\omega,\mu)$ 的第一个反矩：
$$

\frac{1}{\lambda_B(\mu)}
  =\int_0^\infty\! d\omega\;\frac{\phi_+^B(\omega,\mu)}{\omega} .
  

$$
**注（$\mathrm{SCET}_{II}$ 的特有困难）。**

[eq:lambdaB] 的积分在 $\omega\to0$ 处**可能发散**——这是 **端点发散**（endpoint divergence），是 $\mathrm{SCET}_{II}$ 中 快度发散在强子层面的体现。它意味着： 朴素的“软 $\times$ 共线”因子化在 $\mathrm{SCET}_{II}$ 中**不总是成立**， 需要额外的正规化与重求和（快度重整化群、共线异常）。 Neubert 与合作者在这个方向做了大量工作，课程后半段很可能会讲到。

#### 对照总结。

表 4 把两个例子并列。

|            | $\mathrm{SCET}_{I}$                     | $\mathrm{SCET}_{II}$                 |
|:-----------|:----------------------------------------|:-------------------------------------|
| 代表过程   | $e^+e^-$ thrust；$B\to X_s\gamma$ 端点  | $B\to\pi\ell\nu$；Drell–Yan 小 $q_T$ |
| 共线虚度   | $Q^2\lambda^2$                          | $Q^2\lambda^2$                       |
| 软模标度   | 超软 $Q(\lambda^2,\lambda^2,\lambda^2)$ | 软 $Q(\lambda,\lambda,\lambda)$      |
| 软虚度     | $Q^2\lambda^4$（与共线**不同**）        | $Q^2\lambda^2$（与共线**相同**）     |
| 分离机制   | 虚度（$\mu$ 即可）                      | 快度（需额外正规化子 $\nu$）         |
| 匹配步数   | 一步                                    | 两步（经 $\mathrm{SCET}_{I}$）       |
| 典型病理   | 无（领头阶）                            | 快度／端点发散、共线异常             |
| 非微扰输入 | 形状函数                                | LCDA、TMD 分布                       |

$\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 的对照。

## 补充：DIS 在 $x\to1$ 的标度分离

作为第三个（简短的）例子：深度非弹性散射（(deep inelastic scattering), DIS） 在 Bjorken $x\to1$ 时，末态强子系统的不变质量
$$

p_X^2=\frac{1-x}{x}\,Q^2\;\simeq\;Q^2(1-x)\ll Q^2 ,

$$
所以 $\lambda^2=1-x$，标度层级为 $Q\gg Q\sqrt{1-x}\gg Q(1-x)$ （表 1 第二行），又是一个 $\mathrm{SCET}_{I}$ 问题， 因子化为 $H\times J\otimes\big(\text{$x\to1$ 的 PDF}\big)$。 这个例子的价值在于：它把 SCET 与传统的**阈值重求和** （threshold resummation）联系起来，说明 SCET 并不是另起一套， 而是把 1980–90 年代用其他方法得到的重求和结果**系统化、算符化**。

# 课堂可能出现的公式与英汉术语表

## 公式速查（按听课时被写到黑板上的概率排序）

1.  光锥基底与分解：$n^2=\bar n^2=0$，$n\cdot\bar n=2$，
$$

p^\mu=(n\cdot p)\frac{\bar n^\mu}{2}+(\bar n\cdot p)\frac{n^\mu}{2}+p_\perp^\mu ,
            \qquad
            p=(p^+,p^-,p_\perp) .

$$
2.  虚度与点积：
$$

p^2=p^+p^--\boldsymbol{p}_\perp^2 ,
            \qquad
            p\cdot k=\tfrac12\big(p^+k^-+p^-k^+\big)-\boldsymbol{p}_\perp\!\cdot\!\boldsymbol{k}_\perp.

$$
3.  模式标度：共线 $Q(\lambda^2,1,\lambda)$；反共线 $Q(1,\lambda^2,\lambda)$； 超软 $Q(\lambda^2,\lambda^2,\lambda^2)$；软 $Q(\lambda,\lambda,\lambda)$。

4.  场的标度：$\xi_n\sim\lambda$，$A_c\sim(\lambda^2,1,\lambda)$， $q_{us}\sim\lambda^3$，$A_{us}\sim\lambda^2$， $q_s\sim\lambda^{3/2}$，$A_s\sim\lambda$。

5.  投影算符：$P_n=\frac{\not{n}\not{\bar{n}}}{4}$，$P_{\bar n}=\frac{\not{\bar{n}}\not{n}}{4}$， $\not{n}\xi_n=0$，$\bar\xi_n\not{n}=0$。

6.  领头阶共线拉氏量：
$$

\mathcal L_c^{(0)}=\bar\xi_n\left[i\,n\cdot D
            +i\not{D}_\perp\frac{1}{i\,\bar n\cdot D}i\not{D}_\perp\right]\frac{\not{\bar{n}}}{2}\xi_n .

$$
7.  共线夸克传播子：$\dfrac{i\,\bar n\cdot p}{p^2+i0}\dfrac{\not{n}}{2}$。

8.  Wilson 线： $W_n=\mathbf{P}\exp\big[ig_s\!\int_{-\infty}^0\!ds\,\bar n\cdot A_n(x+s\bar n)\big]$， $Y_n=\mathbf{P}\exp\big[ig_s\!\int_{-\infty}^0\!ds\,n\cdot A_{us}(x+sn)\big]$。

9.  规范不变构件：$\chi_n=W_n^\dagger\xi_n$， $\mathcal A_{n\perp}^\mu=\frac1{g_s}W_n^\dagger[iD_\perp^\mu W_n]$。

10. eikonal 近似：$\mathcal M^\mu\simeq g_st^a\dfrac{p^\mu}{p\cdot k}\mathcal M_0$。

11. 领头幂次流：$J^\mu=C_V(Q^2,\mu)\,\bar\chi_{\bar n}\gamma^\mu_\perp\chi_n$，
$$

C_V=1+\frac{\alpha_sC_F}{4\pi}\Big[-L^2+3L-8+\frac{\pi^2}{6}\Big],
            \qquad L=\ln\frac{Q^2}{\mu^2} .

$$
12. 尖点反常量纲：$\Gamma_{\mathrm{cusp}}=\frac{\alpha_s}{4\pi}\,4C_F+\mathcal O(\alpha_s^2)$； RGE $\dfrac{dC_V}{d\ln\mu}=\big[\Gamma_{\mathrm{cusp}}L+\gamma_V\big]C_V$， $\gamma_V=-\frac{\alpha_s}{4\pi}6C_F+\dots$

13. Sudakov 指数：$C_V(\mu)\simeq C_V(Q)\exp\big[-\Gamma_{\mathrm{cusp}}\ln^2(\mu/Q)\big]$。

14. 因子化定理（$\mathrm{SCET}_{I}$ 通式）： $\text{可观测量}=H\times J\otimes J\otimes S+\mathcal O(\lambda)$。

15. 一致性条件：$\gamma_H+2\gamma_J+\gamma_S=0$。

16. $\beta$ 函数：$\dfrac{d\alpha_s}{d\ln\mu}=-\dfrac{\beta_0}{2\pi}\alpha_s^2$， $\beta_0=11-\frac23n_f$。

## 英汉术语表

| 英文                                   | 中文                | 备注 / 出现处                                                                                        |
|:---------------------------------------|:--------------------|:-----------------------------------------------------------------------------------------------------|
| soft-collinear effective theory (SCET) | 软共线有效理论      | 全课程                                                                                               |
| effective field theory (EFT)           | 有效场论            | §3                         |
| light-cone coordinates                 | 光锥坐标            | §5             |
| light-like / null vector               | 类光向量            | $n^2=\bar n^2=0$                                                                                     |
| reference vector                       | 参考向量            | $n,\bar n$                                                                                           |
| power counting                         | 标度计数 / 幂次计数 | §6     |
| expansion parameter                    | 展开参数            | $\lambda$                                                                                            |
| mode                                   | 模式                | 表 2                   |
| hard mode                              | 硬模                | $p^2\sim Q^2$                                                                                        |
| collinear mode                         | 共线模              | $p^2\sim Q^2\lambda^2$                                                                               |
| anti-collinear                         | 反共线              | 沿 $\bar n$ 方向                                                                                     |
| soft mode                              | 软模                | $\mathrm{SCET}_{II}$                                                                                 |
| ultrasoft mode                         | 超软模              | $\mathrm{SCET}_{I}$                                                                                  |
| hard-collinear                         | 硬共线              | $\mathrm{SCET}_{I}$ 中的共线模                                                                       |
| Glauber mode                           | Glauber 模          | 前向散射                                                                                             |
| virtuality                             | 虚度                | $p^2$                                                                                                |
| rapidity                               | 快度                | 式 [eq:rapidity] |
| transverse momentum                    | 横动量              | $p_\perp$                                                                                            |
| opening angle                          | 张角                | $\lambda\sim\theta$                                                                                  |

核心术语。建议听课前把英文一栏遮住自测一遍。

| 英文                              | 中文                    | 备注 / 出现处                                                                                              |
|:----------------------------------|:------------------------|:-----------------------------------------------------------------------------------------------------------|
| matching                          | 匹配                    | §3.2                   |
| Wilson coefficient                | Wilson 系数             | $C_V$                                                                                                      |
| integrate out                     | 积分掉 / 积掉           | 重自由度                                                                                                   |
| operator product expansion (OPE)  | 算符乘积展开            | §3                               |
| expansion by regions              | 按区域展开              | §6.4               |
| method of regions                 | 区域方法                | 同上                                                                                                       |
| scaleless integral                | 无标度积分              | 维数正规化中为零                                                                                           |
| eikonal approximation             | eikonal 近似 / 类光近似 | 式 [eq:eikonal]          |
| Wilson line                       | Wilson 线               | $W_n$, $Y_n$                                                                                               |
| path-ordered exponential          | 路径有序指数            | $\mathbf{P}\exp$                                                                                           |
| label momentum                    | 标签动量                | §7.4                   |
| residual momentum                 | 残余动量                | $k\sim Q\lambda^2$                                                                                         |
| multipole expansion               | 多极展开                | 式 [eq:multipole]    |
| BPS field redefinition            | BPS 场重定义            | 式 [eq:BPS]                      |
| soft-collinear decoupling         | 软–共线解耦             | 式 [eq:decoupling] |
| gauge-invariant building block    | 规范不变构件            | $\chi_n,\mathcal A_{n\perp}$                                                                               |
| factorization theorem             | 因子化定理              | 式 [eq:thrustfact] |
| hard function                     | 硬函数                  | $H=|C_V|^2$                                                                                                |
| jet function                      | 喷注函数                | $J$                                                                                                        |
| soft function                     | 软函数                  | $S$                                                                                                        |
| shape function                    | 形状函数                | $B\to X_s\gamma$                                                                                           |
| light-cone distribution amplitude | 光锥分布振幅            | LCDA, $\phi_+^B$                                                                                           |

术语表（续）：算符、函数与技术概念。

| 英文                                | 中文                 | 备注 / 出现处                                                                                              |
|:------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------|
| cusp anomalous dimension            | 尖点反常量纲         | $\Gamma_{\mathrm{cusp}}$                                                                                   |
| anomalous dimension                 | 反常量纲             | $\gamma$                                                                                                   |
| renormalization group (RG)          | 重整化群             | §1.3               |
| resummation                         | 重求和               | $\alpha_s^nL^{2n}$                                                                                         |
| Sudakov logarithm / suppression     | Sudakov 对数 / 压低  | 式 [eq:sudakovexp] |
| leading power                       | 领头幂次             | $\mathcal O(\lambda^0)$                                                                                    |
| power correction                    | 幂次修正             | $\mathcal O(\lambda)$                                                                                      |
| leading logarithm (LL/NLL/NNLL)     | 领头对数（次领头等） | 对数精度                                                                                                   |
| rapidity divergence                 | 快度发散             | $\mathrm{SCET}_{II}$                                                                                       |
| rapidity regulator                  | 快度正规化子         | $\nu$                                                                                                      |
| collinear anomaly                   | 共线异常             | Becher–Neubert                                                                                             |
| zero-bin subtraction                | 零区间减除           | 软／共线重叠                                                                                               |
| endpoint divergence                 | 端点发散             | 式 [eq:lambdaB]          |
| plus distribution                   | 加号分布             | $[\,\cdot\,]_+$                                                                                            |
| splitting function                  | 分裂函数             | $P_{qq}$ 等                                                                                                |
| threshold resummation               | 阈值重求和           | DIS $x\to1$                                                                                                |
| transverse-momentum dependent (TMD) | 横动量依赖           | Drell–Yan 小 $q_T$                                                                                         |
| heavy quark effective theory (HQET) | 重夸克有效理论       | §3.3                     |

术语表（续）：重整化群、重求和与 $\mathrm{SCET}_{II}$ 相关概念。

# 常见困惑与澄清

1.  **软与共线到底差在哪里？两者不是都让 $p\cdot k\to0$ 吗？**

    答：是的，两者都让传播子分母 [eq:irorigin] 变小，但**方式不同**：

    - **软**：$k^\mu$ 的**所有分量**一起变小， $k\sim Q(\lambda^2,\lambda^2,\lambda^2)$（或 $Q(\lambda,\lambda,\lambda)$）。 它是各向同性地“变软”，能量小、方向随意。

    - **共线**：$k^\mu$ 的分量**不均匀**地小， $k\sim Q(\lambda^2,1,\lambda)$。能量可以是 $\mathcal O(Q)$， 只是角度小。

    在光锥坐标下这个区别一目了然：软模在 $(\ln k^+,\ln k^-)$ 平面上 沿**对角线**移动（快度不变，虚度变），共线模沿**反对角线** （虚度不变，快度变）。这也是为什么必须学光锥坐标： 在 Cartesian 分量里这两个极限看起来是一回事。

2.  **$\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 的直觉是什么？**

    答：一句话——**看末态是“一个有质量的喷注”还是“一个单独的轻强子”**。

    - **$\mathrm{SCET}_{I}$**：末态是喷注，允许有 $\mathcal O(\sqrt{Q\Lambda_{\mathrm{QCD}}})$ 的不变质量。喷注内部还有“空间”容纳额外辐射， 所以共线模的虚度（$Q^2\lambda^2$）明显高于软模（$Q^2\lambda^4$）。 *例*：thrust、$B\to X_s\gamma$ 端点、DIS $x\to1$。

    - **$\mathrm{SCET}_{II}$**：末态是一个具体的强子（$\pi$、$\rho$）， 或测量了一个直接约束横动量的量（Drell–Yan 的 $q_T$）。 这时共线模被压到 $p^2\sim\Lambda_{\mathrm{QCD}}^2$（或 $q_T^2$），与软模同虚度。 *例*：$B\to\pi\ell\nu$、$B\to\gamma\ell\nu$、小 $q_T$ 谱。

    更技术化的判据：算一算 $($共线虚度$)$ 与 $($软虚度$)$。相等 $\Rightarrow$ $\mathrm{SCET}_{II}$，需要快度正规化子；不相等 $\Rightarrow$ $\mathrm{SCET}_{I}$，$\overline{\mathrm{MS}}$ 足够。

3.  **为什么 SCET 拉氏量里有 $1/(i\bar n\cdot D)$ 这种“非局域”的东西？ 它会不会破坏因果性？**

    答：不会。它来自积掉小分量场 $\eta_n$（式 [eq:etasol]）， 物理上代表沿 $\bar n$ 方向的**离壳**传播——离壳的东西传播距离 $\sim1/(\bar n\cdot p)\sim1/Q$，在 EFT 的分辨率下就是“瞬时”的。 非局域性只沿**光锥方向**，且被 $1/Q$ 压低。 这与 Fermi 理论中 $1/M_W^2$ 展开留下局域算符是同一回事， 只不过这里“展开的方向”是横向／虚度方向，光锥方向保持完整 （见第 7.6 小节的注）。

4.  **标签动量和残余动量的区分是不是人为的？分界线在哪？**

    答：分界线**确实是人为的**，但物理结果不依赖它——这正是 “标签／残余”表述必须配合零区间减除的原因。 如果你觉得这套记账法别扭，可以直接用位置空间的多极展开 （式 [eq:multipole]），那里没有人为分界。 两种表述给出相同的因子化定理与相同的反常量纲。

5.  **什么是零区间减除？为什么需要它？**

    答：把一个圈动量积分拆成“共线区域 $+$ 软区域”时， 两个区域在**重叠部分**被重复计算了 （回忆第 4.3 小节：$P_{qq}(z)$ 在 $z\to1$ 既软又共线）。 零区间减除就是减掉这个重叠：
$$

\text{总和}=\big(\text{共线}\big)+\big(\text{软}\big)-\big(\text{重叠}\big).

$$
在维数正规化中，重叠项常常是**无标度积分**因而为零（第 6.4 小节教训 (4)），所以“看起来没做什么”； 但在 $\mathrm{SCET}_{II}$ 里它非零且至关重要。

6.  **什么是快度发散？维数正规化为什么救不了它？**

    答：考虑一个软–共线同虚度的积分，沿 $(\ln k^+,\ln k^-)$ 平面的 **对角线方向**（即固定 $k^+k^-=$ 常数、让 $k^-/k^+\to\infty$）积分。 被积函数在这个方向上不衰减，给出 $\int dy$ 型的发散。 而维数正规化的 $\epsilon$ 只改变**虚度**方向的量纲计数， 对“沿固定虚度的对角线”无能为力。所以必须引入独立的 **快度正规化子**（常见记号 $\nu$、$\eta$、$\delta$、$\alpha$， 各家不同），并相应地有**快度重整化群**。 Becher–Neubert 的**共线异常**是处理同一问题的另一种 （在很多情形更简洁的）方式：它把快度依赖组织成一个普适的、 可指数化的因子 $\big(Q^2/\text{标度}^2\big)^{-F(\alpha_s)}$。

7.   **“加号分布”$[\,\cdot\,]_+$ 是什么？为什么处处都是它？**

    答：它是把“实发射的 $1/\tau$ 型端点发散”与“虚修正的 $\delta(\tau)$” 合并成一个良好定义的分布的记账方式，定义为
$$

\int_0^1\! d\tau\;\big[f(\tau)\big]_+\,g(\tau)
      =\int_0^1\! d\tau\; f(\tau)\big[g(\tau)-g(0)\big] .

$$
典型例子 $\Big[\dfrac{\ln\tau}{\tau}\Big]_+$。 在 SCET 中喷注函数与软函数的固定阶表达式就是这类分布， 它们的卷积（式 [eq:thrustfact] 中的 $\otimes$） 就是“分布的卷积”。技术上麻烦，概念上没有新东西。

8.  **$\mu$ 依赖看起来到处都有，怎么保证最终答案与 $\mu$ 无关？**

    答：靠一致性条件 [eq:consistency]。每个因子单独依赖 $\mu$， 但反常量纲之和为零，所以乘积（卷积）在**所计算的阶**上与 $\mu$ 无关。 实际操作中人们**故意**让每个因子在自己的自然标度取值 （$\mu_H,\mu_J,\mu_S$ 各不相同），这才实现重求和； 残留的 $\mu$ 依赖是高阶效应，常被用作**理论误差估计**。

9.  **SCET 与传统 QCD 重求和方法（CSS、Catani–Trentadue 等）是什么关系？**

    答：在两者都适用的范围内**结果一致**。SCET 的优势在于： （i）用算符与矩阵元给出每个因子的**定义**，从而可以逐阶计算、 逐阶重整化；（ii）幂次修正有系统的组织（$\mathcal L^{(k)}$）； （iii）把不同过程的共性暴露出来（同一个 $\Gamma_{\mathrm{cusp}}$、同一个 $J$）。 劣势是入门记号成本高——这份讲义就是为了降低这个成本。

10. **为什么处处是 $C_F$ 和 $4C_F$？这些数字要背吗？**

    答：不必背，但要知道**它们来自颜色荷**。eikonal 近似 （式 [eq:eikonal]）告诉我们软辐射只看颜色荷， 所以 $\Gamma_{\mathrm{cusp}}$ 的领头系数正比于发射者的 Casimir： 夸克线是 $C_F=4/3$，胶子线是 $C_A=3$（这叫 (Casimir scaling)，在三圈仍然成立，四圈开始破坏）。 听课时看到 $\Gamma_0=4C_F$，脑中应该立刻联想到 “这是一条夸克 Wilson 线的贡献”。

11. **$\lambda$ 到底该取多少？它是物理量吗？**

    答：$\lambda$ 不是物理量，是**记账参数**。它的值由所研究的运动学 区域决定（例如 thrust 问题里 $\lambda=\sqrt\tau$）。 重要的不是 $\lambda$ 的数值，而是**各个量按 $\lambda$ 的幂次排序**， 从而知道领头幂次结果的误差是 $\mathcal O(\lambda)$ 还是 $\mathcal O(\lambda^2)$。

# 听课重点

## 课前必须已经会的（自测清单）

在第一堂课之前，请确认自己能**不看讲义**完成以下各项：

1.  写出 $n,\bar n$ 的定义与归一化，并把任意 $p^\mu$ 分解成 [eq:lcdecomp]。

2.  由分解式推出 $p^2=p^+p^--\boldsymbol{p}_\perp^2$ 与 $p\cdot k=\frac12(p^+k^-+p^-k^+)-\boldsymbol{p}_\perp\!\cdot\!\boldsymbol{k}_\perp$。

3.  说明为什么 $n$-共线动量标度是 $Q(\lambda^2,1,\lambda)$， 以及 $\lambda$ 的几何含义（张角）。

4.  证明 $P_n=\not{n}\not{\bar{n}}/4$ 是幂等投影算符，并写出四条恒等式 [eq:fouriden]。

5.  复述 eikonal 近似的推导（三行），并说出它的物理含义。

6.  说清“双对数 $=$ 软对数 $\times$ 共线对数”。

7.  说清 $\mathrm{SCET}_{I}$ 与 $\mathrm{SCET}_{II}$ 的判据（虚度 vs. 快度）。

## 课上要盯住的五件事

$n\cdot\bar n=2$ 还是 $1$？$L=\ln(Q^2/\mu^2)$ 还是 $\ln(\mu^2/Q^2)$？ $D_\mu=\partial_\mu-igA_\mu$ 还是 $+$？三元组顺序是 $(+,-,\perp)$ 还是 $(-,+,\perp)$？ **把这四条抄在笔记第一页**，后面每个公式的符号都靠它。

老师写下一个算符时，用表 3 当场数一下阶数。 如果数出来不是领头幂次，就要问自己“为什么它还在这里” （通常答案是：这是幂次修正的一节，或者它被 Dirac 代数消灭了）。

是 UV 还是 IR？和谁抵消？这是理解匹配为什么合法的关键 （第 6.4 小节教训 (1)）。

硬函数、喷注函数、软函数的反常量纲里都有它，且系数受 一致性条件 [eq:consistency] 约束。 盯住 $\Gamma_{\mathrm{cusp}}$ 就能看清因子化的骨架。

领头幂次？哪个 $\lambda$？哪些模式被假定存在？ 什么情况下会失效（Glauber、端点发散、非全局对数 (non-global logarithms)）？ **EFT 的价值一半在于结论，一半在于误差估计。**

## 记笔记的建议

- 为“模式表”（表 2）与“场标度表”（表 3） 各留一页，全程增补。

- 画 $(\ln p^+,\ln p^-)$ 平面图（第 6.3 小节）， 每讲一个新过程就在图上标出它的模式。这张图能解决 80% 的困惑。

- 每个因子化定理旁边写三样东西： **自然标度**、**反常量纲**、**幂次修正阶数**。

- 遇到符号／约定冲突时不要硬记，回到定义式现推—— 这也是为什么本讲义坚持给出完整推导。

# 进一步学习路线

下面按**推荐阅读顺序**给出线索。arXiv 编号仅供检索定向， 若与老师给出的版本不符，以课程材料为准。

## 第一优先：系统性讲义

T. Becher, A. Broggio, A. Ferroglia, *Introduction to Soft-Collinear Effective Theory*, Lecture Notes in Physics 896 (Springer, 2015)，arXiv:1410.1892。  
**最贴合本课程的教材**。位置空间／多极展开表述， 与 Becher–Neubert 一系的记号一致。 建议与本讲义第 5–7 节对读。

M. Neubert, *Les Houches Lectures on Renormalization Theory and Effective Field Theories*，arXiv:1901.06573。  
**授课教师本人的讲义**。重整化、匹配、RG 的概念基础， 是理解“为什么匹配是 IR 有限的”最好的中文以外读物。 建议在读 SCET 之前先读这一份。

I. W. Stewart, MIT 8.851 *Effective Field Theory* 课程讲义 （MIT OpenCourseWare）。  
标签动量表述的标准来源，习题极佳。 与 \[1
$$

 对读可以同时掌握两套语言。

T. Cohen,  
*As Scales Become Separated: Lectures on Effective Field Theory*， arXiv:1711.00554。  
EFT 一般思想（含按区域展开）的友好入门， 适合补第 3 节的背景。

## 第二优先：原始文献（了解概念如何被建立）

C. W. Bauer, S. Fleming, M. Luke, *Summing Sudakov logarithms in $B\to X_s\gamma$ in effective field theory*，arXiv:hep-ph/0005275。  
SCET 的“第零篇”，从 $B\to X_s\gamma$ 出发。

C. W. Bauer, S. Fleming, D. Pirjol, I. W. Stewart, *An Effective Field Theory for Collinear and Soft Gluons: Heavy to Light Decays*，arXiv:hep-ph/0011336。  
共线拉氏量与标签动量表述的奠基文献。 本讲义第 7.2 小节的推导即出自此脉络。

C. W. Bauer, D. Pirjol, I. W. Stewart, *Soft-Collinear Factorization in Effective Field Theory*， arXiv:hep-ph/0109045。  
BPS 场重定义与软–共线解耦（本讲义式 [eq:BPS]–[eq:decoupling]）。

M. Beneke, A. P. Chapovsky, M. Diehl, T. Feldmann, *Soft-collinear effective theory and heavy-to-light currents beyond leading power*，arXiv:hep-ph/0206152。  
位置空间／多极展开表述，以及幂次修正的系统构造。

## 第三优先：与本课程主题直接相关的专题

T. Becher, M. Neubert, *Infrared singularities of scattering amplitudes in perturbative gauge theory*，arXiv:0903.1126 （以及后续 arXiv:0904.1021）。  
任意多腿振幅的红外结构与 $\Gamma_{\mathrm{cusp}}$ 的普适性。

T. Becher, M. Neubert, *Drell-Yan production at small $q_T$, transverse parton distributions and the collinear anomaly*，arXiv:1007.4005。  
**$\mathrm{SCET}_{II}$ 与共线异常的代表作**，与本讲义 第 10 节 Q6 直接对应。

J. Chiu, A. Jain, D. Neill, I. Z. Rothstein,  
*The Rapidity Renormalization Group*，arXiv:1104.0881。  
快度重整化群的另一套框架，与 

$$
10
$$

 互为参照。

M. Beneke, T. Feldmann, *Factorization of heavy-to-light form factors in soft-collinear effective theory*，arXiv:hep-ph/0211358。  
$B\to\pi$ 型形状因子（本讲义第 8.2 小节 (b)）。

## 背景与工具书

- A. V. Manohar, M. B. Wise, *Heavy Quark Physics* (Cambridge, 2000)：HQET 的标准教材， 对应本讲义第 3.3 小节。

- M. Neubert, *Heavy quark symmetry*, Phys. Rept. **245** (1994) 259， arXiv:hep-ph/9306320：授课教师的经典综述。

- V. A. Smirnov, *Applied Asymptotic Expansions in Momenta and Masses* (Springer)：**按区域展开的权威参考**， 本讲义第 6.4 小节的算例属于该书最简单的一类。

- R. K. Ellis, W. J. Stirling, B. R. Webber, *QCD and Collider Physics* (Cambridge)： 分裂函数、thrust、传统重求和的背景。

## 一条建议的四周自学路线

1.  本讲义第 1–4 节 $+$ 参考 

$$
4
$$

 （EFT 一般思想、按区域展开）。目标：能自己做第 6.4 小节的算例并推广到两圈玩具积分。

2.  本讲义第 5–6 节 $+$ 

$$
1
$$

 的 光锥与标度计数章节。目标：能独立数出任意算符的 $\lambda$ 阶数。

3.  本讲义第 7 节 $+$ 

$$
1
$$

 的拉氏量与 Wilson 线章节 $+$ 

$$
7
$$

。目标：能自己推 [eq:LSCET]，并解释 BPS 重定义。

4.  本讲义第 8 节 $+$ 

$$
1
$$

 的 thrust 章节 $+$ 

$$
10
$$

。 目标：能写下 [eq:thrustfact] 并用一致性条件 [eq:consistency] 自查反常量纲。

# Dirac 代数与光锥恒等式速查

#### 光锥向量。

$$
\begin{gathered}
  n^2=\bar n^2=0,\qquad n\cdot\bar n=2,\\
  n^\mu=(1,0,0,1),\qquad \bar n^\mu=(1,0,0,-1)\quad(\text{标准选择}),\\
  g_\perp^{\mu\nu}=g^{\mu\nu}-\frac{n^\mu\bar n^\nu+\bar n^\mu n^\nu}{2},
  \qquad g_{\perp\,\mu}^{\ \ \mu}=d-2 .
\end{gathered}
$$

#### $\gamma$ 矩阵。

$$
\begin{gathered}
  \not{n}\not{n}=\not{\bar{n}}\not{\bar{n}}=0,
  \qquad
  \not{n}\not{\bar{n}}+\not{\bar{n}}\not{n}=4,\\
  \mathrm{Tr}[\not{n}\not{\bar{n}}]=4\,(n\cdot\bar n)=8,\\
  \not{n}\gamma^\mu\not{n}=2n^\mu\,\not{n},
  \qquad
  \gamma_\perp^\mu\,\not{n}=-\not{n}\,\gamma_\perp^\mu,
  \qquad
  \gamma_\perp^\mu\,\not{\bar{n}}=-\not{\bar{n}}\,\gamma_\perp^\mu,\\
  \gamma_\perp^\mu\gamma_{\perp\mu}=d-2,\\
  \not{D}_\perp\not{D}_\perp=D_\perp^2-\frac{g_s}{2}\,
  \sigma_\perp^{\mu\nu}G^\perp_{\mu\nu},
  \qquad
  \sigma^{\mu\nu}\equiv\frac{i}{2}\big[\gamma^\mu,\gamma^\nu\big],
  \qquad
  \big[D_\mu,D_\nu\big]=-ig_s\,G_{\mu\nu} .
\end{gathered}
$$

 （末式对约定 $D_\mu=\partial_\mu-ig_sA_\mu$ 成立； 推导只需把 $\gamma^\mu\gamma^\nu$ 拆成对称与反对称部分。）

#### 投影算符。

$$
\begin{gathered}
  P_n=\frac{\not{n}\not{\bar{n}}}{4},\qquad P_{\bar n}=\frac{\not{\bar{n}}\not{n}}{4},
  \qquad P_n+P_{\bar n}=\mathbf1,\qquad P_n^2=P_n,\qquad P_nP_{\bar n}=0,\\
  P_n\gamma_\perp^\mu=\gamma_\perp^\mu P_{\bar n},
  \qquad
  \frac{\not{n}}{2}\frac{\not{\bar{n}}}{2}=P_n,\\
  \not{n}\,\xi_n=0,\quad \bar\xi_n\,\not{n}=0,\quad
  \not{\bar{n}}\,\eta_n=0,\quad \bar\eta_n\,\not{\bar{n}}=0,\quad
  \bar\xi_n\,\gamma_\perp^\mu\,\xi_n=0 .
\end{gathered}
$$

#### 分解式。

$$
\begin{gathered}
  p^\mu=(n\cdot p)\frac{\bar n^\mu}{2}+(\bar n\cdot p)\frac{n^\mu}{2}+p_\perp^\mu,\\
  \not{D}=\not{n}\,\frac{\bar n\cdot D}{2}+\not{\bar{n}}\,\frac{n\cdot D}{2}+\not{D}_\perp,\\
  p^2=p^+p^--\boldsymbol{p}_\perp^2,
  \qquad
  d^4p=\frac12\,dp^+dp^-d^2p_\perp,
  \qquad
  y=\frac12\ln\frac{p^-}{p^+} .
\end{gathered}
$$

# 标度计数一页速查

|                                 |           共线（$n$）           |        超软（$\mathrm{SCET}_{I}$）         |         软（$\mathrm{SCET}_{II}$）         |
|:--------------------------------|:-------------------------------:|:------------------------------------------:|:------------------------------------------:|
| 动量 $(p^+,p^-,p_\perp)/Q$      |     $(\lambda^2,1,\lambda)$     |     $(\lambda^2,\lambda^2,\lambda^2)$      |        $(\lambda,\lambda,\lambda)$         |
| 虚度 $p^2/Q^2$                  |           $\lambda^2$           |                $\lambda^4$                 |                $\lambda^2$                 |
| 坐标 $(x^+,x^-,x_\perp)\cdot Q$ | $(1,\lambda^{-2},\lambda^{-1})$ | $(\lambda^{-2},\lambda^{-2},\lambda^{-2})$ | $(\lambda^{-1},\lambda^{-1},\lambda^{-1})$ |
| $d^4x$                          |         $\lambda^{-4}$          |               $\lambda^{-8}$               |               $\lambda^{-4}$               |
| 夸克场                          |       $\xi_n\sim\lambda$        |           $q_{us}\sim\lambda^3$            |           $q_s\sim\lambda^{3/2}$           |
| 胶子场 $A^\mu$                  |     $(\lambda^2,1,\lambda)$     |                $\lambda^2$                 |                 $\lambda$                  |
| 场强 $F$                        |           $\lambda^2$           |                $\lambda^4$                 |                $\lambda^2$                 |
| $\mathcal L^{(0)}$              |           $\lambda^4$           |                $\lambda^8$                 |                $\lambda^4$                 |

**使用方法**：任给一个算符，把各因子的 $\lambda$ 幂次相加， 与同扇区的 $\mathcal L^{(0)}$ 比较；差 $\lambda^k$ 即为 $k$ 阶幂次修正。 若结果是 $\lambda^0$ 差异却不在领头拉氏量中，检查是否被 Dirac 代数 （如 $\bar\xi_n\gamma_\perp\xi_n=0$）消灭。
