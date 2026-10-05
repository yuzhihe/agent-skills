# 设计模式入口

[返回任务入口](index.md)

具体组件或交互需求从这里找候选；整页布局优先按任务查。标签表示案例中有相应证据，不保证整个流程或所有操作已验证。
先看使用边界，再读候选的分析和对应状态截图。组件示例可作辅助参考，不能因此替换整页风格。列表顺序不是推荐排名。

| 需求与常见说法 | 候选与使用边界 |
| --- | --- |
| 数据表格 / 列对齐 | [Grafana Play · 数据仪表盘](cases/grafana-dashboard/analysis.md)（公开仪表盘局部；未编辑，部分面板加载不稳定。）；[React-admin · 订单操作后台](cases/react-admin-orders/analysis.md)（已验证行选择；未执行批量动作，空结果缺少说明。） |
| 行选择 / 批量操作 | [React-admin · 订单操作后台](cases/react-admin-orders/analysis.md)（已验证行选择；未执行批量动作，空结果缺少说明。） |
| 筛选菜单 / 筛选抽屉 | [Google Fonts · 字体发现](cases/google-fonts/analysis.md)（已操作手机筛选抽屉；未逐项验证筛选结果。）；[React-admin · 订单操作后台](cases/react-admin-orders/analysis.md)（已验证行选择；未执行批量动作，空结果缺少说明。）；[Ionic Conference · 移动议程](cases/ionic-conference/analysis.md)（旧演示部署；筛选仅开关面板，未验证全部目的地。） |
| 资源搜索 / 预览比较 | [Figma Community](cases/figma-community/analysis.md)（社区资源首页；不是设计编辑器。）；[Unsplash](cases/unsplash/analysis.md)（图像发现页；需自有或可用图片，未验证查询。）；[Google Fonts · 字体发现](cases/google-fonts/analysis.md)（已操作手机筛选抽屉；未逐项验证筛选结果。） |
| 购物车抽屉 / 订单摘要 | [Spree · 购物车与结账](cases/spree-checkout/analysis.md)（已查看结账与摘要；未提交订单，未验证支付结果。） |
| 结账 / 配送与支付表单 | [Spree · 购物车与结账](cases/spree-checkout/analysis.md)（已查看结账与摘要；未提交订单，未验证支付结果。） |
| 表单校验 / 输入错误 | [Tally · 联系表单模板](cases/tally-contact/analysis.md)（模板错误反馈；预览可跳过错误，未验证成功提交。）；[SurveyJS · 分步与条件表单](cases/surveyjs-wizard/analysis.md)（已验证分页、条件追问与格式错误；未最终提交或保存草稿。） |
| 条件表单 / 选择后追问 | [SurveyJS · 分步与条件表单](cases/surveyjs-wizard/analysis.md)（已验证分页、条件追问与格式错误；未最终提交或保存草稿。） |
| 分步表单 / 上一步与下一步 | [SurveyJS · 分步与条件表单](cases/surveyjs-wizard/analysis.md)（已验证分页、条件追问与格式错误；未最终提交或保存草稿。） |
| 移动底部导航 | [Airbnb](cases/airbnb/analysis.md)（房源发现局部；未覆盖预订流程。）；[Ionic Conference · 移动议程](cases/ionic-conference/analysis.md)（旧演示部署；筛选仅开关面板，未验证全部目的地。） |
| 深浅主题 / 暗色模式 | [Radix Themes · 主题与按钮状态](cases/radix-theme-states/analysis.md)（仅组件状态；加载为预置示例，窄屏矩阵有裁切。）；[Tiptap · 富文本编辑工作区](cases/tiptap-editor/analysis.md)（已看工具与主题；未验证保存、协作、软键盘和替换结果。） |
| 按钮禁用 / 加载状态 | [Radix Themes · 主题与按钮状态](cases/radix-theme-states/analysis.md)（仅组件状态；加载为预置示例，窄屏矩阵有裁切。） |
| 富文本编辑 / 格式工具条 | [Tiptap · 富文本编辑工作区](cases/tiptap-editor/analysis.md)（已看工具与主题；未验证保存、协作、软键盘和替换结果。） |
| 社区主题 / 回复流 | [Discourse Meta · 社区主题阅读](cases/discourse-topic/analysis.md)（已看回复与阅读面板；跳转未执行，未研究发帖。） |
| 长讨论阅读位置 / 跳转面板 | [Discourse Meta · 社区主题阅读](cases/discourse-topic/analysis.md)（已看回复与阅读面板；跳转未执行，未研究发帖。） |
| 折叠展开 / 服务分流 | [Citizens Advice · 服务分流指南](cases/citizens-advice-service/analysis.md)（已展开一个服务分类；未发起联系或提交资料。） |
| 定价卡片 / 套餐比较 | [飞书 · 中文定价比较](cases/feishu-pricing/analysis.md)（桌面档位与比较表；窄屏卡片有裁切，报价为快照。） |
| 文字个人主页 / 经历时间线 | [Derek Sivers · 文字型个人网站](cases/sivers-personal/analysis.md)（文字型主页；标题字体有加载差异，研究区无需图片。） |
| 文档目录 / 页内导航 | [MDN CSS 文档](cases/mdn-docs/analysis.md)（CSS 概览首屏；其他文档和目录操作未完整验证。）；[Cash App · 颜色规范](cases/cash-app-guidelines/analysis.md)（品牌规范子页；颜色定义与截图呈色需区分。） |
| 预约月历 / 日期与时段 | [Cal.com · 预约日历示例](cases/cal-booking/analysis.md)（已选择日期；未预约，手机后续时段未完整研究。） |

未找到对应模式时，可按任务索引找相近参考；仍不适合就说明缺口，使用专业判断，不把缺陷或未验证状态当作推荐。
