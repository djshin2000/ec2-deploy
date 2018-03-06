# EC2 Deploy project

AWS의 EC2 배포를 연습하는 프로젝트입니다.
`.secrets`폴더내의 파일로 비밀 키를 관리합니다.

DB로 PostgresSQL을 사용하며, 'local'환경에서는 'localhost'의 DB, ''

## requirements

- Python (3.6)

## Installation

```
pip install -r requirements.txt
```


## Secrets

**`.secrets/base.json`**

```json
{
  "SECRET_KEY": "<Django settings SECRET_KEY value>"
}

```

**'.secrets/dev.json'**

> PostgreSQL(AWS RDS)을 사용한다

```json
{
  "DATABASE": {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "<자신의 RDS주소 ex)instance",
        "NAME": "ec2_deploy",
        "USER": "djshin2000",
        "PASSWORD": "dj03046820",
        "PORT": 5432
    }
  }
}

```