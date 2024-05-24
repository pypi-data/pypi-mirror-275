# request-api-builder
Request builder for quick testing API

## Use
 1. Import RequestBuilder
```python
from request_builder import RequestBuilder
```
2. Set cookie and base url
```python
BuildRequests.set_cookie(cookie)
BuildRequests.set_base_url(base_url)
```
3. Create request
```python
# GET
request_get = RequestBuilder(
    method='get',
    url_template='https://test.com/{id}/another/{another_id}',
    id='123',
    another_id='456',
    query_param_1='value1',
    query_param_2='value2',
)
# POST
request_post = RequestBuilder(
    method='post',
    url_template='https://test.com/{id}/another/{another_id}',
    data={},
    id='123',
    another_id='456',
    query_param_1='value1',
    query_param_2='value2',
)
```