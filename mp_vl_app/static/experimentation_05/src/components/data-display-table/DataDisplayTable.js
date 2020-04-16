import React from 'react';
import Table from "@material-ui/core/Table";
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableRowAsLink from './TableRowAsLink';

class DataDisplayTable extends React.Component {
    static defaultProps = {
        headClassName: 'table-head',
        bodyClassName: 'table-body',
        rowClassName: 'table-row',
        cellClassName: 'table-cell',
        dataList: []
    }

    componentDidMount() {

    }

    componentWillMount() {

    }

    render() {
        return (
            <Table>
                <TableHead className={this.props.headClassName}>
                    <TableRow className={this.props.rowClassName}>
                        {this.props.headers.map((header, i) => {
                            return <TableCell key={i}>{header.label}</TableCell>
                        })}
                    </TableRow>
                </TableHead>
                <TableBody className={this.props.bodyClassName}>
{console.log(this.props.dataList)}
                    {this.props.dataList && this.props.dataList.map((data, i) => {
                        return (
                            <TableRowAsLink
                                rowClassName={this.props.rowClassName}
                                cellClassName={this.props.cellClassName}
                                key={i}
                                hover={true}
                                headers={this.props.headers}
                                data={data}
                                href={`${this.props.urlPrefix}${data._id}`}
                            />
                        )
                    })}
                </TableBody>
            </Table>
        );
    }
}

export default DataDisplayTable;
