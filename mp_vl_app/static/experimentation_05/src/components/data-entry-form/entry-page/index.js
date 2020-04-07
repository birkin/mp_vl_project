import React from 'react';

import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { Button, Icon } from '@material-ui/core';
import { withStyles } from '@material-ui/styles';
import Table from "@material-ui/core/Table";
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import { isEqual } from 'lodash';

import { changeEntry } from '../actions';
// TODO
import displayDate from '../../../displayDate';

const styles = {
    footer: {
        marginTop: '25px',
        marginBottom: '35px',
        textAlign: 'center'
    },
    capitalize: {
        textTransform: 'capitalize'
    }
}

const mapStateToProps = state => {
    return {
        dataList: state.dataentryform.dataList,
        currentData: state.dataentryform.currentData,
    };
};
  
const mapDispatchToProps = dispatch => {
    return {
        changeEntry: (id) => dispatch(changeEntry(id)),
    };
}

class EntryPage extends React.Component {

    static defaultProps = {
        className: "entry-page",
        dataList: [],
    }

    componentDidMount() {
        if (this.props.dataList) {
            this.props.changeEntry(this.props.id);
        }
    }

    componentDidUpdate(prevProps) {
        if (!isEqual(prevProps.id, this.props.id)) {
            this.props.changeEntry(this.props.id);
        }
        if (!isEqual(prevProps.dataList, this.props.dataList)) {
            this.props.changeEntry(this.props.id);
        }
    }

    renderPeople(list) {
        if (!list || list.length === 0) {
            return <div>No information</div>
        }
        const keys = [
            "name",
            "race",
            "ethnicity",
            "nationality",
            "gender",
            "martialStatus",
            "occupation",
            "age",
            "literacy"
        ]
        const tableHead = 
            <TableHead>
                <TableRow>
                    {keys.map((header, i) => {
                        return <TableCell className={this.props.classes.capitalize} key={i}>{header}</TableCell>
                    })}
                </TableRow>
            </TableHead>;
        const tableBody = 
            <TableBody>
                {list.map((obj, i) => {
                    return (
                        <TableRow
                            key={i}
                        >
                            {keys.map((key, j) => {
                                let formattedData;
                                let data = list[i][key];
                                if (Array.isArray(data)) {
                                    formattedData = data.join(', ');
                                } else {
                                    formattedData = data;
                                }
                                return <TableCell key={`${i}-${j}`}>{formattedData}</TableCell>
                            })}
                        </TableRow>
                    );
                })}
            </TableBody>;

        return (
            <Table>
                {tableHead}
                {tableBody}
            </Table>
        )
    }

    render() {
        const id = this.props.id;
        const data = this.props.currentData;
        var innerElement;
        if (!data) {
            innerElement = <div>This entry was not found. Please make sure the URL is correct.</div>    
        } else {
            innerElement = (
                <div>
                    <h1>{data.title || <em>No title</em>}</h1>
                    <p>{data.eventCategory}</p>
                    <em>{displayDate(data.date)} {data.location && `in ${data.location}`}</em>
                    <p>{data.description}</p>
                    <hr />
                    <h2>Location</h2>
                    <p>Place: {data.location || <em>Not provided</em>}</p>
                    <p>Coordinates (lat, lng): ({data.latitude || 'N/A'}, {data.longitude || 'N/A'})</p>
                    <p>Rationale: {data.locationRationale || <em>Not provided</em>}</p>
                    <hr />
                    <h2>Victims</h2>
                    {this.renderPeople(data.victims)}
                    <p>Number of Victims: {data.numberOfVictims || <em>Not provided</em>}</p>
                    <p>Victims Category: {data.victimCategory ? data.victimCategory.join(', ') : <em>Not provided</em>}</p>
                    <h2>Aggressors</h2>
                    {this.renderPeople(data.aggressors)}
                    <p>Agressors Category: {data.aggressorCategory ? data.aggressorCategory.join(', ') : <em>Not provided</em>}</p>
                    <hr />
                    <h2>Metadata</h2>
                    <p>{(!data.womenInvolved || data.womenInvolved === "Unknown") ? "Unknown whether there were women involved" : data.womenInvolved}</p>
                    <p>Types of violence: {data.typesOfViolence ? data.typesOfViolence.join(', ') : <em>Not provided</em>}</p>
                    <p>Case Outcome Type: {data.caseOutcomeType ? data.caseOutcomeType : <em>Not provided</em>}</p>
                    <p>Case Outcome Subtypes: {
                        data.caseOutcomeType ?
                            data.caseOutcomeType === "Seeking Justice" ?
                                data.caseOutcomeForSeekingJustice && data.caseOutcomeForSeekingJustice.join(', ') : 
                                data.caseOutcomeType === "Disavowed or Erased Violence" ? 
                                    data.caseOutcomeForDisavowedOrErasedViolence && data.caseOutcomeForDisavowedOrErasedViolence.join(', ') :
                                    <em>Not provided</em> :
                            <em>Not provided</em>
                    }</p>
                    <p>Alleged Crime(s): {data.allegedCrime ? data.allegedCrime.join(', ') : <em>Not provided</em>}</p>
                    <p>Availabed Records: {data.availableRecords ? data.availableRecords.join(', ') : <em>Not provided</em>}</p>
                    <hr />
                    <h2>Sources</h2>
                    <h3>Primary Sources</h3>
                    {data.primarySources ? data.primarySources.map((source, i) => 
                        <p key={i} className="MARKDOWN">{source}</p>
                    ) : <p>No sources</p>}
                    <h3>Secondary Sources</h3>
                    {data.secondarySources ? data.secondarySources.map((source, i) => 
                        <p key={i} className="MARKDOWN">{source}</p>
                    ) : <p>No sources</p>}
                    <h2>Researcher Notes</h2>
                    <p>{data.researcherNotes || <em>Not provided</em>}</p>
                    <div className={this.props.classes.footer}>
                        <Button
                            variant="contained"
                            color="secondary"
                            size="large"
                            // TODO remove dependency on edit suffix
                            onClick={() => this.props.history.push(`/entry/${id}/edit`)}
                        >
                            Edit &nbsp; <Icon>edit_icon</Icon>
                        </Button>
                    </div>
                </div>
            );
        }
        return (
            <div className={this.props.className}>
                {innerElement}
            </div>
        );
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(withStyles(styles)(EntryPage)));