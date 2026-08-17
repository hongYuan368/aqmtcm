# 广义对称性（Generalized Symmetry）课前预习讲义 — 面向 Daniel Brennan 教授课程《Generalized Symmetry》

*课前自学材料（简体中文，英文术语另列）*

> 本文由 LaTeX 课前讲义转换为 Markdown，可在 GitHub 直接阅读。公式已按 GitHub 渲染要求处理（独立公式块、常用宏已展开）。若仍有个别公式异常，请对照同目录 `.tex`。

> **摘要**
>
> 本讲义为选修 Daniel Brennan 教授《广义对称性》（Generalized Symmetry） 课程的同学准备的**课前预习**材料。预设读者学过基础量子力学与量子场论 （正则量子化、路径积分、Feynman 规则），但**没有系统学习过广义对称性／ 高阶形式对称性**（higher-form symmetry），也可能对微分形式语言不熟悉。
>
> 讲义围绕一条主线展开：**对称性 $=$ 拓扑算符** （(symmetry) $=$ (topological operator)）。 这句话是整个领域的“重新表述”（reformulation），一旦接受它， “为什么可以有 $p$-form 对称性”“为什么会有不可逆对称性” 就都变成自然的推论，而不是需要额外记忆的新概念。为此我们： （一）先用最传统的 Noether 定理把守恒流推出来， 再**把它改写成拓扑算符**，让读者亲眼看到两种语言等价； （二）**完整给出每一步数学推导**，包括微分形式、Stokes 定理、 Maxwell 理论中 1-form 对称性的全部细节，每一步都可用纸笔复核； （三）强调物理图像与**可证伪的判据** （“怎样判断某个算符是拓扑的”“怎样判断对称性被自发破缺”）。
>
> 所有英文术语首次出现时括号标注，并在第 11 节汇总为英汉术语表。

# 导读

## 这门课到底在讲什么

过去十年，量子场论（(quantum field theory), QFT）中“对称性”的定义被 系统地扩充了。传统教科书里的对称性是：

*一个群 $G$ 作用在场上，使作用量不变；由 Noether 定理得到守恒流 $j^\mu$ 与守恒荷 $Q$。*

这个定义有三个隐含假设，而**每一个都可以去掉**：

1.  **荷作用在局域算符（点状对象）上**。 去掉它 $\Rightarrow$ 荷可以作用在**线、面等拓展对象**上， 得到 $p$-form 对称性（$p$-form symmetry）。

2.  **对称性作用是可逆的（群）**。 去掉它 $\Rightarrow$ **不可逆对称性** （non-invertible symmetry），对称算符只满足融合代数 （fusion algebra）而未必有逆。

3.  **对称性由连续变换的生成元定义**。 去掉它 $\Rightarrow$ 离散、有限群甚至“范畴型”对称性 （categorical symmetry）都被统一描述。

把这三条统称为**广义（全局）对称性** （generalized global symmetry）。它们的共同语言是： 

$$
\boxed{\ \text{一个对称性} \;\Longleftrightarrow\;
  \text{一族\emph{拓扑}算符（在时空中支撑于某个子流形上）}\ }
$$

## 为什么值得学

这不只是形式上的重新包装，它带来了真正的新结果：

- **禁闭的对称性判据**。4 维 $\mathrm{SU}(N)$ Yang–Mills 理论有一个 $\mathbb{Z}_N$ 的 1-form 中心对称性（center symmetry）； **禁闭（confinement）等价于这个 1-form 对称性未被自发破缺**， Wilson 圈的面积律就是它的序参量。这把“禁闭”从一个定性描述 变成了一个对称性破缺的判断（第 10 节）。

- **新的 ’t Hooft 反常与相图约束**。高阶形式对称性之间的混合反常 （mixed anomaly）给出对低能物理的严格限制， 例如 4 维 Yang–Mills 在 $\theta$ 角处的相变结构。

- **“同一个局域理论”的全局结构分类**。$\mathrm{U}(1)$ 与 $\mathrm{U}(1)/\mathbb{Z}_N$ 规范理论有相同的局域动力学，却有不同的线算符谱； 这种差别正是由 1-form 对称性的“规范化”（gauging）选择决定的。

- **不可逆对称性带来的选择定则**。例如 Kramers–Wannier 对偶 在 2 维 Ising 临界点上就是一条不可逆拓扑线， 它给出普通群论看不到的关联函数约束。

## 本讲义的结构与建议读法

本讲义有意把“旧语言”与“新语言”**并置**：

- 第 2–4 节完全是传统内容 （群论、拉氏量、正则量子化、Noether 定理）， 但**结尾处做一次关键改写**（第 4.6 小节）， 把 $Q$ 写成 $\int_\Sigma\star j$ 并证明它只依赖 $\Sigma$ 的同调类。 **这一步是整门课的枢纽**，请务必自己推一遍。

- 第 5–6 节介绍拓展算符与拓扑算符， 把“对称性 $=$ 拓扑算符”这句话讲清楚。

- 第 7 节做推广，第 8 节区分 “荷”与“缺陷”。

- 第 9 节是**全篇重心**：Ising 的 $\mathbb{Z}_2$、 Maxwell 理论 1-form 对称性的完整推导、$\mathrm{U}(1)$ 对偶直觉。

- 第 10–14 节是自发破缺、反常、术语表、 困惑澄清、听课重点与文献路线。

#### 三条阅读路径。

第 2.4 小节（微分形式速成）$\to$ 第 4.6 小节（$Q$ 的拓扑改写）$\to$ 第 7 节的表 1（$p$-form 对称性字典）$\to$ 第 9.2 小节（Maxwell 例子）$\to$ 第 11 节术语表 $\to$ 第 13 节听课重点。

按顺序全读并完成正文中的**练习**。重点动手项有四个： Noether 流的两个例子；Ward 恒等式； Maxwell 的 Gauss 律推导； Wilson 圈与 ’t Hooft 线的连接数计算。

第 2.4 小节 $+$ 附录 15（微分形式与拓扑速查）。

## 符号与约定

- 时空维数记作 $d$（含时间），度规号差取 $\eta_{\mu\nu}=\mathrm{diag}(-,+,+,\dots,+)$， 除特别说明外用自然单位 $\hbar=c=1$。 **注意**：广义对称性文献中 $(-,+,\dots)$ 与 $(+,-,\dots)$ 两种号差都常见，欧氏与洛伦兹信号也混用； 本讲义在需要时会明确指出。

- 时空流形记作 $\mathcal{M}_d$（或 $X$）；其中的 $k$ 维闭子流形记作 $\Sigma_k,\ \mathcal{M}_k,\ C$（曲线）等。

- 微分形式用 $\omega_{(p)}$ 表示 $p$-形式；外微分 $\mathrm{d}$， Hodge 星号 $\star$。

- “$q$-form 对称性”中的 $q$ 指**被作用的带荷对象的维数** （$q=0$ 即普通对称性作用在点状局域算符上）。 这是 Gaiotto–Kapustin–Seiberg–Willett 的约定，全篇统一使用。

- 规范场 $A$ 视作 1-形式（$A=A_\mu\mathrm{d}x^\mu$）， 场强 $F=\mathrm{d}A$。规范群为 $\mathrm{U}(1)$ 时 $A$ 是实的； 非阿贝尔时 $A$ 取值于李代数。

**注意。**

本领域**约定极不统一**：$2\pi$ 因子的位置、 电磁对偶中 $e^2$ 的放法、“$p$-form”里 $p$ 指荷还是指算符维数、 反常的符号……都因作者而异。本讲义的策略是： **每个关键公式都给出可自查的推导**， 这样即使老师用了别的约定，你也能当场把因子对上。

# 预备知识

本节复习后面要用的四样工具：群论语言、拉氏量形式、正则量子化， 以及**微分形式**。前三样多数读者已熟悉，可快速浏览； 第 2.4 小节即使学过也建议细读， 因为广义对称性的全部陈述都写在这套语言里。

## 群论基础

**定义（群）。**

集合 $G$ 配一个乘法 $G\times G\to G$，满足结合律、存在单位元 $e$、 每个元素 $g$ 存在逆元 $g^{-1}$。若还满足 $g_1g_2=g_2g_1$，称 **阿贝尔群**（abelian group）。

后面反复出现的具体群：

- $\mathbb{Z}_N=\{0,1,\dots,N-1\}$，加法模 $N$；等价地 $\{1,\omega,\dots,\omega^{N-1}\}$，$\omega=e^{2\pi i/N}$，乘法。 阿贝尔、有限、**离散**。

- $\mathrm{U}(1)=\{e^{i\alpha}:\alpha\in[0,2\pi)\}$：阿贝尔、**连续**、紧致。 它是本课程最重要的群。

- $\mathrm{SU}(N)$：非阿贝尔、连续、紧致。其**中心** （center）为 

$$
Z\big(\mathrm{SU}(N)\big)
            =\Big\{\omega\,\mathbf 1_N:\ \omega^N=1\Big\}\cong\mathbb{Z}_N .
$$

 这个 $\mathbb{Z}_N$ 将在第 9.2.6 小节变成 1-form 对称性。

**定义（表示）。**

群 $G$ 的（有限维）**表示**（representation）是同态 $\rho:G\to GL(V)$，即 $\rho(g_1g_2)=\rho(g_1)\rho(g_2)$。 物理上：场按某个表示变换，$\phi\to\rho(g)\phi$。

**例（$\mathbb{Z}_N$ 的一维表示与“$N$ 度”）。**

 $\mathbb{Z}_N$ 的所有一维表示为 $\rho_n(\omega)=\omega^n$，$n=0,\dots,N-1$。 对 $\mathrm{SU}(N)$ 的表示 $R$，其中心 $\omega\mathbf 1$ 作用为 $\rho_R(\omega\mathbf 1)=\omega^{n_R}\mathbf 1$， $n_R\in\mathbb{Z}_N$ 称为该表示的 **$N$ 度**（$N$-ality）。 基本表示 $n=1$，伴随表示 $n=0$。 第 9.2.6 小节会看到：$n_R$ 就是 Wilson 线在 1-form 中心对称性下的荷。

#### 李代数与生成元。

对连续群，取 $g=e^{i\alpha^aT^a}$， $T^a$ 为生成元，满足 $[T^a,T^b]=if^{abc}T^c$。 无穷小变换 $\delta\phi=i\alpha^aT^a\phi$。 对 $\mathrm{U}(1)$ 只有一个生成元，$\delta\phi=i\alpha\phi$。

#### 正规子群与商群。

若 $H\triangleleft G$，可作商 $G/H$。 这在“规范化对称性”（gauging）时至关重要： 规范化 $H$ 得到的理论，其对称性与 $G/H$ 有关， 且会**产生新的对偶对称性**（第 8.5 小节）。

**例（$\mathrm{U}(1)$ 与 $\mathrm{U}(1)/\mathbb{Z}_N$）。**

$\mathbb{Z}_N\subset\mathrm{U}(1)$（$N$ 次单位根）， $\mathrm{U}(1)/\mathbb{Z}_N\cong\mathrm{U}(1)$ 作为抽象群同构， 但作为**规范群**它们给出不同理论： 允许的电荷格（charge lattice）不同。 第 9.3 小节会回到这一点。

## 拉氏量形式

场论由作用量给出。设场为 $\phi^a(x)$（$a$ 标记场的种类与分量）， 

$$
S[\phi]=\int_{\mathcal{M}_d}\mathrm{d}^dx\;\mathcal{L}\big(\phi^a,\partial_\mu\phi^a\big).
$$

**命题（Euler–Lagrange 方程）。**

$S$ 在 $\phi\to\phi+\delta\phi$（$\delta\phi$ 在边界上为零）下取极值的条件是 

$$
\boxed{\ \frac{\partial \mathcal{L}}{\partial \phi^a}
  -\partial_\mu\!\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\right)=0\ }
$$

**证明。**

$$
\begin{aligned}
  \delta S
  &=\int\mathrm{d}^dx\left[\frac{\partial \mathcal{L}}{\partial \phi^a}\delta\phi^a
    +\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\partial_\mu\delta\phi^a\right]
  \notag\\
  &=\int\mathrm{d}^dx\left[\frac{\partial \mathcal{L}}{\partial \phi^a}
    -\partial_\mu\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\right]\delta\phi^a
    +\underbrace{\int\mathrm{d}^dx\;\partial_\mu\!\left[
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\delta\phi^a\right]}_{\text{边界项}=0} .
\end{aligned}
$$

 因 $\delta\phi^a$ 任意，方括号必须为零。

**例（本讲义要用的三个拉氏量）。**

1.  **实标量**：$\mathcal{L}=-\tfrac12\partial_\mu\varphi\partial^\mu\varphi
            -V(\varphi)$。若 $V(\varphi)=V(-\varphi)$，有 $\mathbb{Z}_2$ 对称性 $\varphi\to-\varphi$。

2.  **复标量**：$\mathcal{L}=-\partial_\mu\phi^*\partial^\mu\phi-V(|\phi|^2)$， 有 $\mathrm{U}(1)$ 对称性 $\phi\to e^{i\alpha}\phi$。

3.  **Maxwell**：$\mathcal{L}=-\dfrac{1}{4e^2}F_{\mu\nu}F^{\mu\nu}$， $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$。 **注意这里没有带电物质场**——这正是第 9.2 小节能找到 1-form 对称性的原因。

（号差 $(-,+,+,+)$；不同号差下整体符号会变，物理结论不变。）

## 正则量子化简要

正则量子化的三步：

1.  **定义共轭动量** 

$$
\pi_a(x)=\frac{\partial \mathcal{L}}{\partial \dot\phi^a(x)} .
$$

2.  **等时正则关系**（把 Poisson 括号换成交换子） 

$$
\big[\phi^a(t,\boldsymbol{x}),\ \pi_b(t,\boldsymbol{y})\big]
              =i\,\delta^a_{\ b}\,\delta^{d-1}(\boldsymbol{x}-\boldsymbol{y}),
              \qquad
              [\phi,\phi]=[\pi,\pi]=0 .
$$

3.  **Hamilton 量生成时间演化** 

$$
H=\int\mathrm{d}^{d-1}x\,\big(\pi_a\dot\phi^a-\mathcal{L}\big),
              \qquad
              \dot{\mathcal{O}}=i[H,\mathcal{O}] .
$$

**要点。**

本讲义只用正则量子化做一件事： **验证守恒荷 $Q$ 确实生成对称变换**（第 4.4 小节）。 这条验证是理解 [eq:slogan] 的必要一步： “对称算符”$U=e^{i\alpha Q}$ 之所以是算符， 正因为 $Q$ 由场算符构成并作用在 Hilbert 空间上。

#### 路径积分表述。

后面讨论关联函数与 Ward 恒等式时会用 

$$
\big\langle \mathcal{O}_1(x_1)\cdots\mathcal{O}_n(x_n)\big\rangle
  =\frac{1}{Z}\int\!\mathcal{D}\phi\;
  \mathcal{O}_1(x_1)\cdots\mathcal{O}_n(x_n)\;e^{iS[\phi]},
  \qquad
  Z=\int\!\mathcal{D}\phi\;e^{iS[\phi]} .
$$

 在欧氏信号下 $e^{iS}\to e^{-S_E}$。 **广义对称性的大部分论证在欧氏信号、路径积分语言下最自然**， 因为“把算符支撑在任意子流形上并连续形变”在那里是显然的操作。

## 微分形式速成

这是本节最重要的部分。广义对称性的所有陈述—— 守恒律、算符支撑、连接数——都用微分形式写才简洁。

### $p$-形式与楔积

**定义（$p$-形式）。**

$d$ 维流形上的 **$p$-形式**（$p$-form）是完全反对称张量场， 写作 

$$
\omega=\frac{1}{p!}\,\omega_{\mu_1\cdots\mu_p}\,
  \mathrm{d}x^{\mu_1}\wedge\cdots\wedge\mathrm{d}x^{\mu_p},
  \qquad
  \omega_{\cdots\mu_i\cdots\mu_j\cdots}=-\omega_{\cdots\mu_j\cdots\mu_i\cdots} .
$$

 $p=0$ 即标量函数。因反对称性，$d$ 维中 $p>d$ 的形式恒为零。

**楔积**（wedge product）满足 

$$
\mathrm{d}x^\mu\wedge \mathrm{d}x^\nu=-\,\mathrm{d}x^\nu\wedge \mathrm{d}x^\mu,
  \qquad
  \omega_{(p)}\wedge\eta_{(q)}=(-1)^{pq}\,\eta_{(q)}\wedge\omega_{(p)} .
$$

 特别地，奇数次形式与自身的楔积为零：$\omega_{(1)}\wedge\omega_{(1)}=0$。

### 外微分

**定义（外微分）。**

$\mathrm{d}:\Omega^p\to\Omega^{p+1}$， 

$$
\mathrm{d}\omega=\frac{1}{p!}\,\partial_\nu\omega_{\mu_1\cdots\mu_p}\,
  \mathrm{d}x^\nu\wedge \mathrm{d}x^{\mu_1}\wedge\cdots\wedge \mathrm{d}x^{\mu_p} .
$$

两条核心性质： 

$$
\boxed{\ \mathrm{d}^2=0\ },
  \qquad
  \mathrm{d}\big(\omega_{(p)}\wedge\eta_{(q)}\big)
  =\mathrm{d}\omega_{(p)}\wedge\eta_{(q)}
  +(-1)^p\,\omega_{(p)}\wedge \mathrm{d}\eta_{(q)} .
$$

 $\mathrm{d}^2=0$ 的理由：$\mathrm{d}^2\omega$ 的系数含 $\partial_\rho\partial_\nu\omega_{\cdots}$， 对 $\rho\nu$ 对称，而 $\mathrm{d}x^\rho\wedge \mathrm{d}x^\nu$ 反对称，故相消。

**例（电磁学就是外微分）。**

$A=A_\mu \mathrm{d}x^\mu$ 是 1-形式， 

$$
F=\mathrm{d}A=\partial_\mu A_\nu\,\mathrm{d}x^\mu\wedge \mathrm{d}x^\nu
  =\frac12\big(\partial_\mu A_\nu-\partial_\nu A_\mu\big)
  \mathrm{d}x^\mu\wedge \mathrm{d}x^\nu
  =\frac12 F_{\mu\nu}\mathrm{d}x^\mu\wedge \mathrm{d}x^\nu .
$$

 于是 Bianchi 恒等式**自动成立**： 

$$
\mathrm{d}F=\mathrm{d}^2A=0
  \qquad\Longleftrightarrow\qquad
  \partial_{[\rho}F_{\mu\nu]}=0 .
$$

 规范变换 $A\to A+\mathrm{d}\lambda$ 使 $F$ 不变，同样因 $\mathrm{d}^2=0$。

**定义（闭形式与恰当形式）。**

$\mathrm{d}\omega=0$ 称 $\omega$ **闭**（closed）； $\omega=\mathrm{d}\eta$ 称 $\omega$ **恰当**（exact）。 由 $\mathrm{d}^2=0$，恰当 $\Rightarrow$ 闭；反之不一定 （差别由拓扑刻画，见 [eq:deRham]）。

### Stokes 定理

**定理（Stokes）。**

设 $\mathcal{M}_{p+1}$ 是 $(p+1)$ 维带边流形，边界 $\partial\mathcal{M}_{p+1}$， $\omega$ 为 $p$-形式，则 

$$
\boxed{\ \int_{\mathcal{M}_{p+1}}\mathrm{d}\omega
  =\int_{\partial\mathcal{M}_{p+1}}\omega\ }
$$

**要点。**

 **Stokes 定理是本课程使用频率最高的工具。** 广义对称性中几乎每一次“算符可以自由形变”的论证， 都是 [eq:stokes] 加上“被积形式是闭的”这两件事的组合。 请把这句话记牢：

*闭形式在同调等价的子流形上积分值相同。*

**证明（要点（同调不变性））。**

设 $\Sigma$ 与 $\Sigma'$ 是两个 $p$ 维闭子流形， 且它们“同调”（homologous），即存在 $(p+1)$ 维 $V$ 使 $\partial V=\Sigma-\Sigma'$。若 $\mathrm{d}\omega=0$，则 

$$
\int_\Sigma\omega-\int_{\Sigma'}\omega
  =\int_{\partial V}\omega
  =\int_V \mathrm{d}\omega=0 .
$$

### Hodge 星号与守恒律

**定义（Hodge 星号）。**

在 $d$ 维带度规流形上，$\star:\Omega^p\to\Omega^{d-p}$， 

$$
(\star\omega)_{\mu_1\cdots\mu_{d-p}}
  =\frac{1}{p!}\,\sqrt{|g|}\;
  \epsilon_{\mu_1\cdots\mu_{d-p}\nu_1\cdots\nu_p}\,
  \omega^{\nu_1\cdots\nu_p} .
$$

 在欧氏号差下 $\star\star=(-1)^{p(d-p)}$；洛伦兹号差下多一个整体负号。

现在是关键的翻译。设 $j=j_\mu \mathrm{d}x^\mu$ 为 1-形式电流， 则 $\star j$ 是 $(d-1)$-形式，$\mathrm{d}\star j$ 是 $d$-形式，正比于体积元：

**命题（守恒律的形式语言）。**

$$
\boxed{\ \partial_\mu j^\mu=0
  \qquad\Longleftrightarrow\qquad
  \mathrm{d}\star j=0\ }
$$

**证明。**

由 [eq:hodge]，$(\star j)_{\mu_1\cdots\mu_{d-1}}
=\sqrt{|g|}\,\epsilon_{\mu_1\cdots\mu_{d-1}\nu}j^\nu$。 取外微分并注意 $d$-形式空间是一维的（正比于 $\mathrm{d}^dx$），得 

$$
\mathrm{d}\star j=\big(\partial_\mu j^\mu\big)\sqrt{|g|}\;
  \mathrm{d}x^1\wedge\cdots\wedge \mathrm{d}x^d
  =\big(\partial_\mu j^\mu\big)\,\mathrm{vol}_d .
$$

 故 $\mathrm{d}\star j=0$ 当且仅当 $\partial_\mu j^\mu=0$。

同理，对反对称的 $(q+1)$ 阶张量电流 $J^{\mu_1\cdots\mu_{q+1}}$（即 $(q+1)$-形式 $J$）： 

$$
\partial_{\mu_1}J^{\mu_1\cdots\mu_{q+1}}=0
  \qquad\Longleftrightarrow\qquad
  \mathrm{d}\star J=0 ,
  \qquad
  \star J\in\Omega^{d-q-1} .
$$

 **请记住 $\star J$ 的次数是 $d-q-1$**： 它决定了对称算符支撑在多少维的子流形上（第 7 节）。

### de Rham 上同调与连接数

**定义（de Rham 上同调）。**

$$
H^p(\mathcal{M},\mathbb{R})
  =\frac{\{\text{闭 }p\text{-形式}\}}{\{\text{恰当 }p\text{-形式}\}} .
$$

 它测量“闭但不恰当”的程度，是纯拓扑量。

**例（$S^2$ 上的磁通）。**

球面 $S^2$ 上 $H^2(S^2)\cong\mathbb{R}\ne0$。 磁单极子场强 $F$ 满足 $\mathrm{d}F=0$ 但**不能**整体写成 $\mathrm{d}A$， 其“通量” $\frac{1}{2\pi}\oint_{S^2}F=m\in\mathbb{Z}$ 就是拓扑数 （Dirac 量子化）。这个例子将在第 9.2.4 小节直接使用。

**定义（连接数）。**

 设 $\mathcal{M}_p$ 与 $\mathcal{M}_q$ 是 $d$ 维时空中两个**不相交**的闭子流形， 且 

$$
\boxed{\ p+q+1=d\ }
$$

 则可定义整数**连接数**（linking number）$\mathrm{Link}(\mathcal{M}_p,\mathcal{M}_q)$： 取 $(p+1)$ 维 $V$ 使 $\partial V=\mathcal{M}_p$， 则 $\mathrm{Link}=$ $V$ 与 $\mathcal{M}_q$ 的（带符号）相交数。

**例（$d=3$：两条圈）。**

$p=q=1$，$1+1+1=3$ $\checkmark$。这就是通常绳结理论里两条闭曲线的连接数。

**例（$d=4$：2 维面与 1 维圈）。**

$p=2,q=1$，$2+1+1=4$ $\checkmark$。 一个 2 维球面 $\Sigma_2$ 可以“套住”一条曲线 $C$。 这正是第 9.2 小节中对称算符与 Wilson 线的关系。

**要点。**

 条件 [eq:linkdim] 是全课程的**维数记账法则**。 遇到任何“对称算符作用在带荷对象上”的陈述， 先用它检查维数是否配得上：配不上就一定记错了。

#### $\delta$-函数形式（Poincaré 对偶）。

对 $d$ 维时空中的 $k$ 维闭子流形 $\mathcal{M}_k$， 定义 $(d-k)$-形式 $\delta_{\mathcal{M}_k}$，使得对任意 $k$-形式 $\omega$ 

$$
\int_{\mathcal{M}_d}\delta_{\mathcal{M}_k}\wedge\omega
  =\int_{\mathcal{M}_k}\omega .
$$

 它是“支撑在 $\mathcal{M}_k$ 上的 $\delta$ 函数”。 这个记号能把“线算符插入”写进运动方程，见 [eq:modifiedEOM]。

**练习。**

 (a) 在 $d=4$ 中验证 $F\wedge F$ 是 4-形式， 并证明 $F\wedge F=\mathrm{d}(A\wedge F)$， 即 $\int F\wedge F$ 是拓扑项（$\theta$ 项）。  
(b) 用 [eq:hodge] 验证 $d=4$ 中 $\star(\mathrm{d}x^0\wedge \mathrm{d}x^1)\propto \mathrm{d}x^2\wedge \mathrm{d}x^3$。  
(c) 对 $q$-form 电流，用 [eq:linkdim] 验证： 若对称算符支撑在 $(d-q-1)$ 维流形上， 则带荷对象必为 $q$ 维。

# 普通对称性：连续／离散、全局／规范

在推广之前，必须把“普通对称性”的三组区分讲得非常干净， 因为广义对称性的每一步推广都精确地对应着放松其中某一条。

## 对称性的定义

**定义（经典对称性）。**

一个场变换 $\phi^a\to\phi'^a=\phi^a+\delta\phi^a$ 称为作用量 $S$ 的 **对称性**，若 

$$
S[\phi']=S[\phi]
  \qquad\text{或更一般地}\qquad
  \delta\mathcal{L}=\partial_\mu K^\mu
$$

 即拉氏量最多变化一个全导数（此时作用量在合适边界条件下不变）。

**注意。**

量子层面上还要求**路径积分测度**不变； 测度不变性的破坏就是**反常**（anomaly）。 第 10 节会区分两类反常： “阻碍规范化”的 ’t Hooft 反常，与“真正破坏守恒律”的 ABJ 型反常。

## 连续 vs 离散

- **连续对称性**（continuous symmetry）： 变换由连续参数标记，如 $\phi\to e^{i\alpha}\phi$。 存在无穷小形式 $\delta\phi=i\alpha\phi$， 因此**有 Noether 流**（第 4 节）。

- **离散对称性**（discrete symmetry）： 如 $\varphi\to-\varphi$（$\mathbb{Z}_2$）、时间反演 $T$、 空间反射 $P$、电荷共轭 $C$。**没有**连续参数， 因此**没有守恒流**，只有守恒的算符 $U$（$U^2=1$ 等）。

**要点。**

 传统教科书对离散对称性的处理是“瘸腿”的： 有对称算符 $U$ 却没有流，于是所有以 $j^\mu$ 为中心的技术 （Ward 恒等式、荷代数）都用不上。

**广义对称性的第一个好处就是修好了这条腿**： 把对称性定义为**拓扑算符**而不是流， 连续与离散就被统一处理了——连续情形的算符恰好可以写成 $\exp(i\alpha\int\star j)$，离散情形则不能，但两者都是拓扑算符。 这也是为什么本课程能同时讨论 $\mathbb{Z}_2$ 与 $\mathrm{U}(1)$。

## 全局 vs 规范：本课程最重要的区分

**定义（全局与规范）。**

若变换参数 $\alpha$ 是**常数**（不依赖时空点）， 称**全局对称性**（global symmetry）； 若参数可取任意函数 $\alpha(x)$ 而作用量仍不变 （通常需引入规范场），称**规范对称性**（gauge symmetry）。

**注意（必须彻底接受的观念）。**

 **规范对称性不是对称性，而是描述的冗余** （redundancy of description）。理由：

- 规范变换**不改变物理态**：$|\psi\rangle$ 与其规范变换像 是 Hilbert 空间中*同一个*矢量；物理 Hilbert 空间由 规范不变态构成（Gauss 律约束）。

- 因此规范“对称性”**不能自发破缺**， 也没有相应的选择定则。所谓“Higgs 机制破坏规范对称性” 是一种历史遗留的说法，严格讲被破坏的是全局部分。

- **全局**对称性才有物理后果： 选择定则、Goldstone 玻色子、’t Hooft 反常约束。

本课程标题里的“广义对称性”全称是**广义全局对称性** （generalized global symmetry）——中间那个 “global” 不是装饰。

**要点。**

 虽然规范对称性本身不是对称性， 它却是**产生**高阶形式对称性的主要机制：

*规范场的存在使得线／面算符（Wilson 线等）成为自然的观测量， 而作用在这些拓展算符上的对称性就是高阶形式对称性。*

这就是为什么第 9 节的核心例子全是规范理论。

**例（对比表）。**

考虑复标量 $\phi$，电荷 1。

|                    | 全局 $\mathrm{U}(1)$                     | 规范 $\mathrm{U}(1)$                                              |
|:-------------------|:-----------------------------------------|:------------------------------------------------------------------|
| 变换               | $\phi\to e^{i\alpha}\phi$，$\alpha$ 常数 | $\phi\to e^{i\alpha(x)}\phi$，$A_\mu\to A_\mu+\partial_\mu\alpha$ |
| 是否需引入 $A_\mu$ | 否                                       | 是                                                                |
| 守恒流             | $j^\mu$，物理可测                        | $j^\mu$ 成为 Gauss 律约束                                         |
| 可否自发破缺       | 可以（Goldstone）                        | 不可（只是冗余）                                                  |
| 物理后果           | 选择定则、粒子数守恒                     | 定义相互作用、无独立后果                                          |

**练习。**

说明为什么“规范对称性不能自发破缺”与“超导体中 $\mathrm{U}(1)$ 被破坏” 这两句话并不矛盾。（提示：超导中被破坏的是电子数的*全局* $\mathrm{U}(1)$；而规范场获得质量的现象在广义对称性语言中可描述为 1-form 对称性的行为，见第 9.2.7 小节。）

# Noether 定理完整推导

本节给出完整推导：变分 $\to$ 守恒流 $\to$ 守恒荷 $\to$ （关键一步）**拓扑算符**。前三步是标准内容， 第四步是通往广义对称性的门。

## 定理与推导

**定理（Noether）。**

 设 $S=\int \mathrm{d}^dx\,\mathcal{L}(\phi^a,\partial_\mu\phi^a)$ 在无穷小变换 

$$
\phi^a\longrightarrow\phi^a+\epsilon\,\Delta^a(\phi,\partial\phi)
$$

 下满足 $\delta\mathcal{L}=\epsilon\,\partial_\mu K^\mu$（$\epsilon$ 为常数）。 则在运动方程成立时（on-shell），电流 

$$
\boxed{\ j^\mu=\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\Delta^a-K^\mu\ }
$$

 满足守恒律 $\partial_\mu j^\mu=0$。

**证明。**

**第 1 步（变分）。**直接对 $\mathcal{L}$ 做变分， 注意 $\delta(\partial_\mu\phi^a)=\partial_\mu(\delta\phi^a)$： 

$$
\delta\mathcal{L}
  =\frac{\partial \mathcal{L}}{\partial \phi^a}\,\delta\phi^a
  +\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\partial_\mu\big(\delta\phi^a\big),
  \qquad \delta\phi^a=\epsilon\Delta^a .
$$

**第 2 步（用运动方程消去 $\partial\mathcal{L}/\partial\phi$）。** 由 Euler–Lagrange 方程 [eq:EL]， 

$$
\frac{\partial \mathcal{L}}{\partial \phi^a}
  =\partial_\mu\!\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\right).
$$

 代入 [eq:noether1]： 

$$
\begin{aligned}
  \delta\mathcal{L}
  &=\partial_\mu\!\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\right)\epsilon\Delta^a
   +\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\partial_\mu\big(\epsilon\Delta^a\big)
  \notag\\[2pt]
  &=\epsilon\,\partial_\mu\!\left[
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\Delta^a\right],
  
\end{aligned}
$$

 最后一步就是乘积法则的逆用（这里用到 $\epsilon$ 是常数）。

**第 3 步（与假设比较）。** 按对称性假设 $\delta\mathcal{L}=\epsilon\,\partial_\mu K^\mu$， 与 [eq:noether3] 相减： 

$$
\epsilon\,\partial_\mu\!\left[
  \frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\Delta^a-K^\mu\right]=0 .
$$

 因 $\epsilon\ne0$ 任意，方括号的散度为零，即 [eq:noethercurrent]。

**注（为什么必须“在壳”）。**

第 2 步用了运动方程。这是本质的： **Noether 守恒律是运动方程的推论**， 而不是恒等式。对比 [eq:bianchi] 的 Bianchi 恒等式 $\mathrm{d}F=0$——它*不*依赖运动方程，是恒等式。 第 9.2 小节会看到，这两类来源 分别给出 Maxwell 理论的**电**与**磁** 1-form 对称性， 而“一个来自运动方程、一个来自恒等式”这个区别正是 它们在加入物质场后命运不同的原因。

## 从流到荷

**命题（守恒荷）。**

定义在固定时刻 $t$ 的空间切片上的积分 

$$
Q(t)=\int_{\mathbb{R}^{d-1}}\mathrm{d}^{d-1}x\;j^0(t,\boldsymbol{x}),
$$

 若场在空间无穷远处足够快衰减，则 $\dfrac{\mathrm{d}Q}{\mathrm{d}t}=0$。

**证明。**

$$
\frac{\mathrm{d}Q}{\mathrm{d}t}
  =\int \mathrm{d}^{d-1}x\;\partial_0 j^0
  \overset{\partial_\mu j^\mu=0}{=}
  -\int \mathrm{d}^{d-1}x\;\partial_i j^i
  \overset{\text{Stokes}}{=}
  -\oint_{S^{d-2}_\infty}\mathrm{d}S_i\;j^i=0 .
$$

**注意。**

“衰减足够快”不是小事。若允许场在无穷远不衰减， $Q$ 可以不守恒，或者出现**额外**的守恒荷。 本课程后面会看到，正是对“边界／无穷远行为”的仔细处理 区分了不同的全局结构。

## 两个完整算例

**例（复标量的 $\mathrm{U}(1)$ 流）。**

 取例 [ex:threelag](2)： $\mathcal{L}=-\partial_\mu\phi^*\partial^\mu\phi-V(|\phi|^2)$。 对称变换 $\phi\to e^{i\alpha}\phi$，无穷小 

$$
\delta\phi=i\alpha\phi,\qquad \delta\phi^*=-i\alpha\phi^* .
$$

 势项只依赖 $|\phi|^2$ 故不变；动能项也不变，所以 $K^\mu=0$。 计算导数： 

$$
\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi)}=-\partial^\mu\phi^*,
  \qquad
  \frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^*)}=-\partial^\mu\phi .
$$

 代入 [eq:noethercurrent]（把 $\alpha$ 提出，$\Delta=i\phi$， $\Delta^*=-i\phi^*$）： 

$$
\begin{aligned}
  j^\mu
  &=\big(-\partial^\mu\phi^*\big)\big(i\phi\big)
   +\big(-\partial^\mu\phi\big)\big(-i\phi^*\big)
  \notag\\
  &=i\left(\phi^*\partial^\mu\phi-\phi\,\partial^\mu\phi^*\right).
  
\end{aligned}
$$

 验证守恒： 

$$
\partial_\mu j^\mu
  =i\left(\phi^*\Box\phi-\phi\,\Box\phi^*\right)
  \overset{\text{EOM}}{=}
  i\left(\phi^*\,\phi\,V'-\phi\,\phi^*\,V'\right)=0 . \checkmark
$$

 （用了运动方程 $\Box\phi=V'(|\phi|^2)\phi$ 及其复共轭。）

**例（平移与能量–动量张量）。**

 取变换为时空平移 $x^\mu\to x^\mu-\epsilon^\nu\delta^\mu_\nu$， 即 $\delta\phi^a=\epsilon^\nu\partial_\nu\phi^a$。 此时 $\mathcal{L}$ 本身也平移：$\delta\mathcal{L}=\epsilon^\nu\partial_\nu\mathcal{L}
=\epsilon^\nu\partial_\mu(\delta^\mu_\nu\mathcal{L})$， 故 $K^\mu{}_\nu=\delta^\mu_\nu\mathcal{L}$。代入 [eq:noethercurrent]： 

$$
\boxed{\ T^\mu{}_\nu
  =\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\,\partial_\nu\phi^a
  -\delta^\mu_\nu\,\mathcal{L}\ },
  \qquad
  \partial_\mu T^\mu{}_\nu=0 .
$$

 每个 $\nu$ 给一个守恒流；对应的荷是能量与动量 $P_\nu=\int \mathrm{d}^{d-1}x\,T^0{}_\nu$。

**练习。**

对实标量 $\mathcal{L}=-\tfrac12(\partial\varphi)^2-V(\varphi)$， 证明 $\mathbb{Z}_2$ 对称性 $\varphi\to-\varphi$ **不**给出 Noether 流 （提示：$\Delta$ 必须是无穷小的，而 $\varphi\to-\varphi$ 无法连续地 连到恒等变换）。这再次说明要点 [kp:discrete] 的必要性。

## 荷生成对称变换（正则验证）

守恒荷不只是个数，它是**生成元**。这里用例 [ex:u1current] 做完整验证。

自由复标量（$V=m^2|\phi|^2$）的共轭动量 

$$
\pi=\frac{\partial \mathcal{L}}{\partial \dot\phi}=\dot\phi^*,
  \qquad
  \pi^*=\frac{\partial \mathcal{L}}{\partial \dot\phi^*}=\dot\phi .
$$

 由 [eq:u1current] 取 $\mu=0$（号差 $(-,+,+,+)$ 下 $\partial^0=-\partial_0$，此处把整体符号吸收进 $Q$ 的定义， 最终结论不依赖该约定）： 

$$
j^0=i\big(\phi\,\pi-\phi^*\pi^*\big),
  \qquad
  Q=\int \mathrm{d}^{d-1}x\;i\big(\phi\,\pi-\phi^*\pi^*\big).
$$

 用正则关系 [eq:canonical]， $[\phi(\boldsymbol{x}),\pi(\boldsymbol{y})]=i\delta^{d-1}(\boldsymbol{x}-\boldsymbol{y})$： 

$$
\begin{aligned}
  \big[Q,\phi(\boldsymbol{x})\big]
  &=\int \mathrm{d}^{d-1}y\;i\,\phi(\boldsymbol{y})\,
    \big[\pi(\boldsymbol{y}),\phi(\boldsymbol{x})\big]
  \notag\\
  &=\int \mathrm{d}^{d-1}y\;i\,\phi(\boldsymbol{y})\,
    \big(-i\,\delta^{d-1}(\boldsymbol{x}-\boldsymbol{y})\big)
  \;=\;\phi(\boldsymbol{x}).
  
\end{aligned}
$$

 （$\phi^*\pi^*$ 项与 $\phi$ 交换为零。）于是对有限参数 

$$
\boxed{\ U_\alpha=e^{i\alpha Q}:
  \qquad
  U_\alpha\,\phi(x)\,U_\alpha^{-1}
  =\phi+i\alpha[Q,\phi]+\cdots
  =e^{i\alpha}\phi(x)\ }
$$

 恰好是我们出发的对称变换。$\checkmark$

**要点。**

 [eq:Uacts] 定义的 $U_\alpha=e^{i\alpha Q}$ 就是**对称算符** （symmetry operator）。注意它满足 

$$
U_\alpha\,U_\beta=U_{\alpha+\beta},
  \qquad
  U_\alpha^{-1}=U_{-\alpha},
$$

 即**可逆**，且乘法就是群 $\mathrm{U}(1)$ 的乘法。 广义对称性放松的正是 [eq:groupfusion]： 若只要求算符相乘时闭合成某个代数而不要求有逆， 就得到不可逆对称性。

## Ward 恒等式：荷如何“测量”算符

在关联函数层面，对称性表现为 Ward 恒等式。 设 $\mathcal{O}(y)$ 是带荷 $q$ 的局域算符，即 

$$
U_\alpha\,\mathcal{O}(y)\,U_\alpha^{-1}=e^{iq\alpha}\,\mathcal{O}(y),
  \qquad\text{无穷小地}\qquad
  \delta\mathcal{O}=i q\alpha\,\mathcal{O}.
$$

#### 推导。

在路径积分 [eq:pathintegral] 中做一个**局域**的 变换 $\phi\to\phi+\epsilon(x)\Delta$，其中参数 $\epsilon$ 现在依赖 $x$。 因为常数 $\epsilon$ 时 $\delta S=0$，一般 $\epsilon(x)$ 时 $\delta S$ 必须 正比于 $\partial_\mu\epsilon$： 

$$
\delta S=-\int \mathrm{d}^dx\;\epsilon(x)\,\partial_\mu j^\mu ,
$$

 （把 $\int\partial_\mu\epsilon\,j^\mu$ 分部积分而得）。 路径积分对场的重命名不变，故 

$$
0=\delta\Big\langle \mathcal{O}(y)\Big\rangle
  =\Big\langle i\,\delta S\;\mathcal{O}(y)\Big\rangle
   +\Big\langle \delta\mathcal{O}(y)\Big\rangle .
$$

 代入 [eq:deltaSlocal] 与 $\delta\mathcal{O}(y)=i q\,\epsilon(y)\mathcal{O}(y)$， 并对任意 $\epsilon(x)$ 成立，得

**命题（Ward 恒等式）。**

$$
\boxed{\
  \partial_\mu\big\langle j^\mu(x)\,\mathcal{O}(y)\big\rangle
  = q\;\delta^{d}(x-y)\,\big\langle \mathcal{O}(y)\big\rangle \ }
$$

 （整体符号依赖 $j$ 与 $Q$ 的符号约定；结构是关键。）

#### 最重要的推论。

把 [eq:ward] 在一个包住 $y$ 的 $d$ 维区域 $V$ 上积分，并用 Stokes 定理： 

$$
\oint_{\partial V}\big\langle \star j\;\mathcal{O}(y)\big\rangle
  =\int_V \big\langle \mathrm{d}\star j\;\mathcal{O}(y)\big\rangle
  = q\,\big\langle\mathcal{O}(y)\big\rangle
  \qquad (y\in V).
$$

**要点。**

 [eq:chargebylinking] 是本讲义**第一个真正重要的结论**：

*把对称算符支撑在一个包围算符 $\mathcal{O}$ 的闭曲面上， 测得的就是 $\mathcal{O}$ 的荷。*

换句话说，**“带荷”是一个关于“包围”（拓扑连接）的陈述**， 而不是关于“在同一点”的陈述。 一旦这样理解，把“包围”换成“连接”就自然地推广到 高维带荷对象——这就是 $p$-form 对称性。

## 关键改写：$Q$ 是拓扑算符

现在做整门课的枢纽一步。把 [eq:chargedef] 的荷用微分形式重写：

**定义（曲面上的荷）。**

对 $d$ 维时空中任意闭的 $(d-1)$ 维子流形 $\Sigma_{d-1}$，定义 

$$
\boxed{\ Q(\Sigma_{d-1})=\int_{\Sigma_{d-1}}\star j ,
  \qquad
  U_\alpha(\Sigma_{d-1})=\exp\!\Big[i\alpha\!\int_{\Sigma_{d-1}}\star j\Big]\ }
$$

取 $\Sigma_{d-1}=\{t=\text{const}\}$ 的空间切片就回到 [eq:chargedef]（因为 $\star j$ 在等时面上的分量正是 $j^0$）。 但 [eq:Qsurface] 允许 $\Sigma$ 是**任意**闭曲面—— 甚至是弯曲的、不等时的、多个连通分支的。

**定理（对称算符是拓扑的）。**

 设 $\mathrm{d}\star j=0$（即 $\partial_\mu j^\mu=0$）。 若 $\Sigma$ 与 $\Sigma'$ 同调，即存在 $d$ 维区域 $V$ 使 $\partial V=\Sigma-\Sigma'$，且 $V$ 内没有带荷算符插入，则 

$$
Q(\Sigma)=Q(\Sigma'),
  \qquad
  U_\alpha(\Sigma)=U_\alpha(\Sigma') .
$$

**证明。**

直接用 Stokes 定理 [eq:stokes] 与守恒律： 

$$
Q(\Sigma)-Q(\Sigma')
  =\int_{\partial V}\star j
  =\int_V \mathrm{d}\star j
  =0 .
$$

**要点。**

 定理 [thm:topological] 就是标语 [eq:slogan]。请体会它的分量：

1.  **“守恒”与“拓扑”是同一件事的两种说法。** $\partial_\mu j^\mu=0$ $\Leftrightarrow$ $U_\alpha(\Sigma)$ 在连续形变下不变。

2.  **对称算符不必放在等时面上。** 它是一个支撑在*某个子流形*上的算符， 这件事在传统表述里完全被“$Q=\int \mathrm{d}^{d-1}x\,j^0$”掩盖了。

3.  **“不变”有前提**：形变过程中不能扫过带荷算符。 若扫过了，$Q$ 就跳变一个荷量——这正是 [eq:chargebylinking] 的内容，也是对称性作用的机制。

4.  **定义里已经不再需要 $j$ 了。** 我们真正用到的只是“存在一族支撑在 $(d-1)$ 维闭曲面上的、 拓扑的、可逆的算符”。把 $j$ 扔掉， 离散对称性也被涵盖；把维数改掉，$p$-form 对称性就出现了。

**注（两种“不变”的对比）。**

初学时容易混淆两句话：

- “$Q$ 不随时间变化”——传统说法， 对应 $\Sigma$ 与 $\Sigma'$ 是两个不同时刻的等时面。

- “$Q(\Sigma)$ 只依赖 $\Sigma$ 的同调类”——广义说法， 上一条是它的特例（两个等时面确实同调， 中间夹的 $V$ 就是这段时空）。

所以广义表述**严格更强**，并没有丢掉任何旧内容。

**练习。**

 (a) 在 $d=4$ 中，取 $\Sigma$ 为半径 $R$ 的球面 $\times$ 时间区间的边界， 说明 [eq:topological] 如何同时包含“电荷守恒”与“电荷与 $R$ 无关”。  
(b) 若 $V$ 内含有一个荷为 $q$ 的算符 $\mathcal{O}$， 把定理 [thm:topological] 的证明与 [eq:chargebylinking] 结合， 写出 $Q(\Sigma)-Q(\Sigma')$ 等于多少。  
(c) 用 [eq:linkdim] 检查：$(d-1)$ 维对称算符与 $0$ 维局域算符的连接数是否有定义？ （答：$(d-1)+0+1=d$ $\checkmark$。）

# QFT 中的算符与关联函数：局域 vs 拓展

要谈“作用在线上的对称性”，先要承认线本身是合法的观测量。 本节把算符按**支撑集维数**分类。

## 关联函数是理论的定义

一个 QFT 的全部信息可以编码在所有算符的关联函数中： 

$$
\big\langle \mathcal{O}_1(x_1)\,\mathcal{O}_2(x_2)\cdots\big\rangle .
$$

 两个理论若所有关联函数相同，就是同一个理论。 所以**“有哪些算符”是理论定义的一部分**—— 这句话在第 9.3 小节会变得非常实在： $\mathrm{U}(1)$ 与 $\mathrm{U}(1)/\mathbb{Z}_N$ 规范理论的*局域*动力学完全相同， 差别只在**允许哪些线算符存在**。

## 局域算符

**定义（局域算符）。**

**局域算符**（local operator）支撑在时空中的一个**点**上： $\mathcal{O}(x)$。它是 $0$ 维算符。

例子：$\varphi(x)$、$\phi^*\phi(x)$、$T^{\mu\nu}(x)$、 $F_{\mu\nu}F^{\mu\nu}(x)$，以及 2 维 CFT 中的顶点算符 $e^{i n\varphi(x)}$。

**注意。**

在规范理论中，$\phi(x)$ 本身**不是**好的算符（不规范不变）。 规范不变的局域算符必须是如 $|\phi|^2$、$F_{\mu\nu}F^{\mu\nu}$ 之类。 这个限制**正是**拓展算符登场的原因： 带电荷的信息无法装进局域算符，只能装进线算符。

## 拓展算符

**定义（拓展算符）。**

**拓展算符**（extended operator）支撑在时空中一个 $p$ 维子流形上（$p\ge1$），记作 $\mathcal{O}(\mathcal{M}_p)$。 $p=1$ 称**线算符**（line operator）， $p=2$ 称**面算符**（surface operator），依此类推。

**例（Wilson 线：最重要的线算符）。**

 对 $\mathrm{U}(1)$ 规范场，沿闭曲线 $C$ 定义 

$$
\boxed{\ W_n(C)=\exp\!\left[i\,n\oint_C A\right]
  =\exp\!\left[i\,n\oint_C A_\mu\,\mathrm{d}x^\mu\right],
  \qquad n\in\mathbb{Z}\ }
$$

 **规范不变性**：在 $A\to A+\mathrm{d}\lambda$ 下 

$$
\oint_C A\;\longrightarrow\;\oint_C A+\oint_C \mathrm{d}\lambda
  =\oint_C A+\int_{\partial C}\lambda
  =\oint_C A ,
$$

 因为 $C$ 闭合故 $\partial C=\emptyset$。$\checkmark$

**整数量子化**：若 $\lambda$ 是允许绕圈的（大规范变换）， $\oint_C \mathrm{d}\lambda\in2\pi\mathbb{Z}$，要求 $W$ 单值就需 $n\in\mathbb{Z}$。

**物理意义**：$W_n(C)$ 是一个**电荷为 $n$ 的无穷重（探针）粒子 沿 $C$ 运动的世界线**。取 $C$ 为时间方向的直线即一个静止的静态电荷。

对非阿贝尔群，需路径有序化并取迹： 

$$
W_R(C)=\mathrm{Tr}_R\,\mathbf{P}\exp\!\left[i\oint_C A\right].
$$

**例（’t Hooft 线）。**

 **’t Hooft 线**（’t Hooft line）$T_m(C)$ 是**磁**荷 $m$ 的 探针粒子（磁单极子）的世界线。它不像 [eq:wilson] 那样有简单的 “$\exp\oint$”表达式，而是通过**边界条件**定义： 要求在环绕 $C$ 的小球面 $S^2$ 上 

$$
\frac{1}{2\pi}\oint_{S^2}F=m\in\mathbb{Z}.
$$

 即“挖掉 $C$ 并规定其周围有 $m$ 个单位磁通”。 在对偶描述中（$F\leftrightarrow\star F$）它变成 Wilson 线。

**例（面算符与其他）。**

2-维面算符的例子：

- $\exp\big[i\alpha\int_{\Sigma_2}\star F/e^2\big]$—— 第 9.2 小节的**对称算符**本身。

- 2 维中的**拓扑缺陷线**（(topological defect line), TDL）—— 第 9.1 小节的 Ising 例子。

- 弦的世界面、畴壁（domain wall）。

## “真算符” vs “可端接的算符”

一个重要而微妙的区分：

**定义（真算符与非真算符）。**

一个线算符若能**独立**定义在任意闭曲线上， 称**真线算符**（genuine line operator）。 若它必须作为某个面算符的边界出现 （即“线只能是面的边”），则称**非真的** （non-genuine）。

**例（被屏蔽的 Wilson 线）。**

 若理论中存在**动力学的**电荷 1 的物质场 $\psi$， 则 $W_1$ 可以“断开”：一段开放的 Wilson 线 $\bar\psi(x)\,e^{i\int_x^y A}\,\psi(y)$ 是规范不变的局域算符对。 于是 $W_1(C)$ 不再携带守恒的荷——它可以被物质屏蔽 （screened）。 **这就是电 1-form 对称性被动力学电荷破坏的机制** （第 9.2.5 小节量化）。

**要点。**

 判断一个理论有没有 1-form 对称性，操作上就是问：

*存在不能被任何动力学物质端接或屏蔽的线算符吗？*

有 $\Rightarrow$ 它们按某个群分类，那个群就是 1-form 对称群。

# 拓扑算符的物理图像

第 4.6 小节已经证明对称算符是拓扑的。 本节反过来，把“拓扑算符”当作**出发点**， 建立完整的物理图像。

## 定义与判据

**定义（拓扑算符）。**

 支撑在闭子流形 $\mathcal{M}_k$ 上的算符 $U(\mathcal{M}_k)$ 称为**拓扑的** （topological），若在**任何**关联函数中， 连续形变 $\mathcal{M}_k\to\mathcal{M}_k'$ 都不改变结果， 只要形变过程中 $\mathcal{M}_k$ **不扫过其他算符插入点**： 

$$
\big\langle U(\mathcal{M}_k)\;\mathcal{O}_1\cdots\mathcal{O}_n\big\rangle
  =\big\langle U(\mathcal{M}_k')\;\mathcal{O}_1\cdots\mathcal{O}_n\big\rangle .
$$

**注（等价的三种判据）。**

以下三条等价，实际计算中常混用：

1.  关联函数在形变下不变（[eq:topodef]，最本质）。

2.  该算符与能量–动量张量“解耦”： $U$ 不依赖度规，即 $\delta U/\delta g_{\mu\nu}=0$。 直觉：不依赖度规 $\Rightarrow$ 不知道距离与形状 $\Rightarrow$ 拓扑。

3.  对连续对称性，被积形式是闭的：$\mathrm{d}\star J=0$ （由定理 [thm:topological]）。

**例（对照：不是拓扑的算符）。**

$\exp\big[i\oint_C A\big]$（Wilson 线）**不是**拓扑算符： 它的期望值依赖 $C$ 的面积或周长（第 9.2.7 小节）。 而 $\exp\big[i\alpha\oint_{\Sigma_2}\star F/e^2\big]$ **是**拓扑算符 （因为 $\mathrm{d}\star F=0$）。 **这个对照极其重要**：Wilson 线是*带荷对象*， 面算符是*对称算符*，两者角色完全不同，不要混为一谈。

## 融合：拓扑算符的乘法

把两个拓扑算符支撑在同一个（或无限接近的）子流形上， 它们的乘积仍是拓扑算符，可以按某种规则重新展开：

**定义（融合规则）。**

$$
U_a(\mathcal{M}_k)\times U_b(\mathcal{M}_k)
  =\sum_c N_{ab}^{\ \ c}\;U_c(\mathcal{M}_k),
  \qquad N_{ab}^{\ \ c}\in\mathbb{Z}_{\ge0}
$$

 称**融合规则**（fusion rule）。

两种情形：

- **可逆（群）情形**：右边只有一项且系数为 1， $U_a\times U_b=U_{a\cdot b}$。 此时 $\{U_a\}$ 构成群，存在 $U_{a^{-1}}$ 使 $U_a\times U_{a^{-1}}=U_{\mathbf 1}$。 这是普通对称性，如 [eq:groupfusion]。

- **不可逆情形**：右边是多项之和， 于是**没有**逆元。此时称 **不可逆对称性**（non-invertible symmetry）。 典型例子（第 9.1 小节）： 

$$
\mathcal N\times\mathcal N=\mathbf 1+\eta .
$$

**要点。**

 为什么把不可逆的东西也叫“对称性”？因为对称性的**实用价值** ——给出关联函数的**选择定则与约束**——只需要 “存在拓扑算符”这一条，并不需要可逆性。 拓扑性保证算符可以自由移动、穿过、包围其他算符， 从而产生恒等式；有没有逆元并不影响这一点。

## 作用机制：穿过与包围

拓扑算符怎样“作用”在别的算符上？有两个等价图像。

#### 图像一：包围（测量荷）。

把 $U_\alpha(\Sigma_{d-1})$ 收缩成一个包围 $\mathcal{O}(y)$ 的小球面。 由 [eq:chargebylinking]， 

$$
U_\alpha\big(S^{d-1}\text{ 包围 }y\big)\;\mathcal{O}(y)
  = e^{iq\alpha}\,\mathcal{O}(y) .
$$

 若 $\Sigma$ 不包围任何算符，可以收缩到一点并消失（$=1$）。

#### 图像二：穿过（作用于态）。

在正则量子化图像中，取 $\Sigma$ 为等时面， 则 $U_\alpha$ 是作用在 Hilbert 空间上的算符。 把 $\Sigma$ 从 $\mathcal{O}$ 的“过去”移动到“未来”， 就相当于让 $U$ **穿过** $\mathcal{O}$： 

$$
U_\alpha\;\mathcal{O}(y)\;U_\alpha^{-1}=e^{iq\alpha}\,\mathcal{O}(y)
  \qquad\Longleftrightarrow\qquad
  U_\alpha\,\mathcal{O}(y)=e^{iq\alpha}\,\mathcal{O}(y)\,U_\alpha .
$$

两个图像的等价性：把 [eq:passthrough] 里“穿过前”减“穿过后”， 两张等时面拼成一个包围 $\mathcal{O}$ 的闭曲面，就回到 [eq:surround]。 下面这个“图”值得自己画一遍：

|               包围图像               |                       |                    穿过图像                     |
|:------------------------------------:|:---------------------:|:-----------------------------------------------:|
| $\Sigma$ 是包住 $\mathcal{O}$ 的小球 | $\Longleftrightarrow$ |          $\Sigma$ 是等时面，前后各一张          |
|         读出 $e^{iq\alpha}$          | $\Longleftrightarrow$ | 交换 $U$ 与 $\mathcal{O}$ 得相位 $e^{iq\alpha}$ |
|          适合欧氏／路径积分          |                       |            适合洛伦兹／Hilbert 空间             |

**要点。**

 **学会在两个图像间自由切换**是听这门课的核心技能。 课堂上说“把这条线扫过那个算符”“把这个面收缩掉”时， 用的是图像一的语言； 说“荷”“选择定则”“Hilbert 空间分解”时，用的是图像二的语言。

## 为什么“拓扑”正好对应“对称性”

最后回答一个概念性问题：为什么拓扑性是对称性的本质， 而不只是一个附带性质？

1.  **拓扑性 $=$ 守恒**。定理 [thm:topological]： 算符可形变 $\Leftrightarrow$ $\mathrm{d}\star j=0$。 “荷不随时间变化”只是“可以把曲面往时间方向推”的特例。

2.  **拓扑性 $=$ 与动力学无关**。 拓扑算符不依赖度规，因而不依赖能标； 它在紫外与红外**同样有效**。 这正是对称性能给出严格约束（而非近似关系）的原因， 也是**反常匹配**（第 10.2.3 小节） 能成立的根据。

3.  **拓扑性 $=$ 可以放在任何地方**。 既然能任意形变，就能支撑在任意维数的子流形上—— 只要那个维数使得“包围／连接”有意义。 这直接给出下一节的推广。

# 从 0-form 到 $p$-form：广义全局对称性

现在做推广。所有材料都已就位，推广本身只是**改一个数字**。

## 推广的逻辑

回顾普通（$0$-form）对称性的三个要素：

| 要素         | $0$-form 情形                             |
|:-------------|:------------------------------------------|
| 守恒流       | 1-形式 $j$，$\mathrm{d}\star j=0$         |
| 对称算符支撑 | $(d-1)$ 维闭曲面 $\Sigma_{d-1}$（余维 1） |
| 带荷对象     | $0$ 维局域算符 $\mathcal{O}(y)$           |
| 连接数条件   | $(d-1)+0+1=d$ $\checkmark$                |

把最后一行的“$0$”换成“$q$”，其他各行随之调整，就得到定义。

**定义（$q$-form 全局对称性）。**

 $d$ 维 QFT 具有**$q$-form 全局对称性**（$q$-form global symmetry） 群 $G$，指存在一族算符 $U_g(\mathcal{M}_{d-q-1})$，$g\in G$，满足：

1.  支撑在**余维 $q+1$**（即维数 $d-q-1$）的闭子流形上；

2.  **拓扑**（定义 [def:topological]）；

3.  融合遵循群乘法： $U_g\times U_h=U_{gh}$（可逆情形）；

4.  作用在**$q$ 维带荷算符**上，通过连接数给出相位／作用。

对连续 $G=\mathrm{U}(1)$，存在守恒的 $(q+1)$-形式电流 $J$： 

$$
\boxed{\ \mathrm{d}\star J=0,
  \qquad
  U_\alpha(\mathcal{M}_{d-q-1})
  =\exp\!\left[i\alpha\!\int_{\mathcal{M}_{d-q-1}}\star J\right]\ }
$$

 其中 $\star J\in\Omega^{d-q-1}$，次数与支撑维数匹配。$\checkmark$

**要点。**

 **维数自查三连**。看到任何 $q$-form 对称性的陈述， 立刻检查： 

$$
\begin{aligned}
  \text{电流次数}&=q+1, \\
  \text{对称算符维数}&=d-q-1
  \quad(\text{余维 } q+1), \\
  \text{带荷对象维数}&=q,
  \qquad (d-q-1)+q+1=d\ \checkmark
\end{aligned}
$$

 三者必须同时对上。这条自查能挡掉初学阶段 90% 的错误。

## 字典表

| $q$   | 电流       | 对称算符支撑         | 带荷对象        | 典型例子                                                                                                                                                                                                  |
|:------|:-----------|:---------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $0$   | 1-形式 $j$ | $(d-1)$ 维（余维 1） | 点（局域算符）  | 粒子数 $\mathrm{U}(1)$、Ising $\mathbb{Z}_2$                                                                                                                                                              |
| $1$   | 2-形式 $J$ | $(d-2)$ 维（余维 2） | 线（Wilson 线） | Maxwell 电／磁对称性、$\mathrm{SU}(N)$ 中心                                                                                                                                                               |
| $2$   | 3-形式 $J$ | $(d-3)$ 维（余维 3） | 面（弦世界面）  | 2-形式规范场理论、轴子弦                                                                                                                                                                                  |
| $d-1$ | $d$-形式   | $0$ 维（点）         | $(d-1)$ 维      | “宇宙分解”，见第 12 节 Q[q:dminus1] |

$q$-form 对称性字典（$d$ 维时空）。

**例（$d=4$，$q=1$：本课程主力）。**

$d=4$ 中的 1-form 对称性： 电流是 2-形式，对称算符支撑在 $4-1-1=2$ 维闭曲面上， 带荷对象是 1 维的线算符。 第 9.2 小节将完整实现这个例子。

## 高阶形式对称性必定是阿贝尔的

一个漂亮而重要的结构性结果：

**命题。**

 对 $q\ge1$，$q$-form 对称性群必为阿贝尔群。

**证明（物理论证）。**

对 $q\ge1$，对称算符支撑在维数 $d-q-1\le d-2$ 的子流形上， 即**余维至少 2**。余维 $\ge2$ 的两个子流形在 $d$ 维空间中 可以**互相绕过而不相交**：想象 $d=3$ 中两条直线（余维 2）， 它们可以平移错开。

因此对任意两个对称算符 $U_g(\mathcal{M})$、$U_h(\mathcal{M}')$， 总能连续地把它们交换位置而不让支撑集相交； 由拓扑性，关联函数在此过程中不变，故 

$$
U_g\,U_h=U_h\,U_g
  \qquad\Longrightarrow\qquad
  gh=hg .
$$

对比 $q=0$：对称算符是余维 1 的（等时面）， 两张等时面**无法**互相绕过——它们有确定的时间先后顺序， 所以乘法可以不交换，允许非阿贝尔群。

**要点。**

命题 [prop:abelian] 解释了为什么文献中 1-form 对称性总是 $\mathrm{U}(1)$、$\mathbb{Z}_N$ 这类阿贝尔群， 而 0-form 可以是 $\mathrm{SU}(2)$ 之类。 **“余维 1 才有时间顺序”这个直觉**值得记住， 它在讨论不可逆对称性时还会用到。

## 离散情形与 $\mathbb{Z}_N$

对离散群没有流，但定义 [def:qform] 的 (1)(2)(3)(4) 仍然成立。 最常见的是 $\mathbb{Z}_N$ 的 $q$-form 对称性： 算符 $U_k(\mathcal{M}_{d-q-1})$，$k\in\mathbb{Z}_N$，满足 

$$
U_k\times U_l=U_{k+l\ \mathrm{mod}\ N},
  \qquad
  \big(U_1\big)^N=\mathbf 1 .
$$

 作用在带荷 $n$ 的 $q$ 维算符上给相位 $e^{2\pi i kn/N}$。 第 9.2.6 小节的 $\mathrm{SU}(N)$ 中心对称性正是此类。

## 不可逆与高群：概念地图

为免第一堂课被术语淹没，这里给一张**概念地图**， 说明各名词的相互关系。它们都是“对称性 $=$ 拓扑算符”的不同放松方向。

| 名称                                                       | 放松了什么                          | 本讲义位置                                                                                                                                                                               |
|:-----------------------------------------------------------|:------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $q$-form 对称性                                            | 带荷对象可以是 $q$ 维               | 第 7 节                                                                                                    |
| 高群（higher group）        | 不同 $q$ 的对称性非平凡地纠缠在一起 | 本小节（仅概念）                                                                                                                                                                         |
| 不可逆对称性                                               | 融合规则无逆元                      | 第 9.1 小节、Q[q:noninv] |
| 范畴型对称性（categorical） | 用融合范畴而非群来组织全部拓扑算符  | 第 14 节文献                                                                                           |

**注（高群一句话）。**

若把一个 0-form 对称性的背景场 $A$ 打开后， 1-form 对称性的背景场 $B$ 的规范变换里出现了 $A$ （形如 $B\to B+\mathrm{d}\lambda+\text{（含 }A\text{ 的项）}$）， 则两者不能独立处理，合起来叫**2-群**。 第一次听课时只需知道这个词的存在。

# 荷与缺陷

本节澄清一组极易混淆的概念：**对称算符**、**带荷算符**、 **缺陷**。三者维数不同、角色不同， 课堂上若混用会完全听不懂。

## 三类对象的严格区分

|                  |                                                  |                                                 |                                       |
|:-----------------|:-------------------------------------------------|:------------------------------------------------|:--------------------------------------|
|                  | 对称算符                                         | 带荷算符                                        | 缺陷                                  |
|                  | (symmetry operator) | (charged operator) | (defect) |
| 维数（$q$-form） | $d-q-1$                                          | $q$                                             | 多为 $d-q-1$，但**不闭合**            |
| 是否拓扑         | **是**                                           | 一般**否**                                      | 视情形                                |
| 是否可形变       | 是                                               | 否（期望值依赖形状）                            | 端点／边界固定                        |
| 作用             | 测量／作用于他者                                 | 被测量                                          | 修改真空／边界条件                    |
| Maxwell 例子     | $e^{i\alpha\oint_{\Sigma_2}\star F/e^2}$         | $W_n(C)$                                        | 开放的对称算符                        |
| Ising 例子       | $\prod_j\sigma^x_j$                              | $\sigma^z_j$                                    | 畴壁                                  |

## 荷：由连接数定义

**定义（$q$-form 荷）。**

设 $\mathcal{O}(\mathcal{M}_q)$ 是 $q$ 维算符，$U_\alpha(\mathcal{M}_{d-q-1})$ 是 $q$-form 对称算符。称 $\mathcal{O}$ 带荷 $n$，若 

$$
\boxed{\
  \big\langle U_\alpha(\mathcal{M}_{d-q-1})\;\mathcal{O}(\mathcal{M}_q)\;\cdots\big\rangle
  = e^{\,i\alpha\,n\,\mathrm{Link}(\mathcal{M}_{d-q-1},\,\mathcal{M}_q)}\;
  \big\langle \mathcal{O}(\mathcal{M}_q)\cdots\big\rangle \ }
$$

这是 [eq:surround] 的直接推广：$q=0$ 时“连接”就是“包围”。

**要点。**

 **荷不是“在算符上贴的标签”，而是一个连接数的读数。** 这个转变是理解广义对称性的心理门槛。 一旦接受它，就不会再问“一条线怎么可能带荷”—— 因为荷本来就是“别的东西绕着它转一圈得到的相位”。

## 缺陷：把对称算符“打开”

**定义（对称缺陷）。**

把对称算符 $U_g$ 支撑在一个**带边**的子流形上 （即不闭合），得到的对象称**对称缺陷** （symmetry defect）或**扭曲缺陷**（twist defect）。 其**边界**是一个更低维的对象， 在该边界上理论被修改。

**例（Ising 畴壁：最直观的缺陷）。**

 1$+$<!-- -->1 维 Ising 链（第 9.1 小节）的 $\mathbb{Z}_2$ 对称算符是 

$$
U=\prod_{j=-\infty}^{+\infty}\sigma^x_j
  \qquad(\text{支撑在整条空间切片上，闭合}).
$$

 把乘积**截断**到半无穷区间： 

$$
U_{\text{半}}=\prod_{j\le 0}\sigma^x_j
  \qquad(\text{不闭合}) .
$$

 $U_{\text{半}}$ **不再**与 $H$ 交换： 它在 $j=0$ 与 $j=1$ 之间的键上留下一个**畴壁** （domain wall）。这个畴壁就是缺陷的端点， 它是一个真实的、局域的激发（有能量代价 $\sim J$）。

**要点。**

 **“闭合 $\Rightarrow$ 对称算符（拓扑、无能量代价）； 带边 $\Rightarrow$ 缺陷（边界是物理激发）”**。 这条对应关系在所有例子中都成立，是记住区别的最好办法。 在 $q$-form 情形，$q$-form 对称缺陷的边界是一个 $(d-q-2)$ 维对象。

## 扭曲边界条件与扭曲扇区

缺陷的另一个用途：定义**扭曲扇区**（twisted sector）。 把对称缺陷沿**时间**方向插入（即支撑在 “空间的一部分 $\times$ 全部时间”上），等价于对场施加 **扭曲边界条件**（twisted boundary condition）： 

$$
\phi(x+L)=g\cdot\phi(x)
  \qquad(g\in G).
$$

 在配分函数语言中， 

$$
Z_g=\mathrm{Tr}\!\left[g\,e^{-\beta H}\right]
  \quad\text{（把 }g\text{ 插在时间圈上）},
$$

 而**把 $g$ 插在空间圈上**给出扭曲扇区的 Hilbert 空间 $\mathcal{H}_g$。两者由**模变换**（modular transformation）联系 ——这在 2 维 CFT 中是标准工具，也是判断不可逆对称性的实用手段。

## 规范化：把全局对称性“求和掉”

**定义（规范化）。**

**规范化**（gauging）一个（有限）$q$-form 对称性 $G$， 指在路径积分中**对所有可能的对称缺陷网络求和**： 

$$
Z_{\text{gauged}}
  =\frac{1}{|G|^{\#}}\sum_{\text{网络}}\;Z\big[\text{缺陷网络}\big].
$$

 等价地：引入 $G$ 的 $(q+1)$-形式规范场并对其求和。

规范化的三条重要后果：

1.  **原来的带荷算符被投影掉**。求和把非中性算符的 期望值平均为零，于是它们不再是好算符。

2.  **出现新的“对偶”对称性**。 规范化 $d$ 维中的 $q$-form 群 $G$（阿贝尔）， 得到一个新的 $(d-q-2)$-form 对称性，群为 $\hat G$（对偶群）。 

$$
\text{gauge } q\text{-form } G
              \;\Longrightarrow\;
              \text{新的 } (d-q-2)\text{-form } \hat G .
$$

 *检查 $q=0$、$d=2$、$G=\mathbb{Z}_2$*：新对称性是 $(2-0-2)=0$-form 的 $\mathbb{Z}_2$——正是 Ising 的 Kramers–Wannier 对偶对称性。$\checkmark$ （第 9.1 小节）

3.  **存在反常时无法规范化**。这就是 ’t Hooft 反常的定义 （第 10.2 小节）。

**练习。**

 用 [eq:dualsym] 验证： (a) 在 $d=4$ 中规范化一个 0-form $\mathbb{Z}_N$， 得到什么形式的对称性？（答：$(4-0-2)=2$-form $\mathbb{Z}_N$。）  
(b) 在 $d=4$ 中规范化一个 1-form $\mathbb{Z}_N$，得到什么？ （答：$(4-1-2)=1$-form $\mathbb{Z}_N$——**形式不变**， 这正是 4 维中 $\mathrm{U}(1)$ 与 $\mathrm{U}(1)/\mathbb{Z}_N$ 规范理论互相转化的原因， 见第 9.3 小节。）  
(c) 在 $d=3$ 中规范化 0-form $\mathbb{Z}_N$，得到 $1$-form $\mathbb{Z}_N$； 说明这与 3 维 $\mathbb{Z}_N$ 规范理论（Dijkgraaf–Witten 理论） 中 Wilson 线与 ’t Hooft 线的辫结相位如何联系。

# 典型例子

本节是全讲义重心。三个例子分工如下： **Ising** 演示 0-form 对称性的全部要素（含不可逆对称性的最简实例）； **Maxwell** 给出 1-form 对称性的**完整推导**； **$\mathrm{U}(1)$ 对偶**提供把两者串起来的直觉。

## 例一：Ising 模型与 $\mathbb{Z}_2$

### 模型与对称算符

取 1$+$<!-- -->1 维横场量子 Ising 链，格点 $j$ 上是自旋 $1/2$： 

$$
H=-J\sum_j \sigma^z_j\sigma^z_{j+1}-h\sum_j\sigma^x_j,
  \qquad J,h>0 .
$$

**命题（$\mathbb{Z}_2$ 对称性）。**

算符 

$$
\boxed{\ U=\prod_j\sigma^x_j\ }
  \qquad\text{满足}\qquad
  U^2=1,\qquad [U,H]=0 .
$$

**证明。**

$U^2=\prod_j(\sigma^x_j)^2=1$。$\checkmark$ 与 $H$ 交换：$\sigma^x_j$ 与自身交换，故第二项显然不变。 对第一项，用 $\sigma^x\sigma^z\sigma^x=-\sigma^z$ 得 

$$
U\,\sigma^z_j\sigma^z_{j+1}\,U^{-1}
  =\big(-\sigma^z_j\big)\big(-\sigma^z_{j+1}\big)
  =\sigma^z_j\sigma^z_{j+1} . \checkmark
$$

#### 维数记账。

$d=2$（一维空间 $+$ 时间），$q=0$。 对称算符应支撑在 $d-q-1=1$ 维流形上： 在固定时刻，$U$ 是**整条空间切片**上所有 $\sigma^x$ 的乘积—— 确实是 1 维的。$\checkmark$（要点 [kp:dimensioncheck]） 带荷对象是 0 维的局域算符：$\sigma^z_j$ 带荷 $1$（$\mathbb{Z}_2$ 奇）， 因为 $U\sigma^z_jU^{-1}=-\sigma^z_j$。

### 两个相与自发破缺

- **有序相**（$J\gg h$）：基态近似为 $|\!\uparrow\uparrow\uparrow\cdots\rangle$ 与 $|\!\downarrow\downarrow\downarrow\cdots\rangle$， 两重退化，$\langle\sigma^z\rangle\ne0$。 $U$ 把两个基态**互换**，故 **$\mathbb{Z}_2$ 自发破缺**（spontaneously broken）。

- **无序相**（$h\gg J$）：基态唯一， 近似 $\bigotimes_j|\rightarrow\rangle_j$（$\sigma^x$ 的本征态）， $\langle\sigma^z\rangle=0$，$U|0\rangle=+|0\rangle$， 对称性**未破缺**。

- 两相之间在 $J=h$ 有二阶相变，连续极限是 $c=1/2$ 的 Ising 共形场论（Ising CFT）。

**要点。**

 0-form 对称性自发破缺的**判据**： 存在带荷的*局域*算符具有非零期望值 （**序参量**，(order parameter)）： $\langle\mathcal{O}\rangle\ne0$ 且 $\mathcal{O}$ 带荷。 等价地：基态退化，对称算符在基态间置换。 第 9.2.7 小节会看到 1-form 情形的类似判据， 只不过序参量从局域算符换成**线算符**。

### 缺陷：畴壁

按第 8.3 小节，把 [eq:isingU] 截断： 

$$
U_{\le0}=\prod_{j\le 0}\sigma^x_j .
$$

 它在 $j=0,1$ 之间制造一个**畴壁**。在有序相中， 畴壁是一个真实的、可局域化的激发（能量 $\sim 2J$）， 它**就是缺陷的端点**。

这个例子清楚展示要点 [kp:defect-vs-operator]：

- 完整乘积（闭合）$\Rightarrow$ 对称算符，与 $H$ 交换，无能量代价；

- 截断乘积（带边）$\Rightarrow$ 缺陷，端点是有能量的激发。

### Kramers–Wannier 对偶与规范化

定义**对偶变量**，住在链的**键**（即 $j+\tfrac12$）上： 

$$
\mu^x_{j+\frac12}\equiv\sigma^z_j\sigma^z_{j+1},
  \qquad
  \mu^z_{j+\frac12}\equiv\prod_{k\le j}\sigma^x_k .
$$

 可以验证 $\mu^{x,z}$ 满足同样的 Pauli 代数。代入 [eq:ising]： 

$$
H=-J\sum \mu^x_{j+\frac12}
    -h\sum \mu^z_{j-\frac12}\mu^z_{j+\frac12} ,
$$

 即**同一个模型，但 $J\leftrightarrow h$ 互换**。

**要点。**

 Kramers–Wannier 对偶（Kramers–Wannier duality）$J\leftrightarrow h$：

- 把**有序相映到无序相**，反之亦然；

- 在**临界点 $J=h$ 处成为理论的自映射**—— 这是一个*对称性*！

- 注意 [eq:KWvars] 中 $\mu^z$ 是一个**半无穷乘积**， 即一个**缺陷**。所以对偶算符本质上是非局域的。

在现代语言中：KW 对偶 $=$ **规范化 $\mathbb{Z}_2$ 对称性** （第 8.5 小节）再作场重命名。 由 [eq:dualsym]，$d=2$、$q=0$、$G=\mathbb{Z}_2$ 规范化后得到 $(2-0-2)=0$-form 的 $\hat{\mathbb{Z}_2}=\mathbb{Z}_2$——即对偶模型中新的 $\mathbb{Z}_2$。 $\checkmark$

### 不可逆对称性：Ising 临界点的三条拓扑线

在临界点（Ising CFT）上，$d=2$ 中的 0-form 对称算符支撑在 1 维流形上， 即**拓扑缺陷线**（(topological defect line), TDL）。 Ising CFT 恰好有**三条**： 

$$
\mathbf 1\ (\text{恒等}),
  \qquad
  \eta\ (\mathbb{Z}_2\ \text{对称线}),
  \qquad
  \mathcal N\ (\text{KW 对偶线}) .
$$

 它们的融合规则（[eq:fusion] 的具体实现）为 

$$
\boxed{\
  \eta\times\eta=\mathbf 1,
  \qquad
  \eta\times\mathcal N=\mathcal N\times\eta=\mathcal N,
  \qquad
  \mathcal N\times\mathcal N=\mathbf 1+\eta\ }
$$

**要点。**

 **$\mathcal N$ 没有逆元**，因此是**不可逆对称性**。 理由很直接：若存在 $\mathcal N^{-1}$，则由 $\mathcal N\times\mathcal N=\mathbf 1+\eta$ 两边左乘 $\mathcal N^{-1}$ 得 $\mathcal N=\mathcal N^{-1}+\mathcal N^{-1}\eta$， 但融合系数是**非负整数**，无法让一条线等于两条线之和。 $\mathcal N$ 的“量子维数”是 $\sqrt2$（不是整数）， 这是不可逆性的标志。

#### $\mathcal N$ 的作用与选择定则。

Ising CFT 有三个初级场：$\mathbf 1$、能量算符 $\varepsilon$、 自旋算符 $\sigma$。三条线在它们上的作用（本征值）为

| 作用于       | $\mathbf 1$ | $\varepsilon$ | $\sigma$ |
|:-------------|:-----------:|:-------------:|:--------:|
| $\eta$       |    $+1$     |     $+1$      |   $-1$   |
| $\mathcal N$ |  $+\sqrt2$  |   $-\sqrt2$   | $\boldsymbol{0}$  |

最后一格的 $0$ 是关键：**$\mathcal N$ 把 $\sigma$ 消灭**。 一个可逆算符不可能有零本征值——这又一次证明了不可逆性， 并直接给出**选择定则**： 把 $\mathcal N$ 收缩到包围 $\sigma$ 的小圈上，关联函数为零， 从而某些关联函数被迫消失。这类约束是普通群论**看不到**的， 也是不可逆对称性的实用价值。

**注。**

$\eta$ 在 $\sigma$ 上取 $-1$ 说明 $\sigma$ 是 $\mathbb{Z}_2$ 奇的 （对应格点上的 $\sigma^z$）， 在 $\varepsilon$ 上取 $+1$ 说明能量算符是 $\mathbb{Z}_2$ 偶的 （对应格点上的 $\sigma^x$ 或 $\sigma^z\sigma^z$）。 这与第 9.1 小节开头的格点分析完全一致。$\checkmark$

**练习。**

\(a\) 用 [eq:isingfusion] 计算 $\mathcal N\times\mathcal N\times\mathcal N$， 并验证结果与 $2\mathcal N$ 一致。  
(b) 由表中数据验证融合规则在“本征值相乘”层面自洽： $(\pm\sqrt2)^2=2=1+1$ 对 $\mathbf 1,\varepsilon$ 成立； $0^2=0=1+(-1)$ 对 $\sigma$ 成立。$\checkmark$ 这个自洽检查是判断融合规则记对没记对的好办法。

## 例二：Maxwell 理论中的 1-form 对称性（完整推导）

这是本讲义最重要的推导，请逐步复核。

### 设定与两个方程

考虑 4 维（$d=4$）**纯** $\mathrm{U}(1)$ 规范理论， 即 Maxwell 理论，**没有任何带电物质场**： 

$$
S=-\frac{1}{4e^2}\int \mathrm{d}^4x\;F_{\mu\nu}F^{\mu\nu}
   =-\frac{1}{2e^2}\int F\wedge\star F ,
  \qquad F=\mathrm{d}A .
$$

理论满足两个方程，来源截然不同：

$$
\boxed{
  \begin{aligned}
    \text{运动方程：}&\quad \partial_\mu F^{\mu\nu}=0
      &&\Longleftrightarrow&&\ \mathrm{d}\star F=0 ,\\
    \text{Bianchi 恒等式：}&\quad \partial_{[\rho}F_{\mu\nu]}=0
      &&\Longleftrightarrow&&\ \mathrm{d}F=0 .
  \end{aligned}}
$$

**要点。**

 **请牢记这两行的不对称性**：

- $\mathrm{d}\star F=0$ 来自**变分作用量**， 因此**加入物质场后会被修改**（源项出现）。

- $\mathrm{d}F=0$ 来自 $F=\mathrm{d}A$ 与 $\mathrm{d}^2=0$， 是**恒等式**，**不依赖任何动力学**， 只有在允许磁单极子（$A$ 不整体存在）时才被修改。

两个 1-form 对称性分别源于这两行， 命运也因此不同（第 9.2.5 小节）。

### 两个守恒的 2-形式电流

按定义 [def:qform]，$d=4$、$q=1$ 需要 2-形式电流。 [eq:twoequations] 恰好提供两个：

**命题（电与磁 1-form 对称性）。**

定义 

$$
\star J_e\equiv\frac{1}{e^2}\,\star F
  \qquad\text{与}\qquad
  \star J_m\equiv\frac{1}{2\pi}\,F ,
$$

 两者都是 2-形式且都闭： 

$$
\mathrm{d}\star J_e=\frac{1}{e^2}\mathrm{d}\star F=0\ (\text{运动方程}),
  \qquad
  \mathrm{d}\star J_m=\frac{1}{2\pi}\mathrm{d}F=0\ (\text{Bianchi}) .
$$

#### 维数自查（要点 [kp:dimensioncheck]）。

$q=1$，$d=4$：电流是 $q+1=2$-形式 $\checkmark$； $\star J$ 是 $d-q-1=2$-形式 $\checkmark$（上面两个都是 2-形式）； 对称算符支撑在 2 维闭曲面上 $\checkmark$； 带荷对象是 1 维的线 $\checkmark$； 连接数 $2+1+1=4$ $\checkmark$。全部对上。

**定义（Maxwell 的两个对称算符）。**

对任意 2 维闭曲面 $\Sigma_2\subset\mathcal{M}_4$： 

$$
\boxed{\
  U_e^{(\alpha)}(\Sigma_2)
  =\exp\!\left[\frac{i\alpha}{e^2}\oint_{\Sigma_2}\star F\right],
  \qquad
  U_m^{(\beta)}(\Sigma_2)
  =\exp\!\left[\frac{i\beta}{2\pi}\oint_{\Sigma_2}F\right] \ }
$$

 由定理 [thm:topological]，两者都是**拓扑算符**。

### 推导：电对称性作用在 Wilson 线上

现在完整推导 $U_e$ 在 Wilson 线上的作用。

#### 第 1 步：把 Wilson 线插入作用量。

插入 $W_n(C)=\exp[in\oint_C A]$ 等价于在作用量中加一项 $n\oint_C A$。用 Poincaré 对偶 [eq:poincare] 把线积分写成时空积分： 

$$
n\oint_C A=n\int_{\mathcal{M}_4}\delta_C\wedge A ,
$$

 其中 $\delta_C$ 是支撑在 $C$ 上的 **3-形式** （$d-k=4-1=3$ $\checkmark$）。

#### 第 2 步：变分。

对 $A\to A+\delta A$ 变分总作用量 $S_{\rm tot}=-\frac{1}{2e^2}\int F\wedge\star F+n\int\delta_C\wedge A$。 动能项给出 $\propto\frac{1}{e^2}\mathrm{d}\star F$，源项给出 $n\,\delta_C$， 于是运动方程被修改为 

$$
\boxed{\ \frac{1}{e^2}\,\mathrm{d}\star F=n\,\delta_C\ }
$$

 （整体符号取决于定向与号差约定；下面只用它的*绝对*效果。）

#### 第 3 步：用 Stokes 定理算荷。

取 $\Sigma_2=\partial V_3$，其中 $V_3$ 是一个 3 维区域， 与 $C$ **恰好相交一次**（即 $\Sigma_2$ 与 $C$ 的连接数为 1）。则 

$$
\begin{aligned}
  \frac{1}{e^2}\oint_{\Sigma_2}\star F
  &\overset{\text{Stokes}}{=}
   \frac{1}{e^2}\int_{V_3}\mathrm{d}\star F
  \notag\\
  &\overset{\eqref{eq:modifiedEOM}}{=}
   n\int_{V_3}\delta_C
  \notag\\
  &\overset{\text{Poincaré 对偶}}{=}
   n\cdot\#\big(V_3\cap C\big)
  \;=\;n .
  
\end{aligned}
$$

#### 第 4 步：结论。

代入 [eq:maxwellops]： 

$$
\boxed{\
  U_e^{(\alpha)}(\Sigma_2)\;W_n(C)
  = e^{\,i\alpha n\,\mathrm{Link}(\Sigma_2,C)}\;W_n(C)\ }
$$

 这正是 [eq:chargedef-q] 的形式： **Wilson 线 $W_n$ 在电 1-form 对称性下带荷 $n$**。$\blacksquare$

**注（Gauss 律图像）。**

 [eq:fluxisn] 的物理内容就是高中电磁学的 Gauss 律。 取 $\Sigma_2$ 为固定时刻包围电荷的球面 $S^2$， 则 $\frac{1}{e^2}\oint_{S^2}\star F$ 恰为**电通量** $\oint_{S^2}\boldsymbol{E}\cdot \mathrm{d}\boldsymbol{S}$，而 Gauss 律说它等于所包围的电荷 $n$。

于是 [eq:UeonW] 的意思是：

*“电 1-form 对称算符”就是“测量电通量的算符”， 而它的荷就是被套住的电荷。*

**这个例子说明广义对称性并不神秘**： 它把一个人人都会的操作（用高斯面测电荷） 重新识别为一个对称性的作用。新的地方在于： 把 $S^2$ 换成任意 2 维闭曲面、把“包围”换成“连接”， 并认识到 $W_n(C)$ 是被作用的*线*算符而不是点算符。

### 磁对称性与 ’t Hooft 线

对磁对称性，带荷对象是 **’t Hooft 线** $T_m(C)$（例 [ex:thooft]）。 按定义 [eq:thooftdef]，环绕 $C$ 的小球面上磁通为 $m$： 

$$
\frac{1}{2\pi}\oint_{\Sigma_2}F=m\qquad
  \big(\mathrm{Link}(\Sigma_2,C)=1\big),
$$

 于是直接由 [eq:maxwellops] 

$$
\boxed{\
  U_m^{(\beta)}(\Sigma_2)\;T_m(C)
  =e^{\,i\beta m\,\mathrm{Link}(\Sigma_2,C)}\;T_m(C)\ }
$$

注意这里**不需要**修改运动方程：$m$ 的整数性来自 第 2.4 小节 $S^2$ 上 $H^2\ne0$ 的拓扑论证 （Dirac 量子化），而非来自动力学。 这与要点 [kp:two-sources] 完全吻合。$\checkmark$

**注（一个值得向老师提问的细节）。**

$\frac{1}{2\pi}\oint_{\Sigma_2}F\in\mathbb{Z}$ 对任意闭 $\Sigma_2$ 成立 （$A$ 是 $\mathrm{U}(1)$ 联络），因此 $\beta$ 是 $2\pi$ 周期的， 磁对称群确实是 $\mathrm{U}(1)$。 但 $\frac{1}{e^2}\oint_{\Sigma_2}\star F$ 在*纯* Maxwell 理论中 是一个**连续**的实数，其“整数性”只在 $\Sigma_2$ 套住 Wilson 线时由 [eq:fluxisn] 保证。 因此“电 1-form 对称群是 $\mathrm{U}(1)$ 还是 $\mathbb{R}$”依赖于 如何精确设定带荷线算符谱与全局结构。 文献中通常写 $\mathrm{U}(1)_e^{(1)}\times\mathrm{U}(1)_m^{(1)}$； 这是一个值得课上确认约定的地方。

### 加入物质场：对称性如何被破坏

现在检验要点 [kp:two-sources]。加入一个电荷为 $q$ 的 **动力学**物质场 $\psi$，则运动方程变为 

$$
\frac{1}{e^2}\mathrm{d}\star F=\star j_\psi\ne0
  \qquad\Longrightarrow\qquad
  \mathrm{d}\star J_e\ne0 .
$$

 $\star J_e$ 不再闭 $\Rightarrow$ $U_e(\Sigma_2)$ **不再是拓扑算符** $\Rightarrow$ 连续的电 1-form 对称性**被破坏**。

#### 但残留一个 $\mathbb{Z}_q$。

物质场电荷为 $q$，因此它能**屏蔽**（例 [ex:screening]） 电荷为 $q$ 整数倍的 Wilson 线： 

$$
W_n\ \sim\ W_{n+q}
  \qquad\Longrightarrow\qquad
  \text{线算符按}\ n\ \mathrm{mod}\ q\ \text{分类}.
$$

 于是剩下的 1-form 对称群是 

$$
\boxed{\ \mathrm{U}(1)_e^{(1)}\ \longrightarrow\ \mathbb{Z}_q^{(1)}\ }
$$

 特别地，若存在电荷 $1$ 的物质场（如普通 QED 中的电子，$q=1$）， 则 $\mathbb{Z}_1=$ 平凡群，**电 1-form 对称性被完全破坏**。

#### 磁对称性则依然存活。

$\mathrm{d}F=0$ 是恒等式， 加入*电*荷物质不影响它。只有引入**动力学磁单极子** 才会破坏磁 1-form 对称性。

**要点。**

 这解释了一个初学者常有的疑问： **“为什么教科书里从没提过 1-form 对称性？”** 因为现实世界的 QED 有电荷 $1$ 的电子， 电 1-form 对称性被完全破坏； 而磁对称性虽然存活，却因为没有动力学磁单极子而很少被用到。 1-form 对称性在**纯规范理论** （如格点 Yang–Mills、拓扑物态）中才显出威力。

### $\mathrm{SU}(N)$ 的 $\mathbb{Z}_N$ 中心对称性

把上面的逻辑搬到非阿贝尔理论。取 4 维纯 $\mathrm{SU}(N)$ Yang–Mills （只有胶子，无基本表示物质）。

由 [eq:center]，$Z(\mathrm{SU}(N))=\mathbb{Z}_N$。定义对称算符 $U_k(\Sigma_2)$，$k\in\mathbb{Z}_N$，作用在表示 $R$ 的 Wilson 线上： 

$$
\boxed{\
  U_k(\Sigma_2)\;W_R(C)
  =\exp\!\left[\frac{2\pi i\,k\,n_R}{N}\mathrm{Link}(\Sigma_2,C)\right] W_R(C)\ }
$$

 其中 $n_R$ 是表示 $R$ 的 $N$ 度（例 [ex:Nality]）。

- 基本表示：$n_R=1$，荷非零 $\Rightarrow$ 是好的序参量。

- 伴随表示：$n_R=0$，荷为零。这与物理一致： 伴随 Wilson 线可以被胶子屏蔽，不携带守恒荷。

- 这就是**$\mathbb{Z}_N$ 1-form 中心对称性** （$\mathbb{Z}_N$ one-form center symmetry）。 加入基本表示的动力学夸克（$n_R=1$）会像 [eq:UtoZq] 一样把它完全破坏—— 这正是为什么真实 QCD 没有精确的中心对称性。

### 禁闭 $=$ 1-form 对称性未破缺

现在是这套语言最漂亮的物理回报。

按要点 [kp:ssb-0form]，判断对称性是否自发破缺要看 **带荷算符的期望值**。对 1-form 对称性， 带荷算符是 Wilson 线，于是序参量是 $\langle W(C)\rangle$。 取 $C$ 为边长 $L$、$T$ 的大矩形圈，两种可能行为：

$$
\big\langle W(C)\big\rangle\ \sim\
  \begin{cases}
    e^{-\sigma\,\mathrm{Area}(C)}
      & \text{面积律（\textup{(area law)}）}\\[4pt]
    e^{-c\,\mathrm{Perimeter}(C)}
      & \text{周长律（\textup{(perimeter law)}）}
  \end{cases}
$$

**要点。**

| $\langle W(C)\rangle$ | 1-form 对称性  | 物理相                                                 |
|:----------------------|:---------------|:-------------------------------------------------------|
| 面积律                | **未**自发破缺 | **禁闭**（confinement） |
| 周长律                | **已**自发破缺 | 解禁闭 / Coulomb 相                                    |

理由（直觉版）：周长律意味着可以通过重整化 （吸收掉与 $C$ 长度成正比的自能）使 $\langle W\rangle$ 保持有限非零， 即“带荷算符有非零期望值”$\Rightarrow$ 破缺。 面积律使 $\langle W\rangle$ 随面积指数衰减到零， 无法用局域重整化救回来 $\Rightarrow$ 未破缺。

**注（为什么这是个进步）。**

“禁闭”原本是个现象学描述（夸克拔不出来、有线性势 $V(r)=\sigma r$）。 现在它变成了一个**对称性破缺的判断**， 从而可以套用所有关于对称性破缺的一般理论 （序参量、Landau 论证、反常匹配）。 特别地，在纯 Yang–Mills 中 $\mathbb{Z}_N$ 是**精确**对称性， 所以“禁闭相”是一个有严格定义的相，而不只是强耦合的定性说法。

**注（光子是 1-form 对称性破缺的 Goldstone 玻色子）。**

在自由 Maxwell（Coulomb 相），$\langle W(C)\rangle$ 服从周长律， 故**电与磁 1-form 对称性都自发破缺**。 按与 Goldstone 定理平行的逻辑，破缺应伴随无质量激发—— 那正是**光子**。 所以“为什么光子无质量”有一个对称性解释： 它是 1-form 对称性自发破缺的 Goldstone 模。 第 10 节会再谈。

**练习。**

 (a) 把 [eq:fluxisn] 的每一步的形式次数写出来， 确认所有积分都在正确维数的流形上进行。  
(b) 说明为什么 $U_e$ 与 $U_m$ 互相交换 （提示：命题 [prop:abelian]，两个 2 维面在 4 维中可以错开）。  
(c) 若在 $\mathrm{SU}(N)$ 理论中加入 $N$ 度为 $2$ 的物质场， 残留的中心对称性是什么？ （答：$\mathbb{Z}_{\gcd(2,N)}$；例如 $N=4$ 时残留 $\mathbb{Z}_2$。）

## 例三：$\mathrm{U}(1)$ 对偶的直觉

### 4 维电磁对偶

Maxwell 方程 [eq:twoequations] 在替换 

$$
F\ \longrightarrow\ \star F,
  \qquad \star F\ \longrightarrow\ -F
$$

 下**互换**：运动方程 $\mathrm{d}\star F=0$ 变成 Bianchi $\mathrm{d}F=0$， 反之亦然。这就是**电磁对偶**（electromagnetic duality）。

**要点。**

 在广义对称性语言中，对偶的内容极其干净：

| 原理论                                   | $\longleftrightarrow$ | 对偶理论                                 |
|:-----------------------------------------|:---------------------:|:-----------------------------------------|
| 运动方程 $\mathrm{d}\star F=0$           | $\longleftrightarrow$ | Bianchi $\mathrm{d}F=0$                  |
| 电 1-form 对称性 $\mathrm{U}(1)_e^{(1)}$ | $\longleftrightarrow$ | 磁 1-form 对称性 $\mathrm{U}(1)_m^{(1)}$ |
| Wilson 线 $W_n$                          | $\longleftrightarrow$ | ’t Hooft 线 $T_n$                        |
| 耦合 $e$                                 | $\longleftrightarrow$ | $\sim 1/e$                               |

引入复化耦合 $\tau=\dfrac{\theta}{2\pi}+\dfrac{2\pi i}{e^2}$， 对偶变换是 $\tau\to-1/\tau$（$S$ 对偶）。

### 更简单的类比：2 维紧致标量与 T 对偶

4 维电磁对偶的“最小模型”是 2 维紧致标量场 $\varphi\sim\varphi+2\pi$，作用量（示意） 

$$
S=\frac{R^2}{4\pi}\int \mathrm{d}\varphi\wedge\star\mathrm{d}\varphi .
$$

 它有**两个** 0-form $\mathrm{U}(1)$ 对称性，来源与 Maxwell 完全平行：

|                                              | 电流                                                | 守恒的原因                                    |
|:---------------------------------------------|:----------------------------------------------------|:----------------------------------------------|
| **平移**（动量）对称性 $\varphi\to\varphi+c$ | $j_{\rm s}=\dfrac{R^2}{2\pi}\star\mathrm{d}\varphi$ | 运动方程 $\mathrm{d}\star\mathrm{d}\varphi=0$ |
| **缠绕**（winding）对称性                    | $j_{\rm w}=\dfrac{1}{2\pi}\mathrm{d}\varphi$        | 恒等式 $\mathrm{d}\mathrm{d}\varphi=0$        |

**要点。**

 **请对比这张表与要点 [kp:two-sources]**： 结构**一模一样**—— 一个对称性来自*运动方程*，另一个来自*恒等式*。 这不是巧合，而是“对偶成对出现的对称性”的普遍模式。 掌握这个模式后，看到任何理论都可以问： *它的运动方程和它的恒等式各给我一个什么对称性？*

#### 荷与带荷算符。

- 动量对称性的荷是**动量** $n$， 带荷算符是顶点算符 $e^{in\varphi}$ （在 $\varphi\to\varphi+c$ 下得相位 $e^{inc}$）。

- 缠绕对称性的荷是**缠绕数** $w=\frac{1}{2\pi}\oint \mathrm{d}\varphi\in\mathbb{Z}$， 带荷算符是涡旋／无序算符。

#### T 对偶。

变换 

$$
R\ \longrightarrow\ \frac{1}{R},
  \qquad
  n\ \longleftrightarrow\ w
$$

 是理论的同构，**交换两个 $\mathrm{U}(1)$ 对称性**。 这与 [eq:EMduality] 交换 $\mathrm{U}(1)_e^{(1)}\leftrightarrow\mathrm{U}(1)_m^{(1)}$ 是同一个故事的低维版本。

### 全局结构：同一个局域理论，不同的线算符谱

最后一个概念上重要的点。考虑 4 维规范理论， 规范群取 $\mathrm{U}(1)$ 还是 $\mathrm{U}(1)/\mathbb{Z}_N$？ 两者的**局域**动力学（Feynman 规则、微扰展开、 $\langle F F\rangle$ 关联函数）**完全相同**， 差别只在**允许存在哪些线算符**：

- 取 $\mathrm{U}(1)$：Wilson 线 $W_n$，$n\in\mathbb{Z}$；

- 取 $\mathrm{U}(1)/\mathbb{Z}_N$：允许分数电荷的线， 但 ’t Hooft 线的谱相应受限。

由练习 [ex:gaugecheck](b)，在 $d=4$ 中规范化一个 1-form $\mathbb{Z}_N$ 又得到一个 1-form $\mathbb{Z}_N$，所以这些不同的“全局结构” （global structure）由**规范化 1-form 对称性的不同子群** 互相联系。

**要点。**

 **“理论”不只由拉氏量决定，还由算符谱决定。** 这是 GKSW 论文最有影响的信息之一： 一个拉氏量可能对应**若干个**不同的量子理论， 它们的区别由 1-form 对称性及其规范化选择刻画。 在 $\mathrm{SU}(N)$ 与 $\mathrm{SU}(N)/\mathbb{Z}_N=\mathrm{PSU}(N)$ Yang–Mills 之间、 在 $\mathcal N=4$ 超对称理论的不同全局形式之间， 这个区别都有真实的物理后果。

# 自发破缺与 ’t Hooft 反常：课前级直觉

本节目标不是把反常算清楚（那需要好几周）， 而是让你在第一堂课听到 “anomaly” 时知道**它在问什么问题**。

## 自发破缺的统一判据

**定义（广义自发破缺）。**

一个 $q$-form 对称性称为**自发破缺**的 （spontaneously broken），若存在带荷的 $q$ 维算符 $\mathcal{O}(\mathcal{M}_q)$，其期望值在“去掉与 $\mathcal{M}_q$ 体积成正比的 局域重整化因子”后仍非零： 

$$
\big\langle \mathcal{O}(\mathcal{M}_q)\big\rangle
  \ \sim\ e^{-c\cdot\mathrm{Vol}(\partial\mathcal{M}_q)}
  \times(\text{非零})
  \qquad\text{（“周长律”）} .
$$

 若衰减比这更快（如“面积律”$e^{-\sigma\mathrm{Vol}(\mathcal{M}_q)}$）， 则**未破缺**。

检查两个特例：

| $q$ | 带荷对象                  | 破缺判据                        | 无质量激发（“Goldstone”） |
|:----|:--------------------------|:--------------------------------|:--------------------------|
| $0$ | 局域算符 $\mathcal{O}(x)$ | $\langle\mathcal{O}\rangle\ne0$ | Goldstone 标量玻色子      |
| $1$ | Wilson 线 $W(C)$          | 周长律                          | 无质量规范玻色子（光子）  |

**注（$q=0$ 时 [eq:ssb-general] 退化为老判据）。**

$q=0$ 时 $\mathcal{M}_0$ 是一个点，$\partial\mathcal{M}_0=\emptyset$， “体积”为零，于是 [eq:ssb-general] 就是 $\langle\mathcal{O}\rangle\ne0$。 $\checkmark$ 老判据是新判据的特例。

**要点。**

 广义 Goldstone 定理的一句话版本：

*$q$-form 对称性自发破缺 $\Rightarrow$ 存在无质量的 $q$-form 规范场（其“Goldstone 模”）。*

$q=0$ 给出普通的无质量标量； $q=1$ 给出无质量的 1-form 规范场，即**光子**。 这就是第 9.2.7 小节末尾那句 “光子是 1-form Goldstone 玻色子”的来源。

## 什么是 ’t Hooft 反常

### 先分清两种“反常”

**注意。**

 “反常”这个词在文献里指两件**不同**的事，务必区分：

1.  **ABJ 型／真反常**：对称性在量子层面 *根本不存在*，守恒律被破坏 （如手征对称性因三角图而 $\partial_\mu j^\mu_A\propto F\tilde F$）。 这种“对称性”不能用来做选择定则。

2.  **’t Hooft 反常（’t Hooft anomaly）**： 对称性*完全成立*，守恒律没问题； 但它**不能被规范化**（cannot be gauged）。 这类反常**非常有用**，因为它给出对低能物理的严格约束。

本课程说 “anomaly” 时，绝大多数指第 (2) 种。

### 定义：背景场语言

规范化一个对称性的第一步是**打开背景场** （background field）。对 $q$-form 对称性 $G$， 背景场是一个 $(q+1)$-形式规范场 $B$： 

$$
q=0:\ \text{1-形式 }A;\qquad
  q=1:\ \text{2-形式 }B;\qquad
  \text{一般 } q:\ (q+1)\text{-形式} .
$$

 配分函数变成 $Z[B]$。

**定义（’t Hooft 反常）。**

 若不存在任何**局域反项**（local counterterm）使 $Z[B]$ 在背景规范变换 $B\to B+\mathrm{d}\lambda$ 下不变， 即总有 

$$
Z[B+\mathrm{d}\lambda]=e^{\,i\,\mathcal A[B,\lambda]}\;Z[B],
  \qquad \mathcal A\ne0\ (\text{模局域反项}),
$$

 则称该对称性有 **’t Hooft 反常**。

**注（反常流入与 SPT 项）。**

[eq:anomalyphase] 的相位可以被“吸收”到 高一维的**拓扑项**中：存在 $(d+1)$ 维的 SPT／Chern–Simons 型作用量 $S_{d+1}[B]$，使得 

$$
Z_d[B]\times e^{iS_{d+1}[B]}
$$

 整体规范不变。这叫**反常流入**（anomaly inflow）。 因此“反常”被 $(d+1)$ 维拓扑项完全分类—— 这是现代处理反常的标准方式。

### 最重要的推论：反常匹配

**定理（’t Hooft 反常匹配（陈述））。**

 ’t Hooft 反常是重整化群流的不变量： 紫外理论与红外理论的反常必须相等。

**证明（直觉论证）。**

反常由拓扑项 $S_{d+1}[B]$ 刻画，而拓扑项**不依赖度规**， 因而不依赖能标（第 6 节第 (2) 条）。 系数是量子化的整数，不能连续变化。 既然它在 RG 流下不能变，紫外与红外必须给出同一个值。

**要点。**

 反常匹配的**威力**：它把“低能会发生什么”从猜测变成了推理。 若紫外理论有非零反常，则红外**不可能**是“平凡的有能隙唯一真空”， 必须满足以下之一：

1.  对称性**自发破缺**（则 Goldstone 模承载反常）；

2.  理论在低能**无能隙**（如 CFT）；

3.  低能是一个**拓扑场论**（TQFT）， 其反常与紫外匹配。

**广义对称性带来的新东西**就是：把这套论证用到 高阶形式对称性上，从而对禁闭、$\theta$ 依赖、 相图结构得到全新的约束。

## 三个层次的反常例子

### 最初等的例子：Dirac 量子化就是一种“互不相容”

考虑 4 维 Maxwell 的 Wilson 线 $W_n$ 与 ’t Hooft 线 $T_m$。 把 $W_n$ 绕着 $T_m$ 走一圈（其世界线扫出一个包围 $T_m$ 的曲面）， 得到 Aharonov–Bohm 型相位 

$$
e^{2\pi i\,n m} .
$$

 要求单值性给出 **Dirac 量子化条件** $nm\in\mathbb{Z}$。

**要点。**

 [eq:diracphase] 的含义是：$W$ 与 $T$ **互不局域** （mutually non-local）。你不能同时把两者都当作“平凡的”算符。 用对称性语言：**电与磁 1-form 对称性不能同时被规范化**—— 这就是它们之间存在**混合 ’t Hooft 反常** （mixed ’t Hooft anomaly）的最直观表现。

### 4 维 Maxwell 的混合反常

把电与磁 1-form 对称性的背景场记为 2-形式 $B_e$、$B_m$。 两者的混合反常由 5 维拓扑项刻画，其结构为 

$$
S_5\ \propto\ \int_{\mathcal{M}_5} B_e\wedge \mathrm{d}B_m
$$

 （具体的 $2\pi$ 归一化因作者而异，请以课上约定为准）。

#### 物理翻译。

[eq:5danomaly] 非零意味着：

- 不能同时规范化 $\mathrm{U}(1)_e^{(1)}$ 与 $\mathrm{U}(1)_m^{(1)}$；

- 因此 Maxwell 理论**不可能**在保持两个对称性的前提下 变成平凡的有能隙理论；

- 由要点 [kp:matching-power]，只剩“对称性破缺”或“无能隙” 两条路。而我们知道答案是：两者都破缺，且理论无能隙—— **无质量光子**正是这个反常的必然后果。$\checkmark$

**要点。**

 把上面几条串起来，得到一个漂亮的论证链：

混合反常 [eq:5danomaly] $\Rightarrow$ 红外不能平凡 $\Rightarrow$ 1-form 对称性破缺（周长律）$\Rightarrow$ 存在 Goldstone 模 $\Rightarrow$ **光子无质量**。

这是本讲义**最值得带进课堂的一条论证**： 它把六七个概念（反常、匹配、破缺、序参量、Goldstone、拓扑算符） 串成一条可复述的因果链。

### $\theta$ 角与时间反演（仅指路）

一个影响很大的应用：4 维 $\mathrm{SU}(N)$ Yang–Mills 的 $\mathbb{Z}_N$ 1-form 中心对称性与时间反演／$\theta$ 周期性之间 存在混合反常。结论是：在 $\theta=\pi$ 处， 理论**不能**既保持时间反演又保持中心对称性并且有唯一有能隙真空， 从而推出 $\theta=\pi$ 处必有相变或自发破缺。 这属于课程后半段内容，第 14 节给出文献。

## 小结：新旧对照

| 概念         | 0-form（旧）        | $q$-form（新）                |
|:-------------|:--------------------|:------------------------------|
| 序参量       | 局域算符期望值      | $q$ 维算符的周长律            |
| Goldstone 模 | 无质量标量          | 无质量 $q$-form 规范场        |
| 反常         | $(d+1)$ 维 SPT 项   | 同样，但背景场是 $(q+1)$-形式 |
| 反常匹配     | 约束低能谱          | 约束禁闭／$\theta$ 依赖／相图 |
| 规范化       | 得对偶 $(d-2)$-form | 得对偶 $(d-q-2)$-form         |

# 课堂公式与英汉术语表

## 核心公式速查

把全篇最该带进课堂的公式集中如下。

#### （一）守恒与拓扑。

$$
\begin{aligned}
  \partial_\mu j^\mu=0
  &\ \Longleftrightarrow\ \mathrm{d}\star j=0
  && \text{（\eqref{eq:conservation}）}\\
  Q(\Sigma_{d-1})=\int_{\Sigma_{d-1}}\star j
  &\ \text{只依赖 }[\Sigma_{d-1}]\in H_{d-1}
  && \text{（定理 \ref{thm:topological}）}\\
  U_\alpha(\Sigma)&=\exp\!\Big[i\alpha\!\int_\Sigma\star j\Big]
  && \text{（\eqref{eq:Qsurface}）}
\end{aligned}
$$

#### （二）Noether。

$$
\begin{aligned}
  j^\mu&=\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\Delta^a-K^\mu
  && \text{（\eqref{eq:noethercurrent}）}\\
  j^\mu_{\mathrm{U}(1)}&=i\big(\phi^*\partial^\mu\phi-\phi\,\partial^\mu\phi^*\big)
  && \text{（\eqref{eq:u1current}）}\\
  T^\mu{}_\nu&=\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi^a)}\partial_\nu\phi^a
    -\delta^\mu_\nu\mathcal{L}
  && \text{（\eqref{eq:stresstensor}）}\\
  \partial_\mu\langle j^\mu(x)\mathcal{O}(y)\rangle
  &=q\,\delta^d(x-y)\langle\mathcal{O}(y)\rangle
  && \text{（\eqref{eq:ward}）}
\end{aligned}
$$

#### （三）$q$-form 对称性。

$$
\begin{aligned}
  \mathrm{d}\star J&=0,\qquad J\in\Omega^{q+1},\quad \star J\in\Omega^{d-q-1}
  && \text{（\eqref{eq:qformop}）}\\
  U_\alpha(\mathcal{M}_{d-q-1})
  &=\exp\!\Big[i\alpha\!\int_{\mathcal{M}_{d-q-1}}\star J\Big]
  && \text{（\eqref{eq:qformop}）}\\
  \langle U_\alpha(\mathcal{M}_{d-q-1})\mathcal{O}(\mathcal{M}_q)\rangle
  &=e^{i\alpha n\mathrm{Link}}\langle\mathcal{O}(\mathcal{M}_q)\rangle
  && \text{（\eqref{eq:chargedef-q}）}\\
  \dim\mathcal{M}_{\rm sym}+\dim\mathcal{M}_{\rm charge}+1&=d
  && \text{（\eqref{eq:linkdim}）}
\end{aligned}
$$

#### （四）Maxwell 的两个对称性。

$$
\begin{aligned}
  U_e^{(\alpha)}(\Sigma_2)
  &=\exp\!\Big[\tfrac{i\alpha}{e^2}\oint_{\Sigma_2}\star F\Big],
  & U_e\,W_n&=e^{i\alpha n\mathrm{Link}}W_n
  && \text{（\eqref{eq:UeonW}）}\\
  U_m^{(\beta)}(\Sigma_2)
  &=\exp\!\Big[\tfrac{i\beta}{2\pi}\oint_{\Sigma_2}F\Big],
  & U_m\,T_m&=e^{i\beta m\mathrm{Link}}T_m
  && \text{（\eqref{eq:UmonT}）}
\end{aligned}
$$

 加入电荷 $q$ 的动力学物质：$\mathrm{U}(1)_e^{(1)}\to\mathbb{Z}_q^{(1)}$ （[eq:UtoZq]）。

#### （五）Ising 的融合规则。

$$
\eta^2=\mathbf 1,\qquad
  \eta\,\mathcal N=\mathcal N,\qquad
  \mathcal N^2=\mathbf 1+\eta
  \qquad \text{（\eqref{eq:isingfusion}）}
$$

#### （六）规范化与对偶。

$$
\text{gauge }q\text{-form }G\ \text{in }d\text{ dims}
  \ \Longrightarrow\
  (d-q-2)\text{-form }\hat G
  \qquad \text{（\eqref{eq:dualsym}）}
$$

## 英汉术语表

以下按主题分组。请在听课前把**英文**一列读熟—— 课堂上老师大概率直接用英文说这些词。

| 英文                           | 中文                              | 本讲义位置                                                                                                                            |
|:-------------------------------|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| generalized global symmetry    | 广义全局对称性                    | 第 7 节                                                 |
| $q$-form symmetry              | $q$-form 对称性／$q$ 阶形式对称性 | 定义 [def:qform]                                        |
| higher-form symmetry           | 高阶形式对称性（$q\ge1$）         | 第 7 节                                                 |
| higher symmetry                | 高对称性（统称）                  | 第 7.5 小节                                     |
| global symmetry                | 全局对称性                        | 第 3.3 小节                   |
| gauge symmetry / redundancy    | 规范对称性／描述冗余              | 注意 [warn:gauge]                                     |
| continuous / discrete symmetry | 连续／离散对称性                  | 第 3 节                                           |
| symmetry operator              | 对称算符                          | 要点 [kp:U-operator]                            |
| charged operator               | 带荷算符                          | 第 8 节                             |
| local operator                 | 局域算符                          | 第 5 节                                         |
| extended operator              | 拓展算符                          | 第 5.3 小节                                 |
| line / surface operator        | 线／面算符                        | 第 5.3 小节                                 |
| genuine operator               | 真算符（不需依附高维算符）        | 第 5.4 小节                                   |
| Wilson line / loop             | Wilson 线／Wilson 圈              | 例 [ex:wilson]                                          |
| ’t Hooft line                  | ’t Hooft 线                       | 例 [ex:thooft]                                          |
| topological operator           | 拓扑算符                          | 定义 [def:topological]                      |
| topological defect line (TDL)  | 拓扑缺陷线                        | 第 9.1.5 小节                               |
| defect / twist defect          | 缺陷／扭曲缺陷                    | 第 8.3 小节                                   |
| domain wall                    | 畴壁                              | 例 [ex:domainwall]                              |
| twisted boundary condition     | 扭曲边界条件                      | [eq:twisted]                                        |
| twisted sector                 | 扭曲扇区                          | 第 8.3 小节                                   |
| fusion rule / fusion category  | 融合规则／融合范畴                | [eq:fusion]                                           |
| invertible / non-invertible    | 可逆／不可逆                      | 要点 [kp:noninvertible-first] |
| quantum dimension              | 量子维数                          | 要点 [kp:noninvertible-first] |
| center symmetry                | 中心对称性                        | 第 9.2.6 小节                                   |
| $N$-ality                      | $N$ 度                            | 例 [ex:Nality]                                          |
| screening                      | 屏蔽                              | 例 [ex:screening]                                 |
| gauging                        | 规范化（把对称性变成规范对称性）  | 第 8.5 小节                                   |
| global structure               | 全局结构                          | 要点 [kp:globalstructure]             |

英汉术语表（一）：对称性与算符。

| 英文                                | 中文                 | 本讲义位置                                                                                                                      |
|:------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| differential form / $p$-form        | 微分形式／$p$-形式   | 第 2.4 小节                                 |
| wedge product                       | 楔积                 | [eq:wedge]                                        |
| exterior derivative                 | 外微分               | [eq:dsquared]                               |
| closed / exact form                 | 闭形式／恰当形式     | 第 2.4 小节                                 |
| Hodge star                          | Hodge 星号           | [eq:hodge]                                        |
| Stokes’ theorem                     | Stokes 定理          | [eq:stokes]                                     |
| de Rham cohomology                  | de Rham 上同调       | [eq:deRham]                                     |
| homologous / homology class         | 同调／同调类         | [eq:homologyinv]                      |
| codimension                         | 余维                 | 定义 [def:qform]                                  |
| linking number                      | 连接数               | 定义 [def:link]                                     |
| Poincaré dual                       | Poincaré 对偶        | [eq:poincare]                               |
| Bianchi identity                    | Bianchi 恒等式       | [eq:bianchi]                                  |
| Dirac quantization                  | Dirac 量子化         | [eq:diracphase]                         |
| flux                                | 通量                 | 注 [rmk:gauss]                                    |
| Aharonov–Bohm phase                 | Aharonov–Bohm 相位   | [eq:diracphase]                         |
| Ward identity                       | Ward 恒等式          | [eq:ward]                                           |
| order parameter                     | 序参量               | 要点 [kp:ssb-0form]                         |
| spontaneous symmetry breaking (SSB) | 自发对称破缺         | 第 10.1 小节                    |
| Goldstone boson                     | Goldstone 玻色子     | 要点 [kp:goldstone-general] |
| area law / perimeter law            | 面积律／周长律       | [eq:arealaw]                                  |
| confinement / deconfinement         | 禁闭／解禁闭         | 要点 [kp:confinement]                   |
| ’t Hooft anomaly                    | ’t Hooft 反常        | 定义 [def:thooft]                               |
| mixed anomaly                       | 混合反常             | 要点 [kp:mutual]                                  |
| anomaly inflow                      | 反常流入             | 第 10.2 小节                              |
| anomaly matching                    | 反常匹配             | 定理 [thm:matching]                         |
| background (gauge) field            | 背景（规范）场       | 第 10.2 小节                              |
| local counterterm                   | 局域反项             | 定义 [def:thooft]                               |
| SPT phase                           | 对称性保护拓扑相     | 第 10.2 小节                              |
| electromagnetic duality             | 电磁对偶             | [eq:EMduality]                            |
| Kramers–Wannier duality             | Kramers–Wannier 对偶 | 要点 [kp:KW]                                              |
| T-duality                           | T 对偶               | [eq:Tduality]                               |
| winding number                      | 缠绕数               | 第 9.3.2 小节               |
| higher group                        | 高群                 | 第 7.5 小节                               |

英汉术语表（二）：几何、拓扑与反常。

# 常见困惑

以下是初学广义对称性时最常见的十四个困惑， 每条都给出**可操作的**回答（而不只是“多想想就懂了”）。

1.  **“对称性 $=$ 拓扑算符”不是循环定义吗？** 

    不是。这句话的逻辑方向是： *原来*我们用“群作用在场上使作用量不变”定义对称性， 然后*推导出*对称算符是拓扑的（定理 [thm:topological]）。 *现在*我们把这个推论**提升为定义**。

    之所以可以这样做，是因为“拓扑算符”这个概念**独立可判定**： 给你一个算符，你可以直接检查 “它的关联函数在支撑集形变下是否不变”（定义 [def:topological]）。 这个检查不需要事先知道有什么群。

    **收益**：新定义严格更宽—— 它自动包含离散对称性（无流）、$q\ge1$ 的情形（非余维 1）、 以及不可逆情形（无群结构），而旧定义都装不下。

2.  **规范对称性到底算不算对称性？** 

    在本课程语境下：**不算**。见注意 [warn:gauge]。 判别方法：问“它是否作用在物理 Hilbert 空间上非平凡地？”

    - 全局对称性：$U|\psi\rangle$ 一般是*不同*的物理态 （如荷不同的态），$U$ 有非平凡谱。

    - 规范变换：作用在物理态上是**恒等**的 （物理态本来就规范不变），什么也没做。

    不过规范对称性极其重要，因为它**制造**拓展算符与 高阶形式对称性（要点 [kp:gauge-produces]）。 一句口号：*规范冗余不是对称性，但它是广义对称性的产房。*

3.  **对称算符、带荷算符、缺陷，我总是搞混。** 

    用**三个问题**区分（见第 8 节的表）：

    1.  *它是拓扑的吗？* 是 $\Rightarrow$ 对称算符或缺陷； 否 $\Rightarrow$ 带荷算符。

    2.  *它的支撑集闭合吗？* 闭合 $\Rightarrow$ 对称算符； 带边 $\Rightarrow$ 缺陷。

    3.  *它的维数是多少？* $d-q-1$ $\Rightarrow$ 对称算符侧； $q$ $\Rightarrow$ 带荷侧。

    在 Maxwell 例子里：$\oint_{\Sigma_2}\star F$ 是拓扑的、$\Sigma_2$ 闭合、 维数 2 $=d-q-1$ $\Rightarrow$ 对称算符； $W_n(C)$ 不是拓扑的（有面积／周长律）、维数 1 $=q$ $\Rightarrow$ 带荷算符。

4.  **为什么高阶形式对称性一定阿贝尔？** 

    见命题 [prop:abelian]。核心直觉是**余维**：

    - 余维 1（$q=0$）：两张“墙”把时空切成有先后的层， 乘法有顺序 $\Rightarrow$ 可以非阿贝尔。

    - 余维 $\ge2$（$q\ge1$）：两个支撑集可以在多余的方向上 **绕开彼此**，因此顺序无意义 $\Rightarrow$ 必阿贝尔。

    自查：$d=3$ 中两条直线（余维 2）能不能不相交地交换位置？能。 $d=3$ 中两个平面（余维 1）能不能？不能，它们必相交。$\checkmark$

5.  **不可逆的东西凭什么叫“对称性”？** 

    因为对称性的**用处**不需要可逆性。 我们用对称性做三件事： （i）给关联函数选择定则；（ii）组织谱／Hilbert 空间； （iii）通过反常约束低能物理。 这三件事只需要**“存在可自由移动的拓扑算符”**。

    具体看 Ising 的 $\mathcal N$（第 9.1.5 小节）： 它在 $\sigma$ 上的本征值是 $0$， 于是把 $\mathcal N$ 收缩到包围 $\sigma$ 的圈上就得到 “某些关联函数必须为零”——这是一个**真正的选择定则**， 和 $\mathbb{Z}_2$ 给出的选择定则同样有用，只不过 $\mathcal N$ 没有逆。

    **历史类比**：当年把“反演 $P$”“时间反演 $T$”这些离散变换 也叫对称性时，同样有人反对（“它们没有守恒流”）。 概念的边界随着用处而扩张，这是正常的。

6.  **1-form 对称性自发破缺，Goldstone 模在哪？** 

    在**光子**里。见要点 [kp:goldstone-general]： $q$-form 对称性破缺给出无质量的 $q$-form 规范场。 $q=1$ 时那就是一个无质量的 1-form 场 $A_\mu$，即光子。

    初学者常期待“又一个无质量标量”， 但那只对 $q=0$ 成立。破缺的是 1-form 对称性， Goldstone 模的“形式次数”也随之升高。 数一下自由度也自洽：4 维无质量光子 2 个横向极化， 对应两个 1-form 对称性（电、磁）各自破缺。

7.  **$(d-1)$-form 对称性是什么？算符成了点？** 

    对，$q=d-1$ 时对称算符维数是 $d-(d-1)-1=0$，即支撑在**时空点**上。 这意味着存在**局域的拓扑算符**。

    这种情形很特殊：局域拓扑算符 $U(x)$ 因拓扑性而与位置无关， 可以同时对角化，其本征值**标记了互不通信的“宇宙”** （universes）——理论**分解**（decomposition）成若干 超选择扇区。带荷对象是 $(d-1)$ 维的，即畴壁。

    物理例子：2 维 $\mathrm{U}(1)$ 规范理论、 或存在拓扑 $\theta$ 项且真空按 $\theta$ 标记的情形。 第一次听课不必深究，但要认得这个词。

8.  **为什么我学 QFT 时从没遇到 1-form 对称性？** 

    见要点 [kp:whypure]。三个原因叠加：

    1.  标准模型有电荷 $1$ 的物质（电子、夸克）， 把电 1-form 对称性完全破坏（[eq:UtoZq] 取 $q=1$）；

    2.  没有观测到磁单极子，磁 1-form 对称性虽然存在但用不上；

    3.  传统教科书只讲“作用在粒子态上的对称性”， 而 1-form 对称性作用在线算符上， 在散射振幅语言里看不见。

    所以这不是你的知识漏洞，而是**历史与侧重点**的问题。

9.  **有些文献说 higher-form symmetry 是“涌现的／近似的”， 什么意思？** 

    意思是它只在某个能量窗口或某个近似下成立。例如：

    - 若电荷 $q$ 很大，$\mathbb{Z}_q^{(1)}$ 虽是精确的， 但在低能有效理论中常可近似当作 $\mathrm{U}(1)^{(1)}$；

    - 磁 1-form 对称性在有磁单极子的理论中被破坏， 但若单极子很重，在低能下**近似**守恒 （磁流守恒在磁流体力学中就是这样用的）。

    判断方法照旧：*对称算符在多好的近似下是拓扑的？* $\mathrm{d}\star J$ 有多小？

10. **Wilson 线是对称算符还是带荷算符？** 

    在纯 Maxwell 中它是**带荷算符**（被 $U_e$ 作用）。 这是最常见的混淆点，因为 $W_n=e^{in\oint A}$ 的形式 与对称算符 $e^{i\alpha\oint \star F/e^2}$ 长得很像。 区别是被积的东西：

    $A$（不闭：$\mathrm{d}A=F\ne0$）$\Rightarrow$ 不拓扑 $\Rightarrow$ 带荷； $\star F$（闭：$\mathrm{d}\star F=0$）$\Rightarrow$ 拓扑 $\Rightarrow$ 对称算符。

    

    **“看被积形式闭不闭”是最快的判别法。**

11. **“$p$-form 对称性”里的 $p$ 到底数什么？** 

    数**带荷对象的维数**（本讲义的 $q$）。 这是 GKSW 的标准约定，也是绝大多数文献的约定。 但**偶有作者用对称算符的余维或电流次数来命名**， 读文献时务必用要点 [kp:dimensioncheck] 的三连自查 反推作者的约定，不要硬记名字。

12. **’t Hooft 反常和我学过的 ABJ 反常是一回事吗？** 

    不是，见注意 [warn:twoanomalies]。

    - ABJ：对称性**被破坏**，$\partial_\mu j^\mu\ne0$， 守恒律没了。

    - ’t Hooft：对称性**完好**，$\partial_\mu j^\mu=0$； 只是**不能规范化**。

    一个统一的看法：ABJ 反常可以理解为“把某个对称性规范化之后， 另一个对称性出现了 ’t Hooft 反常”， 所以两者在背景场语言中是同一个框架的不同切片。 本课程主要用第二种。

13. **规范化（gauging）与自发破缺有什么关系？** 

    两者**完全不同**，但常被并列提到：

    |              | 自发破缺                 | 规范化                         |
    |:-------------|:-------------------------|:-------------------------------|
    | 是否改变理论 | 否（同一个理论的一个相） | **是**（得到*新*理论）         |
    | 对称性去哪了 | 仍存在，只是真空不对称   | 变成规范冗余，不再是全局对称性 |
    | 后果         | Goldstone 模、真空退化   | 算符谱被投影，出现对偶对称性   |
    | 可否总是做   | 由动力学决定             | 有 ’t Hooft 反常时**不可以**   |

    

14. **为什么老师总要把理论放在一般（弯曲、非平凡拓扑）流形上？** 

    因为**广义对称性的信息藏在拓扑里**。 在 $\mathbb{R}^d$ 上，所有闭曲面都可以收缩到一点， $H^p(\mathbb{R}^d)$ 除 $p=0$ 外全为零， 于是所有连接数都是零、所有对称算符都平凡——**什么都看不见**。

    只有把时空取成有非平凡拓扑的（如 $S^1\times S^3$、$T^4$、 或挖去一条线的 $\mathbb{R}^4$）， 才能有非零的连接数、非平凡的通量扇区、 以及区分不同全局结构的观测量。 所以“放到一般流形上”不是数学炫技，而是**测量工具**。

# 听课重点

## 三条必须听懂的主线

1.  **“对称性 $=$ 拓扑算符”的完整逻辑。** 听老师如何从 $\partial_\mu j^\mu=0$ 走到 “$U(\Sigma)$ 只依赖 $[\Sigma]$”。 若这一步没跟上，后面全部内容都会变成术语堆砌。 **预习对策**：第 4.6 小节。

2.  **维数记账。** 每当老师写下一个对称算符，立刻在笔记边上标注 “$d=?$，$q=?$，支撑维数 $=?$，带荷对象维数 $=?$”。 **预习对策**：要点 [kp:dimensioncheck]、表 1。

3.  **Maxwell 的两个 1-form 对称性。** 这是全课程的标准例子，后面的一切 （反常、对偶、全局结构、禁闭）都会回到它。 **预习对策**：第 9.2 小节， 务必自己推一遍 [eq:fluxisn]。

## 课上要主动记录的六件事

1.  **老师的约定**。$q$ 数什么？$2\pi$ 放哪？ 号差与信号（洛伦兹／欧氏）？ **第一堂课就把约定抄下来**， 否则后面对不上因子会很痛苦。

2.  **每个例子的“三件套”**： 对称算符是什么、带荷对象是什么、荷怎么读出来。 听完一个例子若答不出这三问，就是没听懂。

3.  **哪些结论依赖运动方程，哪些是恒等式** （要点 [kp:two-sources]）。 这决定了加入物质场后对称性是否存活。

4.  **每次出现“不能规范化”时，反常是什么形式**。 记下 $(d+1)$ 维拓扑项的形状，哪怕系数记不准。

5.  **融合规则**。看到 $\mathcal N\times\mathcal N=\cdots$ 这类式子立刻判断可逆性，并用“本征值相乘”自查 （见第 9.1.5 小节练习）。

6.  **老师提到的开放问题**。这个领域仍在快速发展， 老师随口说的“这个还不清楚”往往是很好的课题线索。

## 自检清单：上课前能否回答

1.  我能在 5 行内推出 Noether 流 [eq:noethercurrent]。

2.  我能说明为什么 $\mathrm{d}\star j=0$ 等价于 $U(\Sigma)$ 可自由形变。

3.  给定 $d$ 与 $q$，我能立刻写出对称算符与带荷对象的维数， 并验证 $(d-q-1)+q+1=d$。

4.  我能写出 Maxwell 的两个对称算符 [eq:maxwellops] 并说清各自的守恒来源。

5.  我能推导 $\frac{1}{e^2}\oint_{\Sigma_2}\star F=n$ （即 [eq:fluxisn]）。

6.  我知道为什么加入电荷 $q$ 的物质把 $\mathrm{U}(1)^{(1)}_e$ 打成 $\mathbb{Z}_q^{(1)}$。

7.  我能陈述“禁闭 $\Leftrightarrow$ 1-form 对称性未破缺” 并说出对应的 Wilson 圈行为。

8.  我能区分对称算符、带荷算符、缺陷（Q[q:three] 的三个问题）。

9.  我能从 $\mathcal N^2=\mathbf 1+\eta$ 论证 $\mathcal N$ 不可逆。

10. 我知道 ’t Hooft 反常与 ABJ 反常的区别。

11. 我能说出规范化 $q$-form $G$ 后得到什么对称性 （[eq:dualsym]）。

12. 我理解为什么要在非平凡拓扑的流形上讨论（Q[q:manifold]）。

## 课后 48 小时内应该做的事

- 把课上每个新对称性填进一张自制的表 1 式字典里；

- 至少自己重做一遍课上的连接数／通量计算；

- 把老师用的约定与本讲义的约定做一次对照表， 标出差异（这一步能省掉后面大量困惑）。

# 进一步学习路线

## 建议顺序

1.  **奠基（读原始论文）**。 Gaiotto–Kapustin–Seiberg–Willett， *Generalized Global Symmetries*（arXiv:1412.5148）。 这是本领域的**奠基文献**，通常简称 **GKSW**。 建议读第 1–3 节：那里就是本讲义第 7–9.2 小节的内容， 只是更简洁。读完你会发现本讲义的 Maxwell 推导 与其第 2 节几乎逐行对应。

2.  **本课程直接相关的讲义**。 D. Brennan 与 S. Hong， *Introduction to Generalized Global Symmetries in QFT and Particle Physics*（arXiv:2306.00912）。 **授课老师本人合写的入门讲义**， 侧重与粒子物理的联系。若只读一份补充材料，读这份。

3.  **全景综述**。

    - Córdova–Dumitrescu–Intriligator–Shao， Snowmass 白皮书 *Generalized Symmetries in Quantum Field Theory and Beyond*（arXiv:2205.09545）——最好的“地图”。

    - J. McGreevy， *Generalized Symmetries in Condensed Matter* （arXiv:2204.03045）——凝聚态视角， 对格点模型与 Ising 例子讲得很实在。

4.  **不可逆／范畴型对称性**。

    - S. Schäfer-Nameki， *ICTP Lectures on (Non-)Invertible Generalized Symmetries*（arXiv:2305.18296）。

    - S.-H. Shao， *What’s Done Cannot Be Undone: TASI Lectures on Non-Invertible Symmetries*（arXiv:2308.00747）—— Ising 的 $\mathcal N$ 线在这里讲得最透。

5.  **反常与应用**。

    - Gaiotto–Kapustin–Komargodski–Seiberg， *Theta, Time Reversal, and Temperature* （arXiv:1703.00501）—— $\mathbb{Z}_N$ 1-form 中心对称性与 $\theta$ 角混合反常的 标志性应用。

    - Kapustin–Seiberg， *Coupling a QFT to a TQFT and Duality* （arXiv:1401.0740）——GKSW 的前身， 讲清了“全局结构”的意思。

    - ’t Hooft 1980 年的经典文章 *Naturalness, Chiral Symmetry, and Spontaneous Chiral Symmetry Breaking*——反常匹配论证的源头。

**注意。**

上面的 arXiv 编号供检索定位之用。文献版本、题名与编号偶有变动， **请以老师课上给出的书目为准**， 并在 arXiv 上按作者与题名再确认一次。

## 按主题的补充线索

| 想深入的主题       | 关键词（用于检索）                                                     |
|:-------------------|:-----------------------------------------------------------------------|
| 高群               | higher group, 2-group symmetry, Córdova–Dumitrescu–Intriligator        |
| 对称拓扑场论       | symmetry topological field theory, SymTFT, sandwich construction       |
| 不可逆手征对称性   | non-invertible chiral symmetry, axion, Choi–Córdova–Hsin–Lam–Shao      |
| 不可逆对偶缺陷     | duality defect, Tambara–Yamagami, Kaidi–Ohmori–Zheng                   |
| 2 维 CFT 拓扑线    | Verlinde line, topological defect line, Petkova–Zuber                  |
| 格点起源           | Wegner $\mathbb{Z}_2$ gauge theory, Wilson loop order parameter        |
| 凝聚态应用         | fracton, subsystem symmetry, toric code, Nussinov–Ortiz                |
| 反常的数学         | Freed–Moore–Segal, invertible field theory, cobordism                  |
| 超对称理论中的应用 | $\mathcal N=4$ global structure, $\mathrm{SU}(N)$ vs $\mathrm{PSU}(N)$ |

## 三个动手项目（巩固效果最好）

1.  **格点 $\mathbb{Z}_2$ 规范理论的 1-form 对称性**。 在 3 维（或 4 维）立方格点上写下 Wegner 的 $\mathbb{Z}_2$ 规范理论， 显式构造 1-form 对称算符（是链上 $\sigma^x$ 的乘积， 支撑在对偶格点的闭曲面上）， 验证它与 Hamilton 量交换， 并计算 Wilson 圈在强／弱耦合极限下的面积／周长律。 **这是把本讲义所有抽象概念变成有限维线性代数的最好练习。**

2.  **Ising 链上显式构造 KW 对偶算符**。 用 [eq:KWvars] 在有限链上写出对偶变换矩阵， 数值验证临界点 $J=h$ 处的谱自对偶， 并检查 $\mathcal N$ 在 $\mathbb{Z}_2$ 奇态上的“零本征值”。

3.  **Maxwell 通量扇区**。 把 4 维 Maxwell 放在 $T^2\times\mathbb{R}^2$ 上， 计算磁通 $\frac{1}{2\pi}\oint_{T^2}F=m$ 的各个扇区， 显式看出磁 1-form 对称性如何标记这些扇区。

# 附录：微分形式与拓扑速查

供做题时快速回查。

## 次数记账表

| 对象                                                  | 形式次数 | 可积于                |
|:------------------------------------------------------|:---------|:----------------------|
| 函数 $f$                                              | 0        | 点                    |
| 规范场 $A$                                            | 1        | 曲线 $C$              |
| 场强 $F=\mathrm{d}A$                                  | 2        | 曲面 $\Sigma_2$       |
| $\star F$（$d=4$）                                    | 2        | 曲面 $\Sigma_2$       |
| $q$-form 对称性的电流 $J$                             | $q+1$    | —                     |
| $\star J$                                             | $d-q-1$  | $\mathcal{M}_{d-q-1}$ |
| $k$ 维子流形的 $\delta$ 形式 $\delta_{\mathcal{M}_k}$ | $d-k$    | —                     |
| 体积元 $\mathrm{vol}_d$                               | $d$      | 整个时空              |

## 常用恒等式

$$
\begin{aligned}
  \mathrm{d}^2&=0 \\
  \mathrm{d}(\omega_{(p)}\wedge\eta_{(q)})
    &=\mathrm{d}\omega_{(p)}\wedge\eta_{(q)}
     +(-1)^p\omega_{(p)}\wedge \mathrm{d}\eta_{(q)} \\
  \omega_{(p)}\wedge\eta_{(q)}&=(-1)^{pq}\eta_{(q)}\wedge\omega_{(p)} \\
  \int_{\mathcal{M}_{p+1}}\mathrm{d}\omega_{(p)}
    &=\int_{\partial\mathcal{M}_{p+1}}\omega_{(p)}
    &&\text{(Stokes)}\\
  \star\star\,\omega_{(p)}&=(-1)^{p(d-p)}\omega_{(p)}
    &&\text{(欧氏号差)}\\
  \partial_{\mu_1}J^{\mu_1\cdots\mu_{q+1}}=0
    &\ \Longleftrightarrow\ \mathrm{d}\star J=0 \\
  \int_{\mathcal{M}_d}\delta_{\mathcal{M}_k}\wedge\omega_{(k)}
    &=\int_{\mathcal{M}_k}\omega_{(k)}
    &&\text{(Poincaré 对偶)}\\
  \int_{V_{k}}\delta_{\mathcal{M}_{d-k}}
    &=\#\big(V_k\cap \mathcal{M}_{d-k}\big)
    &&\text{(相交数)}
\end{aligned}
$$

## 维数自查流程

给定一个陈述“$U$ 是 $q$-form 对称算符，作用在 $\mathcal{O}$ 上”：

1.  确认时空维数 $d$。

2.  计算 $\dim U=d-q-1$，与题中给的支撑维数核对。

3.  计算 $\dim\mathcal{O}=q$，与题中给的带荷对象核对。

4.  检查 $\dim U+\dim\mathcal{O}+1=d$。

5.  若用连续对称性，检查电流是 $(q+1)$-形式、$\star J$ 是 $(d-q-1)$-形式。

任一步不通过，就是记错了约定或记错了维数——回到 要点 [kp:dimensioncheck] 重新数。

## 三个例子的完整参数表

|              | Ising（$\mathbb{Z}_2$） | Maxwell（电）                 | Maxwell（磁）            |
|:-------------|:------------------------|:------------------------------|:-------------------------|
| $d$          | 2                       | 4                             | 4                        |
| $q$          | 0                       | 1                             | 1                        |
| 群           | $\mathbb{Z}_2$          | $\mathrm{U}(1)$               | $\mathrm{U}(1)$          |
| $\star J$    | — (离散)                | $\star F/e^2$                 | $F/2\pi$                 |
| 守恒来源     | —                       | 运动方程                      | Bianchi                  |
| 对称算符维数 | 1                       | 2                             | 2                        |
| 对称算符     | $\prod_j\sigma^x_j$     | $e^{i\alpha\oint\star F/e^2}$ | $e^{i\beta\oint F/2\pi}$ |
| 带荷对象维数 | 0                       | 1                             | 1                        |
| 带荷对象     | $\sigma^z_j$            | $W_n(C)$                      | $T_m(C)$                 |
| 荷           | $\pm1$                  | $n\in\mathbb{Z}$              | $m\in\mathbb{Z}$         |
| 破缺相       | 有序相                  | Coulomb 相                    | Coulomb 相               |
| 未破缺相     | 无序相                  | 禁闭相                        | —                        |

## 练习答案要点

- **练习 [ex:forms](a)**： 由 [eq:dsquared] 取 $p=1$， $\mathrm{d}(A\wedge F)=\mathrm{d}A\wedge F-A\wedge \mathrm{d}F
          =F\wedge F-0=F\wedge F$。 故 $\int F\wedge F$ 是全导数的积分，只依赖拓扑。

- **练习 [ex:pivot](b)**： $Q(\Sigma)-Q(\Sigma')=q$，即扫过一个荷 $q$ 的算符时 荷读数跳变 $q$；等价地 $U_\alpha(\Sigma)=e^{iq\alpha}U_\alpha(\Sigma')$ （作用在含该算符的关联函数上）。

- **练习 [ex:gaugecheck]**： (a) 2-form $\mathbb{Z}_N$；(b) 1-form $\mathbb{Z}_N$（形式不变）； (c) 3 维中 0-form $\mathbb{Z}_N$ 规范化得 1-form $\mathbb{Z}_N$， 两者的带荷对象（局域算符与线算符）之间的相互相位 $e^{2\pi i nm/N}$ 就是 $\mathbb{Z}_N$ 规范理论中 电／磁线的辫结相位。

- **练习 [ex:maxwell](c)**： $N$ 度为 2 的物质能屏蔽 $n_R\in2\mathbb{Z}$ 的线， 残留 $\mathbb{Z}_N/\langle 2\rangle=\mathbb{Z}_{\gcd(2,N)}$； $N$ 偶时残留 $\mathbb{Z}_2$，$N$ 奇时完全破坏。

## 一页总结
