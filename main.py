from itertools import islice
import graphviz


def main(filepath):
    records = parse(filepath)
    dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
    dot.format = 'svg'

    for record in islice(records, 0, len(records)):
        if record['name'] == '.':
            continue

        if record['type'] == 'NS':
            dot.node(record['name'], record['name'])
            dot.node(record['value'], record['value'])
            dot.edge(record['name'], record['value'])

        if record['type'] == 'A':
            dot.node(record['value'], record['value'])
            dot.edge(record['name'], record['value'])

    dot.render('zones', view=False)


def parse(filepath):
    records = []
    with open(filepath, 'r') as f:
        while True:
            row = f.readline()
            if row == '':
                break
            line = row.split(';')
            record = {
                'name': line[0],
                'type': line[1],
                'value': line[2].strip('\n'),
            }
            records.append(record)
    return records


main('zone.csv')