def search_object(func):
    def wrapper(*args, **kwargs):
        self, id = args[0], args[1]
        object_id = [x['id'] for x in self.objects]
        left = 0
        right = len(object_id) - 1
        mid = len(object_id) // 2

        while object_id[mid] != id and left <= right:
            if id < object_id[mid]:
                right = mid - 1
            else:
                left = mid + 1 
            mid = (left + right) // 2

        if left > right:
            kwargs.update(object_=None)
            return {'status': '404 Not Found!'}
        kwargs.update(object_=self.objects[mid])
        return {'status': '200 OK', 'msg': self.objects[mid]}
    return wrapper






















# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# left = 0
# right = len(ls) - 1
# mid = len(ls) // 2
# value = int(input('number: '))
# i = 0
# while ls[mid] != value and left <= right:
#     if value < ls[mid]:
#         right = mid - 1
#     else:
#         left = mid + 1 
#     mid = (left + right) // 2
#     i += 1
# if left > right:
#     print('Not Found!')
# else:
#     print(f'{value} = {ls[mid]}')
# print(f'Попытки: {i}')

