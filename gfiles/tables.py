import django_tables2 as tables
from .models import GenericFile
from django_tables2_column_shifter.tables import ColumnShiftTable


class GFileTable(ColumnShiftTable):
    filename = tables.Column(accessor='original_filename',
                                verbose_name='Filename')
    # def update_checkbox_name(self, name):
    #     self.columns.names()[2]=name

    # def __init__(self, data=None, order_by=None, orderable=None, empty_text=None,
    #              exclude=None, attrs=None, row_attrs=None, pinned_row_attrs=None,
    #              sequence=None, prefix=None, order_by_field=None, page_field=None,
    #              per_page_field=None, template=None, default=None, request=None,
    #              show_header=None, show_footer=True, extra_columns=None, checkname='check'):
    #
    #     self.check = CheckBoxColumnDynamicName(accessor="pk",
    #                                        attrs={
    #                                            "input": {'name': checkname},
    #                                            "th__input": {"onclick": "toggle(this)"},
    #                                            "td__input": {"onclick": "addfile22(this)"}},
    #                                        orderable=False)
    #
    #     super(GFileTable, self).__init__(data, order_by, orderable, empty_text,
    #              exclude, attrs, row_attrs, pinned_row_attrs,
    #              sequence, prefix, order_by_field, page_field,
    #              per_page_field, template, default, request,
    #              show_header, show_footer, extra_columns)

    class Meta:

        model = GenericFile
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootsrap.html'

        fields = ('id', )


class GFileTableWithCheck(GFileTable):
    check = tables.CheckBoxColumn(accessor="pk",
                                           attrs={
                                               "th__input": {"onclick": "toggle(this)"},
                                               "td__input": {"onclick": "addfile(this)"}},
                                           orderable=False)


    class Meta:

        model = GenericFile

        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'paleblue'}
        fields = ('id', 'filename', 'check')








