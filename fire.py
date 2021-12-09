import csv  # 导入csv文件
import py2neo  # 导入py2neo库
from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))  # 连接neo4j，将'xxx'分别改为你的用户名和密码
graph.delete_all() # 清除neo4j中原有的结点等所有信息

with open('D:\pythonProject\python\pythonProject3\dm_cllx.csv', 'r', encoding='gbk') as f:
    reader = csv.reader(f)
    for item in reader:
        # if reader.line_num==1:
        #    continue
        print("当前行数：", reader.line_num, "当前内容：", item)
        start_node1 = Node("车辆类型", name=item[1])
        start_node = Node("消防车型", name=item[2])
        end_node = Node("属性值", value=item[3])
        relation = Relationship(start_node, item[0], end_node)
        relation1 = Relationship(start_node1, item[0], start_node)
        #
        graph.merge(start_node, "消防车型", "name")
        graph.merge(end_node, "属性值", "value")
        graph.merge(start_node1,"车辆类型","name")

        graph.merge(relation, "消防车型", "属性值")
        graph.merge(relation1, "车辆类型", "消防车型")
        
    # 注意缩进
with open('D:\pythonProject\python\pythonProject3\dm_hzcs.csv','r', encoding='gbk') as f1:
    locationReader = csv.reader(f1)
    for item in locationReader:
        print("当前行数：", locationReader.line_num, "当前内容：", item)
        start_node1 = Node("火灾场所", name=item[1])
        end_node1 = Node("场所名称", value=item[2])
        relation1 = Relationship(start_node1, item[0], end_node1)
        graph.merge(start_node1, "火灾场所", "name")
        graph.merge(end_node1, "属性值", "value")
        graph.merge(relation1, "火灾场所", "属性值")
with open('D:\pythonProject\python\pythonProject3\dm_jzjg.csv','r', encoding='gbk') as f1:
    locationStructureReader = csv.reader(f1)
    for item in locationStructureReader:
        print("当前行数：", locationStructureReader.line_num, "当前内容：", item)
        start_node2 = Node("建筑结构", name=item[1])
        end_node2 = Node("结构类型", value=item[2])
        relation2 = Relationship(start_node2, item[0], end_node2)
        graph.merge(start_node2, "建筑结构", "name")
        graph.merge(end_node2, "结构类型", "value")
        graph.merge(relation2, "建筑结构", "结构类型")
with open('D:\pythonProject\python\pythonProject3\dm_tqzk.csv','r', encoding='gbk') as f1:
    WeatherReader = csv.reader(f1)
    for item in WeatherReader:
        print("当前行数：", WeatherReader.line_num, "当前内容：", item)
        start_node3 = Node("天气", name=item[1])
        end_node3 = Node("天气类型", value=item[2])
        relation3 = Relationship(start_node3, item[0], end_node3)
        graph.merge(start_node3, "天气", "name")
        graph.merge(end_node3, "天气类型", "value")
        graph.merge(relation3, "天气", "天气类型")
with open('D:\pythonProject\python\pythonProject3\dm_ywqk.csv','r', encoding='gbk') as f1:
    FireDescription = csv.reader(f1)
    for item in FireDescription:
        print("当前行数：", FireDescription.line_num, "当前内容：", item)
        start_node3 = Node("火灾现场描述", name=item[1])
        end_node3 = Node("火灾描述", value=item[2])
        relation3 = Relationship(start_node3, item[0], end_node3)
        graph.merge(start_node3, "火灾现场描述", "name")
        graph.merge(end_node3, "火灾描述", "value")
        graph.merge(relation3, "火灾描述", "火灾现场描述")
with open('D:\pythonProject\python\pythonProject3\gType.csv','r', encoding='gbk') as f1:
    FireType = csv.reader(f1)
    for item in FireType:
        print("当前行数：", FireType.line_num, "当前内容：", item)
        start_node4 = Node("燃烧物具体分类类型", name=item[2])
        end_node4 = Node("燃烧物", value=item[3])
        start_node5 =  Node("燃烧物类型", name=item[1])

        relation4 = Relationship(start_node4, item[0], end_node4)
        relation5 = Relationship(start_node5, item[0], start_node4)

        graph.merge(start_node4, "燃烧物具体分类类型", "name")
        graph.merge(end_node4, "属性值", "value")
        graph.merge(start_node5, "燃烧物类型", "name")

        graph.merge(relation4, "燃烧物", "属性值")
        graph.merge(relation5, "燃烧物类型", "燃烧物具体分类类型")
    

        