### 1. spring简介

#### 3分钟Quick Start

pom.xml

```xml
<build>
    <!--在打成jar包运行时必须放入插件配置   注意：没有插件配置无法运行打包的项目-->
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```



```java
//这个注解： 修饰范围： 用在类上 只能用在入口类上 只能出现一次
@SpringBootApplication
public class SpringBootDemoApplication {
    public static void main(String[] args){
        //启动springbootl应用参数1：指定入口类的类对象，class参数 2:main函数参数：虚拟机参数，-Dserver.port=8078
        SpringApplication.run(SpringBootDemoApplication.class,args);
    }
}

【1】手工方法：
    1.pom文件引入依赖
    2.resources生成application.yml
    3.创建入口类加入@SpringBootApplication注解
    
【2】自动方法：快速初始化
    1.Spring Initializr
    2.Name: Spring-demo
```



**那么我们来测试一下spring 应用**

![image-20221214002225342](F:\bak\MDimg\image-20221214002225342.png)

```text
springboot = springmvc(控制器controller) + spring（工厂）

@RequestController
@RequestMapping("hello")
http://localhost:8080/hello

注意：springboot项目默认启动没有项目名
```



修改spring配置：

```yml
server:
  port: 8081 # 修改内嵌服务的端口号
  servlet:
  	context-path: /springTestProjectName # 项目名以斜杠开头
```



```yml
最核心的依赖：
```





#### 注解

>  该注解是一个只能作用在类上组合注解
>
> （由@SpringBootConfiguration和@EnableAutoConfiguration和@ComponentScan） 

其中@Target(指定注解作用范围)、@Retention(指定注解什么时候有效)、@Doucumented、@Inherited四个注解为java自带的**元注解**：只能修饰注解的注解。

-  @SpringBootConfiguration：这个注解就是用来自动配置spring、springmvc（底层是去初始化servlet，配置事务生效）相关环境 
-  @EnableAutoConfiguration：开启**自动配置**，自动配置spring相关环境 + 引入第三方技术自动配置环境（mybatis-springboot、redis-springboot等第三方技术）
   -  自动配置未来更多的三方技术：Mybatis、Redis、ES、Rabbit MQ
-  ComponentScan：组件扫描 根据注解发挥注解作用，**默认扫描当前包以及其子包** 



### 2. 环境切换

平时我们的生产环境配置和开发环境配置一般不同，如何在springboot的配置文件中更换不同环境的配置文件

####  方法一 内部切换


1、通过application-XXX.yml命名作为其他环境配置

2、在application.yml中更换配置环境

**测试**

```yml
1. 通过application.yml进行公共配置
server:
  port:8081


2. 创建开发环境application-dev.yml
server:
  servlet:
  	context-path: devpath

3. 创建生产环境application-prod.yml
server:
  servlet:
  	context-path: prodpath

4. 在application.yml设置开启的环境配置
server:
  port:8081
spring:
  profiles:
  	active: dev

----------或者----------
server:
  port:8081
spring:
  profiles:
  	active: prod
  	
  	
  	
  	
4、访问hello请求
localhost:8081/devpath/hello
```



#### 方法二 调用外部的配置文件 

修改启动程序的参数

![image-20221214085454433](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/image-20221214085454433.png?tximg)

```yml
–spring.config.location=外部配置文件的绝对地址
```



### 3. spring管理对象

在springboot中管理单个对象，直接使用spring框架中注解形式创建

**2种方式创建对象**

（1）基于**配置文件**的形式创建对象，spring.xml内使用`<bean>`

（2）基于**注解方式**创建对象，

**@Component** 通过注解创建对象 【通用】

- @Controller 控制器注解，用来创建控制器对象
- @Service 服务注解，用来创建业务层对象
- @Repository 仓库注解DAO层，用来创建Dao层对象--->mybatis可以代理

> 以上注解都有value属性，value属性用来指定工厂中对象的名称



```java
@Autowired   					  //作用：根据类来找
@Qualifier(value="userService")   //作用：用来根据名称注入
UserService userService;
```



（3）**Spring配置**文件的方法创建对象，多个对象

```java
@Configuration //修饰范围：只能用在类上作用：代表这个类是一个配置类====spring.xml
public class BeanMarker {
	
	@Bean
	public User user() {
		return new User();
	}
	
	@Bean
	public Prod prod(){
		return new Prod();
	}
	^…………^
}
```

@Configuration：

- 作用：代表这个类 是一个springboot中配置类

@Bean 注解：

- 创建对象   相当于`spring.xml`书写bean标签，无限制创建<u>多个</u>对象
- 修饰范围：用在方法上或者注解上，作用：用来将方法返回值交给工厂管理
- 方法名：推荐返回值首字母小写代表当前创建对象在工厂中名称



@Value注解

```java

@Value("${name}")
private String name;

属性与配置解耦合
```



### 4. 引入Mybatis

#### 升级为springBoot后

```java
1.引入依赖
    mysql相关 链接Java驱动 druid数据源
    spring相关 springboot-web
    mybatis相关 (mybatis-spring-boot-stater)依赖(mybatis mybatis-spring)
 
2.书写配置
	a.开启注解扫描@SpringBootApplication  @ComponentScan  [省略]
        @MapperScan(basePackages = {"com.company.**.mapper"})
        @SpringBootApplication(scanBasePackages = {"com.company.*"})
		
	b.创建数据源
		1.指定数据源类型
        2.指定数据库驱动
        3.指定ur1
        4.指定username
        5.指定password

	c.创建SqlSessionFactory
        1.指定mapperi配置文件位置
        2.指定实体所在包位置起别名
        
	d.创建DAO：指定DAO接收所在包

	e.创建事务管理器开启注解式事务生效 [省略]


3.测试
    1).建表
    2).开发实体类
    3).开发DAO接口
    4).开发Mapper配置文件
    5).开发Service接口
    6).开发ServiceImpl实现类
    7).测试ServiceImpl
```



##### 1、引入依赖

> (这里还缺少一个引入druid包)

说明：由于springboot整合mybatis版本中默认依赖mybatis因此不需要额外引入mybati版本，否则会出现冲突

```xml
<!-- 统一配置所有的版本号-->
<properties>
    <mybatis-plus.version>3.5.1</mybatis-plus.version>
    <mysql.version>8.0.29</mysql.version>
</properties>


<!-- 定义全局jar版本,模块使用需要再次引入但不用写版本号-->
<dependencyManagement>
    <dependencies>
        <!--Java数据库驱动-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>${mysql.version}</version>
        </dependency>
 
        <!--orm 相关-->
        <dependency>
            <!--依赖包含了 （mybatis mybatis-spring）-->
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-extension</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-annotation</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

提示：mapper注意要以斜開始

![image-20221217153814013](F:\bak\MDimg\image-20221217153814013.png)





### 6. dao注解

- @Mapper：添加在Dao接口上，在工厂中创建代理对象(DAO对象)，但是一次只能作用一个Dao接口，相对麻烦
- @MapperScan：自动扫描对应的包里面的东西
- 总结：
  - Mapper对单个生效，作用：用来在工厂中创建dao对象
  - MapperScan对整个包生效，作用：用来扫描d00接口所在包同时将所有d00接口在工厂中创建对象







### 7. 本地测试：

#### 1、老板的本地测试：spring中

```java
//1、启动工厂
ApplicationCpntext context = new ClassPathXmlApplicationContext("spring.xml");

//2、从工厂中获得指定对象
UserDao userDao = context.getBean("UserDao");

//3、调用方法
useDao.getXXParam()
```



#### 2、升级到springBoot：junit

**测试原则**：先测试dao接口，然后是业务接口。

```xml
<!--spring-boot-stater-test junit单元-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <!--确定范围-->
    <scope>test</scope>
</dependency>
```





```java
1、@SpringBootTest注解 在类加上，启动应用，自然工厂就有了
    作用：在这个类实例化过程中启动springboot应用
2、@Autowired注解 引入由spring代理的类
3、@Test 在方法加上


继承父类也可以不加注解，只需要父类是有@SpringBootTest注解即可
```



### 8. 热部署

![image-20221213235309973](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/image-20221213235309973.png?tximg)

```xml
<!--热部署依赖deVtooLs-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <!--optional:该依赖是否可以传递 true 不会向下传递，当前项目可用-->
    <optional>true</optional>
</dependency>
```



```xml
#2,开启允许在运行过程中修改文件
ctrl+alt+shift+/
---->选择1,Registry-->勾选
compi1er,automake,al1ow,when,app.running这个选项
```

出现：即可以开始热部署了

![image-20221213235545126](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/image-20221213235545126.png?tximg)



#### 8.1. 日志的级别

![image-20221217161216149](F:\bak\MDimg\image-20221217161216149.png)

- ALL：最低等级的，用于打开所有日志记录。 -  TRACE：很低的日志级别，一般不会使用。 

-  **DEBUG**： 指出细粒度信息事件对调试应用程序是非常有帮助的，主要用于开发过程中打印一些运行信息。 
-  **INFO**： 消息在粗粒度级别上突出强调应用程序的运行过程。打印一些你感兴趣的或者重要的信息，这个可以用于生产环境中输出程序运行的一些重要信息，但是不能滥用，避免打印过多的日志。
-  **WARN**： 表明会出现潜在错误的情形，有些信息不是错误信息，但是也要给程序员的一些提示。 
-  **ERROR**： 指出虽然发生错误事件，但仍然不影响系统的继续运行。打印错误和异常信息，如果不想输出太多的日志，可以使用这个级别。 
-  FATAL： 指出每个严重的错误事件将会导致应用程序的退出。这个级别比较高了。重大错误，这种级别你可以直接停止程序了。
-  OFF： 最高等级的，用于关闭所有日志记录。 

### 9. AOP

```java
AOP：Aspect(切面) Oriented(面向) programming面向切面别称
    
    Aspect(切面) = Advice(通知/附加操作) + 切入点(prointcut)
        Advice 通知：业务逻辑中一些附加操作成为通知，分为前置操作、后置操作、环绕操作
    		环绕会开始方法之前启用一下通知，并在方法结束之后会将方法的返回结果传给通知
        Point切入点：配置通知应用于项目中的哪些业务操作
```



#### 9.1 springboot框架AOP

**1、引入依赖**

```xml
<!--引入aop支持-->
<dependency>
	<groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId> 
</dependency>
```

**2、新建面向切面配置包（类）**

```java
/**
 * 自定义切面配置类
 */
@Configuration			//告诉springboot这是一个配置类
@Aspect					//代表这是一个切面 配置类
public class MyAspectConfig {

    @Before("execution(* com.pty.demo3.service.*.*(..))")
    public void AddAnnotation(){
        System.out.println("========前置注解========");
    }
    
    // 切面aspect=advice + pointcut
    // 【前置】代表这是一个核心业务逻辑执行前的前置通知 value用来书写切入点表达式
    // 一般是用来切业务逻辑
	// 不关心返回值 com.pty.service.任意类.任意方法(任意参数)
    @Before("execution(* com.pty.service.*.*(..))")
    public void before(JoinPoint joinPoint){
        System.out.println("======调用前置通知========");
        System.out.println(joinPoint.getTarget());
        System.out.println(joinPoint.getStaticPart().getSignature().getName());
    }

    // AfterReturnning
    
    // 【后置】切面aspect=advice + pointcut  代表这是一个核心业务逻辑执行前的后置通知 value用来书写切入点表达式
    @After("execution(* com.morant.service.*.*(..))")
    public void after(JoinPoint joinPoint){
        System.out.println("======调用后置通知======");
    }

    // 【环绕】相当于[拦截器]
    // 返回值作用：用来将业务方法返回结果返回给调用者
    @Around("execution(* com.morant.service.*.*(..))")
    public Object around(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {<!-- -->
        System.out.println("======环绕放行前======");
        //放行
        Object proceed = proceedingJoinPoint.proceed();
        System.out.println("======环绕放行后======");
        return proceed;
    }
}
```



切入点表达式

```java
1. execution：方法级别切入点表达式 运行效率越低
    execution(* com.morant.service.*.*(..))
    
2. within：美级别切入点表达式 运行效率越高
    within(com.morant.service.*)
    
3. 基于注解的切入点表达式
```





#### 9.2 基于注解的方式

1、注解声名类

```java
package com.pty.demo3.config;


import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface AopAnnotation {
}
```

2、配置一条环绕通知


```java
package com.pty.demo3.config;


import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.context.annotation.Configuration;

@Configuration
@Aspect
public class AOPConfig {

    @Around("@annotation(com.pty.demo3.config.AopAnnotation)")
    public Object defayll(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {

        System.out.println("环绕前置操作");
        Object proceed = proceedingJoinPoint.proceed();
        System.out.println("环绕后置操作");

        return proceed;
    }
}
```



```java
@Service
public class UserServiceImpl implements UserService {
    
	@Override
    @AopAnnotation
    public void update() {
        System.out.println("改");

    }
    
    …………
```

**总结：**

```java
//注解：
@Configuration：告诉springboot这是一个配置类
@Aspect：代表这是一个切面配置类
@Before("execution(* com.morant.service.*.*(..))"):代表这是一个核心业务逻辑执行前的前置通知 value用来书写切入点表达式
@After("execution(* com.morant.service.*.*(..))"):代表这是一个核心业务逻辑执行后的后置通知 value用来书写切入点表达式
@Around("execution(* com.morant.service.*.*(..))"):代表这是一个环绕同志 value用来书写切入点表达式
    
其中
@Before
@After
这两个注解的方法中可以使用JoinPoint连接点类作为参数，可以获得业务逻辑的类名和方法名
获得类名：joinPoint.getTarget()
获得方法名：joinPoint.getStaticPart().getSignature().getName()
    
    
而@Around
需要proceedingJoinPoint连接点类作为参数传递
放行方法：proceedingJoinPoint.proceed() //放行之后回显调用放行后面的代码 然后在执行业务逻辑
```





### 10. Restful API

> 一种软件架构风格、设计风格，而不是标准，只是提供了一组**设计原则**和约束条件。它主要用于客户端和服务器交互类的软件。基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制。

REST本身并没有创造新的技术、组件或服务，而隐藏在RESTfuli背后的理念就是使用Wb的现有特征和能力，更好地使用现有Web标准中的一些准则和约束。虽然REST本身受Web技术的影响很深，但是理论上REST架构风格并不是绑定在HTTP上，只不过目前HTTP是唯一与REST相关的实例。所以我们这里描述的REST也是通过HTTP实现的REST。

#### 10.1 

```
使用RESTful操作资源：

[GET] :/users #查询某用户列表
[GET]：/users/1001 #查询某个用户信息
[POST]：/users #新建用户信息- [PUT]：users/1001 #更新用户信息（全部字段）
[PATCH]：/users/1001 #更新用户信息（部分字段）
[DELETE]：/users/1001 #删除用户信息
```

版本化我们的API

```java
不要给小数，
com.pty.demo1
    v1
    	UserController
    	ProductController
    v2
    	UserController
    	ProductController
```



```xml
200 -oK-一切正常
201 -oK-新的资源已经成功创建
204 -oK-资源已经成功删除

304 -Not Modified -客户端使用缓存数据

400 -BadRequest -请求无效，需要附加细节解释如“JSON无效
401 -Unauthorized -请求需要用户验证
403 -Forbidden-服务器已经理解了请求，但是拒绝服务或这种请求的访问是不允许的。
404 -Notfound-没有发现该资源
422 -UnprocessableEntity-只有服务器不能处理实体时使用，比如图像不能被格式化，或者重要字段
丢失。
500 -Internal Server Error-API开发者应谅道免这种错误


使用详细的错误包装错误：状态码code 数据data header头信息message
{
    "errors":[{
        "userMessage":"Sorry,the requested resource does not exist",
        "internalMessage":"No car found in the database",
        "code":34,
        "more info":"http://dev.mwaysolutions.com/blog/api/v1/errors/12345"
     }]
}


```



#### 10.2 实践

```java
// @RestController:  专用于restful风格 
// @Controller:      专用于传统开发注解

RequestMapping
    GetMapping
    PostMapping

@Controller
@RequestMapping("/v1/users")			//v1版本的所有管理users的接口
public class UserController {

    @GetMapping("/{id}")
    @ResponseBody         	 //将[控制器] 方法的返回值转为json，基本上所有的返回值都是这个，而get相反
    public User user(@PathVariable("id") Integer id){
        return new User(id,"xiaoming",new Date());
    }

    @GetMapping
    @ResponseBody
    public ArrayList<User> users(){
        return null;
    }

    //@RequestBody  将前端传来的json数据转化为对象 相当于反序列
    //@ResponseBody	将后端的对象转化为json传到前端显示 相当于序列化
    @PostMapping
    @ResponseBody
    public void saveuser(@RequestBody User user){
        log.debug("name:{} bir:{} salary{}",user.getName(),user.getBir(),user.getSalary());
    }

    @PutMapping("/{id}")
    @ResponseBody
    public void updateuser(@PathVariable("id") Integer id,@RequestBody User user){
    }

    @DeleteMapping("/{id}")
    @ResponseBody
    public void deleteuser(@PathVariable("id")Integer id){
    }
}
```



