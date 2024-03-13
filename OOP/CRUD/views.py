# CRUD -  C: create, R: read(Listening, detail), U: update, D: delete
from search import search_object

class CreateMixin:
    def _get_or_set_objects(self):
        try:
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_objects()

    def post(self, **kwargs):
        self.id += 1 
        obj = dict(id=self.id, **kwargs)
        print(obj, '!!!')
        self.objects.append(obj)
        return {'status': '201 created', 'msg': obj}
    

class ReadMixin:
    def list(self):
        res = [{'id': obj['id'], 'title': obj['title']} for obj in self.objects]
        return {'status': '200 OK', 'msg': res}
   
    @search_object
    def detail(self, id, **kwargs):
            obj = kwargs['object_']
            if not obj:
                return {'status': '404 Not Found!'}
            return {'status': '200 OK', 'msg': obj}


class UpdateMixin:
    @search_object
    def path(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if not obj:
            return {'status': '404 Not Found!'}
        obj.update(**kwargs)
        return {'status': '200 OK', 'msg': obj}

class DeleteMixin:
    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs['object_']
        if not obj:
            return {'status': '404 Not Found!'}
        self.objects.remove(obj)
        return {'status': '204 Not Content', 'msg': "Deleted"}
      

# obj = CreateMixin()
# obj.post(title='Redmi note 10 lite', description='The best phone for own price and for games!', qty=10, price=250)
# # print