```js
res.forEach((item) => {
  // if (item.authorizedPartQuery !== null) {
    let codeMap = new Map();
    let arr = item.authorizedPartQuery;
    // 1 [2] 3 4 5
    for (let i = arr.length - 1; i >= 0; i--) {
      if (Array.isArray(arr[i].code)) {
        arr.splice(i,1)
        continue;
      }
      for (let j = 0; j < i; j++) {
        if (Array.isArray(arr[j].code)) continue;
        if(this.isSameRow(arr[i], arr[j])){
          let codeList = codeMap.get(arr[i].code) !== undefined ? codeMap.get(arr[i].code) : [arr[i].code];
          codeList.push(arr[j].code)
          codeMap.set(arr[i].code, codeList)
          arr[i].code = codeList;
          arr[j].code = [];
        }
      }
    }
    // 将codeMap中记录的list保存到对应的行
    let apq = item.authorizedPartQuery;
    for (let i = apq.length - 1; i >= 0; i--) {
      let _tmpList = codeMap.get(apq[i].code) === undefined ? [apq[i].code] : codeMap.get(apq[i].code)
      apq[i].code = _tmpList.sort((a,b) => a - b);
    }
    item.authorizedPartQuery = apq;
  // }
});

console.log('aaaaa',res)
```



```cmd
 node D:\ATS\fastlabel-view\src\views\core\auth\test.js
```

