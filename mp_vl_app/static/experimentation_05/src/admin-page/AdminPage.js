import React from 'react';

import { connect } from 'react-redux';

import Table from "@material-ui/core/Table";
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';

const mapStateToProps = state => {
    return {
        schema: state.jsonforms.core.schema,
        uischema: state.jsonforms.core.uischema,
    }
}

class AdminPage extends React.Component {

    processSchema(schema) {
        const fields = {};
        for (var entry of Object.entries(schema.properties)) {
            fields[entry[0]] = entry[1].type;
        }
        return fields;
    }

    render() {
        const processedSchema = this.processSchema(this.props.schema);
        const entries = Object.entries(processedSchema);
        return (
            
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Field Name</TableCell>
                        <TableCell>Data Type</TableCell>
                        <TableCell>Is Required?</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {entries.map((entry, i) => {
                        return (
                            <TableRow key={i}>
                                <TableCell>{entry[0]}</TableCell>
                                <TableCell>
                                    <Select value={entry[1]}>
                                        <MenuItem value="string">string</MenuItem>
                                        <MenuItem value="number">number</MenuItem>
                                        <MenuItem value="array">array</MenuItem>
                                        <MenuItem value="object">object</MenuItem>
                                        <MenuItem value="boolean">boolean</MenuItem>
                                    </Select>
                                </TableCell>
                                <TableCell></TableCell>
                            </TableRow>
                        )
                    })}
                </TableBody>
            </Table>
        );
    }
}

export default connect(mapStateToProps)(AdminPage);