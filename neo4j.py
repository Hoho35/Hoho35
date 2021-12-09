# coding:utf-8
from py2neo import Graph, Node, Relationship

# 连接neo4j数据库，输入地址、用户名、密码

graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))

graph.delete_all()
# 创建结点
test_node_1 = Node('ru_yi_zhuan', name='皇帝')  # 修改的部分
test_node_2 = Node('ru_yi_zhuan', name='皇后')  # 修改的部分
test_node_3 = Node('ru_yi_zhuan', name='公主')  # 修改的部分

graph.create(test_node_1)
graph.create(test_node_2)
graph.create(test_node_3)

# 创建关系
# 分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"丈夫、妻子"，两条关系都有属性count，且值为1。
node_1_zhangfu_node_1 = Relationship(test_node_1, '丈夫', test_node_2)
node_1_zhangfu_node_1['count'] = 1
node_2_qizi_node_1 = Relationship(test_node_2, '妻子', test_node_1)
node_2_munv_node_1 = Relationship(test_node_2, '母女', test_node_3)
node_2_qizi_node_1['count'] = 1

graph.create(node_1_zhangfu_node_1)
graph.create(node_2_qizi_node_1)
graph.create(node_2_munv_node_1)

print(graph)
print(test_node_1)
print(test_node_2)
print(node_1_zhangfu_node_1)
print(node_2_qizi_node_1)
print(node_2_munv_node_1)