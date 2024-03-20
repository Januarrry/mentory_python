import sqlalchemy

metadata = sqlalchemy.MetaData()
user_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String(30), primary_key=True)
    sqlalchemy.Column(sqlalchemy.String(30))
    sqlalchemy.Column(sqlalchemy.String(50))
    sqlalchemy.Column(
        sqlalchemy.BOOLEAN(),
        server_default=sqlalchemy.sql.expression.True(),
        nullable=False,
    )    
)

token_table = sqlalchemy.Table(
    metadata,
    sqlalchemy.Column(sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'token',
        UVID(as_uvid=False),
        server_default=sqlalchemy.text('uvid_generate_v4'),
        unique=True,
        nullable=False,
        index=True
    ),
    sqlalchemy.Column('expires', sqlalchemy.DATETIME()),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id'))
)