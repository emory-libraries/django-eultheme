'''
Helper classes for forms and widgets.
'''

from django import forms

class TelephoneInput(forms.TextInput):
    'HTML5 telephone input (prompt for numeric entry)'
    input_type = 'tel'


class FilterSearchForm(forms.Form):
    '''Base class for a search form with filters, for use with
    eultheme/snippets/search_filters.html template.  Can be used as an
    example or extended.
    '''
    start_date = forms.IntegerField(required=False,
        help_text=''''Search by start year;  use with end date to specify a range or single year''',
        widget=TelephoneInput(attrs={'class': 'form-control', 'placeholder': 'Start year'}))
    end_date = forms.IntegerField(required=False,
        help_text='Search by end date; use with start date to specify a range or single year',
        widget=TelephoneInput(attrs={'class': 'form-control', 'placeholder': 'End year'}))

    _adv_fields = []

    @property
    def advanced_fields(self):
        'list fields that are considered part of the "advanced" search'
        return [self[f] for f in self._adv_fields]

    @property
    def advanced_fields_values(self):
        '''boolean flag indicating if any of the advanced search fields have
        values; used to determine if search filter display should not be hidden'''
        return any([f.value() for f in self.advanced_fields])


class DateFilterSearchForm(FilterSearchForm):
    '''Base class for a search form with filters *and* date range searching,
    for use with eultheme/snippets/search_filters.html template.  Can be
    used as an example or extended.

    '''
    start_date = forms.IntegerField(required=False,
        help_text=''''Search by start year;  use with end date to specify a range or single year''',
        widget=TelephoneInput(attrs={'class': 'form-control', 'placeholder': 'Start year'}))
    end_date = forms.IntegerField(required=False,
        help_text='Search by end date; use with start date to specify a range or single year',
        widget=TelephoneInput(attrs={'class': 'form-control', 'placeholder': 'End year'}))


    @property
    def advanced_fields_values(self):
        '''boolean flag indicating if any of the advanced search fields have
        values; used to determine if search filter display should not be hidden'''
        filter_fields = set(self.advanced_fields).union(set([self['start_date'], self['end_date']]))
        return any([f.value() for f in filter_fields])