# use ssms;
# -- 用户表
# create table if not exists users (
#     user_id int primary key,
#     username varchar(50),
#     email varchar(100),
#     register_date date
# );
#
# -- 商品表
# create table if not exists products (
#     product_id int primary key,
#     product_name varchar(100),
#     price decimal(10,2),
#     stock int
# );
#
# -- 订单表
# create table if not exists orders (
#     order_id int primary key,
#     user_id int,
#     order_date date,
#     total_amount decimal(10,2),
#     foreign key (user_id) references users(user_id)
# );
#
# -- 订单详情表
# create table if not exists order_items (
#     order_id int,
#     product_id int,
#     quantity int,
#     primary key (order_id, product_id),
#     FOREIGN KEY (order_id) REFERENCES orders(order_id),
#     FOREIGN KEY (product_id) REFERENCES products(product_id)
# );
#
# # 查询所有用户的用户名和注册日期。
# select username,register_date from users;
#
# # 查询商品表中价格大于100的商品名称和价格。
# select product_name,price from products where price > 100;
#
# # 查询订单表中2024年1月1日之后的所有订单。
# select * from orders where order_date > '2024年1月1日';
#
# # 查询用户表中邮箱以@gmail.com结尾的用户。
# select * from users where email like '%gmail.com';
# # select * from users where email regexp '^.@gmail.com$';
#
# # 查询订单详情表中购买了商品ID为3的所有记录。
# select * from order_items where product_id = 3;
# # select * from order_items where order_id like '%3%';
#
# # 查询所有商品，按价格从高到低排序。
# select * from products order by price desc;
#
# # 查询最近注册的3个用户（按注册日期降序）。
# select * from users order by register_date desc limit 3;
#
# # 查询订单金额最高的前5个订单。
# select * from orders order by total_amount desc limit 5;
#
# # 查询商品库存大于50的商品，按库存升序排序。
# select * from products where stock > 50 order by stock;
# # select * from products order by stock > 50;
#
# # 查询用户表中第6到第10条记录（假设按user_id升序）。
# select * from users order by user_id limit 5 offset 5;
# # select * from users order by user_id limit 6,10;
#
# # 计算所有商品的总库存。
# select count(stock) from products;
#
# # 查询每个用户的订单数量（提示：使用GROUP BY）。
# select user_id,count(*) as order_count from orders group by user_id;
# # select order_date,count(*) from orders group by order_date;
#
# # 查询每个订单的平均订单金额。
# select avg(total_amount) as avg_order_amount from orders;
#
# # 查询被购买次数最多的商品ID（提示：结合order_items和COUNT）。
# select product_id,count(*) as purchase_count from order_items
# group by product_id order by purchase_count desc limit 1;
#
# # 查询订单总金额超过500的用户的用户ID。
# select user_id from orders where total_amount > 500;
# # select user_id,count(total_amount) > 500 from orders;
#
# # 查询每个订单的用户名和订单金额（连接orders和users）。
# select u.username,o.total_amount from orders o inner join users u on o.user_id = u.user_id;
#
# # 查询购买了商品名称为“iPhone”的订单ID和购买数量（连接order_items、products）。
# select o.order_id,o.quantity from order_items o inner join products p on o.product_id = p.product_id where product_name = 'iPhone';
#
# # 查询每个用户的注册日期和最近一次订单的日期（连接users和orders）。
# select u.username,u.register_date,max(o.order_date) as last_order_date from users u left join orders o on u.user_id = o.user_id group by u.user_id;
# # select users.register_date,orders.order_date from users inner join orders on users.user_id = orders.user_id;
#
# # 查询所有用户及其订单数，包括没有订单的用户（左连接）。
# select u.username,count(o.order_id) as order_count from users u left join orders o on u.user_id = o.user_id group by u.user_id;
# # select users.username,order_items.quantity from users left join order_items on users.user_id = order_items.order_id;
#
# # 查询每个商品的商品名称和总销售数量（连接products和order_items，用SUM(quantity)）。
# select p.product_name,sum(o.quantity) as total_sold from products p inner join order_items o on p.product_id = o.product_id group by p.product_id;
# # select products.product_name, sum(order_items.quantity) from products inner join order_items on order_items.order_id = products.product_id;
