from graphviz import Digraph

er = Digraph('ER', filename='er.gv', engine='dot')

er.node('customer', 'Customer', shape='box')
er.node('order', 'Order', shape='box')
er.node('product', 'Product', shape='box')

er.edge('customer', 'order', label='places')
er.edge('order', 'product', label='contains')

er.render(format='png', view=True)


import pandas as pd

tables = {
    'Customer': [
        ['customer_id', 'INTEGER', 'PRIMARY KEY'],
        ['name', 'VARCHAR(255)', 'NOT NULL'],
        ['email', 'VARCHAR(255)', 'NOT NULL']
    ],
    'Order': [
        ['order_id', 'INTEGER', 'PRIMARY KEY'],
        ['customer_id', 'INTEGER', 'FOREIGN KEY'],
        ['order_date', 'DATE', 'NOT NULL']
    ],
    'Product': [
        ['product_id', 'INTEGER', 'PRIMARY KEY'],
        ['name', 'VARCHAR(255)', 'NOT NULL'],
        ['price', 'DECIMAL(10, 2)', 'NOT NULL']
    ]
}

for table_name, table_data in tables.items():
    df = pd.DataFrame(table_data, columns=['Column', 'Data Type', 'Constraints'])
    df.to_html(f'{table_name}.html', index=False)


from graphviz import Digraph

rel = Digraph('Relation', filename='relation.gv', engine='dot')

rel.node('customer', 'Customer', shape='box')
rel.node('order', 'Order', shape='box')
rel.node('product', 'Product', shape='box')

rel.edge('customer', 'order', label='1:N')
rel.edge('order', 'product', label='M:N')

rel.render(format='png', view=True)



from graphviz import Digraph

dfd = Digraph('DFD', filename='dfd.gv', engine='dot')

dfd.node('customer', 'Customer', shape='circle')
dfd.node('order_process', 'Order Process', shape='rectangle')
dfd.node('order_db', 'Order Database', shape='cylinder')

dfd.edge('customer', 'order_process', label='Order Request')
dfd.edge('order_process', 'order_db', label='Store Order')
dfd.edge('order_db', 'order_process', label='Order Data')

dfd.render(format='png', view=True)


from graphviz import Digraph

st = Digraph('State', filename='state.gv', engine='dot')

st.node('new', 'New', shape='circle')
st.node('in_progress', 'In Progress', shape='circle')
st.node('completed', 'Completed', shape='doublecircle')
st.node('cancelled', 'Cancelled', shape='doublecircle')

st.edge('new', 'in_progress', label='start')
st.edge('in_progress', 'completed', label='finish')
st.edge('in_progress', 'cancelled', label='cancel')

st.render(format='png', view=True)