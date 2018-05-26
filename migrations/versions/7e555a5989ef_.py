"""empty message

Revision ID: 7e555a5989ef
Revises: 
Create Date: 2018-05-25 19:56:47.122312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e555a5989ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_name', sa.String(length=100), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('img', sa.String(length=100), nullable=False),
    sa.Column('account', sa.String(length=32), nullable=False),
    sa.Column('sex', sa.SmallInteger(), nullable=False),
    sa.Column('state', sa.SmallInteger(), nullable=False),
    sa.Column('_last_time', sa.Integer(), nullable=False),
    sa.Column('_create_time', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account')
    )
    op.create_table('tb_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=100), nullable=False),
    sa.Column('role_type', sa.SmallInteger(), nullable=False),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('_role_pri', sa.Text(), nullable=True),
    sa.Column('_create_time', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_role_admin',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['tb_admin.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['tb_role.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('role_id', 'admin_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_role_admin')
    op.drop_table('tb_role')
    op.drop_table('tb_admin')
    # ### end Alembic commands ###