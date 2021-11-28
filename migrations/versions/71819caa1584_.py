"""empty message

Revision ID: 71819caa1584
Revises: d01bd18cb572
Create Date: 2021-11-28 23:25:58.406259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71819caa1584'
down_revision = 'd01bd18cb572'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('circle', sa.String(length=50), nullable=False),
    sa.Column('zone', sa.String(length=20), nullable=False),
    sa.Column('dob', sa.String(length=24), nullable=False),
    sa.Column('dod', sa.String(length=24), nullable=False),
    sa.Column('yop', sa.String(length=4), nullable=False),
    sa.Column('cemetry', sa.String(length=250), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_cemetry'), 'record', ['cemetry'], unique=False)
    op.create_index(op.f('ix_record_circle'), 'record', ['circle'], unique=False)
    op.create_index(op.f('ix_record_dob'), 'record', ['dob'], unique=False)
    op.create_index(op.f('ix_record_dod'), 'record', ['dod'], unique=False)
    op.create_index(op.f('ix_record_name'), 'record', ['name'], unique=True)
    op.create_index(op.f('ix_record_timestamp'), 'record', ['timestamp'], unique=False)
    op.create_index(op.f('ix_record_yop'), 'record', ['yop'], unique=False)
    op.create_index(op.f('ix_record_zone'), 'record', ['zone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_record_zone'), table_name='record')
    op.drop_index(op.f('ix_record_yop'), table_name='record')
    op.drop_index(op.f('ix_record_timestamp'), table_name='record')
    op.drop_index(op.f('ix_record_name'), table_name='record')
    op.drop_index(op.f('ix_record_dod'), table_name='record')
    op.drop_index(op.f('ix_record_dob'), table_name='record')
    op.drop_index(op.f('ix_record_circle'), table_name='record')
    op.drop_index(op.f('ix_record_cemetry'), table_name='record')
    op.drop_table('record')
    # ### end Alembic commands ###
