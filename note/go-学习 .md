# 疑问点

- 切片究竟是用了同一个底层数组还是？具体是做了什么？
    - 观察物理地址
    - 转成汇编看
- map是如何实现的？

```go
package main

D:\demo>go run demo.go
error: <nil>
程序继续执行...

language := make(map[string]map[string]string)
language["php"] = make(map[string]string, 1)
language["php"]["id"] = "1"
language["php"]["desc"] = "php是世界上最美的语言"
language["golang"] = make(map[string]string, 1)
language["golang"]["id"] = "2"
language["golang"]["desc"] = "golang抗并发非常good"
fmt.Println(language)


type定义补充

07 存储一个 uint8 的变量需要多大内存？


```



# Go Grammar

## Basic data type

- Go 是静态类型语言，一旦某个变量被声明，那么它的类型就无法再改变了。
- 类型别名就是同一个类型的另一个名字。所以，rune 和 int32 可以互换使用。
    - 拓展：type celsius float64
    - 方法可以与类型/构造体关联
- 某些语言里，经常把 1 和 0 当作 true 和 false，但是在 Go 里面不行。
- 默认值
    - 整数int（根据架构不同而变为int32或int64）、float64
    - 注意：引用类型的默认值为nil，需要分配内存空间（引用已有值类型，或通过内建函数new()/make()来分配）

- 13115018336

```go
//预定义常量：true，false和iota

// iota可以被认为是一个编译器修改的常量，在没有个const关键字出现时被重置为0，然后在下一个const出现之前，
//没出现一次iota，其所在的数字会自动增1
const (
    c0 = iota//c0=0
    c1 = iota//c1=1
    c2 = iota//c2=2
)

const (
    x = 1 << iota // x==1(iota在每个const开头被重设为0)
    y = 1 << iota// y==2
    z = 1 << iota// z==4

)

for idx, value := range sli {
    fmt.Println(idx, value) //10
}

fmt.Println(math.Abs(piggyBank-0.3)<0.0001)
```





## Function

### example

- Go是一种100%传递值的语言。因此，func的输入是该函数的本地输入：在该func之外，更改是不可见的。
- golang 支持多返回值，这是一个很大的不同点

**推荐写法**

```go
func swap(x, y string) (string) {
	return x+y
}
func swap(x, y string) (string, string) {
	return y, x
}


// 定义传值用* 用起来就&
// Group creates a new router group. You should add all the routes that have common middlewares or the same path prefix.
// For example, all the routes that use a common middleware for authorization could be grouped.
func (group *RouterGroup) Group(relativePath string, handlers ...HandlerFunc) *RouterGroup {
	return &RouterGroup{
		Handlers: group.combineHandlers(handlers),
		basePath: group.calculateAbsolutePath(relativePath),
		engine:   group.engine,
	}
}
```



延迟执行的函数会被压入栈中 return后按照先进后出的顺序调用
延迟执行的函数其参数会立即求值



```go
type binOp func(int,int) int
var op binOp
add := func(i,j int) int{return i+j}
op=add
n=op(100,200)
```

### 执行过程分析

词法分析 => 语法分析 => 类型检查 => 中间代码 => 代码优化 => 生成机器码

Go 语言编译器的中间代码具有静态单赋值（Static Single Assignment、SSA）



[Go 语言设计与实现](https://draveness.me/golang/docs/part1-prerequisite/ch01-prepare/golang-debug/)

https://blog.51cto.com/u_13784902/2470250





## Pointer

> `*` in front of a pointer value gets the value that is pointed by the pointer.
>
> `&` in front of a value gets the memory address of that value
>
> `*` in front of a type denotes a pointer type.

- G0语言的函数和方法都是按值传递参数的，这意味着函数总是操作于被传递参数的副本。
  - 这句话说明了：地址可以有副本，但是对象的副本传递过去很多时候达不成想要的效果，无法正确操作指定内存中的对象（为了共享数据才给方法传递指针）
  - 当指针被传递到函数时，函数将接收传入的内存地址的副本。之后函数可以通过解引用内存地址来修改指针指向的值。
- `&取地址` 与 `*解引用`
  - 取址符：&取物理地址 
  - 取值符：*与汇编一样，都是取地址符号，取出来地址就是对应的另一个变量。（解引用）
  - 数据类型：*指向的类型 
- 方法传递时，获取指定字段的内存地址：`study（&stuXiaMing.Head）`



**简单例子理解指针**

```go
func main() {
	num := 100              // 定义一个变量
	numAddress := &num      // 取物理地址
	numValue := *numAddress // 从物理地址中取值
    
	fmt.Printf("counter : %-16d memory address: %-16p\n", num, &num)
	fmt.Printf("P       : %-16p memory address: %-16p *P: %-16d\n", numAddress, &numAddress, *numAddress)
	fmt.Printf("V       : %-16d memory address: %-16p\n", numValue, &numValue)
}
```

验证：

```
counter : 100              address: 0xc00001c0b8    
P       : 0xc00001c0b8     address: 0xc00000a028     *P: 100
V       : 200              address: 0xc00001c0b9    
```



Question：到底是 `函数本身` 还是 `函数执行的结果` 赋给变量

```go
func main() {
   // var abc func(a int, b int) (int, int) = function3
   // abc是一个type为func(a int, b int) (int, int) 的类型变量，直接指向这一行代码段（只读）
   
   abc := function3
   fmt.Println(abc(1, 2)) //输出lbd good
   abc = function33       //函数也可以作为变量，经常有的，就当作一个地址呗，汇编经常就这么写的
   fmt.Println(abc(1, 2)) //输出lbd good
}
```

直接赋值方法名 等价于 得到方法的地址


## Container

### array

对数组的理解：数组是一种固定长度且有序的元素集合。

- 底层一样：在编译的时候就需要为数组准备好固定的空间，代码运行过程中可以更改物理地址上存储的值，但是不能更改分配好的空间大小。（数组的地址写死，不允许更改）

- 数组也是一种值，函数通过值传递来接受参数。所以数组作为函数的参数就非常低效。（推荐使用slice作为参数在方法传递）

```go
arr := [...]int{1,2,3,4}
arr2 := arr          // 深拷贝，在内存中重新开辟一段空间

arr := [3]int{}
fmt.Println(arr)      //[0 0 0]
fmt.Println(cap(arr)) //3
fmt.Println(len(arr)) //3

sli := make([]int, 0, 10)
fmt.Println(sli)      //[]
fmt.Println(len(sli)) //0
fmt.Println(cap(sli)) //10

sli = append(append(sli, 1), 2)
```



### slice

- 当 slice 的容量不足以执行 append 操作时，Go 必须创建新数组并复制旧数组中的内容。
- 共享数组需要了解一下方法`ShareSlice()`

```go
func main() {
	arr1 := [...]string{
		"Mercury", "Venus", "Earth", "Mars",
		"Jupiter", "Saturn", "Uranus", "Neptune",
	}

	fmt.Println("--------限制新建切片容量：增长到6就深拷贝一个arr，与原数组无关------------")
    // 左闭右开原则
	arr2 := arr1[0:4:5]
	arr3 := append(arr2, "Ceres")
	arr4 := append(append(arr2, "Ceres"), "cares2")
	arr5 := append(arr4, "Ceres")
	fmt.Println("arr1", &arr1[0], arr1)
	fmt.Println("arr2", &arr2[0], arr2)
	fmt.Println("arr3", &arr3[0], arr3)
	fmt.Println("arr4", &arr4[0], arr4)
	fmt.Println("arr5", &arr5[0], arr5)

	fmt.Println("--------新建切片容量大于原有的才会深拷贝新arr----------")
	arr2 = arr1[0:7]
	arr3 = append(append(arr2, "Ceres"), "aaa")
	fmt.Println("arr1", &arr1[0], arr1)
	fmt.Println("arr2", &arr2[0], arr2)
	fmt.Println("arr3", &arr3[0], arr3)
}

```



#### 窗口变小的例子

```go
func reclassify(planets *[]string) {
   *planets = (*planets)[0:3]
}

func main() {
   slice := []string{
      "Mercury", "Venus", "Earth", "Mars",
   }
   fmt.Printf("memory address: %-16p slice :%s\n", &slice, slice)
   reclassify(&slice)
   fmt.Printf("memory address: %-16p slice :%s\n", &slice, slice)
}
```



### map

- 是一种隐式指针
  - map 在被赋值或者呗作为参数传递的时候不会被复制，新变量或函数参数将指向相同的map在内存中。
  - map 的键和值都可以是指针类型，但尽量用基本类型和string做key，不要和自己过不去

```go
// go语言没有set实现，可以自己实现
set := make(map[float64]bool)
for _, t := range temperatures {
    set[t] = true
}
```



#### map和slice

在方法传递过程的区别

```go
func main() {
    stats := map[int]int{1: 10, 10: 2}
    incrAll(stats)
    fmt.Print(stats)
}

func incrAll(stats map[int]int) {
    for k := range stats {
        stats[k]++
    }
}
```



```go
func main() {
    stats := []int{10, 5}
    add(stats, 2)
    fmt.Print(stats)
}

func add(stats []int, n int) {
    stats = append(stats, n)
}
```



### struct

- json 包的 Marshal 函数可以将 struct 中的数据转化为 JSON 格式。
    - Marshal 函数只会对 struct 中被导出的字段进行编码。（私有变量不可导出）
- 组合优于继承
    - Favor object composition over class inheritance.
    - Use of classical inheritance is always optional;every problem that it solves can be solved another way.
- 使用指针作为接收者的策略应该始终如一：
    - 如果一种类型的某些方法需要用到指针作为接收者，就应该为这种类型的所有方法都是用指针作为接收者

```go
func main() {
	type location struct {
		Name  float64 `json:"name"`
		Age   float64 `json:"age"`
	}
    
    bytes, err := json.Marshal(curiosity)

}
```

**struct嵌入实现方法的转发**

```go
type Student struct {
	name
	age
	hand
	head
}
type name string
type age int
type hand struct {
	long int
}
type head struct{}

func (hand) hit(obj string) {
	fmt.Println("我打了" + obj)
}
func (head) think(obj string) {
	fmt.Println("我在思考关于" + obj)
}

func main() {
	stuXiaMing := Student{
		name: "小明", age: 12, hand: hand{}, head: head{},
	}
	stuXiaMing.hit("棒槌")
	stuXiaMing.think("帮帮")
}
```



## interface

- 隐式实现接口
  - 简化代码：隐式接口允许您在不定义显式接口的情况下实现多态。
  - 提高代码可读性：隐式接口允许您在实现多态时使用更直接、更简单的语法。
  - 提高代码灵活性：隐式接口允许您在不改变已有代码的情况下实现多态。
  - 降低可读性：没有显式定义的接口类型
- 接口一般命名都是有er作为后缀，类似：xxer

```go
- 方法的接受者是类型的时候，传递指针或者类型变量都能取到需要用的值，方法正常。
- 反过来，接受者是指针的时候，传递一个类型变量（副本），那么显然违背了方法本意。

type age int

func (age *age) inc() string{
    fmt.Println("涨到", *age)
}

func main() {
    num := 
}
```



**提示汇总**：

```go
type 定义熟记。其中 type A=B 这种别名，一般只用于兼容性处理，所以不需要过多关注；
• 先有抽象再有实现，所以要先定义接口
• 鸭子类型：一个结构体有某个接口的所有方法，它就实现了这个接口；
```



## nil

**最佳实践**

```go
func sortStrings(s []string, less func(i, j int) bool) {
   if less == nil {
      less = func(i, j int) bool { return s[i] < s[j] }
   }
   sort.Slice(s, less)
}

func main() {
   food := []string{"onion", "carrot", "celery"}
   sortStrings(food, nil)
   fmt.Println(food)
}
```



## Debugger

> 这里有一个坑，最新的dlv不能和最新的go版本匹配，delve是goland的默认编译器，目前还不支持最新版的GO（2023年2月9日 GO：V1.20.0），一旦需要调试，就会出现在断点前卡死的现象。

### 获取方式

1、和平时拉取go第三方库的方式一样

1. 执行`go get -u github.com/go-delve/delve/cmd/dlv`
2. 打开 `Help->Edit Customer Properties`，若提示文件不存在，点击创建。
3. `dlv.path=D:/Go_WorkSpace/bin/dlv.exe` 重启Goland就可以了

2、自定义delve编译器方法：

```go
1、下载delve包
git clone https://github.com/go-delve/delve.git
cd delve/cmd/dlv/
go build
go install

3、进入goland， Help->Edit Custom VM options，加入
      -Ddlv.path=D:\git\go\delve\bin\dlv

4、重启goland，就可以断点“下一步”了
```



### 参考教程

https://www.modb.pro/db/46508

https://chai2010.cn/advanced-go-programming-book/ch3-asm/ch3-09-debug.html



# Go dev

## notice











# Go Web

https://mm.edrawsoft.cn/app/editor/zYSbA42wSiV6gZ0Yv9svEwnP1mktEpkT?page=4294967396&

## 关注重点

处理请求、内置 Handler、请求、Form、响应、模板、路由、JSON、中间件、请求上下文、HTTPS、HTTP/2、测试、性能分析、部署



```go
http.Handle
func Handle(pattern string, handler Handler) { DefaultServeMux.Handle(pattern, handler) }

http.HandleFunc
func HandleFunc(pattern string, handler func(ResponseWriter, *Request))

type HandlerFunc func(ResponseWriter, *Request)
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
```

怎么组合最后都是给到server里面使用的

```go
mh := myHandler{} // 实现了ServeHTTP方法的构造体

server := http.Server{
    Addr:    "localhost:8080",
    Handler: &mh,
}
server.ListenAndServe()
//http.ListenAndServe("localhost:8080", nil)
```



## 常用命令

![image-20230214095250030](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302140952404.png?tximg)

```go
go help [xx]

go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
go mod tidy
go mod download

export GIN_MODE = release
```

启动失败：

`file`的`invalidate caches`

 



# aq-work

## 项目结构

| 文件夹       | 说明                  | 描述                                                         |
| ------------ | --------------------- | ------------------------------------------------------------ |
| `api`        | api层                 | api层                                                        |
| `--v1`       | v1版本接口            | v1版本接口                                                   |
| `config`     | 配置包                | config.yaml对应的配置结构体                                  |
| `core`       | 核心文件              | 核心组件(zap, viper, server)的初始化                         |
| `docs`       | swagger文档目录       | swagger文档目录                                              |
| `global`     | 全局对象              | 全局对象                                                     |
| `initialize` | 初始化                | router,redis,gorm,validator, timer的初始化                   |
| `--internal` | 初始化内部函数        | gorm 的 longger 自定义,在此文件夹的函数只能由 `initialize` 层进行调用 |
| `middleware` | 中间件层              | 用于存放 `gin` 中间件代码                                    |
| `model`      | 模型层                | 模型对应数据表                                               |
| `--request`  | 入参结构体            | 接收前端发送到后端的数据。                                   |
| `--response` | 出参结构体            | 返回给前端的数据结构体                                       |
| `packfile`   | 静态文件打包          | 静态文件打包                                                 |
| `resource`   | 静态资源文件夹        | 负责存放静态文件                                             |
| `--excel`    | excel导入导出默认路径 | excel导入导出默认路径                                        |
| `--page`     | 表单生成器            | 表单生成器 打包后的dist                                      |
| `--template` | 模板                  | 模板文件夹,存放的是代码生成器的模板                          |
| `router`     | 路由层                | 路由层                                                       |
| `service`    | service层             | 存放业务逻辑问题                                             |
| `source`     | source层              | 存放初始化数据的函数                                         |
| `utils`      | 工具包                | 工具函数封装                                                 |
| `--timer`    | timer                 | 定时器接口封装                                               |
| `--upload`   | oss       | oss接口封装                                 |



- `api` api层
    - `v1` v1版本接口
        - `/work`
        - `/system`
        - `enter.go`
- `model ` 接口完成CRUD所必须的实体模型，配置入参……
    - `/work` 业务分层
        - `/request` 入参结构体
        - `/response` 出参结构体
- `router` 路由层
    - 
- `config`
- `core` 核心组件(zap, viper, server)的初始化
    - 




## 比较重要的构造体

```go

type ApiGroup struct {
    SystemApiGroup  system.ApiGroup
    ExampleApiGroup example.ApiGroup
    WorkApiGroup    work.ApiGroup
}

type RouterGroup struct {
   System  system.RouterGroup
   Example example.RouterGroup
   Work    work.RouterGroup
}
```





