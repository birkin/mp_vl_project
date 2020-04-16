import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import Cookie from 'js-cookie';
import configureStore from './configureStore';
import * as serviceWorker from './serviceWorker';

import { CssBaseline } from '@material-ui/core';
import { ThemeProvider } from '@material-ui/styles';

import './index.css';
import theme from './theme';

import App from './App';

const store = configureStore();
window.store = store;

let user = null;
const auth = Cookie.get('auth-token');
if (auth) {
    user = auth.split(":")[0];
}

ReactDOM.render(
    <Provider store={store}>
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <App user={user} />
        </ThemeProvider>
    </Provider>,
    document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
