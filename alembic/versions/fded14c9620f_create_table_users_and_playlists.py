"""create table users and playlists

Revision ID: fded14c9620f
Revises: 
Create Date: 2022-10-01 12:26:31.763954

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fded14c9620f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('created_data', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlists',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('decription', sa.String(), nullable=True),
    sa.Column('owner_id', postgresql.UUID(), nullable=True),
    sa.Column('created_data', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_playlists_decription'), 'playlists', ['decription'], unique=False)
    op.create_index(op.f('ix_playlists_title'), 'playlists', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_playlists_title'), table_name='playlists')
    op.drop_index(op.f('ix_playlists_decription'), table_name='playlists')
    op.drop_table('playlists')
    op.drop_table('users')
    # ### end Alembic commands ###
