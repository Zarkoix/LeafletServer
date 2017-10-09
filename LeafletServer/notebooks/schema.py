"""
Schema for Notebooks
"""

import graphene
from graphene_django.types import DjangoObjectType
from LeafletServer.notebooks.models import Notebook
from LeafletServer.sections.schema import SectionInput, save_section
from LeafletServer import auth_filter, helpers

class NotebookType(DjangoObjectType):
    """
    Class for NotebookType
    """
    class Meta:
        """
        Meta class for NotebookType
        """
        model = Notebook

class Query(object):
    """
    Notebook Query
    """
    notebook = graphene.Field(NotebookType, id=graphene.Int(),
                              title=graphene.String())
    notebooks = graphene.List(NotebookType)

    def resolve_notebook(self, info, id=None, title=None): #pylint: disable=no-self-use,unused-argument,redefined-builtin
        """
        Returns Single Notebook
        """
        return auth_filter.resolve_model(info, id, title, Notebook)

    def resolve_notebooks(self, info): #pylint: disable=no-self-use,unused-argument
        """
        Returns list of Notebooks
        """
        return auth_filter.resolve_models(info, Notebook)

class CreateNotebook(graphene.Mutation):
    """
    Notebook Creation Mutation
    """
    class Arguments:
        """
        Input Class
        """
        title = graphene.String(required=True)
        #sharing = graphene.String()
        color = graphene.String()
        location = graphene.Int()
        favorite = graphene.Boolean()
        section = SectionInput()

    notebook = graphene.Field(lambda: NotebookType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, color="", location="", favorite="False", #pylint:disable=unused-argument, too-many-arguments
               section=None):
        """
        Create and return Notebook
        """
        notebook = Notebook(owner=info.context.user)
        notebook.title = title
        if notebook.color is not None:
            notebook.color = color
        if notebook.location is not None:
            notebook.location = location
        if notebook.favorite is not None:
            notebook.favorite = favorite
        notebook.last_edited_by = info.context.user
        #if sharing is not None:
        #    notebook.sharing = ast.literal_eval(args.get('sharing'))
        notebook.save()
        print(notebook)

        if isinstance(section, dict):
            save_section(info, notebook, section.title, section.favorite,
                         section.leaflet)
        ok = True

        return CreateNotebook(notebook=notebook, ok=ok)

class EditNotebookTitle(graphene.Mutation):
    """
    Mutation for editing Notebook Title
    """
    class Arguments:
        """
        Input Class
        """
        title = graphene.String(required=True)
        id = graphene.Int(required=True)

    notebook = graphene.Field(lambda: NotebookType)

    @staticmethod
    def mutate(root, info, title, id): #pylint:disable=unused-argument, too-many-arguments, redefined-builtin
        """
        Mutate Notebook
        """
        notebook = helpers.mutate_model(info, id, Notebook, title, "title")
        ok = True

        return EditNotebookTitle(notebook=notebook, ok=ok)

class EditNotebookColor(graphene.Mutation):
    """
    Mutation for editing Notebook Color
    """
    class Arguments:
        """
        Input Class
        """
        color = graphene.String(required=True)
        id = graphene.Int(required=True)

    notebook = graphene.Field(lambda: NotebookType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, color, id): #pylint:disable=unused-argument, too-many-arguments, redefined-builtin
        """
        Mutate Notebook
        """
        notebook = helpers.mutate_model(info, id, Notebook, color, "color")
        ok = True

        return EditNotebookColor(notebook=notebook, ok=ok)

class EditNotebookLocation(graphene.Mutation):
    """
    Mutation for editing Notebook Location
    """
    class Arguments:
        """
        Input Class
        """
        location = graphene.Int(required=True)
        id = graphene.Int(required=True)

    notebook = graphene.Field(lambda: NotebookType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, location, id): #pylint:disable=unused-argument, too-many-arguments, redefined-builtin
        """
        Mutate Notebook
        """
        notebook = helpers.mutate_model(info, id, Notebook, location,
                                        "location")
        ok = True

        return EditNotebookLocation(notebook=notebook, ok=ok)

class EditNotebookFavorite(graphene.Mutation):
    """
    Mutation for editing Notebook Favorite
    """
    class Arguments:
        """
        Input Class
        """
        favorite = graphene.Boolean(required=True)
        id = graphene.Int(required=True)

    notebook = graphene.Field(lambda: NotebookType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, favorite, id): #pylint:disable=unused-argument, too-many-arguments, redefined-builtin
        """
        Mutate Notebook
        """
        notebook = helpers.mutate_model(info, id, Notebook, favorite,
                                        "favorite")
        ok = True

        return EditNotebookFavorite(notebook=notebook, ok=ok)

class DeleteNotebook(graphene.Mutation):
    """
    Mutation for deleting a Notebook
    """

    class Arguments:
        """
        Input Class
        """
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id): #pylint:disable=unused-argument, too-many-arguments, redefined-builtin
        """
        Mutate Notebook
        """
        delete = helpers.delete_model(info, id, Notebook)

        return DeleteNotebook(ok=delete) #pylint:disable=no-value-for-parameter


class Mutation(object):
    """
    Section Mutations
    """
    create_notebook = CreateNotebook.Field()
    edit_notebook_title = EditNotebookTitle.Field()
    edit_notebook_color = EditNotebookColor.Field()
    edit_notebook_location = EditNotebookLocation.Field()
    edit_notebook_favorite = EditNotebookFavorite.Field()
    delete_notebook = DeleteNotebook.Field()
