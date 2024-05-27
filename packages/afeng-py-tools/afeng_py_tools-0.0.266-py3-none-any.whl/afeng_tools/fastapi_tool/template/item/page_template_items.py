from typing import Any, Optional

from pydantic import BaseModel


class PageTemplateItem(BaseModel):
    """页面模板项"""
    page_header_template: str
    page_footer_template: str
    data_dict: Optional[dict[str, Any]] = None
