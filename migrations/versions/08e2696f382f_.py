"""empty message

Revision ID: 08e2696f382f
Revises: 66153d2a7cd8
Create Date: 2021-12-13 22:11:17.480678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08e2696f382f'
down_revision = '66153d2a7cd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_notification_message', table_name='notification')
    op.drop_index('ix_notification_status', table_name='notification')
    op.drop_index('ix_notification_subject', table_name='notification')
    op.drop_index('ix_notification_timestamp', table_name='notification')
    op.drop_table('notification')
    op.add_column('stencil', sa.Column('date', sa.DateTime(), nullable=False))
    op.add_column('stencil', sa.Column('file', sa.LargeBinary(), nullable=False))
    op.drop_index('ix_stencil_file_path', table_name='stencil')
    op.create_index(op.f('ix_stencil_date'), 'stencil', ['date'], unique=False)
    op.drop_column('stencil', 'file_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stencil', sa.Column('file_path', sa.VARCHAR(length=256), nullable=False))
    op.drop_index(op.f('ix_stencil_date'), table_name='stencil')
    op.create_index('ix_stencil_file_path', 'stencil', ['file_path'], unique=False)
    op.drop_column('stencil', 'file')
    op.drop_column('stencil', 'date')
    op.create_table('notification',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.TEXT(), nullable=False),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=6), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_notification_timestamp', 'notification', ['timestamp'], unique=False)
    op.create_index('ix_notification_subject', 'notification', ['subject'], unique=False)
    op.create_index('ix_notification_status', 'notification', ['status'], unique=False)
    op.create_index('ix_notification_message', 'notification', ['message'], unique=False)
    # ### end Alembic commands ###