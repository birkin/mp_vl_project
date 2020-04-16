import React from 'react';

import { connect } from 'react-redux';
import { Redirect, Route, withRouter } from 'react-router-dom';

const mapStateToProps = state => {
    return {
        user: state.authentication.user
    }
}

class ProtectedRoute extends React.Component {

    render() {
        var redirectElement;
        const user = this.props.user || {role:"ADMIN"};
        if (!user) {
            redirectElement = <Redirect to="/" />;
        }

        if (user) {
            const allowedRoles = this.props.allowedRoles;
            const hasNecessaryRole = allowedRoles.indexOf(user.role) >= 0;
            if (!hasNecessaryRole) {
                redirectElement = <Redirect to="/" />;
            }
        }

        return <Route
            path={this.props.path}
            render={(props) => {
                if (redirectElement) {
                    return redirectElement;
                } else {
                    return this.props.render(props);
                }
            }}
        />
    }
}

export default connect(mapStateToProps)(withRouter(ProtectedRoute));