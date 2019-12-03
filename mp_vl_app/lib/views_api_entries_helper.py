import logging, pprint


log = logging.getLogger(__name__)


def massage_doc_data( doc_dct ):
    """ Updates doc data so it can be jsonized.
        Called by views.api_entries() """
    doc_dct['_id'] = str( doc_dct['_id'] )
    doc_dct['date'] = 'foo'
    if 'metadata' in doc_dct.keys():
        if 'lastEditedAt' in doc_dct['metadata'].keys():
            doc_dct['metadata']['lastEditedAt'] = str( doc_dct['metadata']['lastEditedAt'] )
    log.debug( f'updated doc_dct, ```{pprint.pformat(doc_dct)}```' )
    return doc_dct


def stringify_date( date_dct ):
    """ Converts given date-fields to str.
        Called by views.api_entries() """
    return 'foo'


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
