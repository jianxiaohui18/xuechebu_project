import yaml
def read_data():
    with open('../data/login_test.yaml',encoding='utf-8')as f:
        data = yaml.safe_load(f)
        data_list = []
        for i in data:
            data_list.append((i.get('username'),i.get('pwd')))
        print(data_list)
        return data_list