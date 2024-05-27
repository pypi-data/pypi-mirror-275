from typing import Optional
from pydantic import BaseModel


class UserProfile(BaseModel):
    about: Optional[str] = None
    active: bool
    avatar_url: str
    back_number_post_images_count: int
    back_number_post_videos_count: int
    banner_url: str
    cant_receive_message: bool
    current_back_number_plan: Optional[str] = None
    followers_count: int
    followings_count: int
    has_approved_user_identification: bool
    id: str
    is_bought_back_number: bool
    is_followed: bool
    is_following: bool
    is_official: bool
    is_official_creator: bool
    is_subscribed: bool
    label: Optional[str] = None
    likes_count: int
    limited_posts_count: int
    link_instagram_id: Optional[str] = None
    link_instagram_url: Optional[str] = None
    link_tiktok_id: Optional[str] = None
    link_tiktok_url: Optional[str] = None
    link_twitter_id: Optional[str] = None
    link_twitter_url: Optional[str] = None
    link_youtube_url: Optional[str] = None
    name: str
    post_images_count: int
    post_videos_count: int
    posts_count: int
    sns_link1: Optional[str] = None
    sns_link2: Optional[str] = None
    username: str
