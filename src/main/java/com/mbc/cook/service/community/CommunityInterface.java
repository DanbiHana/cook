package com.mbc.cook.service.community;

import java.time.LocalDate;

public interface CommunityInterface {
    public long getCommunityNum();
    public String getCommunityTitle();
    public String getCommunityId();
    public String getCommunityContent();
    public LocalDate getCommunityDate();
    public LocalDate getCommunityUpdateDate();
    public int getCommunityReadcnt();
}
