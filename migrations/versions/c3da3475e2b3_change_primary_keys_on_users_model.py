"""change primary keys on users model

Revision ID: c3da3475e2b3
Revises: 
Create Date: 2019-03-27 23:07:42.348928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3da3475e2b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_v2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('node_id', sa.String(), nullable=True),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.Column('gravatar_id', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('html_url', sa.String(), nullable=True),
    sa.Column('followers_url', sa.String(), nullable=True),
    sa.Column('following_url', sa.String(), nullable=True),
    sa.Column('gists_url', sa.String(), nullable=True),
    sa.Column('starred_url', sa.String(), nullable=True),
    sa.Column('subscriptions_url', sa.String(), nullable=True),
    sa.Column('organizations_url', sa.String(), nullable=True),
    sa.Column('repos_url', sa.String(), nullable=True),
    sa.Column('events_url', sa.String(), nullable=True),
    sa.Column('received_events_url', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('site_admin', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('blog', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hireable', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('public_repos', sa.Integer(), nullable=True),
    sa.Column('public_gists', sa.Integer(), nullable=True),
    sa.Column('followers', sa.Integer(), nullable=True),
    sa.Column('following', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_v2_id'), 'user_v2', ['id'], unique=False)
    op.create_index(op.f('ix_user_v2_login'), 'user_v2', ['login'], unique=True)
    op.create_table('token_blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('token_type', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user_v2.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token_blacklist')
    op.drop_index(op.f('ix_user_v2_login'), table_name='user_v2')
    op.drop_index(op.f('ix_user_v2_id'), table_name='user_v2')
    op.drop_table('user_v2')
    # ### end Alembic commands ###