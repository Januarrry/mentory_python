import sqlalchemy

metadata = sqlalchemy.metaData()

# post_table = (
#     "post",
#     metadata,
# sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column('user_id', sqlalchemy.models.ForeignKey(users_table.c.from django.db import models)
#     sqlalchemy.Column(sqlalchemy.String(200))
#     sqlalchemy.Column(sqlalchemy.String(50))
#     sqlalchemy.Column)

posts_table = (
    (
        "posts",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
        sqlalchemy.Column("created_when", sqlalchemy.DATETIMEO),
        sqlalchemy.Column("title", sqlalchemy.String(200)),
        sqlalchemy.Column("content", sqlalchemy.TextO),
    ),
)
