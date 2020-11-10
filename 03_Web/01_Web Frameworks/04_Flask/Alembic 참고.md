# Alembic 참고

## Installation

```bash
$ pip install alembic
$ alembic init `폴더 이름`
```



## Quick Start

```bash
# alembic.ini

$ sqlalchemy.url = driver://user:pass@localhost/dbname
$ sqlalchemy.url = mysql+pymysql://user:pass@localhost/dbname
$ sqlalchemy.url = sqlite:///app.db
```



```python
# env.py

import sys
sys.path.append('model 파일이 있는 경로')
import model # 파일이름
target_metadata = model.Base.metadata
```



## Migration

```bash
# alembic 버전 파일 만들기
$ alembic revision -m '제목'
# alembic 자동 버전 파일 만들기
$ alembic revision --autogenerate -m '제목'
# migration 실행하기
$ alembic upgrade head # 최신
$ alembic upgrade +2
$ alembic downgrade -1
```



```

import sys
sys.path.append('C:/Users/42Maru/Soom/QAE_OJT_nlp_platform/back')

from app.repository import model
target_metadata = model.Base.metadata


sqlalchemy.url = sqlite:///app.db
```







***참고**

https://sssunho.tistory.com/1