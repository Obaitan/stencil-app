"""empty message

Revision ID: d01bd18cb572
Revises: cc84dc4b3342
Create Date: 2021-11-28 20:57:38.313203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd01bd18cb572'
down_revision = 'cc84dc4b3342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=200), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_resource_link'), 'resource', ['link'], unique=True)
    op.create_index(op.f('ix_resource_timestamp'), 'resource', ['timestamp'], unique=False)
    op.create_index(op.f('ix_resource_title'), 'resource', ['title'], unique=True)
    op.create_index(op.f('ix_resource_type'), 'resource', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_resource_type'), table_name='resource')
    op.drop_index(op.f('ix_resource_title'), table_name='resource')
    op.drop_index(op.f('ix_resource_timestamp'), table_name='resource')
    op.drop_index(op.f('ix_resource_link'), table_name='resource')
    op.drop_table('resource')
    # ### end Alembic commands ###