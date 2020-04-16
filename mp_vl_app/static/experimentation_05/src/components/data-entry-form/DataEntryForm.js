import React from 'react';

import { connect } from 'react-redux';

import { init } from './actions';

const mapStateToProps = state => {
    return {
        isLoading: state.dataentryform.isLoading
    }
}

const mapDispatchToProps = dispatch => {
    return {
        init: (dataUrl, schemaUrl, uischemaUrl) => dispatch(init(dataUrl, schemaUrl, uischemaUrl))
    }
}

class DataEntryForm extends React.Component {

    static defaultProps = {
        loadingClassName: 'loading'
    }

    constructor(props) {
        super(props);
        this.props.init(props.dataUrl, props.schemaUrl, props.uischemaUrl);
    }

    render() {
        if (this.props.isLoading) {
            return <div className={this.props.loadingClassName}>Loading</div>
        } else {
            return this.props.render(this.props);
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DataEntryForm);