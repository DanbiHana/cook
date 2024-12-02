package com.mbc.cook.dto.community;

import com.mbc.cook.entity.community.CommunityEntity;
import jakarta.validation.constraints.NotBlank;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDateTime;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class CommunityDTO {
    long communityNum;

    @NotBlank(message = "글 제목을 입력해주세요.")
    String communityTitle;

    String communityId;

    @NotBlank(message = "글 내용을 입력해주세요.")
    String communityContent;

    LocalDateTime communityDate;
    LocalDateTime communityUpdateDate;
    int communityReadcnt;

    public CommunityEntity communityEntity() {
        return (new CommunityEntity(communityNum,communityTitle,communityId,communityContent,communityDate,communityUpdateDate,communityReadcnt));
    }
}
