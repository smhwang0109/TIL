- User
    - email
    - password
    - first_name
    - last_name
    - username
    - followers
    - is_staff

```python
from faker import Faker 
f = Faker()

@classmethod
def dummy(cls, n, admin):
    for _ in range(n):
        cls.objects.create(
            email = f.email()
            password = 'tlsdudcks1'
            first_name = f.name()
            last_name = f.name()
            username = f.user_name()
            is_s
        )
```



- Movie
  - title
  - poster
  - distributor
  - director
  - leading_actor
  - release_date
  - genre - SF, 멜로, 액션, 코미디, 스릴러, 음악/뮤지컬, 판타지
  - summary

```python
from faker import Faker
import random

f = Faker()

@classmethod
def dummy(cls, n):
    for _ in range(n):
        cls.objects.create(
            title = f.name()
            # poster = 
            # distributor = User.objects.get()
            director = f.name()
            leading_actor = f.name()
            release_date = f.past_date()
            genre = random.choice(['SF','멜로','액션','코미디','스릴러','음악/뮤지컬','판타지'])
            summary = f.paragraphs()
        )
```

- Review
  - movie
  - user
  - title
  - content
  - rank
  - created_at
  - updated_at

```python
from faker import Faker 

f = Faker()

@classmethod
def dummy(cls, n):
    for _ in range(n):
        cls.objects.create(
            # movie = 
            # user = 
            title = f.name()
            content = f.paragraph()
            rank = randomInt(1,5)
            created_at = f.past_date()
            updated_at = f.past_date()
        )
```

- Comment
  - review와 1:N
  - author
  - content
  - created_at
  - updated_at

```python
from faker import Faker 

f = Faker()

@classmethod
def dummy(cls, n):
    for _ in range(n):
        cls.objects.create(
            # review = 
            # author = 
            content = 
            created_at = 
            updated_at = 
        )
```

