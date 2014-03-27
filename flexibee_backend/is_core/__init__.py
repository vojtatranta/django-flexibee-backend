from django.db.models.loading import get_model
from django.utils.datastructures import SortedDict
from django.db.transaction import get_connection

from is_core.main import UIRestModelISCore
from is_core.generic_views.inline_form_views import TabularInlineFormView
from is_core.generic_views.table_views import TableView

from flexibee_backend import config


class FlexibeeIsCore(UIRestModelISCore):

    def init_request(self, request):
        get_connection('flexibee').set_db_name(self.get_company().flexibee_db_name)

    def get_company(self):
        raise NotImplemented
