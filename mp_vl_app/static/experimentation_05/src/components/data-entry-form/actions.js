import { Actions as JSONFormsActions } from '@jsonforms/core';

export const ActionTypes = {
    INIT: '@dataentryform/INIT',
    CHANGE_LOADING: '@dataentryform/CHANGE_LOADING',

    FETCH_DATA: '@dataentryform/FETCH_DATA',
    FETCH_SCHEMA: '@dataentryform/FETCH_SCHEMA',
    FETCH_UI_SCHEMA: '@dataentryform/FETCH_UI_SCHEMA',

    CHANGE_ENTRY: '@dataentryform/CHANGE_ENTRY',
    MAKE_ENTRY: '@dataentryform/MAKE_ENTRY',
    SAVE_ENTRY: '@dataentryform/SAVE_ENTRY',
    DELETE_ENTRY: '@dataentryform/DELETE_ENTRY',

    FETCH_DATA_SUCCESS: '@dataentryform/FETCH_DATA_SUCCESS',
    FETCH_SCHEMA_SUCCESS: '@dataentryform/FETCH_SCHEMA_SUCCESS',
    FETCH_UI_SCHEMA_SUCCESS: '@dataentryform/FETCH_UI_SCHEMA_SUCCESS',
    CREATE_ENTRY_SUCCESS: '@dataentryform/CREATE_ENTRY_SUCCESS',
    SAVE_ENTRY_SUCCESS: '@dataentryform/SAVE_ENTRY_SUCCESS',
    DELETE_ENTRY_SUCCESS: '@dataentryform/DELETE_ENTRY_SUCCESS',
    // FETCH_DATA_ERROR: '@dataentryform/FETCH_DATA_ERROR',
    // FETCH_SCHEMA_ERROR: '@dataentryform/FETCH_SCHEMA_ERROR',
    // FETCH_UI_SCHEMA_ERROR: '@dataentryform/FETCH_UI_SCHEMA_ERROR',
    // CREATE_ENTRY_ERROR: '@dataentryform/CREATE_ENTRY_ERROR',
    // SAVE_ENTRY_ERROR: '@dataentryform/SAVE_ENTRY_ERROR',
    // DELETE_ENTRY_ERROR: '@dataentryform/DELETE_ENTRY_ERROR',
}

const init = (dataUrl, schemaUrl, uischemaUrl) => ({
    type: ActionTypes.INIT,
    payload: {
        dataUrl,
        schemaUrl,
        uischemaUrl
    }
});

const changeLoading = (isLoading, scrollX, scrollY) => ({
    type: ActionTypes.CHANGE_LOADING,
    payload: {
        isLoading,
        scrollX,
        scrollY
    },
});

const fetchData = (url) => ({
    type: ActionTypes.FETCH_DATA,
    payload: {
        url
    },
});

const fetchSchema = (url) => ({
    type: ActionTypes.FETCH_SCHEMA,
    payload: {
        url
    },
});

const fetchUISchema = (url) => ({
    type: ActionTypes.FETCH_UI_SCHEMA,
    payload: {
        url
    },
});

const changeEntry = (id) => ({
    type: ActionTypes.CHANGE_ENTRY,
    payload: {
        id
    }
});

const makeEntry = (urlPrefix, url) => ({
    type: ActionTypes.MAKE_ENTRY,
    payload: {
        urlPrefix,
        url
    }
});


const saveEntry = (url, data, userId) => ({
    type: ActionTypes.SAVE_ENTRY,
    payload: {
        url,
        data,
        userId
    },
});

const deleteEntry = (url, id) => ({
    type: ActionTypes.DELETE_ENTRY,
    payload: {
        url,
        id
    },
});



const fetchDataSuccess = (data) => ({
    type: ActionTypes.FETCH_DATA_SUCCESS,
    payload: {
        data
    },
});

const fetchSchemaSuccess = (schema) => ({
    type: ActionTypes.FETCH_SCHEMA_SUCCESS,
    payload: {
        schema
    },
});

const fetchUISchemaSuccess = (uischema) => ({
    type: ActionTypes.FETCH_UI_SCHEMA_SUCCESS,
    payload: {
        uischema
    },
});

const createEntrySuccess = (id, data) => ({
    type: ActionTypes.CREATE_ENTRY_SUCCESS,
    payload: {
        id,
        data
    }
})

const saveEntrySuccess = (data) => ({
    type: ActionTypes.SAVE_ENTRY_SUCCESS,
    payload: {
        data
    },
});

const deleteEntrySuccess = (id) => ({
    type: ActionTypes.DELETE_ENTRY_SUCCESS,
    payload: {
        id
    },
});

const jsonformsInit = (schema, uischema) => 
    JSONFormsActions.init({}, schema, uischema);

const setJsonformsData = (data) => 
    JSONFormsActions.update('', () => data);

export {
    init,
    changeLoading,
    fetchData,
    fetchSchema,
    fetchUISchema,

    changeEntry,
    makeEntry,
    saveEntry,

    deleteEntry,

    fetchDataSuccess,
    fetchSchemaSuccess,
    fetchUISchemaSuccess,

    createEntrySuccess,
    saveEntrySuccess,

    deleteEntrySuccess,

    jsonformsInit,
    setJsonformsData,
}