#
# import ast
# import requests
#
#
#
#     def post(self,get_infos):
#         url = self.hosts + get_infos["�����ַ"]
#         response = self.session.post(url =url,
#                                      headers = self.headers,
#                                      params = ast.literal_eval(get_infos["�������(get)"]),
#                                      data = get_infos["�ύ����(post)"]
#                                      )
#         response.encoding = response.apparent_encoding
#     #     �������ٴ����ϵ�
#     def request(self,step_info):
#         request_type = step_info["����ʽ"]
#         if request_type == "get":
#             result = self.get(step_info)
#         elif request_type == "post":
#             result = self.post(step_info)
#         else:
#             result = {'code':3,'result':'����ʽ��֧��'}
#         return result
#
#     def request_by_step(self,step_infos):
#         for step_info in step_infos:
#             temp_result = self.request(step_info)
#             if temp_result['code']!=0:
#                 break
#         return temp_result
#
#
#
# if __name__ == "__main__":
#     get_infos={''}
#     # RequestsUtils().request()