import { routerMiddleware, connectRouter } from 'connected-react-router';
import { createBrowserHistory } from 'history';
import { applyMiddleware, combineReducers, compose, createStore} from 'redux';
import createSagaMiddleware from 'redux-saga';

import { reducers as dataentryformReducer, initialState as dataentryformInitialState } from './components/data-entry-form';
import { rootSaga as dataentryformRootSaga } from './components/data-entry-form';


/**
 * Allow intergration with Redux Dev Tools
 */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__(
    { trace: true, traceLimit: 25 }
) || compose;

export const history = createBrowserHistory();
const sagaMiddleware = createSagaMiddleware();

const reducers = Object.assign({},
    dataentryformReducer,
    { router: connectRouter(history) },
    { authentication: (state = {}, action) => state },
    { noop: (state = {}, _) => state }
);

const initialState = Object.assign({},
    dataentryformInitialState
);

export default () => {
    const store = createStore(
        combineReducers(reducers),
        initialState,
        composeEnhancers(applyMiddleware(
            routerMiddleware(history),
            sagaMiddleware
        ))
    );

    sagaMiddleware.run(dataentryformRootSaga);
    return store;
}
