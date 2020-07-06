from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, data_status=200, data_message=0, results=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        # 定义数据返回的状态
        data = {
            "status": data_status,
            "message": data_message
        }

        # 判断results是否有结果
        if results is not None:
            data['results'] = results

        # 如果还需要传递自定义参数 使用kwargs接受

        data.update(kwargs)

        # 获取一个response对象 需要将自定义的response响应回去
        super().__init__(data=data, status=http_status, headers=headers, exception=exception)
# from django.template.response import SimpleTemplateResponse
# from rest_framework.serializers import Serializer
#
#
# class Response(SimpleTemplateResponse):
#
#     def __init__(self, data=None, status=None,
#                  template_name=None, headers=None,
#                  exception=False, content_type=None):
#         super().__init__(None, status=status)
#
#         if isinstance(data, Serializer):
#             msg = (
#                 'You passed a Serializer instance as data, but '
#                 'probably meant to pass serialized `.data` or '
#                 '`.error`. representation.'
#             )
#             raise AssertionError(msg)
#
#         self.data = data
#         self.template_name = template_name
#         self.exception = exception
#         self.content_type = content_type
