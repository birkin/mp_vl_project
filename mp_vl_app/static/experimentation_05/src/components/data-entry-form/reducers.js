import { ActionTypes } from './actions';

import { jsonformsReducer } from '@jsonforms/core';

const rootReducer = (state = {}, action) => {
    if (action.type === ActionTypes.CHANGE_LOADING) {
        const payload = action.payload;
        const isLoading = payload.isLoading;
        const scrollX = payload.scrollX === undefined ? state.scrollX : payload.scrollX;
        const scrollY = payload.scrollY === undefined ? state.scrollY : payload.scrollY;
        return Object.assign({}, state, {
            isLoading,
            scrollX,
            scrollY
        });
    }
    if (action.type === ActionTypes.FETCH_DATA_SUCCESS) {
        const payload = action.payload;
        const data = payload.data;
        return Object.assign({}, state, {
            dataList: data
        });
    }
    if (action.type === ActionTypes.CHANGE_ENTRY) {
        const payload = action.payload;
        const id = payload.id;
        const dataList = state.dataList;
        const data = dataList.find(item => item._id === id);
        return Object.assign({}, state, {
            currentData: data
        });
    }
    if (action.type === ActionTypes.CREATE_ENTRY_SUCCESS) {
        const payload = action.payload;
        const id = payload.id; //@TODO: Do we need this?
        const data = payload.data;
        const dataList = state.dataList;
        const newDataList = dataList.concat(data);
        console.log(data);
        return Object.assign({}, state, {
            dataList: newDataList
        })
    }
    if (action.type === ActionTypes.SAVE_ENTRY_SUCCESS) {
        const payload = action.payload;
        const data = payload.data;
        const id = data._id;
        const currentDataList = state.dataList;
        const newDataList = currentDataList.slice();
        const index = currentDataList.findIndex(item => item._id === id);
        if (index < 0) {
            console.error("Cannot find entry to update")
            return state;
        } else {
            newDataList[index] = data;
            return Object.assign({}, state, {
                dataList: newDataList,
                saveMessage: "Save Successful"
            });
        }
    }
    return state;
}

export default Object.assign({}, 
    {
        dataentryform: rootReducer,
        jsonforms: jsonformsReducer()
    }
);

/*
const rootReducerOLD = (state = {}, action) => {
    if (action.type === INIT) {
        const payload = action.payload;
        const data = payload.data;
        if (!data) {
            return state;
        }
        const duplicateData = data.map(dataItem => Object.assign({}, dataItem));
        return Object.assign({}, state, {
            hasBeenStarted: true,
            hash: Math.random(),
            data: duplicateData
        });
    }
    if (action.type === SAVE) {
        const payload = action.payload;
        const data = payload.data;
        const id = payload.id;
        const currentDataList = state.data;
        const duplicateDataList = currentDataList.map(item => Object.assign({}, item));
        const index = currentDataList.findIndex(item => item._id === id);
        if (index < 0) {
            duplicateDataList.push({
                id: id,
                ...data
            });
        } else {
            duplicateDataList[index] = data;
        }
        return Object.assign({}, state, {
            // currentId: 
            data: duplicateDataList
        });
    }
    if (action.type === SET_CURRENT_DATA) {
        const id = action.payload.id;
        if (!state.data) {
            return state;
        }
        const data = state.data.find(item => item._id === id);
        console.log(id, data)
        return Object.assign({}, state, {
            currentData: data
        });
    }
    return state;
}
*/