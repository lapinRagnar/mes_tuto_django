class Post():

  POSTS = [
    {'id': 1, 'title': 'premier titre', 'body': 'premier body' },
    {'id': 2, 'title': 'deuxime titre', 'body': 'deuxime body' },
    {'id': 3, 'title': 'troisieme titre', 'body': 'troisieme body' },
  ]

  @classmethod
  def all(cls):
    return cls.POSTS

  @classmethod
  def find(cls, id):
    return cls.POSTS[int(id)-1]

