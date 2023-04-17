print('hello world')

hashed_password = hashlib.md5(request.params['foo']).hexdigest()
