链表是Redis的最基本数据结构，由adlist.h和adlist.c定义，使用双向链表。  
## Adlist.h
定义listNode为链表中的结点。  
```
typedef struct listNode {
    struct listNode *prev; //前驱结点
    struct listNode *next; //后继结点
    void *value; //结点值
} listNode;
```

定义listIter为链表的
```
typedef struct listIter {
    listNode *next;
    int direction;
} listIter;
```
