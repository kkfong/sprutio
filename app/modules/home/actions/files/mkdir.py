from core import FM


class MakeDir(FM.BaseAction):
    def __init__(self, request, path, **kwargs):
        super(MakeDir, self).__init__(request=request, **kwargs)

        self.path = path

    def run(self):
        request = self.get_rpc_request()

        result = request.request('local/make_dir', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path)
        answer = self.process_result(result)
        return answer
