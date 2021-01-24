# C++ 팁

### 시간 초과(cin, cout)

세팅방법

```
ios_base::sync_with_stdio(false); //stdio와 iostream 입출력함수들과의 동기화를 푼다
cin.tie(NULL);
cout.tie(NULL); 
```

구조체 포인터 delete

```
vector<Struct*>::iterator iter;
    for (iter=struct.begin(); iter != struct.end(); ++iter ){
        delete *iter;
    }
    struct.clear();
```
