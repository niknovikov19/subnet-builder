```mermaid
graph LR
    P1["P1<br/>HH"]
    P2["P2<br/>HH"]
    P3["P3<br/>HH"]
    P1 -->|P1->P1: 1| P1
    P1 -->|P1->P2: 2| P2
    P2 -->|P2->P3: 3| P3
    P3 -->|P3->P3: 4| P3
```