## 0 bug C/C++商用工程之道
***
#### 商用工程开发思路
* **系统分析**
    
```
* 接到用户需求时，避免马上从编程角度开始思考，应首先理解需求，采用自上而下的策略（先搭框架，逐步细化）。  
* 对于需求，先看已有的相关文档，再讨论不明确的地方，最后确认优化时侧重时间还是空间以及特定要求等。  
* 在程序模块上，对数据以“宽进严出”作则，即对上家给的数据不作要求或不作过多要求，统统吃下；内部对于自己的数据做严格的校验，不符合的做出一定的log日志后抛弃。  
* 对于一个项目的各个需要通信的网络角色，固定统一的名称。  
* 确认基本的网络拓扑图。  
```

* **商用程序员对开发的理解**　

```
* 一切皆可为资源。系统分析首先是资源分析。资源包括技术资源、人力人际资源、处理对象资源等等。    
* 选择算法以最简化为原则，满足需求为原则，并且随时关注资源的消耗，成本的控制。  
* 客观。一分为二辩证看待问题，遇事，既不轻易肯定也不轻易否定，先分析再决策。  
* 善于利用资源，同事、领导也可作为资源，遇到问题，既不会不思进取、轻言放弃，也不会死钻牛角尖、拒绝帮助。  
* 不回避责任也不讳言能力不够，尽早暴露问题，规避项目风险。  
* 技术上，应选择熟悉的、最适用的技术去解决问题。  
* 在满足需求的前提下，尽可能解决成本，控制资源。  
* 平衡。对于成本巨大的需求，应给出详细的分析说明文档，以请求降低需求等等。  
* 遇事要多沟通。  
* 忌讳把单项性能做到登峰造极，避免占用过多其他部分的资源。  
* 忌单兵作战，应团队协作。  
* “服务”意识：  
    1. 设计和实施工程项目时，不要眼睛老是看着自己的模块，多想想别人的模块是如何实现的，有没有好的方法让大家工作完成更好。  
    2. 随时考虑“上家”的数据是否有疏漏，帮助上家查漏补缺。  
    3. 谨慎地调用“下家”的模块，确保给出正确的数据参数，避免下家崩溃。  
    4. 主动热情地和同伴讨论问题，把问题尽量暴露在明处，自己有问题，主动请大家帮助，别人的问题，也主动思考。  
    5. 即使是模块级程序员，也试图用系统分析的思维考虑系统整体设计，帮助架构师或主管完善设计，从自己的模块角度提出优化建议，并积极讨论，努力把工作做得更好。  
    6. 以较为职业的态度和所有伙伴沟通，讨论问题对事不对人，尽量持客观的态度分析和解决问题，以获得团队成员的认同。  
    7. 遇到事情勇于承担责任，对工作尽心尽力，一切以完成项目为出发点，尽力使自己和团队完成项目任务。  
    8. 高度负责任地完成自己的工作，努力做到0 bug，以较高的产品质量，实现对项目整体目标的支撑。  
    9. 主动关注其他一些对项目实施有帮助的情况和风险，及时提出建议，帮助团队查漏补缺。  
* 服务，就是某种资源的拥有者对外提供的一种功能调用，其他模块在需要时通过对该服务提出申请完成功能，避免自行处理。技术上也应有“服务”意识。  
* 模块处理的数据和逻辑区域简单化，以简洁的应用接口NPI和API来实现互相之间的沟通，彼此既不关心对方实施细节，也拒绝别人关心。高内聚，低耦合。  
* 资源最近原则，降低传输成本。  
```

* **基本开发思路**　

```
* 资源有其有限性，在接到需求时第一要务为落实边界。边界决定数据结构，边界决定算法。  
* 一切皆可细分。对于需求，需要细分，细分到每个小功能，落实到程序可实现的地步。  
* 网络状况，永远只能分析，不能被观察。  
* 永远不要相信一条链路、一个模块会永远完好，也不要相信一次调用一定会成功，需要设置很多校验机制，仔细检查每次调用返回的结果，随时判定服务的成功与否，并处理每一个错误的情况，书写具有较高自防范性和自恢复性的程序逻辑，保证系统在任何错误下都能自动恢复，持续服务。  
* 灵活，逆向思维。  
* 考虑将成熟的代码模块做成工程程序库。并且只做增量补充，不做删改操作，避免旧工程的崩溃。  
* 做通用模块时，做到短小精悍。  
* 单笔交易失败不算失败。要做到出现bug有日志记录方便查询，能自动恢复，无资源泄漏，无崩溃，无累积性逻辑错误。  
```

* **数据传输各个角色的开发思路**  

```
* 服务器开发以稳定为主导思想，开发思路偏保守，尽量使用成熟技术，回避新技术的使用。
* 客户端程序技术多偏新，对程序的稳定性有一定放宽。  
* 服务器设计必须对所有资源的使用做专门的设计，及时做好资源回收，避免泄露。  
* 
```
