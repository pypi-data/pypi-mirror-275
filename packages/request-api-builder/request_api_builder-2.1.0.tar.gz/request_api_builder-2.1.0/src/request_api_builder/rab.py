import requests


class BuildRequests:
    cookie = None
    base_url = None

    @classmethod
    def set_cookie(cls, cookie):
        cls.cookie = cookie

    @classmethod
    def set_base_url(cls, base_url):
        cls.base_url = base_url

    @classmethod
    def get_request(cls, url_template, params=None,  **url_params):
        url = cls.base_url + url_template.format(**url_params)
        response = requests.get(
            url,
            headers={"Cookie": cls.cookie},
            params=params,
        )
        return response

    @classmethod
    def post_request(cls, url_template, data=None, **url_params):
        url = cls.base_url + url_template.format(**url_params)
        response = requests.post(
            url,
            headers={"Cookie": cls.cookie},
            data=data,
        )
        return response

    @classmethod
    def patch_request(cls, url_template, data=None, **url_params):
        url = cls.base_url + url_template.format(**url_params)
        response = requests.patch(
            url,
            headers={"Cookie": cls.cookie},
            data=data,
        )
        return response

    @classmethod
    def delete_request(cls, url_template, **url_params):
        url = cls.base_url + url_template.format(**url_params)
        response = requests.delete(
            url,
            headers={"Cookie": cls.cookie},
        )
        return response


def build_request(method, url_template, data=None, **kwargs):
    br = BuildRequests()
    url_params = {k: v for k, v in kwargs.items() if '{' + k + '}' in url_template}
    query_params = {k: v for k, v in kwargs.items() if '{' + k + '}' not in url_template}

    if method.lower() == 'get':
        return br.get_request(url_template, params=query_params, **url_params)
    elif method.lower() == 'post':
        return br.post_request(url_template, data=data, **url_params)
    elif method.lower() == 'patch':
        return br.patch_request(url_template, data=data, **url_params)
    elif method.lower() == 'delete':
        return br.delete_request(url_template, **url_params)
    else:
        raise ValueError("Invalid method. Use 'get' or 'post'.")
