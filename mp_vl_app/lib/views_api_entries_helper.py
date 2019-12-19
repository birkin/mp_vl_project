import functools, json, logging, pprint
from typing import Tuple

import pymongo


log = logging.getLogger(__name__)


def massage_docs( entries_query: pymongo.cursor.Cursor ) -> str:
    """ Converts doc-objects into json for response.
        NB: Because `entries_query` is a pymongo-cursor, applying a slice would act as a filter to the variable itself, not to a copy, as may be expected.
        Called by views.api_entries() """
    entries_jsn = '{}'
    try:
        entries = []
        for ( idx, doc ) in enumerate( entries_query ):  # ( idx -> int, doc -> dict )
            doc: dict = massage_doc_data( doc )
            entries.append( doc )
        log.debug( f'stringify_month.cache_info(), ```{stringify_month.cache_info()}```' )
        log.debug( f'entries (first 10), ```{pprint.pformat(entries[0:10])}```' )
        entries_jsn = json.dumps( entries, sort_keys=True, indent=2 )
    except:
        log.exception( 'problem processing mongo data' )
        pass
    return entries_jsn


def massage_doc_data( doc: dict ) -> dict:
    """ Updates doc data so it can be jsonized.
        Called by massage_docs() """
    log.debug( f'initial doc, ```{pprint.pformat(doc)}```' )
    doc['_id'] = str( doc['_id'] )
    doc['id_clean'] = str( doc['_id'] )  # so template can access this key
    if doc.get( 'date', None ):
        doc['date_display'] = stringify_date( doc['date'] )
    else:
        doc['date_display'] = '(no date info)'
    if 'metadata' in doc.keys():
        if 'lastEditedAt' in doc['metadata'].keys():
            doc['metadata']['lastEditedAt'] = str( doc['metadata']['lastEditedAt'] )
        if 'lastEditedBy' in doc['metadata'].keys():
            if type( doc['metadata']['lastEditedBy'] ) != str:
                doc['metadata']['lastEditedBy'] = str( doc['metadata']['lastEditedBy'] )
    log.debug( f'updated doc, ```{pprint.pformat(doc)}```' )
    return doc


def stringify_date( date_dct ) -> str:
    """ Creates and returns a display-date string from given date-fields.
        Called by massage_doc_data() """
    date_display_str = 'INVALID DATE'
    ( year, month, day, modifier, year_as_bool, month_as_bool, day_as_bool, modifier_as_bool ) = initialize_date_data( date_dct )
    if ( year_as_bool and month and modifier_as_bool and day ):
        date_display_str = f'{year} {month} {day} ({modifier})'
    elif ( year_as_bool and month_as_bool and day_as_bool and not modifier_as_bool ):
        date_display_str = f'{year} {month} {day}'
    elif ( year_as_bool and modifier_as_bool and month_as_bool and not day_as_bool ):
        date_display_str = f'{year} {month} ({modifier})'
    elif ( year_as_bool and not modifier_as_bool and month_as_bool and not day_as_bool ):
        date_display_str = f'{year} {month}'
    elif ( year_as_bool and modifier_as_bool and not month_as_bool and not day_as_bool ):
        date_display_str = f'{modifier} {year}'
    elif ( year_as_bool and not modifier_as_bool and not month_as_bool and not day_as_bool ):
        date_display_str = f'{year}'
    return date_display_str


def initialize_date_data( date_dct ) -> Tuple:
    """ Initializes vars.
        Called by stringify_date() """
    log.debug( f'date_dct, ```{date_dct}```' )
    ( year, month, day, modifier ) = (
        date_dct.get('year', None), date_dct.get('month', None), date_dct.get('day', None), date_dct.get('modifier', None) )  # ( year: int, month: int or float, day: int, modifier: str )
    month: str = stringify_month( date_dct['month'] )
    year_as_bool = True if year else False
    month_as_bool = True if month else False
    day_as_bool = True if day else False
    modifier_as_bool = True if modifier else False
    log.debug( f'year, `{year}`; month, `{month}`; day, `{day}`; modifier, `{modifier}`; year_as_bool, `{year_as_bool}`; month_as_bool, `{month_as_bool}`; day_as_bool, `{day_as_bool}`; modifier_as_bool, `{modifier_as_bool}`' )
    return ( year, month, day, modifier, year_as_bool, month_as_bool, day_as_bool, modifier_as_bool )


@functools.lru_cache( maxsize=16 )
def stringify_month( num ) -> str:  # TypeVar( 'num', int, float )
    """ Converts given month number to appropriate string.
        Called by initialize_date_data() """
    log.debug( f'num, `{num}`; type(num), `{type(num)}`' )
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    month_int = month_names[ int(num) - 1 ]
    log.debug( f'month_int, `{month_int}`' )
    return month_int
