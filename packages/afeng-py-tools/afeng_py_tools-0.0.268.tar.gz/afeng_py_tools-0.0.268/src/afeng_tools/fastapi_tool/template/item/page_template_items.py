from typing import Any, Optional

from pydantic import BaseModel


class PageTemplateItem(BaseModel):
    """页面模板项"""
    # 页面html中head标签元素
    html_head_template: Optional[str] = None
    # 页面头部模板
    page_header_template: Optional[str] = None
    # 页面底部模板
    page_footer_template: Optional[str] = None
    data_dict: Optional[dict[str, Any]] = None
