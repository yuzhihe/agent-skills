# 覆盖说明

版本 0.5.1 · 50 个案例 · 2026-10-05。本页帮助判断资料够不够，不是每次设计的必读文件。具体组件或交互可先查 [设计模式入口](patterns.md)。案例数量是唯一案例数，任务标签允许交叉；某一页面的证据不能证明整个流程已经覆盖。

## 本轮补充与使用边界

| 原先偏弱的内容 | 优先参考 | 已取得的证据 | 仍未覆盖的部分 |
| --- | --- | --- | --- |
| 密集后台与表格操作 | [React-admin 订单](cases/react-admin-orders/analysis.md)、[GitHub Issues](cases/github-issues/analysis.md) | 表格、筛选菜单、行选择、批量动作入口、手机摘要、无匹配搜索 | 权限、真实批量执行、复杂详情编辑；无结果截图是缺陷示例 |
| 购物车与结账 | [Spree](cases/spree-checkout/analysis.md)、[IKEA 商品](cases/ikea-product/analysis.md) | 加购抽屉、结账字段、配送/支付区域、桌面摘要、手机摘要展开 | 最终订单、支付失败/成功、退款售后、中文地址流程 |
| 分步、条件问题与错误 | [SurveyJS](cases/surveyjs-wizard/analysis.md)、[Tally](cases/tally-contact/analysis.md) | 前后导航、无效邮箱、条件追问、空字段错误 | 完整注册/新用户引导、草稿持久化、最终提交及服务器错误 |
| 移动 App 式 Web | [Ionic 议程](cases/ionic-conference/analysis.md)、[Tiptap](cases/tiptap-editor/analysis.md)、[Spree](cases/spree-checkout/analysis.md) | 底部导航/工具条、全屏筛选、手机折叠摘要 | 软键盘、安全区、离线、原生手势、长流程触控验证 |
| 深浅主题与组件状态 | [Radix Themes](cases/radix-theme-states/analysis.md)、[Tiptap](cases/tiptap-editor/analysis.md) | 实际切换主题、按钮变体、预置禁用/加载、格式工具可用状态 | 独立成功/错误结果页、优秀空状态、骨架加载；WCAG 审计与系统主题联动 |
| 中文长文与教程 | [阮一峰博客](cases/ruanyifeng-longform/analysis.md)、[少数派](cases/sspai/analysis.md) | 标题/元信息、段落、图解、代码区与窄屏阅读 | 中文知识库编辑后台、中文社区回复与真实中文移动交易 |
| 少素材的个人风格 | [Derek Sivers](cases/sivers-personal/analysis.md)、[Works in Progress](cases/works-in-progress/analysis.md) | 文字摘要、时间线、内联链接、About 子页、编辑式层级 | 更多中文个人身份/履历实例；Sivers 标题字体有加载时序差异 |
| 专业与机构服务 | [Citizens Advice](cases/citizens-advice-service/analysis.md)、[Cal.com](cases/cal-booking/analysis.md) | 用户需求分流、折叠说明、预约日期选择 | B2B 专业服务完整转化、有效咨询提交、预约确认 |
| 社区讨论 | [Discourse](cases/discourse-topic/analysis.md)、[GitHub Issues](cases/github-issues/analysis.md) | 首帖/回复、参与摘要、移动阅读位置面板 | 发帖、引用编辑、审核、举报、通知与权限 |
| 编辑工作区 | [Tiptap](cases/tiptap-editor/analysis.md) | 正文聚焦、格式菜单、主题切换、查找/替换弹层 | 自动保存、离线恢复、协作冲突、撤销和查找替换结果 |
| 定价 | [飞书](cases/feishu-pricing/analysis.md) | 中文档位及展开比较 | 用量/阶梯计价交互仍偏弱，暂无新的已完成案例 |

## 数量与风格判断

本轮增加 10 个案例，其中一个中文长文，其余九个英文页面；整库为 43 个英文、6 个中文、1 个日文案例。中文仍然明显少，不能把英文交互直接翻译文字就视为中文适配完成。

克制文字、务实操作、秩序感、浅色/深色组件、机构服务等方向已有可用参考；原库的鲜明品牌、摄影、插画和编辑风格继续保留。此库足够为常见网页任务选主参考与辅助参考，但不是每个行业、每种审美、每条业务流程的完整组件库。

下一轮有明确任务时优先补：优秀空/错/成功/骨架状态、用量定价、中文移动操作和完整引导流程。仅增加另一批营销首页，对这些缺口帮助较小。
