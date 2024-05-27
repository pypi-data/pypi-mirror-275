from typing import Optional

from pydantic import BaseModel, Field


class ArticleInfoItem(BaseModel):
    """文章信息项"""
    code: str = Field(title='编码')
    title: str = Field(title='标题')
    sub_title: Optional[str] = Field(default=None, title='副标题')
    description: Optional[str] = Field(title='简介', default=None)
    publish_time: Optional[str] = Field(title='发布时间', default=None)


class ArticleDetailInfoItem(ArticleInfoItem):
    """文章详情信息项"""
    content: Optional[str] = Field(title='内容', default=None)
