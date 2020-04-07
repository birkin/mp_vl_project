import { call, put, putResolve, select, takeEvery, all, take } from 'redux-saga/effects';
import { push } from 'connected-react-router';

import { 
    changeLoading,
    fetchDataSuccess,
    fetchSchemaSuccess,
    fetchUISchemaSuccess,
    createEntrySuccess,
    saveEntrySuccess,
    
    ActionTypes
} from './actions';
import API from './api';
import { Actions as JSONFormsActions } from '@jsonforms/core';

/**
 * @TODO Replace with API call
 */
const init = function* (action) {
    const payload = action.payload;
    const { dataUrl, schemaUrl, uischemaUrl } = payload;

    yield put(changeLoading(true));
    try {
        const [data, schema, uischema] = yield all([
            call(() => API.fetchData(dataUrl)),
            call(() => API.fetchSchema(schemaUrl)),
            call(() => API.fetchUISchema(uischemaUrl))
        ]);
        yield put(JSONFormsActions.init({}, schema, uischema));
        yield put(fetchDataSuccess(data));
        yield put(fetchSchemaSuccess(schema));
        yield put(fetchUISchemaSuccess(uischema));
    } catch (err) {
        console.error(err);
        /** @TODO */
    }
    yield put(changeLoading(false));
}

const fetchData = function* (action) {
    console.log("in fetch data")
    const payload = action.payload;
    const url = payload.url;
    yield put(changeLoading(true));
    try {
        const data = yield call(() =>
            fetch(url)
            .then(result => result.json())
        );
        yield put(fetchDataSuccess(data));
        return data;
    } catch (err) {
        console.error(err.stack);
        /** @TODO */
    }
    yield put(changeLoading(false));
}

const makeEntry = function* (action) {
    const payload = action.payload;
    const urlPrefix = payload.urlPrefix;
    const url = payload.url;
    yield put(changeLoading(true));
    try {
        const response = yield call(() => API.createEntry(url));
        const id = response.id;
        const data = response.data;
        yield put(createEntrySuccess(id, data));
        yield put(push(`${urlPrefix}${id}`));
    } catch (err) {
        console.error(err.stack);
        /** @TODO */
    }
    yield put(changeLoading(false));
}

const saveEntry = function* (action) {
    const payload = action.payload;
    const url = payload.url;
    const data = payload.data;
    const userId = payload.userId;
    const scrollX = window.scrollX;
    const scrollY = window.scrollY + 60; // To account for the save message
    yield put(changeLoading(true));
    try {
        /** @TODO Determine if we need response */
        yield call(() => API.updateEntry(url, data, userId));
        yield put(saveEntrySuccess(data));
    } catch (err) {
        console.error(err);
        /** @TODO */
    }
    yield put(changeLoading(false, scrollX, scrollY));
}

const watchInitSaga = function* () {
    yield takeEvery(ActionTypes.INIT, init);
}

const watchFetchDataSaga = function* () {
    yield takeEvery(ActionTypes.FETCH_DATA, fetchData);
}

const watchMakeEntrySaga = function* () {
    yield takeEvery(ActionTypes.MAKE_ENTRY, makeEntry);
}

const watchSaveEntrySaga = function* () {
    yield takeEvery(ActionTypes.SAVE_ENTRY, saveEntry);
}

export default function* rootSaga() {
    yield all([
        watchInitSaga(),
        watchFetchDataSaga(),
        watchMakeEntrySaga(),
        watchSaveEntrySaga()
    ]);
}