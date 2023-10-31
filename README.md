# student_sys
django studing 
## overview
* 这是一个练习django项目的仓库

## 常用命令

初始化django项目

```
django-admin startproject 项目名称
```



创建APP

```
python manage.py startapp app名称
```



### 其他

- `python manage.py makemigrations` 创建迁移文件
- * 所谓迁移文件，就是将model里面定义的迁移到数据库中
  * 每一个model相当于一个数据表，field相当于其中一个字段
- `python manage.py migrate` 创建表
- `python manage.py createsuperuser` 根据提示，输出用户名，邮箱，密码

进入数据库进行交互

```
python .\manage.py dbshell
```

* linux能看到
* .tables  查看所有表



启动项目

```
python manage.py runserver

python manage.py runserver 192.168.124.222:8000
```

## ORM

对象关系映射

把定义好的类映射到对应的数据库的表上，django的model就是ORM的一个具体体现
