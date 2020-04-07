import React from 'react';

import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { Prompt } from 'react-router-dom';

import { JsonForms } from '@jsonforms/react';

import { withStyles } from '@material-ui/styles';
import Button from '@material-ui/core/Button';

import Cookie from 'js-cookie';

import { isEqual } from 'lodash';

import { changeEntry, saveEntry, setJsonformsData, changeLoading } from '../actions';

const styles = {
    footer: {
        marginTop: '25px',
        textAlign: 'center'
    },
    button: {
        margin: '0 10px',
    }
}

const mapStateToProps = state => {
    return {
        newData: state.jsonforms.core.data,
        dataList: state.dataentryform.dataList,
        currentData: state.dataentryform.currentData,
        scrollY: state.dataentryform.scrollY,
        saveMessage: state.dataentryform.saveMessage,
    };
};
  
const mapDispatchToProps = dispatch => {
    return {
        changeEntry: (id) => dispatch(changeEntry(id)),
        setJsonformsData: (data) => dispatch(setJsonformsData(data)),
        saveEntry: (url, data, userId) => dispatch(saveEntry(url, data, userId)),
        changeLoading: (isLoading, scrollX, scrollY) => dispatch(changeLoading(isLoading, scrollX, scrollY))
    };
}

class EditPage extends React.Component {

    static defaultProps = {
        className: "edit-page",
        dataList: [],
    }

    constructor(props) {
        super(props);

        this.scrollElement = this.scrollElement.bind(this);
    }

    scrollElement() {
        window.requestAnimationFrame(() => {
            if (this.props.scrollY && (window.scrollY !== this.props.scrollY)) {
                window.scrollTo(0, this.props.scrollY);
            }
        });
    }

    componentDidMount() {
        this.scrollElement();
        if (this.props.dataList) {
            this.props.changeEntry(this.props.id);
        }
        if (!isEqual(this.props.currentData, this.props.newData)) {
            this.props.setJsonformsData(this.props.currentData);
        }
    }

    componentDidUpdate(prevProps) {
        if (!isEqual(prevProps.id, this.props.id)) {
            this.props.changeEntry(this.props.id);
        }
        if (!isEqual(prevProps.currentData, this.props.currentData) && !isEqual(this.props.currentData, this.props.newData)) {
            this.props.setJsonformsData(this.props.currentData);
        }
        if (!isEqual(prevProps.dataList, this.props.dataList)) {
            this.props.changeEntry(this.props.id);
        }
    }

    render() {
        const id = this.props.id;
        const data = this.props.currentData;
        const newData = this.props.newData;
        var innerElement;
        if (!data) {
            innerElement = <div>This entry was not found. Please make sure the URL is correct.</div>    
        } else {
            innerElement = (
                <div>
                    <h1>Editing Entry</h1>
                    <p>This entry has the following ID: {id}</p>
                    <JsonForms />
                    <div>
                        {isEqual(data, newData) && this.props.saveMessage && <p>{this.props.saveMessage}</p>}
                    </div>
                    <div className={this.props.classes.footer}>
                        <Button
                            className={this.props.classes.button}
                            variant="outlined"
                            onClick={() => {
                                const message = "This will delete all fields on this entry. Are you sure?";
                                if (window.confirm(message)) {
                                    this.props.setJsonformsData({
                                        _id: id
                                    });
                                }
                            }}
                        >
                            Clear
                        </Button>
                        <Button
                            className={this.props.classes.button}
                            variant="outlined"
                            onClick={() => {
                                const message = "This will undo all edits you have made on this entry. Are you sure?";
                                if (window.confirm(message)) {
                                    this.props.setJsonformsData(data);
                                }
                            }}
                        >
                            Reset
                        </Button>
                        <Button
                            className={this.props.classes.button}
                            variant="contained"
                            onClick={() => this.props.history.push(`.`)}
                        >
                            Cancel
                        </Button>
                        <Button
                            className={this.props.classes.button}
                            color="secondary"
                            variant="contained"
                            onClick={() => this.props.saveEntry(`${this.props.dataUrl}/${id}`, newData, Cookie.get('auth-token').split(':')[0])}
                        >
                            Save
                        </Button>
                    </div>
                    <Prompt
                        when={!isEqual(data, newData)}
                        message={"You have unsaved changes. Are you sure you want to continue? These edits will be lost."}
                    />
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

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(withStyles(styles)(EditPage)));