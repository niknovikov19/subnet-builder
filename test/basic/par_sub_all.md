
<div style="position: relative; padding-top: 30px;">  
  <!-- your info text, absolutely positioned inside the container -->
  <div style="
      position: absolute;
      top: 0;
      right: 0;
      font-size: 0.8em;
      color: #666;
    ">
    Active: a, l, l<BR>Frozen: a, l, l
  </div>
</div>

```mermaid
graph LR
    P0["P0<br/>C0<br/>HH"]
    P1["P1<br/>C0<br/>HH"]
    P2["P2<br/>C0<br/>HH"]
    P3["P3<br/>C0<br/>HH"]
    P4["P4<br/>C1<br/>HH"]
    P5["P5<br/>C1<br/>HH"]
    P6["P6<br/>C1<br/>HH"]
    P7["P7<br/>C1<br/>HH"]
    P6frz["P6frz<br/>NetStim"]
    P1frz["P1frz<br/>NetStim"]
    P0frz["P0frz<br/>NetStim"]
    P5frz["P5frz<br/>NetStim"]
    P7frz["P7frz<br/>NetStim"]
    P2frz["P2frz<br/>NetStim"]
    P3frz["P3frz<br/>NetStim"]
    P0frz -->|C0->P4| P4
    P1frz -->|C0->P4| P4
    P2frz -->|C0->P4| P4
    P3frz -->|C0->P4| P4
    P0frz -->|P0->C1| P4
    P0frz -->|P0->C1| P5
    P0frz -->|P0->C1| P6
    P0frz -->|P0->C1| P7
    P1frz -->|P1->P5| P5
    P5frz -->|P5->P1| P1
    P2frz -->|P23->P67| P6
    P2frz -->|P23->P67| P7
    P3frz -->|P23->P67| P6
    P3frz -->|P23->P67| P7
    P6frz -->|P6->P23| P2
    P6frz -->|P6->P23| P3
    P6frz -->|P67->P3| P3
    P7frz -->|P67->P3| P3
```