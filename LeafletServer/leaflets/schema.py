"""
Schema for Leaflets
"""

import graphene
from graphene_django.types import DjangoObjectType
from LeafletServer.leaflets.models import Leaflet
from LeafletServer.sections.models import Section
from LeafletServer.leaves.schema import LeafInput, save_leaf
from LeafletServer import auth_filter

class LeafletType(DjangoObjectType):
    """
    Class for LeafletType
    """
    class Meta:
        """
        Meta class for LeafletType
        """
        model = Leaflet

class Query(object):
    """
    Leaflet Query
    """
    leaflet = graphene.Field(LeafletType, id=graphene.Int(),
                             title=graphene.String())
    leaflets = graphene.List(LeafletType)

    def resolve_leaflet(self, info, id=None, title=None): #pylint: disable=no-self-use,unused-argument,redefined-builtin
        """
        Returns Single Leaflet
        """
        return auth_filter.resolve_model(info, id, title, Leaflet)

    def resolve_leaflets(self, info): #pylint: disable=no-self-use,unused-argument
        """
        Returns list of Leaflets
        """
        return auth_filter.resolve_models(info, Leaflet)

class LeafletInput(graphene.InputObjectType):
    """
    Leaflet Input
    """
    title = graphene.String(required=True)
    favorite = graphene.Boolean()
    leaf = LeafInput()

def save_leaflet(info, section, title, favorite=False, leaf=None):
    """
    Saves Leaflet
    """
    leaflet = Leaflet(owner=info.context.user)
    leaflet.section = section
    leaflet.title = title
    leaflet.favorite = favorite
    leaflet.save()

    if isinstance(leaf, dict):
        save_leaf(info, leaflet, leaf.title, leaf.content, leaf.leaf_type)

    print(leaflet)

    return leaflet

class CreateLeaflet(graphene.Mutation):
    """
    Leaflet Creation Mutation
    """
    class Arguments:
        """
        Input Class
        """
        section_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        favorite = graphene.Boolean()
        leaf = LeafInput()

    leaflet = graphene.Field(lambda: LeafletType)

    @staticmethod
    def mutate(root, info, title, section_id, favorite=False, leaf=None): #pylint: disable=unused-argument, too-many-arguments
        """
        Create and return Leaflet
        """
        section = Section.objects.get(id=section_id)
        return CreateLeaflet(leaflet=save_leaflet(info, section, title,
                                                  favorite, leaf))

class Mutation(object):
    """
    Leaflet Mutations
    """
    create_leaflet = CreateLeaflet.Field()
