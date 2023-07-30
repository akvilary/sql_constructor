t to be ready to use
sql_text: str = container.dumps()
```

### Build query with dynamic variables
#### Set variable instantly
```python
import sql_constructor as sc
def get_select_product_query(product_name: str):
    q = sc.SqlQuery()
    q['select'](
        'c.identifier as id',
        'c.name',
    )
    q['from'](
        'catalog as c'
    )
    q['where'](
        'c.name = !product_name'
    )(product_name=product_name)
    return q
```

#### or later in SqlContainer
```python
import sql_constructor as sc
q = sc.SqlQuery()
q['select'](
    'c.identifier as id',
    'c.name',
)
q['from'](
    'catalog as c'
)
q['where'](
    'c.name = !product_name'
)
container: sc.SqlContainer = q()
# you could cache container and set container's variables later
container.vars['product_name'] = 'Smart'
sql_text: str = container.dumps()
```
