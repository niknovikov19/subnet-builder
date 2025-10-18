
<div style="position: relative; padding-top: 30px;">  
  <!-- your info text, absolutely positioned inside the container -->
  <div style="
      position: absolute;
      top: 0;
      right: 0;
      font-size: 0.8em;
      color: #666;
    ">
    Active: P1, P3, P4, P5
  </div>
</div>

```mermaid
graph LR
    P1["P1<br/>C0<br/>HH"]
    P3["P3<br/>C0<br/>HH"]
    P4["P4<br/>C1<br/>HH"]
    P5["P5<br/>C1<br/>HH"]
    P5frz["P5frz<br/>NetStim"]
    P6frz["P6frz<br/>NetStim"]
    P2frz["P2frz<br/>NetStim"]
    P0frz["P0frz<br/>NetStim"]
    P7frz["P7frz<br/>NetStim"]
    P1frz["P1frz<br/>NetStim"]
    P1 -->|C0->P4 -0.4| P4
    P3 -->|C0->P4 -0.4| P4
    P0frz -->|frz_C0->P4 -0.4| P4
    P2frz -->|frz_C0->P4 -0.4| P4
    P0frz -->|frz_P0->C1 -0.1| P4
    P0frz -->|frz_P0->C1 -0.1| P5
    P1 -->|P1->P5 0.3| P5
    P1frz -->|frz_P1->P5 1.2| P5
    P5 -->|P5->P1 0.51| P1
    P5frz -->|frz_P5->P1 4.59| P1
    P6frz -->|frz_P6->P23 6.23| P3
    P6frz -->|frz_P67->P3 67.3| P3
    P7frz -->|frz_P67->P3 67.3| P3
```