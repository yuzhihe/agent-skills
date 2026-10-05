#!/usr/bin/env python3
"""Validate local cases and build the small task index and offline catalog.

Python standard library only. Run with --check to detect broken references or
generated files that have not been refreshed after editing a case's meta.json.
"""

import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "library"
CASES = LIBRARY / "cases"
TASKS = {
    "product": "产品与商业介绍",
    "commerce": "商品与商店",
    "editorial": "阅读与文档",
    "utility": "工具与数据",
    "discovery": "搜索与发现",
    "creator": "创作与社区",
    "education": "教育与健康服务",
    "brand": "品牌与议题",
    "portfolio": "作品展示",
    "pricing": "定价比较",
    "forms": "表单与账户",
    "dashboard": "仪表盘",
}
DENSITY = {"low": "低", "medium": "中", "high": "高"}
LANG = {"en": "英文", "zh": "中文", "multi": "多语言", "ja": "日文"}
TONE = {
    "analytical": "理性", "bold": "鲜明", "bright": "明亮",
    "clean": "清爽", "dark": "暗色", "editorial": "编辑感",
    "energetic": "活跃", "friendly": "友好", "gentle": "柔和",
    "image-led": "图像优先", "minimal": "克制", "neutral": "中性",
    "playful": "活泼", "practical": "务实", "premium": "精致",
    "restrained": "收敛", "structured": "秩序感", "utilitarian": "实用",
    "warm": "温暖",
}
ASSET = {
    "none": "无特殊素材", "product-screenshots": "产品截图",
    "product-photos": "产品图", "commerce-data": "商品数据",
    "editorial-photos": "统一摄影", "illustration": "插画",
    "project-photos": "项目图", "project-data": "项目资料",
    "content-previews": "内容预览", "creator-data": "创作者资料",
    "article-covers": "文章封面", "structured-content": "结构化内容",
    "structured-data": "结构化数据", "trusted-data": "可信数据",
    "charts": "图表", "listing-photos": "列表照片",
    "event-images": "活动图", "event-data": "活动资料",
    "licensed-photos": "可用摄影", "product-images": "产品画面",
    "original-campaign-images": "原创活动视觉",
    "portfolio-images": "作品图",
}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
MARKDOWN_LINK = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")


def escaped(value):
    return html.escape(str(value), quote=True)


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def labels(values, mapping):
    return "、".join(mapping[item] for item in values)


def read_cases():
    errors = []
    cases = []
    seen_orders = set()
    for directory in sorted(path for path in CASES.iterdir() if path.is_dir()):
        path = directory / "meta.json"
        if not path.is_file():
            errors.append(f"{directory.name}: 缺少 meta.json")
            continue
        try:
            case = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            errors.append(f"{path}: JSON 无法读取：{exc}")
            continue
        required = ("order", "id", "name", "source", "studied", "tasks",
                    "density", "assets_needed", "tone", "lang", "summary", "usage")
        missing = [key for key in required if key not in case]
        if missing:
            errors.append(f"{path}: 缺少字段 {', '.join(missing)}")
            continue
        slug = case["id"]
        if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug != directory.name:
            errors.append(f"{path}: id 必须与安全的目录名一致")
            continue
        if not isinstance(case["order"], int) or case["order"] < 1 or case["order"] in seen_orders:
            errors.append(f"{path}: order 必须是唯一正整数")
        seen_orders.add(case["order"])
        for key in ("name", "summary", "usage"):
            if not isinstance(case[key], str) or not case[key].strip():
                errors.append(f"{path}: {key} 不能为空")
        source = case["source"]
        if not isinstance(source, str) or urlparse(source).scheme not in ("http", "https") or not urlparse(source).netloc:
            errors.append(f"{path}: source 需要完整 URL")
        try:
            date.fromisoformat(case["studied"])
        except (ValueError, TypeError):
            errors.append(f"{path}: studied 必须是 YYYY-MM-DD")
        for key, mapping in (("tasks", TASKS), ("assets_needed", ASSET), ("tone", TONE)):
            if not isinstance(case[key], list) or not case[key] or any(
                not isinstance(item, str) or item not in mapping for item in case[key]
            ):
                errors.append(f"{path}: {key} 须为非空的已定义标签数组")
        if (not isinstance(case["density"], str) or case["density"] not in DENSITY
                or not isinstance(case["lang"], str) or case["lang"] not in LANG):
            errors.append(f"{path}: density 或 lang 标签无效")
        for filename in ("analysis.md", "screenshots/desktop.jpg", "screenshots/mobile.jpg"):
            if not (directory / filename).is_file():
                errors.append(f"{directory / filename}: 文件不存在")
        for evidence in directory.glob("evidence-*.json"):
            try:
                json.loads(evidence.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as exc:
                errors.append(f"{evidence}: JSON 无法读取：{exc}")
        analysis = directory / "analysis.md"
        if analysis.is_file():
            body = analysis.read_text(encoding="utf-8")
            for field, pattern in (("source", r"^- 来源：(\S+)"),
                                   ("studied", r"^- 研究日期：(\d{4}-\d{2}-\d{2})")):
                match = re.search(pattern, body, re.MULTILINE)
                if match and match.group(1) != case[field]:
                    errors.append(f"{analysis}: 正文的{field}与 meta.json 不一致")
            for target in MARKDOWN_LINK.findall(body):
                target = target.split("#", 1)[0]
                if target and not urlparse(target).scheme and not (directory / target).is_file():
                    errors.append(f"{analysis}: 本地引用不存在：{target}")
        cases.append(case)
    if not cases:
        errors.append("没有找到有效案例")
    return sorted(cases, key=lambda case: case["order"]), errors


def build_index(cases):
    days = sorted(case["studied"] for case in cases)
    lines = [
        "# 内置案例索引", "",
        f"共 {len(cases)} 个本地案例，研究日期 {days[0]} 至 {days[-1]}。本页由 [构建脚本](../scripts/build_library.py) 生成。", "",
        "先确定页面任务，再读对应的任务索引；比较内容密度和可用素材后，只打开少数案例正文。",
        "风格标签用于辅助选择，不能替代任务适配。案例是局部研究快照，不是完整设计系统或用户已确认的偏好。", "",
        "| 页面任务 | 案例数 | 先看这些案例 |", "| --- | ---: | --- |",
    ]
    for task, label in TASKS.items():
        matching = [case for case in cases if task in case["tasks"]]
        if not matching:
            continue
        examples = "、".join(case["name"] for case in matching[:3])
        lines.append(f"| [{label}](indexes/{task}.md) | {len(matching)} | {md(examples)} |")
    lines += ["", "需要查看所有缩略图时打开 [离线案例浏览页](catalog.html)。样式 JSON 只在需要精确参数时读取。", ""]
    return "\n".join(lines)


def build_task_index(task, cases):
    matching = [case for case in cases if task in case["tasks"]]
    lines = [f"# {TASKS[task]}", "", "[返回任务入口](../index.md) · 按任务与素材选择候选，再阅读分析正文。", "",
             "| 案例 | 可借鉴的组织方式 | 密度 | 素材依赖 | 气质 | 原站语言 |",
             "| --- | --- | --- | --- | --- | --- |"]
    for case in matching:
        path = f"../cases/{case['id']}/analysis.md"
        lines.append(f"| [{md(case['name'])}]({path}) | {md(case['summary'])} | {DENSITY[case['density']]} | "
                     f"{labels(case['assets_needed'], ASSET)} | {labels(case['tone'], TONE)} | {LANG[case['lang']]} |")
    lines += ["", "标签概括研究快照；适合和不适合的条件以案例正文为准。", ""]
    return "\n".join(lines)


def build_catalog(cases):
    template = (LIBRARY / "catalog-template.html").read_text(encoding="utf-8")
    filters = ['<button aria-pressed="true" data-filter="all">全部</button>']
    for task, label in TASKS.items():
        if any(task in case["tasks"] for case in cases):
            filters.append(f'<button aria-pressed="false" data-filter="{task}">{escaped(label)}</button>')
    cards = []
    for position, case in enumerate(cases, 1):
        slug = case["id"]
        name = escaped(case["name"])
        summary = escaped(case["summary"])
        usage = escaped(case["usage"])
        tone = escaped(labels(case["tone"], TONE))
        task = escaped(TASKS[case["tasks"][0]])
        keywords = escaped(" ".join([case["name"], case["summary"], case["usage"],
                                     labels(case["tone"], TONE),
                                     labels(case["assets_needed"], ASSET),
                                     " ".join(TASKS[key] for key in case["tasks"])]))
        evidence = f'<a href="cases/{slug}/evidence-desktop.json">实测样式 ↗</a>' if (
            CASES / slug / "evidence-desktop.json").is_file() else ""
        cards.append(
            f'<article class="case" data-id="{slug}" data-category="{" ".join(case["tasks"])}" data-keywords="{keywords}">'
            f'<button class="preview" aria-label="查看 {name} 截图">'
            f'<img loading="lazy" src="cases/{slug}/screenshots/desktop.jpg" alt="{summary}" width="1280" height="720"></button>'
            f'<div><div class="meta"><span>{position:02d} / {task}</span><span>{tone}</span></div>'
            f'<h2>{name}</h2><p>{summary}</p><div class="links">'
            f'<a href="cases/{slug}/analysis.md">阅读分析 ↗</a>'
            f'{evidence}</div>'
            f'<details><summary>适合什么时候用</summary><p>{usage}</p></details></div></article>'
        )
    days = sorted(case["studied"] for case in cases)
    replacements = {"COUNT": str(len(cases)), "FILTERS": "".join(filters),
                    "CARDS": "\n".join(cards), "DATE_RANGE": f"{days[0]} 至 {days[-1]}"}
    for key, value in replacements.items():
        template = template.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[A-Z_]+\}\}", template):
        raise ValueError("catalog-template.html 中存在未填充的占位符")
    return template


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="校验来源和生成文件，不写入")
    args = parser.parse_args()
    cases, errors = read_cases()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    outputs = {LIBRARY / "index.md": build_index(cases),
               LIBRARY / "catalog.html": build_catalog(cases)}
    for task in TASKS:
        if any(task in case["tasks"] for case in cases):
            outputs[LIBRARY / "indexes" / f"{task}.md"] = build_task_index(task, cases)
    stale = []
    for path, expected in outputs.items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
    if stale:
        print("需要重新生成：" + ", ".join(stale), file=sys.stderr)
        return 1
    print(f"{'校验通过' if args.check else '已生成'}：{len(cases)} 个案例，{len(outputs)} 个索引/浏览文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
