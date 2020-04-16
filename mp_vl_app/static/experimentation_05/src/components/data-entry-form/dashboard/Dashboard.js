import React from 'react';

import DataDisplayTable from '../components/data-display-table/DataDisplayTable';

class Dashboard extends React.Component {

    static defaultProps = {
        className: "dashboard",
        headers: [],
        dataList: []
    }

    componentDidMount() {
    }

    render() {
        return (
            <div className={this.props.className}>
                {this.props.children}
                <DataDisplayTable
                    dataList={this.props.dataList}
                    headers={this.props.headers}
                    urlPrefix="/entry/"
                />
            </div>
        );
    }
}

export default Dashboard;