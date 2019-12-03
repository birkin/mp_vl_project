import logging, pprint


log = logging.getLogger(__name__)


def massage_doc_data( doc_dct ):
    """ Updates doc data so it can be jsonized.
        Called by views.api_entries() """
    log.debug( f'initial doc_dct, ```{pprint.pformat(doc_dct)}```' )
    doc_dct['_id'] = str( doc_dct['_id'] )
    doc_dct['date_display'] = stringify_date( doc_dct['date'] )
    if 'metadata' in doc_dct.keys():
        if 'lastEditedAt' in doc_dct['metadata'].keys():
            doc_dct['metadata']['lastEditedAt'] = str( doc_dct['metadata']['lastEditedAt'] )
        if 'lastEditedBy' in doc_dct['metadata'].keys():
            if type( doc_dct['metadata']['lastEditedBy'] ) != str:
                doc_dct['metadata']['lastEditedBy'] = str( doc_dct['metadata']['lastEditedBy'] )
    log.debug( f'updated doc_dct, ```{pprint.pformat(doc_dct)}```' )
    return doc_dct


def stringify_date( date_dct ):
    """ Converts given date-fields to str.
        Called by massage_doc_data() """
    date_str = ''
    if not date_dct:
        return date_str
    year, month, day, modifier = date_dct.get('year', None), date_dct.get('month', None), date_dct.get('day', None), date_dct.get('modifier', None)
    month = intify_month( date_dct['month'])
    year_as_bool = True if year else False
    month_as_bool = True if month else False
    day_as_bool = True if day else False
    modifier_as_bool = True if modifier else False
    if ( year_as_bool and month and modifier_as_bool and day ):
        date_str = f'{year} {month} {day} ({modifier})'
    elif ( year_as_bool and month_as_bool and day_as_bool and not modifier_as_bool ):
        date_str = f'{year} {month} {day}'
    elif ( year_as_bool and modifier_as_bool and month_as_bool and not day_as_bool ):
        date_str = f'{year} {month} ({modifier})'
    elif ( year_as_bool and not modifier_as_bool and month_as_bool and not day_as_bool ):
        date_str = f'{year} {month}'
    elif ( year_as_bool and modifier_as_bool and not month_as_bool and not day_as_bool ):
        date_str = f'{modifier} {year}'
    elif ( year_as_bool and not modifier_as_bool and not month_as_bool and not day_as_bool ):
        date_str = f'{year}'
    else:
        date_str = 'INVALID DATE'
    return date_str


def intify_month( num ):
    """ Converts given month number to appropriate string.
        Called by stringify_date() """
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    month_int = month_names[ int(num) - 1 ]
    log.debug( f'month_int, `{month_int}`' )
    return month_int


# function monthAsNumberToString(num) {
#     const monthNames = [
#         "January", "February", "March",
#         "April", "May", "June", "July",
#         "August", "September", "October",
#         "November", "December"
#     ];
#     return monthNames[num-1];
# }

# export default (date) => {
#     let string;
#     if (!date) {
#         return;
#     }
#     let { year, month, day, modifier } = date;
#     month = monthAsNumberToString(month);
#     const yearAsBool = !!year;
#     const monthAsBool = !!month;
#     const modifierAsBool = !!modifier;
#     const dayAsBool = !!day;
#     if (yearAsBool && month && modifierAsBool && day) {
#         string = `${year} ${month} ${modifier} ${day}`;
#     } else if (yearAsBool && monthAsBool && dayAsBool && !modifierAsBool) {
#         string = `${year} ${month} ${day}`;
#     } else if (yearAsBool & modifierAsBool && monthAsBool && !dayAsBool) {
#         string = `${year} ${modifier} ${month}`;
#     } else if (yearAsBool && !modifierAsBool && monthAsBool && !dayAsBool) {
#         string = `${year} ${month}`;
#     } else if (yearAsBool && modifierAsBool && !monthAsBool && !dayAsBool) {
#         string = `${modifier} ${year}`;
#     } else if (yearAsBool && !modifierAsBool && !monthAsBool && !dayAsBool) {
#         string = `${year}`;
#     } else {
#         string = "INVALID DATE";
#     }
#     return string;
# }
