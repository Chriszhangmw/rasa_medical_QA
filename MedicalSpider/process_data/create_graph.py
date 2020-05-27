from py2neo import Graph, Node
import json

def process_data(paths):
    diseases = []
    for path in paths:
        disease_data = open(path, 'r', encoding='UTF-8').readlines()
        for data in disease_data:
            disease = json.loads(data)
            diseases.append(disease)
    return diseases

def output_data(data, filepath, jieba_mode=False):
    file = open(filepath, 'w', encoding='UTF-8')
    for line in data:
        # line = json.dumps(line.strip(' \n\r\"'), ensure_ascii=False) + '\n'
        line = line.strip(' \n\r\"')
        if jieba_mode:
            line += ' 18000 nz'
        line += '\n'
        file.write(line)
    file.close()

def extract_drug_producer():
    # middle variables
    drug_dic = {}
    producer_dic = {}
    drug_producer_dic = {}

    # extract data from github address
    with open('./drugs.csv', 'r', encoding='utf-8') as f1:
        data1 = f1.readlines()
        for line in data1:
            line = line.strip()
            line = line.split(',')
            drug_name = line[1]
            drug_order = line[0]
            drug_dic[drug_order] = drug_name
    with open('./producers.csv', 'r', encoding='utf-8') as f2:
        data2 = f2.readlines()
        for line in data2:
            line = line.strip()
            line = line.split(',')
            producer_name = line[1]
            producer_order = line[0]
            producer_dic[producer_order] = producer_name
    with open('./rels_drug_producer.csv', 'r', encoding='utf-8') as f3:
        data3 = f3.readlines()
        for line in data3:
            line = line.strip()
            line = line.split(',')
            drugId = line[0]
            producerId = line[1]
            drugName = drug_dic[drugId]
            producerName = producer_dic[producerId]
            drug_producer_dic[drugName] = producerName
    return drug_producer_dic


class GraphMaker(object):
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="neo4j",
            password="123456"
        )

    def extract_data(self, diseases_dict):
        # diseases = []
        data = dict()

        depts = []
        drugs = []
        symptoms = []
        foods = []
        disease_names = []

        symptom_rel = []
        neopathy_rel = []
        dept_rel = []
        disease_cat_rel = []
        disease_drug_rel = []
        not_eat_rel = []
        can_eat_rel = []

        #add for the producer
        producer = []
        drug_producer_rel = []
        drug_producer_dic = extract_drug_producer()

        for disease in diseases_dict:
            disease_name = disease['name']
            disease_names.append(disease_name)

            if 'drug' in disease:
                drugs += disease['drug']
                for drug in disease['drug']:
                    disease_drug_rel.append([disease_name, drug])
                    if drug in drug_producer_dic.keys():
                        producer_name = drug_producer_dic[drug]
                        producer.append(producer_name)
                        drug_producer_rel.append([drug,producer_name])

            if 'cure_dept' in disease:
                dept = disease['cure_dept']
                depts += disease['cure_dept']
                if len(dept) == 2:
                    big, small = dept[0], dept[1]
                    dept_rel.append([small, big])
                    disease_cat_rel.append([disease_name, small])
                elif len(dept) == 1:
                    disease_cat_rel.append([disease_name, dept[0]])

            if 'symptom' in disease:
                symptoms += disease['symptom']
                for symptom in disease['symptom']:
                    symptom_rel.append([disease_name, symptom])

            if 'neopathy' in disease:
                for neopathy in disease['neopathy']:
                    neopathy_rel.append([disease_name, neopathy])

            if 'can_eat' in disease:
                foods += disease['can_eat']
                for can_eat in disease['can_eat']:
                    can_eat_rel.append([disease_name, can_eat])

            if 'not_eat' in disease:
                foods += disease['not_eat']
                for not_eat in disease['not_eat']:
                    not_eat_rel.append([disease_name, not_eat])

            if 'get_prob' not in disease:
                disease['get_prob'] = '无数据'

            if 'treat_period' not in disease:
                disease['treat_period'] = '无数据'

            if 'treat_cost' not in disease:
                disease['treat_cost'] = '无数据'

            if 'get_way' not in disease:
                disease['get_way'] = '无数据'

        data['diseases'] = diseases_dict
        data['disease_names'] = disease_names
        data['depts'] = set(depts)
        data['drugs'] = set(drugs)
        data['symptoms'] = set(symptoms)
        data['foods'] = set(foods)
        data['producers'] = set(producer)
        data['symptom_rel'] = symptom_rel
        data['neopathy_rel'] = neopathy_rel
        data['dept_rel'] = dept_rel
        data['disease_cat_rel'] = disease_cat_rel
        data['disease_drug_rel'] = disease_drug_rel
        data['not_eat_rel'] = not_eat_rel
        data['can_eat_rel'] = can_eat_rel
        data['drug_producer_rel'] = drug_producer_rel
        return data

    def make_disease_nodes(self, diseases_dict):
        i = 1
        for disease in diseases_dict:
            if i % 50 == 0:
                print("create disease node count=%d" % i)
            node = Node("Disease", name=disease['name'], intro=disease['intro'],
                        cause=disease['cause'], prevent=disease['prevent'], nursing=disease['nursing'],
                        insurance=disease['insurance'], easy_get=disease['easy_get'], get_way=disease['get_way'],
                        get_prob=disease['get_prob'], treat=disease['treat'], treat_prob=disease['treat_prob'],
                        treat_period=disease['treat_period'], treat_cost=disease['treat_cost'],
                        treat_detail=disease['treat_detail']
                        )
            self.g.create(node)
            i += 1
        print("create total disease node count=%d" % (i - 1))
        return

    def make_nodes(self, data):
        self.make_disease_nodes(data['diseases'])
        self.create_nodes("Department", data['depts'])
        self.create_nodes("Drug", data['drugs'])
        self.create_nodes("Symptom", data['symptoms'])
        self.create_nodes("Food", data['foods'])
        self.create_nodes("Producer",data['producers'])
        return

    def make_rels(self, data):
        self.create_rels("Disease", "Disease", data['neopathy_rel'], "has_neopathy", "有并发症")
        self.create_rels("Disease", "Symptom", data['symptom_rel'], "has_symptom", "有症状")
        self.create_rels("Disease", "Drug", data['disease_drug_rel'], "can_use_drug", "可以用药")
        self.create_rels("Department", "Department", data['dept_rel'], "belongs_to", "属于")
        self.create_rels("Disease", "Department", data['disease_cat_rel'], "belongs_to", "属于")
        self.create_rels("Disease", "Food", data['can_eat_rel'], "can_eat", "可以吃")
        self.create_rels("Disease", "Food", data['not_eat_rel'], "not_eat", "不能吃")
        self.create_rels("Drug", "Producer", data['drug_producer_rel'], "drug_producer", "药来自厂商")
        return

    def create_nodes(self, label, entities_names):
        i = 1
        for entity in entities_names:
            if i % 500 == 0:
                print("create %s node count=%d" % (label, i))
            node = Node(label, name=entity)
            self.g.create(node)
            i += 1
        print("create total %s node count=%d" % (label, i - 1))
        return

    def create_rels(self, start_label, end_label, rels, rel_type, name):
        set_rels = []
        for rel in rels:
            set_rels.append('@'.join(rel))
        set_rels = set(set_rels)
        set_rels = [[start, end] for start, end in [r.split('@') for r in set_rels]]
        count = len(set_rels)
        # print(set_rels)
        i = 1
        for start, end in set_rels:
            if i % 500 == 0:
                print("create rel_type: %s, count: %d/%d " % (rel_type, i, count))
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" %\
                    (start_label, end_label, start, end, rel_type, name)
            try:
                self.g.run(query)
                i += 1
            except Exception as e:
                print(e)
        print("finish creating rel_type: %s, count: %d" % (rel_type, i - 1))
        return


if __name__ == '__main__':
    graph_maker = GraphMaker()

    diseases_dict = process_data(['./medical.json'])
    data = graph_maker.extract_data(diseases_dict)

    graph_maker.make_nodes(data)
    graph_maker.make_rels(data)


