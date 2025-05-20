
<div style="position: relative; padding-top: 30px;">  
  <!-- your info text, absolutely positioned inside the container -->
  <div style="
      position: absolute;
      top: 0;
      right: 0;
      font-size: 0.8em;
      color: #666;
    ">
    Active: SOM4, IRE<BR>Frozen: all
  </div>
</div>

```mermaid
graph LR
    SOM4["SOM4<br/>SOM<br/>HH_reduced"]
    IRE["IRE<br/>RE<br/>HH_reduced"]
    SOM5Bfrz["SOM5Bfrz<br/>NetStim"]
    IT3frz["IT3frz<br/>NetStim"]
    PV5Afrz["PV5Afrz<br/>NetStim"]
    NGF3frz["NGF3frz<br/>NetStim"]
    VIP2frz["VIP2frz<br/>NetStim"]
    SOM6frz["SOM6frz<br/>NetStim"]
    HTCfrz["HTCfrz<br/>NetStim"]
    CT5Bfrz["CT5Bfrz<br/>NetStim"]
    PV5Bfrz["PV5Bfrz<br/>NetStim"]
    PV6frz["PV6frz<br/>NetStim"]
    IT5Bfrz["IT5Bfrz<br/>NetStim"]
    CT6frz["CT6frz<br/>NetStim"]
    VIP4frz["VIP4frz<br/>NetStim"]
    NGF2frz["NGF2frz<br/>NetStim"]
    PT5Bfrz["PT5Bfrz<br/>NetStim"]
    SOM3frz["SOM3frz<br/>NetStim"]
    NGF1frz["NGF1frz<br/>NetStim"]
    NGF6frz["NGF6frz<br/>NetStim"]
    VIP5Bfrz["VIP5Bfrz<br/>NetStim"]
    TCMfrz["TCMfrz<br/>NetStim"]
    VIP3frz["VIP3frz<br/>NetStim"]
    PV4frz["PV4frz<br/>NetStim"]
    SOM4frz["SOM4frz<br/>NetStim"]
    PV2frz["PV2frz<br/>NetStim"]
    IREfrz["IREfrz<br/>NetStim"]
    VIP5Afrz["VIP5Afrz<br/>NetStim"]
    NGF5Bfrz["NGF5Bfrz<br/>NetStim"]
    TCfrz["TCfrz<br/>NetStim"]
    CT5Afrz["CT5Afrz<br/>NetStim"]
    IT6frz["IT6frz<br/>NetStim"]
    SOM2frz["SOM2frz<br/>NetStim"]
    VIP6frz["VIP6frz<br/>NetStim"]
    IREMfrz["IREMfrz<br/>NetStim"]
    SOM5Afrz["SOM5Afrz<br/>NetStim"]
    ITP4frz["ITP4frz<br/>NetStim"]
    PV3frz["PV3frz<br/>NetStim"]
    NGF5Afrz["NGF5Afrz<br/>NetStim"]
    IT5Afrz["IT5Afrz<br/>NetStim"]
    NGF4frz["NGF4frz<br/>NetStim"]
    IT2frz["IT2frz<br/>NetStim"]
    ITS4frz["ITS4frz<br/>NetStim"]
    CT5Afrz -->|CxTh_CT5A_IRE| IRE
    CT5Bfrz -->|CxTh_CT5B_IRE| IRE
    CT6frz -->|CxTh_CT6_IRE| IRE
    CT5Afrz -->|EI_CT5A_SOM4_SOM_1| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_2| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_3| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_4| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_5A| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_5B| SOM4
    CT5Afrz -->|EI_CT5A_SOM4_SOM_6| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_1| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_2| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_3| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_4| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_5A| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_5B| SOM4
    CT5Bfrz -->|EI_CT5B_SOM4_SOM_6| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_1| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_2| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_3| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_4| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_5A| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_5B| SOM4
    CT6frz -->|EI_CT6_SOM4_SOM_6| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_1| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_2| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_3| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_4| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_5A| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_5B| SOM4
    IT2frz -->|EI_IT2_SOM4_SOM_6| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_1| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_2| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_3| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_4| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_5A| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_5B| SOM4
    IT3frz -->|EI_IT3_SOM4_SOM_6| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_1| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_2| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_3| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_4| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_5A| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_5B| SOM4
    IT5Afrz -->|EI_IT5A_SOM4_SOM_6| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_1| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_2| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_3| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_4| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_5A| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_5B| SOM4
    IT5Bfrz -->|EI_IT5B_SOM4_SOM_6| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_1| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_2| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_3| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_4| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_5A| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_5B| SOM4
    IT6frz -->|EI_IT6_SOM4_SOM_6| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_1| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_2| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_3| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_4| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_5A| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_5B| SOM4
    ITP4frz -->|EI_ITP4_SOM4_SOM_6| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_1| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_2| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_3| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_4| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_5A| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_5B| SOM4
    ITS4frz -->|EI_ITS4_SOM4_SOM_6| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_1| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_2| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_3| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_4| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_5A| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_5B| SOM4
    PT5Bfrz -->|EI_PT5B_SOM4_SOM_6| SOM4
    NGF1frz -->|II_NGF1_SOM4_1| SOM4
    NGF1frz -->|II_NGF1_SOM4_2| SOM4
    NGF1frz -->|II_NGF1_SOM4_3| SOM4
    NGF1frz -->|II_NGF1_SOM4_4| SOM4
    NGF1frz -->|II_NGF1_SOM4_5A| SOM4
    NGF1frz -->|II_NGF1_SOM4_5B| SOM4
    NGF1frz -->|II_NGF1_SOM4_6| SOM4
    NGF2frz -->|II_NGF2_SOM4_1| SOM4
    NGF2frz -->|II_NGF2_SOM4_2| SOM4
    NGF2frz -->|II_NGF2_SOM4_3| SOM4
    NGF2frz -->|II_NGF2_SOM4_4| SOM4
    NGF2frz -->|II_NGF2_SOM4_5A| SOM4
    NGF2frz -->|II_NGF2_SOM4_5B| SOM4
    NGF2frz -->|II_NGF2_SOM4_6| SOM4
    NGF3frz -->|II_NGF3_SOM4_1| SOM4
    NGF3frz -->|II_NGF3_SOM4_2| SOM4
    NGF3frz -->|II_NGF3_SOM4_3| SOM4
    NGF3frz -->|II_NGF3_SOM4_4| SOM4
    NGF3frz -->|II_NGF3_SOM4_5A| SOM4
    NGF3frz -->|II_NGF3_SOM4_5B| SOM4
    NGF3frz -->|II_NGF3_SOM4_6| SOM4
    NGF4frz -->|II_NGF4_SOM4_1| SOM4
    NGF4frz -->|II_NGF4_SOM4_2| SOM4
    NGF4frz -->|II_NGF4_SOM4_3| SOM4
    NGF4frz -->|II_NGF4_SOM4_4| SOM4
    NGF4frz -->|II_NGF4_SOM4_5A| SOM4
    NGF4frz -->|II_NGF4_SOM4_5B| SOM4
    NGF4frz -->|II_NGF4_SOM4_6| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_1| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_2| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_3| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_4| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_5A| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_5B| SOM4
    NGF5Afrz -->|II_NGF5A_SOM4_6| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_1| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_2| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_3| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_4| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_5A| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_5B| SOM4
    NGF5Bfrz -->|II_NGF5B_SOM4_6| SOM4
    NGF6frz -->|II_NGF6_SOM4_1| SOM4
    NGF6frz -->|II_NGF6_SOM4_2| SOM4
    NGF6frz -->|II_NGF6_SOM4_3| SOM4
    NGF6frz -->|II_NGF6_SOM4_4| SOM4
    NGF6frz -->|II_NGF6_SOM4_5A| SOM4
    NGF6frz -->|II_NGF6_SOM4_5B| SOM4
    NGF6frz -->|II_NGF6_SOM4_6| SOM4
    PV2frz -->|II_PV2_SOM4_1| SOM4
    PV2frz -->|II_PV2_SOM4_2| SOM4
    PV2frz -->|II_PV2_SOM4_3| SOM4
    PV2frz -->|II_PV2_SOM4_4| SOM4
    PV2frz -->|II_PV2_SOM4_5A| SOM4
    PV2frz -->|II_PV2_SOM4_5B| SOM4
    PV2frz -->|II_PV2_SOM4_6| SOM4
    PV3frz -->|II_PV3_SOM4_1| SOM4
    PV3frz -->|II_PV3_SOM4_2| SOM4
    PV3frz -->|II_PV3_SOM4_3| SOM4
    PV3frz -->|II_PV3_SOM4_4| SOM4
    PV3frz -->|II_PV3_SOM4_5A| SOM4
    PV3frz -->|II_PV3_SOM4_5B| SOM4
    PV3frz -->|II_PV3_SOM4_6| SOM4
    PV4frz -->|II_PV4_SOM4_1| SOM4
    PV4frz -->|II_PV4_SOM4_2| SOM4
    PV4frz -->|II_PV4_SOM4_3| SOM4
    PV4frz -->|II_PV4_SOM4_4| SOM4
    PV4frz -->|II_PV4_SOM4_5A| SOM4
    PV4frz -->|II_PV4_SOM4_5B| SOM4
    PV4frz -->|II_PV4_SOM4_6| SOM4
    PV5Afrz -->|II_PV5A_SOM4_1| SOM4
    PV5Afrz -->|II_PV5A_SOM4_2| SOM4
    PV5Afrz -->|II_PV5A_SOM4_3| SOM4
    PV5Afrz -->|II_PV5A_SOM4_4| SOM4
    PV5Afrz -->|II_PV5A_SOM4_5A| SOM4
    PV5Afrz -->|II_PV5A_SOM4_5B| SOM4
    PV5Afrz -->|II_PV5A_SOM4_6| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_1| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_2| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_3| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_4| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_5A| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_5B| SOM4
    PV5Bfrz -->|II_PV5B_SOM4_6| SOM4
    PV6frz -->|II_PV6_SOM4_1| SOM4
    PV6frz -->|II_PV6_SOM4_2| SOM4
    PV6frz -->|II_PV6_SOM4_3| SOM4
    PV6frz -->|II_PV6_SOM4_4| SOM4
    PV6frz -->|II_PV6_SOM4_5A| SOM4
    PV6frz -->|II_PV6_SOM4_5B| SOM4
    PV6frz -->|II_PV6_SOM4_6| SOM4
    SOM2frz -->|II_SOM2_SOM4_1| SOM4
    SOM2frz -->|II_SOM2_SOM4_2| SOM4
    SOM2frz -->|II_SOM2_SOM4_3| SOM4
    SOM2frz -->|II_SOM2_SOM4_4| SOM4
    SOM2frz -->|II_SOM2_SOM4_5A| SOM4
    SOM2frz -->|II_SOM2_SOM4_5B| SOM4
    SOM2frz -->|II_SOM2_SOM4_6| SOM4
    SOM3frz -->|II_SOM3_SOM4_1| SOM4
    SOM3frz -->|II_SOM3_SOM4_2| SOM4
    SOM3frz -->|II_SOM3_SOM4_3| SOM4
    SOM3frz -->|II_SOM3_SOM4_4| SOM4
    SOM3frz -->|II_SOM3_SOM4_5A| SOM4
    SOM3frz -->|II_SOM3_SOM4_5B| SOM4
    SOM3frz -->|II_SOM3_SOM4_6| SOM4
    SOM4frz -->|II_SOM4_SOM4_1| SOM4
    SOM4frz -->|II_SOM4_SOM4_2| SOM4
    SOM4frz -->|II_SOM4_SOM4_3| SOM4
    SOM4frz -->|II_SOM4_SOM4_4| SOM4
    SOM4frz -->|II_SOM4_SOM4_5A| SOM4
    SOM4frz -->|II_SOM4_SOM4_5B| SOM4
    SOM4frz -->|II_SOM4_SOM4_6| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_1| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_2| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_3| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_4| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_5A| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_5B| SOM4
    SOM5Afrz -->|II_SOM5A_SOM4_6| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_1| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_2| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_3| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_4| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_5A| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_5B| SOM4
    SOM5Bfrz -->|II_SOM5B_SOM4_6| SOM4
    SOM6frz -->|II_SOM6_SOM4_1| SOM4
    SOM6frz -->|II_SOM6_SOM4_2| SOM4
    SOM6frz -->|II_SOM6_SOM4_3| SOM4
    SOM6frz -->|II_SOM6_SOM4_4| SOM4
    SOM6frz -->|II_SOM6_SOM4_5A| SOM4
    SOM6frz -->|II_SOM6_SOM4_5B| SOM4
    SOM6frz -->|II_SOM6_SOM4_6| SOM4
    VIP2frz -->|II_VIP2_SOM4_1| SOM4
    VIP2frz -->|II_VIP2_SOM4_2| SOM4
    VIP2frz -->|II_VIP2_SOM4_3| SOM4
    VIP2frz -->|II_VIP2_SOM4_4| SOM4
    VIP2frz -->|II_VIP2_SOM4_5A| SOM4
    VIP2frz -->|II_VIP2_SOM4_5B| SOM4
    VIP2frz -->|II_VIP2_SOM4_6| SOM4
    VIP3frz -->|II_VIP3_SOM4_1| SOM4
    VIP3frz -->|II_VIP3_SOM4_2| SOM4
    VIP3frz -->|II_VIP3_SOM4_3| SOM4
    VIP3frz -->|II_VIP3_SOM4_4| SOM4
    VIP3frz -->|II_VIP3_SOM4_5A| SOM4
    VIP3frz -->|II_VIP3_SOM4_5B| SOM4
    VIP3frz -->|II_VIP3_SOM4_6| SOM4
    VIP4frz -->|II_VIP4_SOM4_1| SOM4
    VIP4frz -->|II_VIP4_SOM4_2| SOM4
    VIP4frz -->|II_VIP4_SOM4_3| SOM4
    VIP4frz -->|II_VIP4_SOM4_4| SOM4
    VIP4frz -->|II_VIP4_SOM4_5A| SOM4
    VIP4frz -->|II_VIP4_SOM4_5B| SOM4
    VIP4frz -->|II_VIP4_SOM4_6| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_1| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_2| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_3| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_4| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_5A| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_5B| SOM4
    VIP5Afrz -->|II_VIP5A_SOM4_6| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_1| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_2| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_3| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_4| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_5A| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_5B| SOM4
    VIP5Bfrz -->|II_VIP5B_SOM4_6| SOM4
    VIP6frz -->|II_VIP6_SOM4_1| SOM4
    VIP6frz -->|II_VIP6_SOM4_2| SOM4
    VIP6frz -->|II_VIP6_SOM4_3| SOM4
    VIP6frz -->|II_VIP6_SOM4_4| SOM4
    VIP6frz -->|II_VIP6_SOM4_5A| SOM4
    VIP6frz -->|II_VIP6_SOM4_5B| SOM4
    VIP6frz -->|II_VIP6_SOM4_6| SOM4
    HTCfrz -->|ITh_HTC_IRE| IRE
    IREMfrz -->|ITh_IREM_IRE| IRE
    IREfrz -->|ITh_IRE_IRE| IRE
    TCMfrz -->|ITh_TCM_IRE| IRE
    TCfrz -->|ITh_TC_IRE| IRE
    HTCfrz -->|ThCx_HTC_SOM4| SOM4
    TCfrz -->|ThCx_TC_SOM4| SOM4
```