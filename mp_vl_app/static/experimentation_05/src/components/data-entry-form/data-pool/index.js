import React from 'react';

import { connect } from 'react-redux';

import Button from '@material-ui/core/Button'

import DataDisplayTable from '../../data-display-table/DataDisplayTable';
import { makeEntry, changeLoading } from '../actions';

const mapStateToProps = state => {
    return {
        dataList: state.dataentryform.dataList
    }
}

const mapDispatchToProps = dispatch => {
    return {
        makeEntry: (urlPrefix, url) => dispatch(makeEntry(urlPrefix, url)),
        changeLoading: (isLoading, scrollX, scrollY) => dispatch(changeLoading(isLoading, scrollX, scrollY))
    };
}

class DataPool extends React.Component {

    static defaultProps = {
        className: "data-pool",
        headers: [],
        dataList: [],
        urlPrefix: '/entry/'
    }

    componentDidMount() {
        this.props.changeLoading(false, 0, 0);
    }

    render() {
        return (
            <div className={this.props.className}>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => this.props.makeEntry(this.props.urlPrefix, this.props.dataUrl)}
                >
                    Create New
                </Button>
                <DataDisplayTable
                    dataList={this.props.dataList}
                    headers={this.props.headers}
                    urlPrefix={this.props.urlPrefix}
                />
            </div>
        );
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DataPool);