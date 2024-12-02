package com.mbc.cook.entity.community;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDateTime;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name = "cookcommunity")
@SequenceGenerator(name = "cook", sequenceName = "community_num_seq", allocationSize = 1, initialValue = 10001)
public class CommunityEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "cook")
    @Column(name = "community_num")
    long communityNum;
    @Column(name = "community_title")
    String communityTitle;
    @Column(name = "community_id")
    String communityId;
    @Column(name = "community_content")
    String communityContent;
    @Column(name = "community_date")
    LocalDateTime communityDate;
    @Column(name = "community_update_date")
    LocalDateTime communityUpdateDate;
    @Column(name = "community_readcnt")
    int communityReadcnt;
}
