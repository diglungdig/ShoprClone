var React = require('react');
var LoginForm = require('LoginForm');


var Login = React.createClass({
  getInitialState: function() {
    return {
      UserName: this.props.UserName,
      Password: this.props.Password
    };
  },

  loginSubmission: function (credentials) {
    this.setState(credentials);
  },

  render: function () {
    var UserName = this.state.UserName;
    var Password = this.state.Password;
      return (
        <div>
          <h2>
            <LoginForm onNewData={this.loginSubmission}/>
            Loaded from Login
          </h2>
        </div>

      );
  }
});

module.exports = Login;