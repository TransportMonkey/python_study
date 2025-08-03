"""
三、SQLAlchemy 实现更新与删除
商品库存管理系统
1、使用 SQLAlchemy 定义 Product 模型：id(主键、自增), name, price, stock
2、实现以下功能
create_product(name, price, stock) # 创建商品
restock_product(product_id, quantity)：# 增加库存
sell_product(product_id, quantity)：# 减少库存（若库存不足则失败）
discontinue_product(product_id)：# 下架商品（删除）
update_price(product_id,price) # 更新商品价格
get_product(product_id) # 查看某个商品，返回字典格式，如： {"id":1,"name":“体恤”,"price":66.9,"stock":1000}
get_all_product() # 返回所有商品列表，如：[{"id":1,"name":“体恤”,"price":66.9,"stock":1000},{"id":2,"name":“短裤”,"price":66.9,"stock":1000}]
get_product_page(page:int,limit:int)  # 获取商品列表（分页数据），返回数据如下 {"count": "本次返回的数据条数","limit":"入参（这里表示用户期望的每页最多返回几条数据)","page":"入参，表示用户希望返回第几页的数据","total":"所有商品的总数"，“data”:[{同get_product返回的格式一致}，...] }
"""